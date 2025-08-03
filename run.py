
import argparse
import json
from jsonschema import validate, ValidationError
import os
from utils import *
from multi_agent import AgentBase, LLMTranslatorAgent, ConfigDivideAgent, ContentTraverseAgent, CriticAgent, counter
from config_parser import build_config_tree_nokia, build_config_tree_huawei
from generate_embeddings import EmbeddingModel, generate_subtree_contexts
import ast


hierarchy_file_path_dict = {
    "huawei-ne40e": "nassim-main/corpus/hierarchy/cmd_tree_hw_system_view.json",
    "nokia-sr": "nassim-main/corpus/hierarchy/cmd_tree_nokia_opt.json"
}

config_manual_path_dict = {
    "huawei-ne40e": "nassim-main/corpus/hw/hw_NE40E_V800R012C10/config_corpus/Configuration",
    "huawei-ce6800": "nassim-main/corpus/hw/hw_CE6800_V300R023C00/config_corpus/Configuration/Configuration_Guide",
}

cmd_manual_path_dict = {
    "huawei-ne40e": "nassim-main/corpus/hw/hw_NE40E_V800R012C10/cmd_corpus/",
    "huawei-ce6800": "nassim-main/corpus/hw/hw_CE6800_V300R023C00/cmd_corpus_json/",
}

# 全局定义设备名称，由命令行参数修改
DEVICE_NAME_DICT = {
    'huawei-ne40e': 'Huawei NE40E router',
    'nokia-sr': 'Nokia SR OS router',
    "huawei-ce6800": 'Huawei CE6800 switch',
    "cisco-catalyst6800": 'Cisco Catalyst 6800 switch',
    "cisco-ios": 'Cisco IOS router',
}

# 默认值，可传参修改
SRC_DEVICE_NAME = 'Nokia SR OS router'
TGT_DEVICE_NAME = 'Huawei NE40E router'


def pure_llm(src_config, model="qwen-max-latest"):
    llm_translator = LLMTranslatorAgent(model=model, src_device=SRC_DEVICE_NAME, tgt_device=TGT_DEVICE_NAME)    
    src_config = purify_configuration(src_config)
    translation = llm_translator.llm(src_config)
    global total_prompt_tokens
    global total_completion_tokens
    total_prompt_tokens += llm_translator.prompt_tokens
    total_completion_tokens += llm_translator.completion_tokens
    purified_translation = purify_configuration(translation)
    logger.info("Purified translation: " + purified_translation)
    logger.info(f"Usage of {llm_translator.name}: {llm_translator.prompt_tokens} prompt tokens, {llm_translator.completion_tokens} completion tokens")
    return purified_translation

def build_config_tree(config, hierarchy_root, parser_type='nokia'):
    if 'huawei' in parser_type:
        config_root = build_config_tree_huawei(config, hierarchy_root)
    elif 'nokia' in parser_type:
        config_root = build_config_tree_nokia(config, hierarchy_root)
    logger.info(f"{parser_type}_config_tree:")
    return config_root

def get_nodes_and_manuals(config_division, src_config_root, manual_type='config'):
    # get the corresponding (target) manuals of each fragment
    for item in config_division:
        logger.info("item type " + str(type(item)))
        cmds = [c.strip() for c in item["Fragment"].split('\n')]
        logger.debug(cmds)
        nodes = []
        manuals = []
        for cmd in cmds:
            node = src_config_root.find_child(cmd)
            if node:
                if node.hierarchy_node.path:
                    if node not in nodes:
                        nodes.append(node)
                        logger.debug(node.cli)
                if node.manuals:
                    manual_with_score = []
                    for manual in node.manuals:
                        manual_with_score.append([manual, 0])   # 每一行可以有多个manual，是或的关系
                    manuals.append(manual_with_score)
        item["Nodes"] = nodes
        manual_name = "TargetConfigManuals" if manual_type == 'config' else "TargetCmdManuals"
        if manual_name not in item:
            item[manual_name] = manuals
        # Top-k 清零？
        # else:
        #     for manuals in item[manual_name]:
        #         for manual in manuals:
        #             manual[1] = 0
    src_config_root.reset_is_chosen()
    return config_division

def validate_json(json_data, schema_path):
    """
    验证 JSON 数据是否符合指定的 JSON Schema
    
    参数:
        json_data (str/dict): 要验证的 JSON 数据（可以是字符串或字典）
        schema_path (str): JSON Schema 文件路径
    
    返回:
        tuple: (bool, str) 第一个元素表示是否验证通过，第二个元素是消息
    """
    try:
        # 如果输入是字符串，先解析为字典
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        
        # 加载 schema
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        
        # 执行验证
        validate(instance=json_data, schema=schema)
        return (True, "JSON 数据符合 Schema")
        
    except json.JSONDecodeError as e:
        return (False, f"JSON 解析错误: {str(e)}")
    except FileNotFoundError:
        return (False, f"Schema 文件未找到: {schema_path}")
    except ValidationError as e:
        return (False, f"Schema 验证失败: {str(e)}")
    except Exception as e:
        return (False, f"发生未知错误: {str(e)}")

def get_division_and_intent(src_config, src_config_root, manual_content_list, model='qwen-max-latest'):
    config_divide_agent = ConfigDivideAgent(model=model, src_device=SRC_DEVICE_NAME, tgt_device= TGT_DEVICE_NAME)
    config_division = None
    max_retry = 3
    while config_division is None:
        config_divide_agent.clear_context() # 每次重新调用清空上下文
        res = config_divide_agent.run(src_config, manual_content_list)
        logger.info("res: " + str(res))
        try:
            parsed_res = parse_rsp(res)
            logger.info(parsed_res)
            config_division = json.loads(parsed_res)
            if not isinstance(config_division, list):   # 避免llm分次返回
                config_division = None
            if len(config_division) == 0:   # llm返回空
                config_division = None
            # 测试是否符合datasets/config_division_schema.json
            schema_path = "datasets/config_division_schema.json"
            is_valid, message = validate_json(config_division, schema_path)
            if is_valid:
                logger.info("Config division JSON is valid")
            if not is_valid:
                logger.error(f"Config division JSON is invalid: {message}")
                config_division = None
        except Exception as e:
            logger.error(f"{e}\nError in parsing response (division), retrying llm...")
        if not config_division:
            max_retry -= 1
            if max_retry == 0:
                logger.error(f"Error in parsing response (division), retried 3 times, exit...")
                return None
    logger.info(config_division)
    # # exit()

    if src_config_root:
        # get the corresponding nodes and manuals of each fragment
        config_division = get_nodes_and_manuals(config_division, src_config_root)

    logger.info(config_division)
    logger.info(f"Usage of {config_divide_agent.name}: {config_divide_agent.prompt_tokens} prompt tokens, {config_divide_agent.completion_tokens} completion tokens")
    global total_prompt_tokens
    global total_completion_tokens
    total_prompt_tokens += config_divide_agent.prompt_tokens
    total_completion_tokens += config_divide_agent.completion_tokens
    return config_division

class EmbeddingCache():
    def __init__(self):
        self.cache = {}
        self.is_set = False
    
    def get(self, key):
        return self.cache.get(key, None)
    
    def set(self, key, value):
        self.cache[key] = value

full_config_corpus_embeddings_cache = EmbeddingCache()     # 全量配置语料库的embedding缓存
full_cmd_corpus_embeddings_cache = EmbeddingCache()        # 全量命令语料库的embedding缓存

# 召回手册：可以写成算法
def retrieve_manuals(config_division: json, src_config: str, tgt_manual_path="nassim-main/corpus/hw/hw_NE40E_V800R012C10/config_corpus/Configuration", ra_rounds=3, ra_top_k = 30, ra_top_k_ratio = 0.5, retrieval_model='qwen-max-latest', voting=True, emb_model='bge-m3', use_mix=True, selector='bm25', manual_type='config'):
    """
    Use LLM to select the most relevant manual directories, then use Embedding Model to retrieve the corresponding manuals
    Args:
        config_division: the division of the source config
        src_config: the source config
        tgt_manual_path: the path of the manual directory
        k: the number of the most relevant manuals
    Returns:
        config_division: the division of the source config with the most relevant manuals
    """


    emb_model = EmbeddingModel(emb_model, 'manual')
    # reranker = RerankerModel()
    tgt_desc_dict = None
    # 使用summarized description，效果不佳，暂时弃用
    # 复用，try检测有没有，如果没有则全部退化
    if manual_type == 'config':
        tgt_desc_path = tgt_manual_path + ".json"
        try:
            tgt_desc_dict = json.load(open(tgt_desc_path, 'r', encoding='utf-8'))
        except:
            logger.error(f"Target manual description file {tgt_desc_path} not found")

    for item in config_division:
        logger.info("Fragment: " + item["Fragment"])
        config_unit = ConfigUnit(item)
        config_unit.print()

        ##### Embedding Intent/Function Sentences ##### 
        sentences = []
        sentence_to_index = {}  # not used
        index_to_cmd = {}
        if manual_type == 'config':
            sentences.append(item["Function"])
            sentence_to_index[item["Function"]] = 0
            index_to_cmd[0] = "Full Fragment"
        else:
            function = item["Function"]
            fragment = item["Fragment"]
            sentence = f"Function: {function}\nConfiguration: {fragment}"   # version_2
            sentences.append(sentence)
            sentence_to_index[sentence] = 0
            index_to_cmd[0] = "Full Fragment"

        # sentences.append(detail["Function"])
        if voting:
            for cmd, function in get_cmd_function(item["Details"]):
                if manual_type == 'config':
                    sentences.append(function)
                else:
                    sentences.append(cmd + "\n" + function)
                sentence_to_index[cmd] = len(sentences) - 1
                index_to_cmd[len(sentences) - 1] = cmd
            if manual_type == 'cmd' and 'Nodes' in item:
                for config_node in item['Nodes']:
                    try:
                        with open(config_node.hierarchy_node.path, 'r', encoding='utf-8') as f:
                            cmd_json = json.load(f)
                        pagetitle = cmd_json["PageTitle"]
                        CLIs = "\n".join(cmd_json['CLIs'])
                        desc = cmd_json['FuncDef']
                        item_path = config_node.hierarchy_node.path.split('.')[0].replace('_', ' ')
                        item_path = item_path.split('/cmd_corpus/')[-1]
                        item_path = item_path.replace('/', ' / ')
                        version_1 = f"{pagetitle}: {desc}\n{CLIs}\n ({item_path})"
                        sentences.append(version_1)
                    except Exception as e:
                        logger.error(f"Error in loading cmd_json: {e}")
                        continue

        logger.debug(f"sentences: {sentences}")
        # sentence_embeddings = emb_model.get_embeddings(sentences)
        sentence_embeddings = emb_model.get_embeddings(sentences, prompt='Instruct: You are a network configuration expert. Extract the most relevant technical documentation summary that precisely match the configuration command or feature description. Focus on exact parameter names, CLI commands, and functional descriptions.\nQuery: ')   


        ##### Embedding Manuals #####
        logger.info(f"##### Retrieve {SRC_DEVICE_NAME} Configuration Manuals #####")
        # Filter: 使用LLM/BERT/BM25获取最相关的manual列表
        content_traverser = ContentTraverseAgent(k=ra_rounds, base_path=tgt_manual_path, model=retrieval_model, manual_type=manual_type, src_device=SRC_DEVICE_NAME, tgt_device= TGT_DEVICE_NAME)
        target_manual_list, target_manual_files = content_traverser.run(config_unit, src_config, selector=selector)
        # logger.info(f"target_manual_list: {target_manual_list}, target_manual_files: {target_manual_files}")
        logger.info(f"len(target_manual_list): {len(target_manual_list)}, len(target_manual_files): {len(target_manual_files)}")
        target_manual_list = [manual_path for manual_path in target_manual_list if os.path.exists(manual_path)]     # 去除不存在的manual
        use_full_corpus = False
        if not target_manual_list and not target_manual_files:  # 未找到相关manual，使用默认全量manual
            logger.info("No manual found, use the default manual")
            target_manual_list = [tgt_manual_path]
            use_full_corpus = True


        # Dense: 对召回的 manual 列表进行embedding
        contexts = []
        index_to_filename = {}
        filename_to_index = {}

        desc_type = 'summarized_desc'
        global full_config_corpus_embeddings_cache
        if use_full_corpus and full_config_corpus_embeddings_cache.is_set:
            logger.info("Using full corpus embeddings cache")
            contexts_embeddings = full_config_corpus_embeddings_cache.get('contexts_embeddings')
            contexts = full_config_corpus_embeddings_cache.get('contexts')
            index_to_filename = full_config_corpus_embeddings_cache.get('index_to_filename')
            filename_to_index = full_config_corpus_embeddings_cache.get('filename_to_index')
        else:
            for manual in target_manual_list:
                _context, _index_to_filename, _filename_to_index = generate_subtree_contexts(manual, len(contexts), manual_type=manual_type, desc_type=desc_type, desc_dict=tgt_desc_dict)
                contexts += _context
                index_to_filename.update(_index_to_filename)
                filename_to_index.update(_filename_to_index)
            for manual in target_manual_files:
                _context, _index_to_filename, _filename_to_index = generate_subtree_contexts(manual, len(contexts), manual_type=manual_type, desc_type=desc_type, desc_dict=tgt_desc_dict)
                contexts += _context
                index_to_filename.update(_index_to_filename)
                filename_to_index.update(_filename_to_index)
            logger.info(f"contexts len: {len(contexts)}")
            if len(contexts) == 0:
                logger.error(f"Error in generating contexts, continue")
                continue
            contexts_embeddings = emb_model.get_embeddings(contexts)
            if use_full_corpus:
                full_config_corpus_embeddings_cache.set('contexts_embeddings', contexts_embeddings)
                full_config_corpus_embeddings_cache.set('contexts', contexts)
                full_config_corpus_embeddings_cache.set('index_to_filename', index_to_filename)
                full_config_corpus_embeddings_cache.set('filename_to_index', filename_to_index)
                full_config_corpus_embeddings_cache.is_set = True
        
        ### 举例
        # "Fragment": "policy-statement \"EXPORT_to_OSPF\"\n    entry 10\n        from\n            protocol direct\n            prefix-list \"SYSTEM\"\n        to\n            protocol ospf\n        action accept\n            type 1",
        # "Function": "Define a policy statement for route exporting.",
        # "Details": {
        #     "policy-statement": {
        #         "Function": "Create a policy statement named \"EXPORT_to_OSPF\".",
        #         "Parameters": {
        #             "Name": "EXPORT_to_OSPF"
        #         }
        #     },
        ### End of E.g.

        # delta_top_k = 5
        # if voting:
        #     # top_k = min(min(ra_top_k, int(len(contexts) * ra_top_k_ratio)), len(contexts))
        #     top_k = min([len(contexts), ra_top_k + delta_top_k * len(sentences)])
        # else:
        #     top_k = min(ra_top_k, len(contexts))
        # find the top-k similar commands in hw_corpus
        top_k = min(ra_top_k, len(contexts))
        logger.info(f"single top-k: {top_k}") 

        logger.info("### FRAGMENT ###\n" + item['Fragment'])
        
        manuals_retrieve = {}
        for i, embedding in enumerate(sentence_embeddings):
            similarities = emb_model.get_similarities(embedding, contexts_embeddings)[0]

            logger.info(f"len(contexts): {len(contexts)}, len(sentences): {len(sentences)}")
            scores, indices = torch.topk(similarities, top_k)
            logger.info(f"\n#### {SRC_DEVICE_NAME} command ({index_to_cmd[i]}) function: {sentences[i]} ")
            # get the top-k similar commands
            for j, (score, idx) in enumerate(zip(scores, indices)):
                idx = idx.item()
                score = score.item()
                filename = index_to_filename[str(idx)]
                # manuals_retrieve.append(filename)
                # new_scores.append((filename, reranker.compute_score([contexts[idx], sentences[i]])[0]))
                manuals_retrieve[filename] = manuals_retrieve.get(filename, 0) + score
                logger.info(f"[{j}] score: {score}, filename: {filename}")
                logger.info(f"idx: {idx}, i: {i}, context: {contexts[idx]}, sentence: {sentences[i]}")
            # sorted_manuals = sorted(new_scores, key=lambda x: x[1], reverse=True)
            # for j, (manual, score) in enumerate(sorted_manuals[:10]):   # 先重排序，再取前十
            #     logger.info(f"[{j}] score: {score}, filename: {manual}")
            #     manuals_retrieve[manual] = manuals_retrieve.get(manual, 0) + score
            # logger.info(f"new_scores: {new_scores}")
        # counts = Counter(manuals_retrieve)

        if use_mix: # 需要讨论是否更好
            ### 混合召回：加入全量手册的top-k (k=len(manuals_retrieve)) ###
            logger.info("### BEGIN MIXED RETRIEVAL ###")
            contexts = []
            index_to_filename = {}
            filename_to_index = {}
            target_manual_list = [tgt_manual_path]

            if full_config_corpus_embeddings_cache.is_set:
                logger.info("Using full corpus embeddings cache in mixed retrieval")
                contexts_embeddings = full_config_corpus_embeddings_cache.get('contexts_embeddings')
                contexts = full_config_corpus_embeddings_cache.get('contexts')
                index_to_filename = full_config_corpus_embeddings_cache.get('index_to_filename')
                filename_to_index = full_config_corpus_embeddings_cache.get('filename_to_index')
            else:
                for manual in target_manual_list:
                    _context, _index_to_filename, _filename_to_index = generate_subtree_contexts(manual, len(contexts), manual_type=manual_type, desc_type=desc_type, desc_dict=tgt_desc_dict)
                    contexts += _context
                    index_to_filename.update(_index_to_filename)
                    filename_to_index.update(_filename_to_index)
                contexts_embeddings = emb_model.get_embeddings(contexts)
                full_config_corpus_embeddings_cache.set('contexts_embeddings', contexts_embeddings)
                full_config_corpus_embeddings_cache.set('contexts', contexts)
                full_config_corpus_embeddings_cache.set('index_to_filename', index_to_filename)
                full_config_corpus_embeddings_cache.set('filename_to_index', filename_to_index)
                full_config_corpus_embeddings_cache.is_set = True

            # manuals_retrieve_full = {}
            for i, embedding in enumerate(sentence_embeddings):
                similarities = emb_model.get_similarities(embedding, contexts_embeddings)[0]
                # top_k = min(ra_top_k * 2 + delta_top_k * len(sentences), len(contexts))    # mix 扩大召回范围，用于后续联合召回
                scores, indices = torch.topk(similarities, top_k)
                logger.info(f"\n#### {SRC_DEVICE_NAME} command ({index_to_cmd[i]}) function: {sentences[i]} ")
                for j, (score, idx) in enumerate(zip(scores, indices)):
                    idx = idx.item()
                    score = score.item()
                    filename = index_to_filename[str(idx)]
                    # manuals_retrieve_full[filename] = manuals_retrieve_full.get(filename, 0) + score
                    manuals_retrieve[filename] = manuals_retrieve.get(filename, 0) + score  # 叠加投票 
                    logger.info(f"[{j}] score: {score}, filename: {filename}")
                    logger.info(f"idx: {idx}, i: {i}, context: {contexts[idx]}, sentence: {sentences[i]}")

        sorted_counts = sorted(manuals_retrieve.items(), key=lambda x: x[1], reverse=True)
        logger.info("### Manuals retrieve: " + str(sorted_counts))
        # LLM as reranker, failed
        # reranked_manuals = []
        # while reranked_manuals == []:
        #     reranker = ContentsRetrievalAgent()
        #     reranked_manuals = reranker.rerank(config_unit.CLIs, src_config, '\n'.join([f'#### {item}\n' for item in config_unit.manuals]), [manual[0] for manual in sorted_counts])
        #     logger.info(reranked_manuals)
        #     exit()
        if manual_type == 'config':
            item["RetrievedConfigManuals"] = sorted_counts
        elif manual_type == 'cmd':
            item["RetrievedCmdManuals"] = sorted_counts
        manual_name = "TargetConfigManuals" if manual_type == 'config' else "TargetCmdManuals"
        # get top-k
        if manual_name in item:
            for manuals in item[manual_name]:
                for manual in manuals:
                    manual[1] = 0   # 清零，避免先前结果影响
                    for i, (manual_path, score) in enumerate(sorted_counts):
                        # logger.info(f"manual: {manual}, manual_path: {manual_path}")
                        if manual[0] in manual_path:                    # 精准匹配
                            manual[1] = i+1
                            break
                        elif manual[0].split('/')[-1] in manual_path:   # 末尾匹配
                            manual[1] = -(i+1)
                            break
                    if manual[1] > len(sorted_counts) or manual[1] < -len(sorted_counts):
                        logger.error(f"Error in matching manual: {manual[0]}, {manual[1]}~{len(sorted_counts)}")
                        exit()

    logger.info(f"Usage of {content_traverser.name}: {content_traverser.llm_agent.prompt_tokens} prompt tokens, {content_traverser.llm_agent.completion_tokens} completion tokens")
    global total_prompt_tokens
    global total_completion_tokens
    total_prompt_tokens += content_traverser.llm_agent.prompt_tokens
    total_completion_tokens += content_traverser.llm_agent.completion_tokens
    return config_division


def cross_retrieval_config(config_division):
    """
    Use config and cmd manuals to cross-retrieve each other
    Args:
        config_division: the division of the source config
    Returns:
        config_division: the division of the source config with the most relevant manuals
    """
    pass
    
def cross_retrieval_cmd(config_division, device_name, ra_top_k_ratio=0.5, ra_top_k=20, emb_model='bge-m3', voting=True):
    """
    Use config and cmd manuals to cross-retrieve each other
    Args:
        config_division: the division of the source config
    Returns:
        config_division: the division of the source config with the most relevant manuals
    """
    logger.info(f"Cross-retrieval cmd manuals for {device_name}")
    # 读取config手册到cmd的映射关系，若没有则构建（config manual -> [(cmd, [cmd manuals]), ...]）
    config2cmd_mapping_path = os.path.join(config_manual_path_dict[device_name], "config2cmd_mapping.json")
    if os.path.exists(config2cmd_mapping_path):
        config2cmd_mapping = json.load(open(config2cmd_mapping_path, 'r', encoding='utf-8'))
    else:
        cmd2filename_path = os.path.join(cmd_manual_path_dict[device_name], "cmd2filename.json")
        if os.path.exists(cmd2filename_path):
            cmd2filename = json.load(open(cmd2filename_path, 'r', encoding='utf-8'))
        else:
            # cmd到文件名的映射
            cmd2filename = {}
            for root, dirs, files in os.walk(cmd_manual_path_dict[device_name]):
                for file in files:
                    if file.endswith(".json"):
                        cmd_file = os.path.join(root, file)
                        cmd_json = json.load(open(cmd_file, 'r', encoding='utf-8'))
                        cmd = cmd_json["PageTitle"]
                        cmd = cmd.split('(')[0].strip()  # 去掉括号及其内容
                        if cmd in cmd2filename:
                            cmd2filename[cmd].append(cmd_file)
                        else:
                            cmd2filename[cmd] = [cmd_file]
            with open(cmd2filename_path, 'w', encoding='utf-8') as f:
                json.dump(cmd2filename, f, ensure_ascii=False, indent=4)

        # config到cmd的映射
        config2cmd_mapping = {}
        for root, dirs, files in os.walk(config_manual_path_dict[device_name]):
            for file in files:
                if file.endswith(".md"):
                    config_file = os.path.join(root, file)
                    cmds = find_cmds(config_file)
                    logger.info(f"cmds: {cmds} for {config_file}")
                    # config2cmd_mapping: {config_file: [(cmd, [cmd_file_paths]), ...]}, use cmd2filename to get cmd_file_paths
                    for cmd in cmds:
                        if cmd in cmd2filename:
                            if config_file in config2cmd_mapping:
                                config2cmd_mapping[config_file].append((cmd, cmd2filename[cmd]))
                            else:
                                config2cmd_mapping[config_file] = [(cmd, cmd2filename[cmd])]
        with open(config2cmd_mapping_path, 'w', encoding='utf-8') as f:
            json.dump(config2cmd_mapping, f, ensure_ascii=False, indent=4)

    emb_model = EmbeddingModel(emb_model, 'manual')
    
    for item in config_division:
        logger.info(item.keys())
        assert "RetrievedConfigManuals" in item, "No config manuals retrieved"
        assert "RetrievedCmdManuals" in item, "No cmd manuals retrieved"

        # 对sentences进行embedding
        sentences = []
        sentence_to_index = {}
        index_to_cmd = {}
        sentences.append(item["Fragment"])
        sentence_to_index[item["Fragment"]] = 0
        index_to_cmd[0] = "Full Fragment"

        if voting:
            for cmd, function in get_cmd_function(item["Details"]):
                sentences.append(cmd + "\n" + function)
                sentence_to_index[cmd] = len(sentences) - 1
                index_to_cmd[len(sentences) - 1] = cmd
        logger.info(f"len(sentences): {len(sentences)}")
        sentence_embeddings = emb_model.get_embeddings(sentences, prompt='Instruct: You are a network configuration expert. Extract the most relevant technical documentation summary that precisely match the configuration command or feature description. Focus on exact parameter names, CLI commands, and functional descriptions.\nQuery: ')
        # sentence_embeddings = emb_model.get_embeddings(sentences)


        # 读取config_division里的所有RetrievedConfigManuals，提取其中对应的cmd_manuals，并在其中进行Dense检索
        cmd_manuals_retrieved = []
        logger.info(f"len(RetrievedConfigManuals): {len(item['RetrievedConfigManuals'])}")
        for config_manual, score in item["RetrievedConfigManuals"]:
            logger.info(f"config_manual: {config_manual}, score: {score}")
            if config_manual in config2cmd_mapping:
                # logger.info(f"  cmd_manuals: {config2cmd_mapping[config_manual]}")
                for cmd, cmd_manuals in config2cmd_mapping[config_manual]:
                    cmd_manuals_retrieved.extend(cmd_manuals)
        # logger.info(f"cmd_manuals_retrieved: {cmd_manuals_retrieved}")
        logger.info(f"len(cmd_manuals_retrieved): {len(cmd_manuals_retrieved)}")

        # 对cmd_manuals_retrieved进行embedding
        contexts = []
        index_to_filename = {}
        filename_to_index = {}

        for cmd_manual in cmd_manuals_retrieved:
            _context, _index_to_filename, _filename_to_index = generate_subtree_contexts(cmd_manual, len(contexts), manual_type='cmd')
            contexts += _context
            index_to_filename.update(_index_to_filename)
            filename_to_index.update(_filename_to_index)
        logger.info(f"len(contexts): {len(contexts)}")
        contexts_embeddings = emb_model.get_embeddings(contexts)

        # 检索召回cmd
        # delta_top_k = 5
        # if voting:
        #     top_k = min([len(contexts), top_k + delta_top_k * len(sentences)])
        # else:
        #     top_k = min(top_k, len(contexts))

        top_k = min(ra_top_k, len(contexts))

        logger.info(f"Top-k: {top_k}")
        manuals_retrieve = {}
        for i, embedding in enumerate(sentence_embeddings):
            similarities = emb_model.get_similarities(embedding, contexts_embeddings)[0]
            # top_k = min(100, len(contexts))
            logger.info(f"len(contexts): {len(contexts)}, len(sentences): {len(sentences)}")
            scores, indices = torch.topk(similarities, top_k)
            logger.info(f"\n#### {SRC_DEVICE_NAME} command ({index_to_cmd[i]}) function: {sentences[i]} ")
            # get the top-k similar commands
            new_scores = []
            for j, (score, idx) in enumerate(zip(scores, indices)):
                idx = idx.item()
                score = score.item()
                filename = index_to_filename[str(idx)]
                # manuals_retrieve.append(filename)
                # new_scores.append((filename, reranker.compute_score([contexts[idx], sentences[i]])[0]))
                manuals_retrieve[filename] = manuals_retrieve.get(filename, 0) + score
                logger.info(f"[{j}] score: {score}, filename: {filename}")
                logger.info(f"idx: {idx}, i: {i}, context: {contexts[idx]}, sentence: {sentences[i]}")

        # # 和原有RetrievedCmdManuals进行叠加
        for cmd_manual, score in item["RetrievedCmdManuals"]:
            if cmd_manual in manuals_retrieve:
                manuals_retrieve[cmd_manual] += score
            else:
                manuals_retrieve[cmd_manual] = score

        sorted_counts = sorted(manuals_retrieve.items(), key=lambda x: x[1], reverse=True)
        logger.info(f"### Manuals retrieve: {str(sorted_counts)}, len(sorted_counts): {len(sorted_counts)}")
        
        item["RetrievedCmdManuals"] = sorted_counts

        # get top-k
        if "TargetCmdManuals" in item:
            for manuals in item["TargetCmdManuals"]:
                for manual in manuals:
                    for i, (manual_path, score) in enumerate(sorted_counts):
                        # logger.info(f"manual: {manual}, manual_path: {manual_path}")
                        if manual[0] in manual_path:                    # 精准匹配
                            manual[1] = i+1
                            break
                        elif manual[0].split('/')[-1] in manual_path:   # 末尾匹配
                            manual[1] = -(i+1)
                            break
                    if manual[1] > len(sorted_counts) or manual[1] < -len(sorted_counts):
                        logger.error(f"Error in matching manual: {manual[0]}, {manual[1]}~{len(sorted_counts)}")
                        exit()
        
    return config_division


def rag_translation(config_division, top_k_ratio=0.5, rag_top_k=30, tgt_hierarchy_root=None, tgt_all_clis=None, model='qwen-max-latest', use_baseline=False): 
    # rag_translator = LLMTranslatorAgent()                           
    curr_translation = "system-view\n"      # 引导生成视图完整的配置
    for item in config_division:
        logger.info("### Translating fragment: " + item["Fragment"])
        rag_translator = LLMTranslatorAgent(model=model, src_device=SRC_DEVICE_NAME, tgt_device= TGT_DEVICE_NAME)   # 每个Translator用于一个片段的翻译，片段内记录上下文
        src_manual_list = []
        target_config_manual_list = []
        target_cmd_manual_list = []
        

        # Baseline：使用人工标注的手册
        if use_baseline:
            if "TargetConfigManuals" not in item:
                logger.error("No TargetConfigManuals found")
            else:
                for manual_list in item["TargetConfigManuals"]:
                    for manual in manual_list:
                        target_config_manual_list.append(get_md_contents(manual[0]))
            if "TargetCmdManuals" not in item:
                logger.error("No TargetCmdManuals found")
            else:
                for manual_list in item["TargetCmdManuals"]:
                    for manual in manual_list:
                        target_cmd_manual_list.append(get_md_contents(manual[0]))
        # RAG：使用召回的手册
        else:
            if "RetrievedConfigManuals" not in item:
                logger.error("No RetrievedConfigManuals found")
            else:
                top_k = min(rag_top_k, len(item["RetrievedConfigManuals"]))
                for i, (manual, score) in enumerate(item["RetrievedConfigManuals"]):
                    target_config_manual_list.append(get_md_contents(manual))
                    if i >= top_k:
                        break
            if "RetrievedCmdManuals" not in item:
                logger.error("No RetrievedCmdManuals found")
            else:
                top_k = min(rag_top_k, len(item["RetrievedCmdManuals"]))
                for i, (manual, score) in enumerate(item["RetrievedCmdManuals"]):
                    # target_cmd_manual_list.append(get_md_contents(manual))
                    target_cmd_manual_list.append(get_json_content(manual))
                    if i >= top_k:
                        break
        # 源设备手册 
        if "Nodes" in item:
            for node in item["Nodes"]:
                src_manual_list.append(node.get_manual_content())

        res = ""
        reqs = ""
        while res == "":
            
            # 第一次生成。确保生成后结果比生成前只多不少
            try:
                res = rag_translator.rag(item['Fragment'], src_manual_list, target_config_manual_list, target_cmd_manual_list, curr_translation, reqs)
                if not res:
                    return ""
            except Exception as e:
                logger.error(f"{e}\nError in translation, retrying llm with smaller Top-k...")
                top_k = int(top_k * 0.8)
                continue
            pured_res = purify_configuration(res)
            if len(pured_res.strip()) < len(curr_translation.strip()):   # 生成的结果比当前翻译少，说明有问题；在req中附加，提升LLM对该问题的关注度
                logger.error(f"Error in translation, result is shorter than current translation, retrying llm")
                logger.info(f"### Current translation:\n{curr_translation}")
                logger.info(f"### Translation result:\n{res}")
                reqs = "Attention: the translation result should contain both the current and preceding translation."
                res = ""

        curr_translation = purify_configuration(res)
        # 如果tgt_hierarchy_root不为空，则进行视图验证（use_view）
        if tgt_hierarchy_root:   # 实时验证反馈，记录反馈前后的fuzzy和blank数量，若有减少则更新翻译
            logger.info("Use view verification...")
            hw_config_root = build_config_tree(curr_translation, tgt_hierarchy_root, 'huawei')
            config_tree = hw_config_root.print_to_str()
            logger.info(f"### Huawei config tree:\n{config_tree}")
            # mismatched_lines = hw_config_root.get_mismatched_lines()
            mismatched_lines = []   # 同时记录view error和syntax error
            mismatched_lines_syntax = []
            mismatched_lines_pure = hw_config_root.get_mismatched_lines(pure=True)
            for line in mismatched_lines_pure:
                fuzzy_matches = get_all_syntax_matches(line.strip(), tgt_all_clis)
                if not fuzzy_matches:
                    mismatched_lines.append(f"- {line} (syntax error)")
                    mismatched_lines_syntax.append(line)
                else:
                    mismatched_lines.append(f"- {line} (syntax correct but view error)")
            if len(mismatched_lines) > 0:   # 存在不匹配的情况，需要反馈调整
                logger.info(f"### Fuzzy and Blank before feedback:\n{mismatched_lines}")
                refined_res = purify_configuration(rag_translator.syntax_refinement(mismatched_lines))
                logger.info(f"### Refinded translation\n: {refined_res}")
                if refined_res:
                    hw_config_root_refined = build_config_tree(refined_res, tgt_hierarchy_root, 'huawei')
                    # config_tree_refined = hw_config_root_refined.print_to_str()
                    # mismatched_lines_refined = hw_config_root_refined.get_mismatched_lines()
                    mismatched_lines_refined_syntax = []
                    mismatched_lines_refined_pure = hw_config_root_refined.get_mismatched_lines(pure=True)
                    for line in mismatched_lines_refined_pure:
                        fuzzy_matches = get_all_syntax_matches(line.strip(), tgt_all_clis)
                        if not fuzzy_matches:
                            mismatched_lines_refined_syntax.append(line)
                    # logger.info(f"### Fuzzy and Blank after feedback:\n{mismatched_lines_refined}")
                    logger.info(f"### Mismatched lines after feedback (all):\n{mismatched_lines_refined_pure}")
                    logger.info(f"### Mismatched lines after feedback (syntax):\n{mismatched_lines_refined_syntax}")
                    if len(mismatched_lines_refined_syntax) < len(mismatched_lines_syntax): # 只看语法错误
                        curr_translation = refined_res
                        logger.info(f"### Refine successful (sLoop syntax mismatch {len(mismatched_lines_syntax)} -> {len(mismatched_lines_refined_syntax)}):\n" + curr_translation)
                    else:
                        logger.info(f"### Refine failed (No improvement, {len(mismatched_lines_syntax)} -> {len(mismatched_lines_refined_syntax)}.")
                else:
                    logger.info("### Refine failed (No refined result).")
            else:
                logger.info("### All lines matched.")
        elif tgt_all_clis:
            # 如果不进行视图验证，则尽量进行语法验证
            # logger.info("Use syntax verification...")
            logger.info("Use syntax verification...")
            # 遍历所有行，进行语法检查，如果不存在可能的匹配项，则标记可能错误，否则标记语法正确
            marked_translation = ""
            mismatched_lines = 0
            for line in curr_translation.split('\n'):
                matched = get_all_syntax_matches(purify_configuration(line).strip(), tgt_all_clis)
                if len(matched) == 0:
                    marked_translation += f"{line} (syntax mismatch)\n"
                    mismatched_lines += 1
                else:
                    marked_translation += f"{line} (syntax matched)\n"
            logger.info("### Marked translation:\n" + marked_translation)
            if mismatched_lines > 0:
                refined_translation = rag_translator.syntax_refinement(marked_translation)
                if refined_translation:
                    mismatched_lines_refined_syntax = 0
                    for line in refined_translation.split('\n'):
                        matched = get_all_syntax_matches(purify_configuration(line).strip(), tgt_all_clis)
                        if len(matched) == 0:
                            mismatched_lines_refined_syntax += 1
                    if mismatched_lines_refined_syntax < mismatched_lines:
                        curr_translation = refined_translation
                        logger.info(f"### Syntax refine successful (mismatch {mismatched_lines} -> {mismatched_lines_refined_syntax}):\n" + curr_translation)
                    else:
                        logger.info(f"### Syntax refine failed (No improvement, mismatch {mismatched_lines} -> {mismatched_lines_refined_syntax}).")
            else:
                logger.info("### All lines matched. No syntax verification needed.")
        else:
            logger.info("No verification in translation process...")
        logger.info("### Partial translation:\n" + curr_translation)
    purified_translation = purify_configuration(curr_translation)
    logger.info("### Final translation:\n" + purified_translation)
    logger.info(f"Usage of {rag_translator.name}: {rag_translator.prompt_tokens} prompt tokens, {rag_translator.completion_tokens} completion tokens")
    global total_prompt_tokens
    global total_completion_tokens
    total_prompt_tokens += rag_translator.prompt_tokens
    total_completion_tokens += rag_translator.completion_tokens
    return purified_translation



def retrieve_semantic_errors_manuals(cfg_comments_json, config_division):
        # 拆分config_division中的Fragments，用于后文的标记
        for item in config_division:
            item['Fragments'] = [[c, 0] for c in item['Fragment'].split('\n')]  

        nokia_cmds = []
        nokia_manuals_contents = []    # [[manual1, manual2, ...], [manual1, manual2, ...], ...]
        hw_cmds = []
        comments = []
        hw_config_manual_paths = []        # [[[manual1, score1], [manual2, score2], ...], [[manual1, score1], [manual2, score2], ...], ...]
        hw_cmd_manual_paths = []        # [[[manual1, score1], [manual2, score2], ...], [[manual1, score1], [manual2, score2], ...], ...]
        for item in cfg_comments_json:
            logger.info(f"Item: {item}")
            if "Equivalent" in item:
                is_queal = False
                if isinstance(item["Equivalent"], bool) and item["Equivalent"]:
                    is_queal = True
                if isinstance(item["Equivalent"], str) and ('True' in item["Equivalent"] or 'true' in item["Equivalent"]):
                    is_queal = True
                if is_queal:
                    if "Nokia" in item and "Huawei" in item and "Comments" in item:
                        for fragment in config_division:
                            for line in fragment['Fragments']:
                                if line[1] == 1:
                                    continue
                                if not item["Nokia"]:
                                    logger.error(f"Nokia error: {item['Nokia']}")
                                    continue
                                if isinstance(item["Nokia"], str):
                                    item["Nokia"] = item["Nokia"].split("\n")
                                for cmd in item["Nokia"]:
                                    if cmd.strip() == line[0].strip():
                                        line[1] = 1 # 标记为已经匹配
                                        cmd = ""    # 避免重复标注
                                        break
                                all_is_matched = True
                                for cmd in item['Nokia']:
                                    if cmd != "":
                                        all_is_matched = False  # 这个片段匹配完毕
                                        break
                                if all_is_matched:
                                    break
                        # mark in the config_division
                    continue
                elif "Nokia" in item and "Huawei" in item and "Comments" in item:
                    nokia_cmds_ = []
                    if isinstance(item["Nokia"], list):
                        nokia_cmds_ = item["Nokia"]
                        nokia_cmds.append(nokia_cmds_)
                    elif isinstance(item["Nokia"], str):
                        nokia_cmds_ = item["Nokia"].split("\n")
                        nokia_cmds.append(nokia_cmds_)
                    else:
                        logger.error(f"Nokia error: {item['Nokia']}")
                        # continue
                        nokia_cmds.append(['(No corresponding Nokia command)'])
                    # mark in config_division and get the manuals
                    target_manuals = {}     # manual: score
                    target_manuals_cmds = {}  # cmd: score
                    for fragment in config_division:
                        fragment_matched = False
                        for line in fragment['Fragments']:
                            if line[1] == 1:
                                continue
                            for cmd in nokia_cmds_:
                                if cmd.strip() == line[0].strip():
                                    line[1] = 1
                                    fragment_matched = True
                        if fragment_matched:
                            if 'RetrievedConfigManuals' in fragment:
                                for manual in fragment['RetrievedConfigManuals']:
                                    target_manuals[manual[0]] = target_manuals.get(manual[0], 0) + manual[1]
                            if 'RetrievedCmdManuals' in fragment:
                                for manual in fragment['RetrievedCmdManuals']:
                                    target_manuals_cmds[manual[0]] = target_manuals_cmds.get(manual[0], 0) + manual[1]
                            nokia_manuals_ = []
                            for node in fragment['Nodes']:
                                nokia_manuals_.append(node.get_manual_content())
                            nokia_manuals_contents.append(nokia_manuals_)
                    sorted_target_manuals = sorted(target_manuals.items(), key=lambda x: x[1], reverse=True)
                    sorted_target_manuals_cmds = sorted(target_manuals_cmds.items(), key=lambda x: x[1], reverse=True)
                    hw_config_manual_paths.append(sorted_target_manuals)
                    hw_cmd_manual_paths.append(sorted_target_manuals_cmds)

                    if isinstance(item["Huawei"], list):
                        hw_cmds.append(item["Huawei"])
                    elif isinstance(item["Huawei"], str):
                        hw_cmds.append(item["Huawei"].split("\n"))
                    else:
                        logger.error(f"Huawei error: {item['Huawei']}")
                        hw_cmds.append(['(No corresponding Huawei command translated)'])
                        # continue
                    if isinstance(item["Comments"], str):
                        comments.append(item["Comments"])
                    else:
                        logger.error(f"Comments error: {item['Comments']}")
                        comments.append("Error")
        return nokia_cmds, hw_cmds, comments, hw_config_manual_paths, hw_cmd_manual_paths, nokia_manuals_contents


def verify_rag(nokia_config, translation, nokia_config_root, hw_config_root, hw_hierarchy_root, config_division, model, top_k = 30):
    """
    Verify the translation with the error commands
    Args:
        hw_config_root: the root of the huawei config tree
        nokia_config_root: the root of the nokia config tree
        config_division: the division of the nokia config (for manual retrieval)
    Returns:
        refined_translation: the refined translation
    """
    # baseline before refinement
    hw_unmatched_lines = hw_config_root.get_mismatched_lines()
    TM = hw_config_root.get_matched_score()

    logger.info(f"### Unmatched lines before: {len(hw_unmatched_lines)}")
    logger.info(f"### Unmatched matched score before: {TM}")
    # if len(hw_unmatched_lines) == 0 and int(TM) == 1:
    #     logger.info("### No unmatched lines, no need for refinement.")
    #     return translation
    
    # 1. Use LLM to get the semantic errors
    critic = CriticAgent(model=model)
    verification_time = time.time()
    huawei_manual_content_list = hw_config_root.get_subtree_manual_content_list()
    nokia_manual_content_list = nokia_config_root.get_subtree_manual_content_list()
    # logger.info(huawei_manual_content_list)
    critic.clear_context()

    cfg_comments_json = None
    max_retry = 3
    while not cfg_comments_json:
        cfg_comments = critic.llm(purify_configuration(nokia_config), translation, nokia_manual_content_list, huawei_manual_content_list)
    #     logger.info(cfg_comments)
        # with open('test.json', 'r', encoding='utf-8') as f:
        #     cfg_comments = f.read()
        try:
            cfg_comments_json = json.loads(cfg_comments)
            break
        except Exception as e:
            max_retry -= 1
            if max_retry == 0:
                logger.error(f"{e}\nError in parsing response (critic), retried 3 times, exit...")
                return translation, []
            logger.error(f"{e}\nError in parsing response (critic), retrying llm...")
            continue

    # 2. 直接遍历config_division，找到对应的错误点并返回手册
    nokia_err_cmds, hw_err_cmds, comments, config_manuals, cmd_manuals, nokia_manual_content = retrieve_semantic_errors_manuals(cfg_comments_json, config_division)
    logger.info(f"len(nokia_err_cmds): {len(nokia_err_cmds)}, len(hw_err_cmds): {len(hw_err_cmds)}, len(comments): {len(comments)}, len(config_manuals): {len(config_manuals)}, len(cmd_manuals): {len(cmd_manuals)}")
    # 3. Use RAG to refine the translation
    curr_unmatched_lines = hw_unmatched_lines
    curr_TM = TM
    curr_translation = translation
    use_refinement = False
    for nokia_err, hw_err, comment, hw_config_manual_paths, hw_cmd_manual_paths, nokia_manual_content in zip(nokia_err_cmds, hw_err_cmds, comments, config_manuals, cmd_manuals, nokia_manual_content):
        logger.info(f"### Error Commands ###\n{hw_err}\n{nokia_err}\n{comment}\n{hw_config_manual_paths}\n{hw_cmd_manual_paths}\n{nokia_manual_content}")
        rag_translator = LLMTranslatorAgent(model=model)
        refined_translation = None 
        this_top_k = top_k
        max_tries = 3
        while not refined_translation and max_tries > 0:
            rag_translator.clear_context()
            try:
                refined_translation = rag_translator.refine_with_semantic_rag(nokia_config, curr_translation, nokia_err, hw_err, comment, hw_config_manual_paths, hw_cmd_manual_paths, nokia_manual_content, this_top_k)
            except Exception as e:
                logger.error(f"{e}\nError in translation, retrying llm with smaller Top-k...")
                this_top_k = int(this_top_k * 0.8)
                max_tries -= 1
                continue
            if not refined_translation:
                logger.error(f"Error in translation, result is empty, retrying llm with smaller Top-k...")
                this_top_k = int(this_top_k * 0.8)
                max_tries -= 1
                continue
            try:
                hw_config_root_refined = build_config_tree(refined_translation, hw_hierarchy_root, 'huawei')
                hw_unmatched_lines_refined = hw_config_root_refined.get_mismatched_lines()
                TM_refined = hw_config_root_refined.get_matched_score()
                logger.info(f"### Fuzzy and Blank before feedback:\n{curr_unmatched_lines}")
                logger.info(f"### Fuzzy and Blank after feedback:\n{hw_unmatched_lines_refined}")
                logger.info(f"### Matched Score before feedback: {TM}, after feedback: {TM_refined}")
                if len(hw_unmatched_lines_refined) <= len(hw_unmatched_lines) and TM_refined >= TM:
                    logger.info(f"### Refine successful (lLoop mismatch {len(hw_unmatched_lines)} -> {len(hw_unmatched_lines_refined)}):\n" + refined_translation)
                    curr_translation = refined_translation
                    curr_unmatched_lines = hw_unmatched_lines_refined
                    curr_TM = TM_refined
                    use_refinement = True
                else:
                    logger.info(f"### Refine failed (lLoop No improvement, {len(hw_unmatched_lines)} -> {len(hw_unmatched_lines_refined)}.")
            except Exception as e:
                logger.error(f"{e}\nError in verification, retrying llm...")
                max_tries -= 1
                continue

    if use_refinement:  # 如果有改进，则使用改进后的翻译
        cfg_comments_json = None
        max_retry = 3
        while not cfg_comments_json:
            cfg_comments = critic.llm(nokia_config, curr_translation, nokia_manual_content_list, huawei_manual_content_list)
        #     logger.info(cfg_comments)
            # with open('test.json', 'r', encoding='utf-8') as f:
            #     cfg_comments = f.read()
            try:
                cfg_comments_json = json.loads(cfg_comments)
                break
            except Exception as e:
                max_retry -= 1
                if max_retry == 0:
                    logger.error(f"{e}\nError in parsing response (critic), retried 3 times, exit...")
                    return curr_translation, []
                logger.error(f"{e}\nError in parsing response (critic), retrying llm...")
                continue

    logger.info(f"Improved unmatched lines: {len(hw_unmatched_lines)} -> {len(curr_unmatched_lines)}")
    logger.info(f"Improved matched score: {TM} -> {curr_TM}")
    logger.info(f"Verification time cost: {time.time() - verification_time}")
    logger.info(f"Usage of {critic.name}: {critic.prompt_tokens} prompt tokens, {critic.completion_tokens} completion tokens")
    global total_prompt_tokens
    global total_completion_tokens
    total_prompt_tokens += critic.prompt_tokens
    total_completion_tokens += critic.completion_tokens
    return curr_translation, cfg_comments_json

def semantic_refinement_with_view(src_config, translation, src_config_root, tgt_hierarchy_root, tgt_all_clis, config_division, model='qwen-max-latest', top_k=30, vendor='huawei'):
    """
    Use semantic refinement to refine the translation
    Args:
        translation: the translation result
        tgt_hierarchy_root: the target hierarchy root
        tgt_all_clis: the target all clis
    Returns:
        translation: the refined translation
    """
    
    logger.info(f"### Semantic refinement...")
    tgt_config_root = build_config_tree(translation, tgt_hierarchy_root, vendor)
    mismatched_lines = []
    mismatched_lines_syntax = []
    mismatched_lines_pure = tgt_config_root.get_mismatched_lines(pure=True)
    for line in mismatched_lines_pure:
        fuzzy_matches = get_all_syntax_matches(line.strip(), tgt_all_clis)
        if not fuzzy_matches:
            mismatched_lines_syntax.append(line)
            mismatched_lines.append(f"- {line} (syntax error) before semantic refinement")
        else:
            mismatched_lines.append(f"- {line} (view error) before semantic refinement")
    
    refined_translation, cfg_comments_json = verify_rag(src_config, translation, src_config_root, tgt_config_root, tgt_hierarchy_root, config_division, model, top_k)

    tgt_config_root_refined = build_config_tree(refined_translation, tgt_hierarchy_root, vendor)
    config_tree_str = tgt_config_root_refined.print_to_str()
    mismatched_lines_refined = []
    mismatched_lines_refined_syntax = []
    mismatched_lines_refined_pure = tgt_config_root_refined.get_mismatched_lines(pure=True)
    for line in mismatched_lines_refined_pure:
        fuzzy_matches = get_all_syntax_matches(line.strip(), tgt_all_clis)
        if not fuzzy_matches:
            mismatched_lines_refined_syntax.append(line)
            mismatched_lines_refined.append(f"- {line} (syntax error) after semantic refinement")
        else:
            mismatched_lines_refined.append(f"- {line} (view error) after semantic refinement")

    if len(mismatched_lines_refined) <= len(mismatched_lines):
        logger.info(f"### Semantic refinement successful (lLoop syntax mismatch {len(mismatched_lines)} -> {len(mismatched_lines_refined)}):\n" + refined_translation)
        return refined_translation, cfg_comments_json, config_tree_str
    else:
        logger.info(f"### Semantic refinement failed (No improvement, {len(mismatched_lines)} -> {len(mismatched_lines_refined)}).")
        return translation, cfg_comments_json, config_tree_str


# 全局定义：记录token使用量
total_prompt_tokens = 0
total_completion_tokens = 0

def return_to_main():
    pass

if __name__ == "__main__":

    # Basic arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-model", type=str, default="qwen-max-latest", help="Base model name: [gpt-4.1, gpt-4o, qwen-max-latest, deepseek-v3]")
    parser.add_argument("--emb-model", type=str, default="bge-m3", help="Embedding model name: [bge-m3, local_model_path]")
    # parser.add_argument("--stream", action="store_true", help="Stream mode")
    parser.add_argument("--method", type=str, default="INTA", help="Method name: [INTA, LLM, VOTE]")
    parser.add_argument("--src-vendor", type=str, default="nokia-sr", help="Source vendor: [nokia-sr, cisco-catalyst6800]")
    parser.add_argument("--tgt-vendor", type=str, default="huawei-ne40e", help="Target vendor: [huawei-ne40e, huawei-ce6800]")
    parser.add_argument("--senario", type=str, default="8refs", help="Dataset name: [8refs, configtrans, geneation, cisco]")
    parser.add_argument("-s", "--src-config-path", type=str, default="test_dataset/Nokia2Huawei/Nokia-with-manual/", help="Source config path")
    parser.add_argument("-t", "--tgt-config-path", type=str, default=None, help="Target config path")
    parser.add_argument("--tgt-cli-path", type=str, default="nassim-main/corpus/hw/hw_CE6800_V300R023C00/cmd_all_flat.json", help="target all cli path, use when not using config tree")
    parser.add_argument("--output-dir", type=str, default="./results", help="Output directory")
    # Experimental arguments
    parser.add_argument("--use-ext-config-division", action="store_true", help="Use external config division (the same root folder with source config)")
    parser.add_argument("--use-ext-config-retrieval", action="store_true", help="Use external config retrieval (the same root folder with source config)")
    parser.add_argument("--ra-only", action="store_true", help="Use only retrieval agent")
    parser.add_argument("--src-config-path-cmd", type=str, default=None, help="Source config path with target command, make sure the same filenames with source config")
    # Model arguments
    parser.add_argument("--use-view", action="store_true", help="Use view")
    parser.add_argument("--use-mix", action="store_true", help="Use mixed retrieval")
    parser.add_argument("--selector-config", type=str, default=None, help="Selector for retrieval: [bm25, llm]")
    parser.add_argument("--selector-cmd", type=str, default=None, help="Selector for retrieval: [bm25, llm]")
    parser.add_argument("--llm-filter-rounds", type=int, default=1, help="llm filter rounds")
    parser.add_argument("--use-cmd-manuals", action="store_true", help="Use command manuals")
    parser.add_argument("--no-sLoop", action="store_true", help="not use sLoop")
    parser.add_argument("--no-lLoop", action="store_true", help="not use lLoop")
    parser.add_argument("--no-voting", action="store_true", help="not use voting in retrieval")
    parser.add_argument("--manual-retrieve-ratio", type=float, default=0.5, help="Manual retrieve ratio")
    # parser.add_argument("--manual-retrieve-tok-k", type=int, default=20, help="Manual retrieve tok k")  # 15 better?
    parser.add_argument("--config-retrieve-top-k", type=int, default=20, help="Config retrieve top k")
    parser.add_argument("--cmd-retrieve-top-k", type=int, default=30, help="Cmd retrieve top k")
    parser.add_argument("--cross-retrieve-top-k", type=int, default=35, help="Cross retrieve top k")
    parser.add_argument("--rag-manuals-ratio", type=float, default=0.5, help="rag manuals ratio")
    parser.add_argument("--rag-manuals-tok-k", type=int, default=20, help="rag manuals tok k")
    parser.add_argument("--use-baseline", action="store_true", help="Use baseline manuals")
    parser.add_argument("--prompt-suffix", type=str, default="Let's think step by step:", help="Prompt suffix")

    args = parser.parse_args() 

    if args.use_ext_config_retrieval:
        assert args.use_ext_config_division, "Use external config retrieval requires external config division"

    
    SRC_DEVICE_NAME = DEVICE_NAME_DICT[args.src_vendor] 
    TGT_DEVICE_NAME = DEVICE_NAME_DICT[args.tgt_vendor] 

    if args.src_vendor in hierarchy_file_path_dict:
        src_hierarchy_file_path = hierarchy_file_path_dict[args.src_vendor] 
    else:
        src_hierarchy_file_path = None
        
    if args.tgt_vendor in hierarchy_file_path_dict:
        tgt_hierarchy_file_path = hierarchy_file_path_dict[args.tgt_vendor] 
    else:
        tgt_hierarchy_file_path = None
    config_manual_path = config_manual_path_dict[args.tgt_vendor]
    cmd_manual_path = cmd_manual_path_dict[args.tgt_vendor]
    logger.info(f"args:\n{args}")


    result_path_llm = os.path.join(args.output_dir, f"LLM_{args.base_model}_{args.src_vendor}_to_{args.tgt_vendor}_{args.senario}_{current_time}")
    result_path_inta = os.path.join(args.output_dir, f"INTA_{args.base_model}_{args.src_vendor}_to_{args.tgt_vendor}_{args.senario}_{current_time}")
    result_path_inter = os.path.join(args.output_dir, f"INTA_{args.base_model}_{args.src_vendor}_to_{args.tgt_vendor}_{args.senario}_{current_time}_wolLoop")
    result_path_report = os.path.join(args.output_dir, f"INTA_{args.base_model}_{args.src_vendor}_to_{args.tgt_vendor}_{args.senario}_{current_time}_report")
    result_path_vote = os.path.join(args.output_dir, f"VOTE_{args.base_model}_{args.src_vendor}_to_{args.tgt_vendor}_{args.senario}_{current_time}")

    logger.info(f"Result path: {result_path_llm}")
    logger.info(f"Result path: {result_path_inta}")
    logger.info(f"Result path: {result_path_inter}")
    logger.info(f"Result path: {result_path_report}")
    logger.info(f"Result path: {result_path_vote}")

    # Load hierarchy trees
    
    if src_hierarchy_file_path:
        src_hierarchy_root, src_all_clis = build_hierarchy_tree(src_hierarchy_file_path)
    if tgt_hierarchy_file_path:
        tgt_hierarchy_root, tgt_all_clis = build_hierarchy_tree(tgt_hierarchy_file_path)
    else:
        if args.tgt_cli_path:
            with open(args.tgt_cli_path, 'r') as fp:
               tgt_all_clis = ast.literal_eval(fp.read())
        else:
            logger.error("tgt_all_clis not given")
            
    

    # Files to exclude (for experiments)
    files_to_exclude = []


    files_to_translate = [fname for fname in os.listdir(args.src_config_path) if not os.path.isdir(os.path.join(args.src_config_path, fname)) if fname not in files_to_exclude]


    files_to_translate = [fname for fname in files_to_translate if fname.endswith(".txt") or fname.endswith(".cfg")]

    logger.info(f"Files to translate: {files_to_translate}")

    times = []

    llm_calls_total = 0

    for file_to_translate in files_to_translate:
        if not file_to_translate.endswith(".txt") and not file_to_translate.endswith(".cfg"):
            continue

        try:    # 避免小模型实验中遇到各种bug

            suffix = 'txt' if file_to_translate.endswith('.txt') else 'cfg'

            logger.info(f"################## Translating {file_to_translate} ##################")

            llm_calls_total += counter.count
            counter.reset()

            file_name = file_to_translate.split(f".{suffix}")[0]
            if args.ra_only and os.path.exists(os.path.join(args.src_config_path, file_name + ".division.json")) and not args.use_ext_config_division:
                logger.info(f"Skip {file_to_translate} (already divided)")
                continue
            config_start_time = time.time()

            # Read source and target configs
            src_config = open(os.path.join(args.src_config_path, file_to_translate), "r", encoding="utf-8").read()
            src_config_cmd = open(os.path.join(args.src_config_path_cmd, file_to_translate), "r", encoding="utf-8").read() if args.src_config_path_cmd else None
            # purified_config = purify_configuration(src_config, keep_manuals=False)
            # logger.info(purified_config)
            # continue

            if not src_config:
                logger.warning(f"Empty source config: {file_to_translate}")
                continue
            tgt_config = open(os.path.join(args.tgt_config_path, file_to_translate), "r", encoding="utf-8").read() if args.tgt_config_path else None

            logger.info(f"Source config:\n{src_config}")
            if src_config_cmd:
                logger.info(f"Source config (command):\n{src_config_cmd}")
            logger.info(f"Target config:\n{tgt_config}")    

            # Initialize Metrics
            EM, BLEU_1, BLEU_2, BLEU_3, BLEU_4 = 0, 0, 0, 0, 0
            ROUGE_1, ROUGE_2, ROUGE_L = 0, 0, 0
            TM, SC = 0, 0

            # LLM Translation
            if args.method == "LLM" or args.method == "VOTE":
                translation_llm = pure_llm(src_config, model=args.base_model)
                logger.info(f"Translation (llm): {translation_llm}")
                if not os.path.exists(result_path_llm):
                    os.makedirs(result_path_llm)
                with open(os.path.join(result_path_llm, f"{file_name}.{suffix}"), "w", encoding="utf-8") as f:
                    f.write(translation_llm)

            if args.method == "INTA" or args.method == "VOTE":
                src_config_root, src_manual_content_list = None, None
                if args.use_view:
                    logger.info(f"##### Building {DEVICE_NAME_DICT[args.src_vendor]} Config Tree #####")
                    ##### Build the source Config Tree #####    
                    src_config_root = build_config_tree(purify_configuration(src_config, keep_manuals=True), src_hierarchy_root, args.src_vendor)
                    src_config_root.print()
                    if src_config_cmd:
                        src_config_cmd_root = build_config_tree(purify_configuration(src_config_cmd, keep_manuals=True), src_hierarchy_root, args.src_vendor)
                        src_config_cmd_root.print()
                    # exit()
                    # continue

                    ##### Find the corresponding Nodes (Config Manual) in source command tree (exact) #####
                    src_manual_content_list = src_config_root.get_subtree_manual_content_list()

                ##### Get the division and intent of the source config #####
                if args.use_ext_config_division:
                    ext_config_division_path = os.path.join(args.src_config_path, file_name + ".division.json")
                    if not os.path.exists(ext_config_division_path):
                        logger.error(f"External config division file {ext_config_division_path} not found")
                        exit()
                    with open(ext_config_division_path, 'r', encoding='utf-8') as f:
                        config_division = json.load(f)
                    if args.use_view:
                        config_division = get_nodes_and_manuals(config_division, src_config_root, 'config')
                else:
                    config_division = get_division_and_intent(src_config, src_config_root, src_manual_content_list, model=args.base_model)
                if not config_division:
                    logger.info("Error: No config division found.")
                    continue
                
                if args.src_config_path_cmd and args.use_view:
                    config_division = get_nodes_and_manuals(config_division, src_config_cmd_root, 'cmd')
                logger.info(f"Config Division: {config_division}")


                retrieval_time = time.time()

                if not args.use_baseline:
                    ##### Retrieve Config Manuals #####
                    if not args.use_ext_config_retrieval:
                        config_division = retrieve_manuals(config_division, src_config, config_manual_path, ra_rounds=args.llm_filter_rounds, ra_top_k=args.config_retrieve_top_k, ra_top_k_ratio=args.manual_retrieve_ratio, retrieval_model=args.base_model, voting=not args.no_voting, emb_model=args.emb_model, use_mix=args.use_mix, selector=args.selector_config, manual_type='config')
                        logger.info(f"Config Division (after config retrieval): {config_division}")
                    else:
                        logger.info(f"Using external config retrieval...")

                    if args.use_cmd_manuals:
                        # ##### Retrieve Command Manuals #####
                        config_division = retrieve_manuals(config_division, src_config, cmd_manual_path, ra_rounds=args.llm_filter_rounds, ra_top_k=args.cmd_retrieve_top_k, ra_top_k_ratio=args.manual_retrieve_ratio, retrieval_model=args.base_model, voting=not args.no_voting, emb_model=args.emb_model, use_mix=args.use_mix, selector=args.selector_cmd, manual_type='cmd')
                        logger.info(f"Config Division (after cmd retrieval): {config_division}")

                        if not os.path.exists(f'logs/{current_time}_before_cross'):
                            os.makedirs(f'logs/{current_time}_before_cross')
                        with open(f'logs/{current_time}_before_cross/{file_name}.division.json', 'w', encoding='utf-8') as f:
                            f.write(json.dumps(config_division, indent=4, cls=MyJsonEncoder))

                        ##### Cross-retrieval #####
                        # for cmd
                        config_division = cross_retrieval_cmd(config_division, args.tgt_vendor, ra_top_k=args.cross_retrieve_top_k)
                        # for config

                    with open(f'logs/{current_time}/{file_name}.division.json', 'w', encoding='utf-8') as f:
                        f.write(json.dumps(config_division, indent=4, cls=MyJsonEncoder))
                    logger.info("Time cost for retrieval: " + str(time.time() - retrieval_time))

                if args.ra_only:
                    continue
                # exit()

                ##### translate fragments with syntax/view verification #####
                translation_time = time.time()
                translation_inta = rag_translation(config_division, top_k_ratio=args.rag_manuals_ratio, rag_top_k=args.rag_manuals_tok_k, tgt_hierarchy_root=tgt_hierarchy_root if args.use_view and not args.no_sLoop else None, tgt_all_clis=tgt_all_clis if not args.no_sLoop else None, model=args.base_model, use_baseline=args.use_baseline)
                if not translation_inta:
                    logger.info(f"Warning: No translations found for {file_to_translate}...")
                    continue
                if 'huawei' in args.tgt_vendor:
                    if not translation_inta.strip().startswith("system-view"):
                        translation_inta = "system-view\n" + translation_inta
                logger.info(f"Translation: {translation_inta}")
                logger.info("Time cost for translation: " + str(time.time() - translation_time))

                # 保存中间结果到 result_path_inter
                if not os.path.exists(result_path_inter):
                    os.makedirs(result_path_inter)
                with open(os.path.join(result_path_inter, f"{file_name}.{suffix}"), "w", encoding="utf-8") as f:
                    f.write(translation_inta)

                ##### semantic verification #####
                if not args.no_lLoop:
                    # refined_translation = 
                    if args.use_view:
                        # 语义检查后进行视图检查
                        # pass
                        logger.info("Use semantic verification...")
                        translation_inta, translated_cfg_comments_json, translated_config_tree_str = semantic_refinement_with_view(src_config, translation_inta, src_config_root, tgt_hierarchy_root, tgt_all_clis, config_division, model=args.base_model, top_k=int(args.rag_manuals_tok_k*1.5))

                        if not os.path.exists(result_path_report):
                            os.makedirs(result_path_report)
                        with open(os.path.join(result_path_report, f"{file_name}.semantic.json"), "w", encoding="utf-8") as f:
                            f.write(json.dumps(translated_cfg_comments_json, indent=4, cls=MyJsonEncoder))
                        with open(os.path.join(result_path_report, f"{file_name}.syntax.txt"), "w", encoding="utf-8") as f:
                            f.write(translated_config_tree_str)

                    else:
                        # 语义检查后进行语法检查
                        pass
                        # refined_translation = syntax_refinement(translation_inta, tgt_all_clis)

                if not os.path.exists(result_path_inta):
                    os.makedirs(result_path_inta)
                with open(os.path.join(result_path_inta, f"{file_name}.{suffix}"), "w", encoding="utf-8") as f:
                    f.write(translation_inta)
            
            if args.method == "VOTE":
                # 综合获取最佳翻译结果（LLM or INTA）
                if args.use_view:
                    pass
                else:
                    SC_LLM = get_syntax_correctness(translation_llm, tgt_all_clis)
                    SC_INTA = get_syntax_correctness(translation_inta, tgt_all_clis)
                    logger.info(f"LLM Translation: {translation_llm} (LLM syntax correctness: {SC_LLM})")
                    logger.info(f"INTA Translation: {translation_inta} (INTA syntax correctness: {SC_INTA})")
                    if SC_LLM > SC_INTA:
                        translation = translation_llm
                        SC = SC_LLM
                        logger.info(f"Final Translation (vote): LLM's version")
                    else:
                        translation = translation_inta
                        SC = SC_INTA
                        logger.info(f"Final Translation (vote): INTA's version")
                    if not os.path.exists(result_path_vote):
                        os.makedirs(result_path_vote)
                    with open(os.path.join(result_path_vote, f"{file_name}.{suffix}"), "w", encoding="utf-8") as f:
                        f.write(translation)
            
            config_end_time = time.time()
            logger.info(f"Time cost for {file_to_translate}: " + str(config_end_time - config_start_time))
            times.append(config_end_time - config_start_time)

        except Exception as e:
            logger.error(f"Error in translating {file_to_translate} ({e}), skipping...")
            continue

    llm_calls_total += counter.count
    logger.info(f"Total LLM calls: {llm_calls_total}")
    logger.info(f"Average time cost: {sum(times) / len(times)}s (Total: {sum(times)}s for {len(times)} files)")
    logger.info(f"Total prompt tokens: {total_prompt_tokens}, total completion tokens: {total_completion_tokens}")

    