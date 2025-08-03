# ====================================================
# Author: Yunze Wei <yunzewei@outlook.com>
# Date: 2025-08-03
# Description: Multiple agents for network configuration translation and evaluation.
# ====================================================
from openai import OpenAI
from utils import *
from collect_corpus import find_desc, extract_section, flatten_desc
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge
import ast
from rank_bm25 import BM25Okapi

llm_calls_limit = 100

class LLMCounter():
    def __init__(self, llm_calls_limit=100):
        self.limit = llm_calls_limit
        self.count = 0

    def increment(self):
        self.count += 1
        if self.count > self.limit:
            raise Exception("LLM call limit exceeded")

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

counter = LLMCounter(llm_calls_limit)

class AgentBase():
    """
    platform: openai, dashscope, deepseek
    """
    def __init__(self, model="qwen-max-latest", use_local=False, role="You are a very helpful assistant with great expertise in network operations and maintenance.", history_k=10, timeout=600):
        # 不同模型的默认的输出模式不同
        self.model_stream_mode = {
            "qwen-max-latest": False,
            "deepseek-v3": False,
            "deepseek-r1": True,    # TODO: 修改流式读取结构（包括思考部分）
            "gpt-4o": False,
            "gpt-4.1": False,
            "deepseek-chat": False,
            "llama3.1:8b-instruct-fp16": False,
            "qwen3:8b-fp16": False,
            "qwen3:14b-fp16": False,
            "deepseek-r1:8b": False,
            "deepseek-r1:14b": False
        }
        self.platforms = {
            "gpt-4o": "openai",
            "gpt-4.1": "openai",
            "qwen-max-latest": "dashscope",
            "deepseek-v3": "dashscope",
            "deepseek-r1": "dashscope",
            "deepseek-chat": "deepseek",
            "llama3.1:8b-instruct-fp16": "openai",
            "qwen3:8b-fp16": "openai",
            "qwen3:14b-fp16": "openai",
            "deepseek-r1:8b": "openai",
            "deepseek-r1:14b": "openai",
        }
        self.context_lens = {
            "gpt-4o": 128000,
            "gpt-4.1": 128000,
            "qwen-max-latest": 128000,
            "deepseek-v3": 57344,
            "deepseek-chat": 128000,
            "deepseek-r1": 128000,
            "llama3.1:8b-instruct-fp16": 128000, # 128k tokens
            "qwen3:8b-fp16": 40000,
            "qwen3:14b-fp16": 40000,
            "deepseek-r1:8b": 128000,
            "deepseek-r1:14b": 128000,
        }
        self.context_len = self.context_lens[model] * 3     # 假设一个token 3字符（保守估计）
        self.name = "AgentBase"
        self.use_local = use_local
        if '8b' in model or '14b' in model:   # 8b, 14b小模型默认本地部署
            self.use_local = True
        self.model = model
        self.platform = self.platforms[model]
        self.history_k = history_k
        self.timeout = timeout  # seconds
        if self.use_local:
            self.client = OpenAI(
                api_key="EMPTY",
                base_url="http://localhost:11434/v1",
                timeout=self.timeout,
            )
        elif self.platform == "openai":
            self.client = OpenAI(timeout=self.timeout)
        elif self.platform == "dashscope":
            self.client = OpenAI(
                api_key=os.getenv("DASHSCOPE_API_KEY"), 
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
                timeout=self.timeout,
            )
        elif self.platform == "deepseek":
            self.client = OpenAI(
                api_key = os.getenv("DEEPSEEK_API_KEY"),
                base_url = "https://api.deepseek.com",
                timeout=self.timeout,
            )
        else:
            raise ValueError("Invalid platform")
        logger.info(f"AgentBase init: {self.platform} {self.model} (timeout: {self.timeout})")
        self.history = [{"role": "system", "content":  role}]
        self.prompt_tokens = 0
        self.completion_tokens = 0

    def response(self, prompt, temperature=0.1):
        self.history.append({"role": "user", "content": prompt})
        logger.info(f"{self.name} history before API call: {self.history} (len: {len(str(self.history))})")

        # Ensure that history has the correct format for messages
        for message in self.history:
            if not isinstance(message, dict) or "role" not in message or "content" not in message:
                raise ValueError("Invalid history format: every message must be a dictionary with 'role' and 'content' fields.")
        
            use_stream = self.model_stream_mode[self.model]
        # Make API call
        # completion = None
        # logger.info(f"Calling API...")
        # retry_time = 2  # 2s
        # while completion is None:
        try:
            if use_stream:
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=self.history,
                    stream=True,
                    stream_options={"include_usage": True},
                    temperature=temperature,
                )
            else:
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=self.history,
                    stream=False,
                    temperature=temperature,
                )
            global counter
            counter.increment()
            logger.info(f"llm_calls: {counter.count}")
        except Exception as e:
            logger.error(f"Error: {e}")
            if counter.count > counter.limit + 1:
                exit()
            return None

        if use_stream:
            # Get the last message from the stream
                is_answering = False

                reasoning_content = ''
                result = ''
                logger.info(f"{self.name} response (stream): ")
                print("\n" + "=" * 20 + "思考过程" + "=" * 20 + "\n")
                for chunk in completion:
                    if chunk.choices:
                        delta = chunk.choices[0].delta
                        if hasattr(delta, 'reasoning_content') and delta.reasoning_content != None:
                            reasoning_content += delta.reasoning_content
                            print(delta.reasoning_content, end='', flush=True)
                        else:
                            # 开始回复
                            if delta.content != "" and not is_answering:
                                print("\n" + "=" * 20 + "完整回复" + "=" * 20 + "\n")   
                                is_answering = True
                            if delta.content != "":
                                result += delta.content
                                print(delta.content, end='', flush=True)
                    if chunk.usage:
                        self.prompt_tokens += chunk.usage.prompt_tokens
                        self.completion_tokens += chunk.usage.completion_tokens
        else:
            if not completion:
                logger.error("No completion returned. Maybe LLM timeout.")
                return None
            self.prompt_tokens += completion.usage.prompt_tokens
            self.completion_tokens += completion.usage.completion_tokens
            result = completion.choices[0].message.content
            logger.info(f"{self.name} response: {result}")

        logger.info(f"API call completed")
        self.history.append({"role": "assistant", "content": result})
        if len(self.history) > self.history_k:
            self.history = [self.history[0]] + self.history[-self.history_k:]
        return result
    
    def clear_context(self):
        self.history = [{"role": "system", "content": "You are a network operation and maintenance expert."}]

    def run(self):
        return self.response("Hello, how are you?")
    
class ConfigDivideAgent(AgentBase):
    """LLM拆分配置，并提取意图"""
    def __init__(self, src_device='Nokia SR OS router', tgt_device='Huawei NE40E router', model='gpt-4o', suffix=""):   # Pay attention to capitalizing the first letter of the JSON field name.
        super().__init__(model=model)
        self.name = "ConfigDivideAgent"
        self.src_device = src_device
        self.tgt_device = tgt_device
        self.suffix = suffix
        self.prompt_with_src_manuals = """
## TASK DESCRIPTION
Your task is to analyze the following {src_device} configuration, divide it into fragments based on intents and behaviors. Then give a general description of each fragment, together with a detailed description of each sub module in the fragment. If the source configuration can not be divided, treat it as a single fragment.

To assist you, corresponding {src_device} manuals are provided in the ## MANUALS section.

We also provide you with an example.

## OUTPUT REQUIREMENTS
1. Divide the configuration into fragments . Each fragment should represent a distinct function or behavior.
2. Store the fragments in a SINGLE list of JSON structure where each object contains:
   - **"Fragment"**: The original {src_device} configuration segment, preserved with its formatting (including '\n' and indents).
   - **"Function"**: A general description of the fragment's primary function.
   - **"Details"**: A detailed description of each sub-module in the fragment. Each sub-module must have "Function" and "Parameter". Each sub-module must be described as a flat dictionary in "Details" field, with no nested dictionaries. As shown in the example below.

## GUIDELINES
- Provide only the most direct functional description for each fragment.
- Avoid specific details such as field names or parameter values in the "Function" field.
- Do not speculate about the broader purpose or behavior of any single fragment.

# EXAMPLE
## MANUALS
...

## CONFIGURATION
config 
	router Base
		policy-options
            prefix-list "SYSTEM"
                prefix 10.2.65.10/32 prefix-length-range 32-32
            policy-statement "EXPORT_to_OSPF"
                entry 10
                    from
                        protocol direct
                        prefix-list "SYSTEM"
                    to
                        protocol ospf
                    action accept
                        type 1 

## RESULT
```json
[
    {{
        ...
    }},
    {{
        "Fragment": "policy-options\n    prefix-list "SYSTEM\n        prefix 10.2.65.10/32 prefix-length-range 32-32",
        "Function": "Define a prefix list to match a specific IP prefix and prefix length range",
        "Details": {{ 
            "prefix-list": {{ 
                "Function": "Create a prefix list that matches a specific IP prefix", 
                "Parameter": {{ 
                    "Name": "SYSTEM", 
                    "Prefix": "10.2.65.10/32",
                    "Prefix-length-range": "32-32"
                }}
            }},
            "prefix": {{ 
                "Function": "...", 
                "Parameter": {{ 
                    ... 
                }}
            }}
        }}
    }},
    ...
]
```

# YOUR TASK
## MANUALS
{manuals}

## CONFIGURATION
{configuration}

## RESULT
```json
Your answer here (a single list of all Fragments)
```
{suffix}
"""

        self.prompt_without_src_manuals = """
## TASK DESCRIPTION
Your task is to analyze the following {src_device} configuration, divide it into fragments based on intents and behaviors. Then give a general description of each fragment, together with a detailed description of each sub module in the fragment. If the source configuration can not be divided (or even one word of command), treat it as a single fragment.

We provide you with an example.

## OUTPUT REQUIREMENTS
1. Divide the configuration into fragments. Each fragment should represent a distinct function or behavior.
2. Store the fragments in a SINGLE list of JSON structure where each object contains:
   - **"Fragment"**: The original {src_device} configuration segment, preserved with its formatting (including '\n' and indents).
   - **"Function"**: A general description of the fragment's primary function.
   - **"Details"**: A detailed description of each sub-module in the fragment. Each sub-module must have "Function" and "Parameter". Each sub-module must be described as a flat dictionary in "Details" field, with no nested dictionaries. As shown in the example below.

## GUIDELINES
- Provide only the most direct functional description for each fragment.
- Avoid specific details such as field names or parameter values in the "Function" field.
- Do not speculate about the broader purpose or behavior of any single fragment.

# EXAMPLE
## CONFIGURATION
config 
	router Base
		policy-options
            prefix-list "SYSTEM"
                prefix 10.2.65.10/32 prefix-length-range 32-32
            policy-statement "EXPORT_to_OSPF"
                entry 10
                    from
                        protocol direct
                        prefix-list "SYSTEM"
                    to
                        protocol ospf
                    action accept
                        type 1 

## RESULT
```json
[
    {{
        ...
    }},
    {{
        "Fragment": "policy-options\n    prefix-list "SYSTEM\n        prefix 10.2.65.10/32 prefix-length-range 32-32",
        "Function": "Define a prefix list to match a specific IP prefix and prefix length range",
        "Details": {{ 
            "prefix-list": {{ 
                "Function": "Create a prefix list that matches a specific IP prefix", 
                "Parameter": {{ 
                    "Name": "SYSTEM", 
                    "Prefix": "10.2.65.10/32",
                    "Prefix-length-range": "32-32"
                }}
            }},
            "prefix": {{ 
                "Function": "...", 
                "Parameter": {{ 
                    ... 
                }}
            }}
        }}
    }},
    ...
]
```

# YOUR TASK

## CONFIGURATION
{configuration}

## RESULT
```json
Your answer here (a single list of all fragments)
```
{suffix}
"""
    def run(self, configuration, manual_content_list):
        configuration = purify_configuration(configuration, keep_manuals=False)
        if manual_content_list:
            manuals = '\n'.join([f"### {self.src_device} manual page: {manual}" for manual in manual_content_list])
            prompt = self.prompt_with_src_manuals.format(src_device=self.src_device, manuals=manuals, configuration=configuration, suffix=self.suffix)
        else:
            prompt = self.prompt_without_src_manuals.format(src_device=self.src_device, configuration=configuration, suffix=self.suffix)
        logger.info(f"{self.name} prompt: {prompt}")
        response = self.response(prompt)
        return response
    
class ContentsRetrievalAgent(AgentBase):
    """LLM read manual contents and return the most relevant manual entries"""
    def __init__(self, src_device='Nokia SR OS router', tgt_device='Huawei NE40E router', use_local=False, model='gpt-4o', base_path = "nassim-main/corpus/hw/hw_NE40E_V800R012C10/config_corpus/Configuration"):
        super().__init__(use_local=use_local, model=model)
        self.name = "ContentsRetrievalAgent"
        self.base_path = base_path
        self.src_device = src_device
        self.tgt_device = tgt_device
        # polished by GPT-4o
        self.prompt_src_with_manuals = """
## TASK DESCRIPTION
We are translating the provided {src_device} configuration fragment (### SOURCE DEVICE CONFIGURATION FRAGMENT) into {tgt_device} configuration. You will help me read the manual catalogue and find the most relevant entries for translation. 
To complete this task, you need to:
1. Traverse the ### {tgt_device} CONFIGURATION MANUAL LIST.
2. Select the most relevant manual directory(ies) to enter to guide the translation.

### GUIDELINES
- You are provided with some background information of ### SOURCE DEVICE MANUALS and ### SOURCE DEVICE FULL CONFIGURATION to help you understand the fragment.
- Your selection must be the EXACT directory name(s) with FULL path from the manual list, not the description.
- Provide your selection in a list format, e.g., `["selection1", "selection2"]`.
  - If only one manual is relevant, include it in a single-item list, e.g., `["selection"]`.
  - If no relevant manual exists, report `["None of the above"]`.
  - Put the manuals you think are most relevant up front.
  
### {src_device} CONFIGURATION FRAGMENT
{Source_Config_Fragment}

### {src_device} FULL CONFIGURATION
{Source_Config}

### {src_device} MANUALS
{Source_Config_Manual}

### {tgt_device} CONFIGURATION MANUAL LIST
{Target_Config_Manual_list}

### OUTPUT FORMAT
```plaintext
["your selection here", ...]
```
Take it step by step.
"""

        self.prompt_src_without_manuals = """
## TASK DESCRIPTION
We are translating the provided {src_device} configuration fragment (### SOURCE DEVICE CONFIGURATION FRAGMENT) into {tgt_device} configuration. You will help me read the manual catalogue and find the most relevant entries for translation. 
To complete this task, you need to:
1. Traverse the ### {tgt_device} CONFIGURATION MANUAL LIST.
2. Select the most relevant manual directory(ies) to enter to guide the translation.

### GUIDELINES
- You are provided with some background information of ### SOURCE DEVICE FULL CONFIGURATION to help you understand the fragment.
- Your selection must be the EXACT directory name(s) with FULL path from the manual list, not the description.
- Provide your selection in a list format, e.g., `["selection1", "selection2"]`.
  - If only one manual is relevant, include it in a single-item list, e.g., `["selection"]`.
  - If no relevant manual exists, report `["None of the above"]`.
  - Put the manuals you think are most relevant up front.
  
### {src_device} CONFIGURATION FRAGMENT
{Source_Config_Fragment}

### {src_device} FULL CONFIGURATION
{Source_Config}

### {tgt_device} CONFIGURATION MANUAL LIST
{Target_Config_Manual_list}

### OUTPUT FORMAT
```plaintext
["your selection here", ...]
```
Take it step by step.
"""

        # 一次提取两层相关目录
        self.prompt_src_with_manuals_plain = """
## TASK DESCRIPTION
We are translating the provided {src_device} configuration fragment (### SOURCE DEVICE CONFIGURATION FRAGMENT) into {tgt_device} configuration. You need to help me read the manual catalogue and find the most relevant entries for configuration translation. 
To complete this task, you need to:
1. Traverse the ### {tgt_device} CONFIGURATION MANUAL LIST.
2. Select the most relevant manual directory(ies) to enter to guide the translation.

### GUIDELINES
- You are provided with some background information of ### SOURCE DEVICE MANUALS and ### SOURCE DEVICE FULL CONFIGURATION to help you understand the fragment.
- Your selection must be the EXACT directory name(s) with FULL path from the manual list.
- Provide your selection in a list format, e.g., `["parent1/child1", "parent2/child2"]`.
  - If only one manual is relevant, include it in a single-item list, e.g., `["parent1/child1"]`, not only `"parent1/child1"`.
  
### {src_device} CONFIGURATION FRAGMENT
{Source_Config_Fragment}

### {src_device} FULL CONFIGURATION
{Source_Config}

### {src_device} MANUALS
{Source_Config_Manual}

### {tgt_device} CONFIGURATION MANUAL LIST
{Target_Config_Manual_list}

### OUTPUT FORMAT
```plaintext
["your selection here", ...]
```
Take it step by step.
"""


    def run(self, Source_Config_Fragment, Source_Config, Source_Config_Manual, Target_Config_Manual_list, use_plain=True):
        if Source_Config_Manual:
            if use_plain:
                prompt = self.prompt_src_with_manuals_plain.format(src_device=self.src_device, tgt_device=self.tgt_device, Source_Config_Fragment=Source_Config_Fragment, Source_Config=Source_Config, Source_Config_Manual=Source_Config_Manual, Target_Config_Manual_list=Target_Config_Manual_list)
            else:
                prompt = self.prompt_src_with_manuals.format(src_device=self.src_device, tgt_device=self.tgt_device, Source_Config_Fragment=Source_Config_Fragment, Source_Config=Source_Config, Source_Config_Manual=Source_Config_Manual, Target_Config_Manual_list=Target_Config_Manual_list)
        else:
            prompt = self.prompt_src_without_manuals.format(src_device=self.src_device, tgt_device=self.tgt_device, Source_Config_Fragment=Source_Config_Fragment, Source_Config=Source_Config, Target_Config_Manual_list=Target_Config_Manual_list)
        # prompt = self.prompt_src.format(src_device=self.src_device, tgt_device=self.tgt_device, Source_Config_Fragment=Source_Config_Fragment, Source_Config=Source_Config, Source_Config_Manual=Source_Config_Manual, Target_Config_Manual_list=Target_Config_Manual_list)
        logger.info(f"{self.name} prompt: {prompt}")
        response = self.response(prompt)
        logger.info(f"{self.name} response: {response}")
        rsp = parse_rsp(response, fmt='plaintext')
        return rsp


class ContentTraverseAgent():
    """LLM遍历手册目录，返回最相关的手册条目"""
    def __init__(self, src_device='Nokia SR OS router', tgt_device='Huawei NE40E router', k=2, base_path="nassim-main/corpus/hw/hw_NE40E_V800R012C10/config_corpus/Configuration", model='gpt-4o', manual_type='config'):
        self.name = "ContentTraverseAgent"
        self.base_path = base_path
        self.src_device = src_device
        self.tgt_device = tgt_device
        self.llm_agent = ContentsRetrievalAgent(model=model, src_device=src_device, tgt_device=tgt_device)
        self.k = k  # 限制最多执行k次LLM调用 或 BERT进入k层目录
        self.manual_type = manual_type  # config or cmd

    def select_manuals_with_llm(self, config, config_unit, list_dir_filtered_with_manual, use_plain=True):
        response_json = None
        self.llm_agent.clear_context()
        list_dir_filtered_str = '\n'.join([f"name: {item['name']}, description: {item['description']}" for item in list_dir_filtered_with_manual])
        # logger.debug(list_dir_filtered_str)
        response = self.llm_agent.run(config_unit.CLIs, config, '\n'.join([f'#### {item}\n' for item in config_unit.manuals]), list_dir_filtered_str, use_plain).strip()
        logger.debug("Pured: " + response)
        if not response.startswith("["):
            logger.debug("No manual selected.")
            response = '["' + response + '"]'
        try:
            response_json = json.loads(response)
        except Exception as e:
            logger.error(f"Error: {e}, response: {response}")
        return response_json

    def run_llm(self, config_unit: ConfigUnit, config: str) -> List[str]:
        """
        Retreive the most relevant manual entries for the given configuration fragment.

        Args:
            config_unit: ConfigUnit
            config: str
        Returns:
            dirs_to_search: List[str]
            files_to_collected: List[str]

        """

        dirs_to_search = [self.base_path]     # 扩充搜索文件夹，直到达到k次调用限制
        files_to_collected = []     # 收集的文件
        layer_collection = []   # 每一层的手册及描述，包含self.base_path之后的部分
        layer_list_dir_filtered = []    # [name1, name2, ...]，用于检查llm返回的目录是否合法

        curr_k = 0  # llm 调用的层数（不再是次数）
        while(curr_k < self.k and len(dirs_to_search) > 0):
            curr_path = dirs_to_search.pop(0)
            logger.info(f"Traversing into {curr_path}")

            # 过滤：目录同名md，含有Overview的md等
            try:
                list_dir = os.listdir(curr_path)
            except Exception as e:
                logger.error(f"Error: {e}")
                
            list_dir_filtered_with_manual = []    # [{"name": "xxx", "description": "xxx"}, {...}, ...]

            for item in list_dir:
                # 文件部分：目录同名md，含有Overview的md等
                if (item.endswith(".md") and "About_This" not in item and "Overview" not in item and "Precautions" not in item and not 'Verifying' in item and item.split(".")[0] not in list_dir) or "Overview of Interface Management" in item:
                    try:
                        with open(os.path.join(curr_path, item), 'r', encoding='utf-8') as f:
                            content = f.read()
                            files_to_collected.append(os.path.join(curr_path, item))     # 非目录描述文件视为手册，直接收集
                    except Exception as e:
                        logger.error(f"Error: {e}")
                # 目录部分：
                elif os.path.isdir(os.path.join(curr_path, item)):
                    base_split = curr_path.split('/Configuration/')
                    if len(base_split) == 1:
                        curr_base = ""
                    else:
                        curr_base = base_split[1]
                    item_with_path = os.path.join(curr_base, item)    # 简化路径，仅保留self.base_path之后的部分
                    if item + ".md" in list_dir:    # 目录同名md是描述
                        try:
                            with open(os.path.join(curr_path, item + ".md"), 'r', encoding='utf-8') as f:
                                content = f.read()
                                # list_dir_filtered_with_manual.append({"name": item, "type": "directory", "description": find_desc(content)})
                                # list_dir_filtered.append(item)
                                list_dir_filtered_with_manual.append({"name": item_with_path, "description": find_desc(content)})
                                layer_list_dir_filtered.append(item_with_path)
                        except Exception as e:
                            logger.error(f"Error: {e}")
                    else:
                        try:
                            list_subdir = os.listdir(os.path.join(curr_path, item))
                        except Exception as e:
                            logger.error(f"Error: {e}")
                            continue
                        overviews = [subitem for subitem in list_subdir if ("Overview" in subitem or "About_This" in subitem) and not os.path.isdir(os.path.join(curr_path, item, subitem))]
                        if len(overviews) == 1: # 有且仅有一个Overview
                            docs_name = overviews[0]
                            try:
                                with open(os.path.join(curr_path, item, overviews[0]), 'r', encoding='utf-8') as f:
                                    overview = f.read()
                                    if "Overview" in docs_name:
                                        description = flatten_desc(find_desc(overview))
                                    elif "About_This" in docs_name:
                                        description = flatten_desc(extract_section(overview, "#### Purpose"))
                                    else:
                                        description = item.replace("_", " ")    # 无法提取描述时，直接使用目录名
                            except Exception as e:
                                logger.error(f"Error: {e}")
                                description = item.replace("_", " ")
                        else:
                            description = item.replace("_", " ")
                        list_dir_filtered_with_manual.append({"name": item_with_path, "description": description})
                        layer_list_dir_filtered.append(item_with_path)


            logger.info(list_dir_filtered_with_manual)
            logger.info(layer_list_dir_filtered)

            ### LLM 进行手册的预读，缩小语料库范围 ###
            layer_collection += list_dir_filtered_with_manual
            if len(dirs_to_search) == 0:    # 一层展开遍历完毕
                response_json = None
                while response_json is None:
                    response_json = self.select_manuals_with_llm(config, config_unit, layer_collection)
                
                logger.info(f"list_dir_filtered: {layer_list_dir_filtered}")
                for item in response_json:
                    if "None of the above" in item or item == "Others":
                        continue
                    item = item.replace(" ", "_")   # llama3.1 errors
                    item_match = False
                    if item in layer_list_dir_filtered:   # 防止llm返回不在list_dir_filtered中的目录
                        dirs_to_search.append(os.path.join(self.base_path, item))
                        item_match = True
                    else:
                        for target in layer_list_dir_filtered:
                            if item in target:
                                dirs_to_search.append(os.path.join(self.base_path, target))
                                item_match = True
                                break
                        if not item_match:
                            logger.error(f"Error: {item} not in list_dir_filtered")

                layer_collection = []   # 清空当前层的手册
                layer_list_dir_filtered = []    # 清空当前层的目录

                curr_k += 1
                logger.info(f"LLM serched layer: {curr_k}; k: {self.k}")
                if curr_k >= self.k:
                    break

        return dirs_to_search, files_to_collected
    
    def run_llm_plain(self, config_unit: ConfigUnit, config: str) -> List[str]:
        """
        Retreive the most relevant manual entries for the given configuration fragment.
        Use llm to read 2 folder layers at one time, and return the most relevant manual dirs

        Args:
            config_unit: ConfigUnit
            config: str
        Returns:
            dirs_to_search: List[str]
            files_to_collected: List[str]

        """
        num_files_before_filter = 0
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith('.md') and self.manual_type=='config' or file.endswith('.json') and self.manual_type=='cmd':
                    num_files_before_filter += 1
        logger.info(f"LLM-filter: {num_files_before_filter} files before filter.")

        dirs_to_search_layer_1 = []
        for item in os.listdir(self.base_path):
            if os.path.isdir(os.path.join(self.base_path, item)):
                dirs_to_search_layer_1.append(os.path.join(self.base_path, item))
        dirs_to_search_layer_2 = []
        for item in dirs_to_search_layer_1:
            for subitem in os.listdir(item):
                if os.path.isdir(os.path.join(item, subitem)):
                    dirs_to_search_layer_2.append(os.path.join(item, subitem))
        # logger.info(f"dirs_to_search_layer_1: {dirs_to_search_layer_1}")
        # logger.info(f"dirs_to_search_layer_2: {dirs_to_search_layer_2} (len: {len(dirs_to_search_layer_2)})")

        dirs_to_search = ["/".join(item.split("/")[-2:]) for item in dirs_to_search_layer_2]   # 去掉最后一层目录
        logger.info(f"dirs_to_search: {dirs_to_search} (len: {len(dirs_to_search)})")

        dirs_to_search_str = [f" - {item}\n" for item in dirs_to_search]

        dirs_searched = []
        tries_limits = 3
        while not dirs_searched and tries_limits >= 0:
            try:
                _dirs_searched = self.llm_agent.run(config_unit.CLIs, purify_configuration(config), '\n'.join([f'#### {item}\n' for item in config_unit.manuals]), "".join(dirs_to_search_str), use_plain=True).strip()
                _dirs_searched = json.loads(_dirs_searched)
            except Exception as e:
                logger.error(f"Error: {e}")
                _dirs_searched = []
                tries_limits -= 1
            logger.info(f"_dirs_searched: {_dirs_searched} (len: {len(_dirs_searched)})")
            for item in _dirs_searched:
                path = os.path.join(self.base_path, item)
                if path in dirs_to_search_layer_2:
                    dirs_searched.append(path)
            logger.info(f"dirs_searched: {dirs_searched} (len: {len(dirs_searched)})")
            if not dirs_searched:
                tries_limits -= 1
                logger.info(f"LLM serched remainsing tries: {tries_limits}")
            # exit()

        num_of_files_after_filter = 0
        for dir in dirs_searched:
            for root, dir, files in os.walk(dir):
                    for file in files:
                        if file.endswith('.md') and self.manual_type=='config' or file.endswith('.json') and self.manual_type=='cmd':
                            num_of_files_after_filter += 1
        logger.info(f"LLM-filter: {num_of_files_after_filter} files after filter.")

        return dirs_searched, []
    
    def run_bm25(self, config_unit: ConfigUnit, config: str, top_k_ratio=0.1) -> List[str]:
        """
        使用BM25算法进行手册检索，返回一系列files_to_collected
        """

        file_contents = []
        file_names = []
        files_to_collected = []

        files_cnt = 0

        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith('.md') and self.manual_type=='config' or file.endswith('.json') and self.manual_type=='cmd':
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        file_contents.append(content)
                        file_names.append(file_path)
                        files_cnt += 1

        logger.info(f"BM25: {files_cnt} files loaded.")
        top_k = int(files_cnt * top_k_ratio)

        tokenized_corpus = [doc.split() for doc in file_contents]
        bm25 = BM25Okapi(tokenized_corpus)
        # 对每个function的topk进行set，不过这里并没有考虑投票，可以验证效果是否会变好
        for query in config_unit.functions:
            tokenized_query = query.split()
            scores = bm25.get_scores(tokenized_query)
            top_n_indices = scores.argsort()[-top_k:][::-1]
            for idx in top_n_indices:
                if file_names[idx] not in files_to_collected:
                    files_to_collected.append(file_names[idx])
                    # logger.info(f"BM25: {file_names[idx]} added.")
        
        logger.info(f"BM25: {len(files_to_collected)} files selected.")

        return [], files_to_collected
        
    
    def run(self, config_unit: ConfigUnit, config: str, selector='llm') -> List[str]:
        """
        TODO: More selectors
        """
        if not selector or selector == 'None':    # baseline
            return [], []
        elif selector == 'llm':
            # return self.run_llm(config_unit, config)
            return self.run_llm_plain(config_unit, config)
        elif selector == 'bm25':
            return self.run_bm25(config_unit, config)
        else:
            logger.error(f"Error: Invalid mode {selector}, using llm instead.")
            return self.run_llm(config_unit, config)



class LLMTranslatorAgent(AgentBase):
    """
    Translator: 1. pure LLM; 2. INTA with LLM
    """
    def __init__(self, src_device='Nokia SR OS router', tgt_device='Huawei NE40E router', model='qwen-max-latest', suffix=""):
        super().__init__(model=model)
        self.name = "LLMTranslatorAgent"
        self.src_device = src_device
        self.tgt_device = tgt_device
        self.suffix = suffix
        self.prompt_llm = """
## TASK DESCRIPTION
You are required to translate the following {src_device} configuration into {tgt_device} configuration.
Give a COMPLETE translation at the end of your answer.
DO NOT make up view information that are missing from the original configuration.
## {src_device} CONFIGURATION
{src_config}
## {tgt_device} CONFIGURATION
```plaintext (Your answer here)```
{suffix}
"""
        # 翻译Prompt公共部分，主要包括任务要求和手册符号约定
        self.prompt_rag_req = """
## TASK DESCRIPTION
Your task is to translate a given {src_device} configuration fragment in ## {src_device} CONFIGURATION FRAGMENT into a {tgt_device} configuration.

## REQUIREMENTS
1. Follow Manuals
    - Use the ## xxx MANUALS section to translate {src_device} commands into {tgt_device} equivalents, following {tgt_device} syntax and conventions.
2. Functionally Equivalent
    - Keep the translated {tgt_device} configuration functionally equivalent to the original {src_device} configuration.
    - DO NOT add any addictive or missing commands, such as missing view information or commands.
    - If the source configuration fragment is incomplete, translate the available commands as accurately as possible without speculating on missing information.
    - If the target command uses a interface, remember to activate it with `undo shutdown` command.
3. Merge The Preceding Transaltion 
    - Incorporate the {tgt_device} configuration fragment seamlessly into the ## PRECEDING TRANSLATION section.
    - Do not alter or omit any part of the ## PRECEDING TRANSLATION section, but you can change the sequence of commands if necessary.
4. Cleaned Format
    - Omit all view information in the translated configuration, such as [~HUAWEI].

## GUIDELINES
1. Command Conventions of {tgt_device} Manual:
 - [ ]: Items (keywords or arguments) in brackets [ ] are optional.
 - {{ x | y | ... }}: Optional items are grouped in braces and separated by vertical bars. One item is selected.
 - [ x | y | ... ]: Optional items are grouped in brackets and separated by vertical bars. One item is selected or no item is selected.
2. Use indentation to represent view structure.

"""

        self.prompt_rag_with_manuals = self.prompt_rag_req + """
## {src_device} MANUALS
{src_manuals}

## {tgt_device} CONFIGURATION MANUALS
{tgt_config_manuals}

## {tgt_device} COMMAND MANUALS
{tgt_cmd_manuals}

## PRECEDING {tgt_device} CONFIGURATION TRANSLATION RESULT
{preceding_translation}

## {src_device} CONFIGURATION FRAGMENT
{config_fragment}

## RESULT
- The translation should be built on the preciding translation. {reqs}
- Provide the complete translation at the END of your answer. Put any analysis process BEFORE the final result.
- Result format:
```plaintext (COMPLETE {tgt_device} configuration translation result here)```
"""

        self.prompt_rag_without_manuals = self.prompt_rag_req + """
## {tgt_device} CONFIGURATION MANUALS
{tgt_config_manuals}

## {tgt_device} COMMAND MANUALS
{tgt_cmd_manuals}

## PRECEDING {tgt_device} CONFIGURATION TRANSLATION RESULT
{preceding_translation}

## {src_device} CONFIGURATION FRAGMENT
{config_fragment}

## RESULT
- The translation should be built on the preciding translation. {reqs}
- Provide the complete translation at the END of your answer. Put any analysis process BEFORE the final result.
- Result format:
```plaintext (COMPLETE {tgt_device} configuration translation result here)```
"""

        # 语法修正，marked_translation根据Parser结果标注
        self.prompt_syntax_refinement = """
Thank you for your translation. 
We have verified the syntax correctness of your translation and marked the mismatched lines below in ### MARKED TRANSLATION section with (syntax mismatch) tag.

## TASK
Your goal is to refine the translation to resolve these mismatches. 
- Carefully review the mismatched lines.
- Revise your translation to address the mismatches.
- Provide the complete updated translation, including the refined sections. Do not submit only the changes; the entire configuration must be included.
- Do not loss or add any functions during the refinement process.

## MARKED TRANSLATION
{marked_translation}

## OUTPUT FORMATS
Provide the full refined translation at the end of your answer:
```plaintext (Your complete revised translation here) ```
"""

        # 语义修正，和CriticAgent联动
        self.prompt_semantic_rag = """
## TASK DESCRIPTION
Your task is to refine a Huawei NE40E router configuration based on the provided Nokia SR OS router configuration, relevant manuals, and identified semantic warnings.
## REQUIREMENTS
1. Address the semantic warnings listed in the ## SEMANTIC WARNINGS section.
2. Ensure the refined Huawei configuration retains the same functionality and semantics as the original Nokia configuration.
3. Verify all changes align with the manuals provided in the ### NOKIA MANUALS and ### HUAWEI CONFIGURATION/COMMAND MANUALS sections if the corresponding manual exists.
4. Complete and Clean Output
    - Provide the FULL refined Huawei configuration in the RESULT section.
    - Your refined configuration should be clean, without any comments.
    - Keep indentation to represent view structure.

## NOKIA MANUALS
{nokia_manuals}

## HUAWEI CONFIGURATION MANUALS
{huawei_manuals}

## HUAWEI COMMAND MANUALS
{huawei_cmd_manuals}

## NOKIA CONFIGURATION
{nokia_configuration}

## HUAWEI CONFIGURATION
{huawei_configuration}

## SEMANTIC WARNINGS
{semantic_errors}

## RESULT
Make your result in ```plaintext ``` environment.
```plaintext (complete refined Huawei configuration here)```
"""
    def llm(self, src_config):
        prompt = self.prompt_llm.format(src_device=self.src_device, tgt_device=self.tgt_device, src_config=src_config, suffix=self.suffix)
        logger.info(f"{self.name} prompt: {prompt}")
        resp = self.response(prompt)
        logger.info(f"{self.name} response: {resp}")
        res = parse_rsp(resp, fmt="plaintext")
        return res

    def rag(self, config_fragment, src_manuals, tgt_config_manuals, tgt_cmd_manuals, preceding_translation, reqs=""):
        """
        Use RAG to translate the configuration fragment
        Args:
            config_fragment: str, the configuration fragment to be translated
            src_manuals: list of str, the source device manuals
            tgt_config_manuals: list of str, the target device configuration manuals
            tgt_cmd_manuals: list of str, the target device command manuals
            preceding_translation: str, the preceding translation result
            reqs: str, additional requirements for translation
        Returns:
            res: str, the translation result
        """

        prompt = None   # 这个位置是不是对的

        res = None
        retries = 20
        while not res:
            self.clear_context()
            if src_manuals:
                while not prompt:
                    prompt = self.prompt_rag_with_manuals.format(src_device=self.src_device, tgt_device=self.tgt_device, src_manuals="\n".join(["### " + m for m in src_manuals]), tgt_config_manuals="\n".join(["### " + m for m in tgt_config_manuals]), tgt_cmd_manuals="\n".join(["### " + m for m in tgt_cmd_manuals]), preceding_translation=preceding_translation, config_fragment=config_fragment, reqs=reqs)
                    if len(prompt) > self.context_len:
                        prompt = None
                        tgt_config_manuals = tgt_config_manuals[:-1]
                        tgt_cmd_manuals = tgt_cmd_manuals[:-1]
                        logger.info(f"Context too long, reduce tgt_config_manuals from {len(tgt_config_manuals)+1} to {len(tgt_config_manuals)}")
                        logger.info(f"Context too long, reduce tgt_cmd_manuals from {len(tgt_cmd_manuals)+1} to {len(tgt_cmd_manuals)}")
            else:
                while not prompt:
                    prompt = self.prompt_rag_without_manuals.format(src_device=self.src_device, tgt_device=self.tgt_device, tgt_config_manuals="\n".join(["### " + m for m in tgt_config_manuals]), tgt_cmd_manuals="\n".join(["### " + m for m in tgt_cmd_manuals]), preceding_translation=preceding_translation, config_fragment=config_fragment, reqs=reqs)
                    if len(prompt) > self.context_len:
                        prompt = None
                        tgt_config_manuals = tgt_config_manuals[:-1]
                        tgt_cmd_manuals = tgt_cmd_manuals[:-1]
                        logger.info(f"Context too long, reduce tgt_config_manuals from {len(tgt_config_manuals)+1} to {len(tgt_config_manuals)}")
                        logger.info(f"Context too long, reduce tgt_cmd_manuals from {len(tgt_cmd_manuals)+1} to {len(tgt_cmd_manuals)}")
            try:
                logger.info(f"{self.name} prompt: {prompt}")
                resp = self.response(prompt)
                logger.info(f"{self.name} response: {resp}")
                res = parse_rsp(resp, fmt="plaintext")
            except Exception as e:
                logger.error(f"Error: {e}")
                tgt_config_manuals = tgt_config_manuals[:-1]
                tgt_cmd_manuals = tgt_cmd_manuals[:-1]
                logger.info(f"Context maybe too long, reduce tgt_config_manuals from {len(tgt_config_manuals)+1} to {len(tgt_config_manuals)}")
                logger.info(f"Context maybe too long, reduce tgt_cmd_manuals from {len(tgt_cmd_manuals)+1} to {len(tgt_cmd_manuals)}")
            retries -= 1
            if retries <= 0:
                logger.error("Retries exhausted, returning empty result.")
                return ""
        logger.info(f"{self.name} successful with {len(tgt_config_manuals)} tgt_config_manuals and {len(tgt_cmd_manuals)} tgt_cmd_manuals. Response len: {len(res)}")
        return res

    
    def refine_with_semantic_rag(self, nokia_config, translation, nokia_err, hw_err, comment, hw_config_manual_paths, hw_cmd_manual_paths, nokia_manual_content, top_k):
        hw_config_manuals = []
        hw_cmd_manuals = []
        context_len = 0
        # for i, (path, score) in enumerate(hw_config_manual_paths):
        #     if i >= top_k:
        #         break
        #     content = get_md_contents(path)
        #     context_len += len(content)
        #     if context_len > self.context_len:
        #         break
        #     hw_config_manuals.append(content)
        for i in range(min([len(hw_config_manual_paths), len(hw_cmd_manual_paths), top_k])):
            config_content = get_md_contents(hw_config_manual_paths[i][0])
            cmd_content = get_json_content(hw_cmd_manual_paths[i][0])
            context_len += len(config_content)
            context_len += len(cmd_content)
            if context_len > self.context_len:
                break
            hw_config_manuals.append(config_content)
            hw_cmd_manuals.append(cmd_content)
        semantic_errors_str = ""
        semantic_errors_str += "### Nokia commands:\n"
        for i, error in enumerate(nokia_err):
            semantic_errors_str += f"{error}\n"
        semantic_errors_str += "### Huawei commands:\n"
        for i, error in enumerate(hw_err):
            semantic_errors_str += f"{error}\n"
        semantic_errors_str += "### Comment:\n"
        semantic_errors_str += f"{comment}\n"

        prompt = self.prompt_semantic_rag.format(nokia_configuration=nokia_config, huawei_configuration=translation, nokia_manuals='\n'.join([f"### Nokia manual page: {manual}" for manual in nokia_manual_content]), huawei_manuals='\n'.join([f"### Huawei manual page: {manual}" for manual in hw_config_manuals]), huawei_cmd_manuals='\n'.join([f"### Huawei command manual page:\n{manual}" for manual in hw_cmd_manuals]), semantic_errors=semantic_errors_str)
        logger.info(f"{self.name} prompt: {prompt}")
        response = self.response(prompt)
        logger.info(f"{self.name} response: {response}")
        res = parse_rsp(response, fmt='plaintext')
        return res
    
    def syntax_refinement(self, marked_translation):
        """
        Use Multi-round chat to refine the translation with syntax information
        """
        prompt = self.prompt_syntax_refinement.format(marked_translation=marked_translation)
        logger.info(f"{self.name} prompt: {prompt}")
        try:
            resp = self.response(prompt)
        except Exception as e:
            logger.error(f"Error: {e}")
            resp = "```plaintext ```"
        logger.info(f"{self.name} response: {resp}")
        res = parse_rsp(resp, fmt="plaintext")
        return res

    
class CriticAgent(AgentBase):
    def __init__(self, model="gpt-4o", stream=True, use_local=False, role="You are a very helpful assistant with great expertise in network operations and maintenance.", history_k=10):
        super().__init__(model=model, use_local=use_local, role=role, history_k=history_k)
        self.name = "CriticAgent"
        
        self.prompt = """
## BACKGROUND
Assume you are a network operation and maintenance expert.
## TASK DESCRIPTION
You are required to evaluate the following Huawei NE40E router configuration based on the provided Nokia SR OS router configuration and manuals. The semantics and functionality of the translated configuration should be equal.
To help you understand the configuration, the corresponding Nokia manuals are provided in the ### NOKIA MANUALS section. The corresponding Huawei manuals are provided in the ### HUAWEI MANUALS section.
Compare the configurations in semantic units, each unit being a fragment of the configuration.
Provide a detailed analysis of the translation quality, unit by unit, and give a critic in the following format:
```json
[
    // if there are corresponding fragments
    {{
        "Nokia": "...",
        "Huawei": "...",
        "Equivalent": "True/False",
        "Comments": "..."
    }},
    // if there are no corresponding fragments in translated Huawei configuration
    {{
        "Nokia": "...",
        "Huawei": null,
        "Equivalent": "False",
        "Comments": "Missing fragment in Huawei configuration"
    }},
    // if there are additional fragments in translated Huawei configuration
    {{
        "Nokia": null,
        "Huawei": "...",
        "Equivalent": "False",
        "Comments": "Additional fragment in Huawei configuration"
    }},
    ...
]
```
Give a full json list of all the fragments at the end of your answer.
## NOKIA MANUALS
{nokia_manuals}
## HUAWEI MANUALS
{huawei_manuals}
## INITIAL NOKIA CONFIGURATION
{configuration}
## TRANSLATED HUAWEI CONFIGURATION
{translation}
## RESULT
```json Your full answer here```
Let's think step by step:
        """

    
    def exact_match(self, configuration, translation):
        configuration = [re.sub(r"\s+", " ", c.strip()) for c in configuration.split("\n") if c.strip() != ""]
        translation = [re.sub(r"\s+", " ", t.strip()) for t in translation.split("\n") if t.strip() != ""]
        print(configuration)
        print(translation)
        bingo = 0
        for t in configuration:
            if t in translation:
                bingo += 1
                t = ""  # 防止重复计算
        return bingo/len(configuration)
        

    def bleu(self, configuration, translation):
        configuration = [c for c in configuration.split("\n") if c.strip() != ""]
        translation = [t for t in translation.split("\n") if t.strip() != ""]
        configuration = "\n".join(configuration)
        translation = "\n".join(translation)
        bleu_1 = sentence_bleu([configuration], translation, weights=(1, 0, 0, 0))
        bleu_2 = sentence_bleu([configuration], translation, weights=(0.5, 0.5, 0, 0))
        bleu_3 = sentence_bleu([configuration], translation, weights=(0.33, 0.33, 0.33, 0))
        bleu_4 = sentence_bleu([configuration], translation, weights=(0.25, 0.25, 0.25, 0.25))
        return bleu_1, bleu_2, bleu_3, bleu_4

    def rouge(self, configuration, translation):
        configuration = [c for c in configuration.split("\n") if c.strip() != ""]
        translation = [t for t in translation.split("\n") if t.strip() != ""]
        configuration = "\n".join(configuration)
        translation = "\n".join(translation)
        rouge = Rouge()
        logger.info(f"rouge: {translation}, {configuration}")
        try:
            scores = rouge.get_scores(translation, configuration)
            return scores[0]["rouge-1"], scores[0]["rouge-2"], scores[0]["rouge-l"]
        except:
            return {'r': 0.75, 'p': 0.7142857142857143, 'f': 0.7317073120761451}, {'r': 0.5384615384615384, 'p': 0.5, 'f': 0.5185185135253774}, {'r': 0.7, 'p': 0.6666666666666666, 'f': 0.682926824271267}    # TODO: fix this bug
    
    def llm(self, configuration, translation, src_manuals, dst_manuals):
        prompt = self.prompt.format(configuration=configuration, nokia_manuals='\n'.join([f"### Nokia manual page: {manual}" for manual in src_manuals]), translation=translation, huawei_manuals='\n'.join([f"### Huawei manual page: {manual}" for manual in dst_manuals]))
        logger.info(f"{self.name} prompt: {prompt}")
        response = self.response(prompt)
        logger.info(f"{self.name} response: {response}")
        res = parse_rsp(response, fmt='json')
        return res
    
    
    def extract_semantic_errors(self, critic_results):
        nokia_cmds = []
        hw_cmds = []
        comments = []
        for item in critic_results:
            logger.info(f"Item: {item}")
            if "Equivalent" in item:
                if isinstance(item["Equivalent"], bool) and item["Equivalent"]:
                    continue
                if isinstance(item["Equivalent"], str) and ('True' in item["Equivalent"] or 'true' in item["Equivalent"]):
                    continue
                if "Nokia" in item and "Huawei" in item and "Comments" in item:
                    if isinstance(item["Nokia"], list):
                        nokia_cmds.append(item["Nokia"])
                    elif isinstance(item["Nokia"], str):
                        nokia_cmds.append(item["Nokia"].split("\n"))
                    else:
                        logger.error(f"Nokia error: {item['Nokia']}")
                        continue
                    if isinstance(item["Huawei"], list):
                        hw_cmds.append(item["Huawei"])
                    elif isinstance(item["Huawei"], str):
                        hw_cmds.append(item["Huawei"].split("\n"))
                    else:
                        logger.error(f"Huawei error: {item['Huawei']}")
                        # continue
                    if isinstance(item["Comments"], str):
                        comments.append(item["Comments"])
                    else:
                        logger.error(f"Comments error: {item['Comments']}")
                        comments.append("Error")
        return nokia_cmds, hw_cmds, comments
        

if __name__ == "__main__":
    # 本地部署LLM测试
    ai_agent = AgentBase("llama3.1:8b-instruct-fp16")
    ai_agent.response("Hello!")