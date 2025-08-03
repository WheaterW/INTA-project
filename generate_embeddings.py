# ====================================================
# Author: Yunze Wei <yunzewei@outlook.com>
# Date: 2025-08-03
# Description: Generates embeddings for command manuals and configurations.
# ====================================================
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from sentence_transformers import SentenceTransformer
from FlagEmbedding import BGEM3FlagModel
from sentence_transformers.util import cos_sim
from collect_corpus import find_desc
from utils import *
from FlagEmbedding import FlagReranker
from FlagEmbedding import FlagICLModel

# file  -> index 
#       -> embedding

model_name = 'bge-m3'  # 'sbert' or 'bge'
# model_name = 'qwen2-1.5b'  # 'sbert' or 'bge'
model_paths = {
    'sbert': 'sentence-transformers/all-mpnet-base-v2',
    'bge-m3': 'BAAI/bge-m3',
    'qwen2-1.5b': '/mnt/ssd0/Alibaba-NLP/gte-Qwen2-1.5B-instruct',   # 本地其他路径
    'gemini': 'gemini-embedding-exp-03-07'
}
corpus_type = 'manual'  # 'manual' or 'cmd'

class EmbeddingModel():
    def __init__(self, model_name, corpus_type='cmd'):
        logger.info(f"Using embedding model {model_name}")
        self.model_name = model_name
        self.model_path = model_paths[model_name] if model_name in model_paths else model_name
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        # self.device = 'cpu'
        logger.info(f'Using device: {self.device}')
        if model_name == 'sbert':
            self.model = SentenceTransformer(self.model_path)
            self.model.to(self.device)
        elif model_name == 'qwen2-1.5b':
            self.model = SentenceTransformer(self.model_path, trust_remote_code=True)
            self.model.max_seq_length = 8192
            self.model.to(self.device)
        elif model_name == 'bge-m3':
            self.model = BGEM3FlagModel(self.model_path)
            # self.model = SentenceTransformer(self.model_path)
            # self.model.to(self.device)
        elif model_name == 'bge-icl':   # TBD.
            examples = [
            {'instruct': 'Given a function description, retrieve the relevant manual',
            'query': 'Define a prefix list to match a specific IP prefix and prefix length range',
            'response': "Configuring an IP Prefix List: An IP prefix list matches IPv4 or IPv6 address prefixes, which are defined by an IP address and a mask length. (in /Configuration/IP_Routing/Routing_Policy_Configuration/Configuring_an_IP_Prefix_List)"},
            {'instruct': '',
            'query': '',
            'response': ""}
            ]
            self.model = FlagICLModel(self.model_path)
        elif '/' in model_name:   # 使用BGEM3FlagModel加载本地模型
            if 'bge' in model_name:
                logger.info(f"Using BGE model {model_name}")
                self.model = BGEM3FlagModel(self.model_path)
            else:
                self.model = SentenceTransformer(self.model_path)
                self.model.to(self.device)
        self.corpus_type = corpus_type  # 'manual' or 'cmd'
        self.embedding_path = "./corpus_embeddings/" + model_name + '/' + corpus_type + '/'
        logger.info(f"Embedding path: {self.embedding_path}")

    def get_embeddings(self, sentences, prompt_name=None, prompt=None):
        if self.model_name == 'sbert':
            embeddings = self.model.encode(sentences)
        elif self.model_name == 'bge-m3':
            embeddings = self.model.encode(sentences)['dense_vecs']
            # embeddings = self.model.encode(sentences)
        elif self.model_name == 'qwen2-1.5b':
            if prompt_name is not None:
                embeddings = self.model.encode(sentences, prompt_name=prompt_name)
            elif prompt is not None:
                embeddings = self.model.encode(sentences, prompt=prompt)
            else:
                embeddings = self.model.encode(sentences)
        elif self.model_name == 'gemini':
            embeddings_res = self.client.models.embed_content(
                model=self.model_path,
                contents=sentences,
            )
            embeddings = [item.values for item in embeddings_res.embeddings]
            # embeddings = list(map(lambda x: x.values, embeddings_res.embeddings))
        elif '/' in self.model_name:   # 使用BGEM3FlagModel加载本地模型
            if 'bge' in self.model_name:
                embeddings = self.model.encode(sentences)['dense_vecs']
            else:
                logger.error(f"Invalid model name {self.model_name}")
                exit()
        elif self.model_name == 'bge-icl':
            logger.error(f"Invalid model name {self.model_name}")
            exit()
        else:
            logger.error(f"Invalid model name {self.model_name}")
            exit()
        
        return embeddings

    def get_similarities(self, query_embedding, embeddings):
        similarities = cos_sim(query_embedding, embeddings)
        return similarities

# TBD.
class RerankerModel():
    def __init__(self, model_name='BAAI/bge-reranker-v2-m3', use_fp16=True):
        self.model = FlagReranker(model_name, use_fp16)
        
    def compute_score(self, list, normalize=False):
        return self.model.compute_score(list, normalize=normalize)

hw_corpus_path = 'nassim-main/corpus/hw/hw_NE40E_V800R012C10/cmd_corpus/'
hw_manual_path = 'nassim-main/corpus/hierarchy/cmd_manual_flat_old.json'

def generate_subtree_contexts(dir_path, base=0, manual_type='config', desc_type='desc', desc_dict=None):
    """
    Generate contexts for the subtree of the directory
    Args:
        dir_path: the path of the directory
        base: the base index of the contexts
        manual_type: the type of the manual, 'config' or 'cmd'
        desc_type: the type of the description, 'desc' or 'summarized_desc'
        desc_dict: the dict of the description, used for 'summarized_desc'
    Returns:
        contexts: a list of contexts
        index_to_filename: a dict mapping index to filename
        filename_to_index: a dict mapping filename to index
    """
    logger.debug(f"Calling generate_subtree_contexts with dir_path: {dir_path}, base: {base}, manual_type: {manual_type}, desc_type: {desc_type}")
    def recursive_list_dir(dir_path):
        if not os.path.isdir(dir_path):     # 合并输入单个文件的场景，这里有bug，会忽略文件夹描述
            # item_path = dir_path
            # file_path = dir_path.split('/')[-1]
            # dir_path = dir_path.split(file_path)[0]
            # dir_list = os.listdir(dir_path)
            # if not 'Overview' in file_path and not 'About_This_Document' in file_path and not 'Example' in file_path and not file_path.split('.')[0] in dir_list:
            #     files.append(item_path)
            #     # return  # bug
            # return 

            if manual_type == 'config' and len(find_cmds(dir_path)) > 0 or manual_type == 'cmd':    # 只考虑有cmd的config文档
                files.append(dir_path)
            return
        try:    # 避免大模型幻觉召回不存在的文件夹
            dir_list = os.listdir(dir_path)
        except:
            return
        for item in dir_list:
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                recursive_list_dir(item_path)
            else:
                if 'Overview' in item:
                    continue
                if 'About_This_Document' in item:
                    continue
                if 'Example' in item:
                    continue
                if item.split('.')[0] in dir_list:
                    # print(f"{item} describes the directory")
                    continue
                if manual_type == 'config' and len(find_cmds(item_path)) > 0 or manual_type == 'cmd': 
                    files.append(item_path)
        return
    
    def generate_contexts_config():
        for item in files:
            # print(item)
            # exit()
            if 'Overview' in item.split('/')[-1]:
                continue
            if 'About_This_Document' in item.split('/')[-1]:
                continue
            if 'Example' in item.split('/')[-1]:
                continue
            with open(item, 'r', encoding='utf-8') as f:
                lines = f.read()

            pattern = r"!\[\]\([^)]*\)"
            lines = re.sub(pattern, '', lines)

            ### retrieve description between === and ###
            desc = find_desc(lines).replace('\n', ' ')
            desc = item.split('.')[0].replace('_', ' ') if not desc else desc
            desc = transform_underline(desc)
            # print(f"{dir_path.split('/')[-1]+'/'+item}: {desc}")
            filename_to_index[item] = len(contexts) + base
            index_to_filename[str(len(contexts) + base)] = item

            # item_name = item.split('.')[0].replace('_', ' ')
            item_name = item.split('/')[-1].split('.')[0].replace('_', ' ')
            item_path = item.split('.')[0].replace('_', ' ')
            item_path = item_path.split('/Configuration/')[-1]
            item_path = item_path.replace('/', ' / ')
            item_parent = item.split('/')[-2].replace('_', ' ')
            item_folder = "/".join(item.split('config_corpus')[-1].split('/')[:-1])
            version_2_2 = f"{item_path}: {desc} (in '{item_parent}' folder)"
            logger.debug(f"Make context: {version_2_2}")
            # item_path = item_path.replace('/', ' > ')
            version_2_3 = f"{item_name}: {desc} ({item_path})"
            version_2_4 = f"{item_path}: {desc}"
            version_3 = f"{item_name}: {desc} ('{item_path}')"
            # logger.info(version_2_2)
            ### Explore the best context ###
            if desc_type == 'desc':
                # contexts.append(desc)   # version 1
                # contexts.append(f"{item_name}: {desc} (in {item.split('/')[-2]} folder)")  # version 2
                # contexts.append(f"{item_name}: {desc} (in {item_folder})")  # version 2.1
                # contexts.append(f"{item_path}: {desc} (in '{item_parent}' folder)")  # version 2.2 final
                contexts.append(version_2_2)  # version 2.2
            elif desc_type == 'summarized_desc':
                try:
                    if item.startswith('/root'):
                        item = item.split('/root/MyConfigTrans/')[-1]
                    desc = f"{version_2_2}\n{desc_dict[item]['desc']}"  # mix version 2.2 and desc_dict
                except:
                    # desc = f"{item_path}: {desc} (in '{item_parent}' folder)"
                    desc = version_2_2
                    # logger.error(f"Error: {item} not in desc_dict")
                    # exit()
                contexts.append(desc)
                # logger.info(desc)
                # exit()
            elif desc_type == 'full':
                contexts.append(lines)
            if contexts:
                logger.debug(f"Add context: {contexts[-1]}")
            
    def generate_contexts_cmd():
        for item in files:
            with open(item, 'r', encoding='utf-8') as f:
                cmd_json = json.load(f)
            if 'PageTitle' not in cmd_json:
                logger.error(f"Error: {item} not in cmd_json (missing PageTitle)")
                continue
            if 'CLIs' not in cmd_json:
                logger.error(f"Error: {item} not in cmd_json (missing CLIs)")
                continue
            if 'FuncDef' not in cmd_json:
                logger.error(f"Error: {item} not in cmd_json (missing FuncDef)")
                continue
            pagetitle = cmd_json['PageTitle']
            CLIs = "\n".join(cmd_json['CLIs'])
            desc = cmd_json['FuncDef']
            filename_to_index[item] = len(contexts) + base
            index_to_filename[str(len(contexts) + base)] = item
            item_path = item.split('.')[0].replace('_', ' ')
            item_path = item_path.split('/cmd_corpus/')[-1]
            item_path = item_path.replace('/', ' / ')
            version_1 = f"{pagetitle}: {desc}\n{CLIs}\n ({item_path})"
            # version_2 = f"{}" 

            contexts.append(version_1)


    files = []
    contexts = []
    index_to_filename = {}
    filename_to_index = {}
    recursive_list_dir(dir_path)
    if manual_type == 'config':
        logger.debug(f"Generate config contexts for {str(files)}")
        generate_contexts_config()
    elif manual_type == 'cmd':
        logger.debug(f"Generate cmd contexts for {str(files)}")
        generate_contexts_cmd()

    return contexts, index_to_filename, filename_to_index

if __name__ == '__main__':

    # 测试Embedding模型
    embedding_model = EmbeddingModel('gemini')
    context1 = 'hello world'
    context2 = ['hello world!', 'hello world!']
    
    embedding1 = embedding_model.get_embeddings(context1)
    print('embedding1:', embedding1, type(embedding1))
    embedding2 = embedding_model.get_embeddings(context2)
    print('embedding2:', embedding2, type(embedding2))
    print(embedding_model.get_similarities(embedding1, embedding2))
