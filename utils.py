# ====================================================
# Author: Yunze Wei <yunzewei@outlook.com>
# Date: 2025-08-03
# Description: Utility functions for network configuration translation and evaluation.
# ====================================================
import json
from typing import List
import logging
import re
import numpy as np
import time
import torch
import os
import copy

logging_level = logging.INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging_level)
current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

if not os.path.exists(f'logs/{current_time}'):
    os.makedirs(f'logs/{current_time}')

fh = logging.FileHandler(f'logs/{current_time}/run.log')
fh.setLevel(logging_level)
ch = logging.StreamHandler()
ch.setLevel(logging_level)
logger.addHandler(fh)
logger.addHandler(ch)

CORPUS_PATH = 'nassim-main/corpus/'


CMD_GRAPH_CACHE = {
    # TODO: (hts) add graph cache 
}
# VERIFY_CACHE = {}


class HierarchyNode:
    """
    Hierarchy nodes of device model
    Took example by ConfigTrans
    """
    def __init__(self):
        self.type = None    # 'cli', 'cli_', 'view'
        self.cli = None
        self.parent = None
        self.renderview = []
        self.children = []
        self.graph_model = None
        self.path = None
        self.depth = 0
        self.is_virtual = False

    def __str__(self):
        return self.cli
    
    def print(self):
        if self.cli != 'virtual root':
            logger.info('  ' * self.depth + self.cli)
        if self.parent:
            logger.info('  ' * self.depth + "(" + self.parent.cli + ")")
        # logger.info('  ' * self.depth + self.cli)
        for child in self.children:
            child.print()

    def find_child(self, cli):
        for child in self.children:
            if child.cli.startswith(cli):
                return child
            else:
                res = child.find_child(cli)
                if res:
                    return res
        return None
    
    def get_view_path(self):
        logger.info(self.cli)
        curr = self.parent
        view_path = [self.cli]
        while curr:
            view_path.append(curr.cli)
            curr = curr.parent
        view_path.reverse()
        return view_path
    
    def print_level1_child(self):
        for child in self.children:
            logger.info(child.cli)

def get_cmd_function(config_dict, cmd=""):
    if not isinstance(config_dict, dict):
        return []
    functions = []
    for key, value in config_dict.items():
        if key == "Function":
            functions.append((cmd, value))
        else:
            functions += get_cmd_function(value, key)
    return functions


class ConfigUnit():
    """
    Configuration unit: a leaf node and all its parent views, and the manuals of the unit
    Args:
        item: a dict in ConfigDivision with keys: Fragment, Nodes, Function, Details
    """
    def __init__ (self, item, debug=False) -> None:
        
        self.CLIs = item['Fragment']

        manuals = []
        if not debug:
            # 如果"Nodes"是键
            if "Nodes" in item:
                for node in item["Nodes"]:
                    manuals.append(node.get_manual_content())
        logger.debug("Manuals: " + str(manuals))

        self.manuals = manuals

        functions = []
        functions.append(item["Function"])
        for _ , function in get_cmd_function(item["Details"]):
            functions.append(function)
        self.functions = functions
    
    def print(self):
        logger.info(self.CLIs)
        for manual in self.manuals:
            logger.info(manual)
        for function in self.functions:
            logger.info(function)
        
class ConfigNode:
    """
    Configuration node: a node in the configuration tree
    """
    def __init__(self, cli, hierarchy_node, parent=None, matched="", cmd_graph=None, secondary_hnode=None, manuals=None) -> None:
        self.cli = cli
        self.hierarchy_node: HierarchyNode = hierarchy_node
        self.secondary_hierarchy_node = secondary_hnode     # 第二匹配节点，可能是视图和精确匹配同时存在
        self.parent = parent
        self.children = []
        self.matched = matched   # 匹配的部分 (""表示虚空节点)
        self.cmd_graph = cmd_graph   # 对应命令图（若匹配成功；若存在secondary则对应secondary）
        # self.matched_idx = 0    # 匹配的部分的索引
        self.is_match = True if self.matched else False   # 是否匹配成功(False表示虚空节点)
        self.is_exact_match = True if self.cmd_graph else False   # 是否精确匹配成功
        self.matched_str = ""   # 匹配的字符串，包括该节点开始的整棵子树
        self.manuals = manuals  # manual list (paths)
        self.is_chosen = False  # 是否被选中，用于配置匹配过程（1：配置片段匹配；2：cmd匹配）

        # 解决回溯匹配时，匹配到视图但是没有匹配到精确的父节点的情况
        if not self.secondary_hierarchy_node and self.hierarchy_node.parent:
            cmd_graph_ = match_cmd_graph(self.cli, self.hierarchy_node.parent.cli)
            if cmd_graph_:
                self.cmd_graph = cmd_graph_
                self.matched = get_matched_str(cmd_graph_)
                self.is_exact_match = True

        # 构造cmd (str, 1/0)
        # 1. 若is_exact_match，则用cmd_graph构造 (1) 
        #   - cmd判定：最外围连续的seq
        # 2. 否则用前缀构造，模糊匹配 (0)
        #   - 保存整个cli，匹配时先做第一轮的严格匹配，若无匹配再开展第二轮的模糊前缀匹配
        cmds = []
        if self.hierarchy_node.type == 'cli':
            if self.is_exact_match:
                for _cmd_graph in self.cmd_graph:
                    if _cmd_graph.type == 'keyword':
                        cmds.append(_cmd_graph.name)
                    else:
                        break
                self.cmd = (" ".join(cmds), 1)
            else:
                self.cmd = (self.cli, 0)
        else:
            self.cmd = ('view point', -1)   # 视图节点的命令为其cli


    def __str__(self):
        return self.cli

    def get_matched_line(self, annotation='cli'):

        if self.cli == 'virtual root':
            return ""
        if self.is_exact_match:
            if annotation == 'cli':
                return '  ' * self.hierarchy_node.depth + self.matched + f" (EXACT) ({self.hierarchy_node.cli}) cmd: {self.cmd}\n"
            elif annotation == 'path':
                return '  ' * self.hierarchy_node.depth + self.matched + f" (EXACT) ({self.hierarchy_node.path}) cmd: {self.cmd}\n"
        # elif self.hierarchy_node.cli == 'blank':
        #     return '  ' * self.hierarchy_node.depth + self.cli + " (BLANK)\n"
        # else:
        #     return '  ' * self.hierarchy_node.depth + self.cli + f" (FUZZY) ({self.hierarchy_node.cli})\n"
        else:
            return '  ' * self.hierarchy_node.depth + self.cli + f" (MISMATCHED) cmd: {self.cmd}\n"
        
    def print_to_str(self):
        res = ""
        res += self.get_matched_line()
        for child in self.children:
            res += child.print_to_str()
        self.matched_str = res
        return res
    
    def get_lines(self):
        return len(self.print_to_str().split("\n"))

    def print_to_str_with_path(self):
        res = ""
        res += self.get_matched_line(annotation='path')
        for child in self.children:
            res += child.print_to_str_with_path()
        self.matched_str = res
        return res
    
    def print(self):
        logger.info(self.print_to_str())

    def get_cmd_tuples(self):
        """
        Return a list of tuples of (cmd, node) for all nodes in the subtree
        """
        cmd_list = []
        if self.cli != 'virtual root':
            cmd_list.append((self.cli, self))   # (cmd, node)
        for child in self.children:
            cmd_list += child.get_cmd_tuples()
        return cmd_list
        

    def get_mismatched_lines(self, pure=False):
        if not self.matched_str:
            self.matched_str = self.print_to_str()
        syntax_problem_list = []
        for item in self.matched_str.split("\n"):
            if not pure:
                if 'FUZZY' in item:
                    syntax_problem_list.append(f" - {item.split(') (')[0]})")
                elif 'BLANK' in item:
                    syntax_problem_list.append(f" - {item}")
                elif 'MISMATCHED' in item and 'quit' not in item and 'return' not in item:  # 去除无用命令
                    syntax_problem_list.append(f" - {item}")
            else:
                if 'MISMATCHED' in item and 'quit' not in item and 'return' not in item:
                    syntax_problem_list.append(item.strip().split("(")[0])  # 去除注释
        return syntax_problem_list

    def get_matched_score(self):
        total_lines = self.print_to_str().split("\n")
        mismatched_lines = self.get_mismatched_lines()
        return 1 - len(mismatched_lines) / len(total_lines)
    
    def find_child(self, cli):
        for child in self.children:
            if child.cli.startswith(cli) and not child.is_chosen:
                # logger.info(child.is_chosen)
                child.is_chosen = True
                if child.hierarchy_node.type == 'cli':
                    for sub_child in child.children:
                        # logger.info(sub_child.cli+ " " + cli)
                        # logger.info(sub_child.cli.startswith(cli))
                        if sub_child.cli.startswith(cli) and sub_child.hierarchy_node.type == 'view':
                            sub_child.is_chosen = True
                            return sub_child            # 优先匹配子节点
                return child
            else:
                res = child.find_child(cli)
                if res:
                    return res
        return None

    def get_matched_cmd(self, line):
        """
        Match the command line with the node
        Args:
            line: command line
        Returns:
            matched: tuple(matched_cmd, is_exact_match)
        """
        line = line.strip()
        if not self.is_chosen:
            if line.startswith(self.cmd[0]):
                # 精准的前缀匹配
                self.is_chosen = True
                logger.info(f"get_matched_cmd: {self.cmd[0]} in {line}")
                return self.cmd
            elif line.startswith('undo') and line[5:].startswith(self.cmd[0]):
                # 精准的前缀匹配
                self.is_chosen = True
                logger.info(f"get_matched_cmd (undo): {self.cmd[0]} in {line}")
                return self.cmd
            elif self.cmd[1] == 0:
                # 模糊的前缀匹配
                if line.strip().split(' ')[0] == self.cmd[0]:
                    self.is_chosen = True
                    logger.info(f"get_matched_cmd (prefix): {self.cmd[0]} in {line}")
                    return self.cmd
        for child in self.children:
            res = child.get_matched_cmd(line)
            if res:
                return res
        return None

    def get_matched_cli_lines(self):
        """
        Get the lines of the command line with the node
        Returns:
            lines: int
        """
        # cli_lines = 1 if self.hierarchy_node.type != 'view' and self.cli != 'virtual root' and self.cli != 'undo shutdown' else 0
        # matched_lines = 1 if self.is_chosen and self.cli != 'undo shutdown' else 0
        cli_lines = 1 if self.hierarchy_node.type != 'view' and self.cli != 'virtual root' else 0
        matched_lines = 1 if self.is_chosen else 0
        if self.hierarchy_node.type != 'view' and not self.is_chosen and self.cli != 'virtual root':
            logger.info(f"get_matched_cli_lines: {self.cli} not chosen")
        for child in self.children:
            child_matched_lines, child_cli_lines = child.get_matched_cli_lines()
            matched_lines += child_matched_lines
            cli_lines += child_cli_lines
        return matched_lines, cli_lines        
        
        

    def reset_is_chosen(self):
        self.is_chosen = False
        for child in self.children:
            child.reset_is_chosen()

    def print_debug(self):
        depth = '  ' * self.hierarchy_node.depth
        logger.info(f"{depth}{self.cli} {self.is_chosen} {self.hierarchy_node.type}")
        for child in self.children:
            child.print_debug()

    def get_manual_content(self) -> str:
        manual_fields = ["FuncDef", "CLIs", "ParentView", "ParaDef"] # ["PageTitle", "FuncDef", "CLIs", "ParentView", "ParaDef", "Example", "ExtraInfo"]
        logger.debug(f"Extracting manual for {self.cli} from {self.hierarchy_node.path}")
        manual_retrieved = ""
        if not self.hierarchy_node.path:
            return ""
        
        with open(os.path.join(CORPUS_PATH, self.hierarchy_node.path), 'r', encoding='utf-8') as f:
            manual = json.load(f)
            manual_retrieved += f"{manual['PageTitle']}\n"
            for field in manual_fields:
                manual_retrieved += f"#### {field}\n{manual[field]}\n"
            if "ExtraInfo" in manual and manual["ExtraInfo"]:
                ExtraInfos = manual["ExtraInfo"].split(" ")
                if len(ExtraInfos) > 150:
                    ExtraInfo = " ".join(ExtraInfos[:150])
                    manual_retrieved += f"#### ExtraInfo\n{ExtraInfo}...\n"
                else:
                    manual_retrieved += f"#### ExtraInfo\n{manual['ExtraInfo']}\n"
            return manual_retrieved

    def get_subtree_manual_list(self) -> List[str]:
        def traverse(node):
            if node.hierarchy_node.path:
                manual_list.append(node.hierarchy_node.path)
            for child in node.children:
                traverse(child)
        manual_list = []
        traverse(self)
        return manual_list
 
    def get_subtree_manual_content_list(self) -> List[str]:
        manual_list = []
        manual_list.append(self.get_manual_content())
        for child in self.children:
            manual_list += child.get_subtree_manual_content_list()
        return list(set(manual_list))
    
    def get_config_units(self) -> List[ConfigUnit]:
        # 递归遍历子树，获取所有的配置单元（叶子结点对应的所有父视图及其手册）
        def traverse(node):
            if len(node.children) == 0:
                views = []
                manual_list = []
                curr = node
                while curr:
                    if curr.cli == 'virtual root':
                        break
                    if curr.cli != views[-1][0] if views else True:
                        views.append((curr.cli, curr.hierarchy_node.depth))
                    if curr.hierarchy_node.path:
                        logger.debug(curr.cli)
                        logger.debug(curr.hierarchy_node.depth)
                        logger.debug(curr.hierarchy_node.path)
                        with open(os.path.join(CORPUS_PATH, curr.hierarchy_node.path), 'r', encoding='utf-8') as f:
                            manual_list.append(f.read())
                    curr = curr.parent
                views.reverse()
                manual_list.reverse()
                config_unit = ""
                for view in views:
                    config_unit += " " * view[1] + view[0] + "\n"
                config_units.append(ConfigUnit(config_unit, manual_list))
                    
            for child in node.children:
                traverse(child)
        config_units = []
        traverse(self)
        return config_units

def get_md_contents(md_path):
    manual_str = ""
    fields = ["Procedure", "Usage Scenario", "Pre-configuration Tasks"]
    with open(md_path, 'r', encoding='utf-8') as f:
        md_contents = f.readlines()
    pause = False
    for line in md_contents:
        if line.startswith("="):
            manual_str += "#### Description\n"
            continue
        # if line.strip().startswith("![]"):
        #     continue
        if line.startswith("####"):
            pause = line[5:].strip() not in fields
        if not pause and line.strip():
            manual_str += line
    
    return manual_str

class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ConfigNode):
            return obj.cli
        return json.JSONEncoder.default(self, obj)

# 遍历构建层次树【来自ConfigTrans】
def build_hierarchy_tree(cmd_tree_path='./nassim-main/corpus/hierarchy/cmd_tree_nokia.json'):
    path_node_dict = {}
    all_clis = []
    current_view = []
    def traverse(hierarchy_root, depth=0):  
        node = HierarchyNode()
        # logger.info(hierarchy_root)
        if hierarchy_root['type'] == 'cli':# : or hierarchy_root['type'] == 'cli_':
            node.type = 'cli'
            node.cli = hierarchy_root['cli']
            all_clis.append(node.cli)
            path_node_dict[hierarchy_root['cli']] = node
        elif hierarchy_root['type'] == 'cli_':
            node.type = 'cli_'
            node.cli = hierarchy_root['name']
            all_clis.append(node.cli)
        elif hierarchy_root['type'] == 'view':
            node.type = 'view'
            node.cli = hierarchy_root['name']
            all_clis.append(node.cli)
        else:
            node.type = 'cli'
            node.cli = hierarchy_root['name']
            all_clis.append(node.cli)

        if 'renderview' in hierarchy_root:
            node.renderview = hierarchy_root['renderview']
        node.depth = depth
        if depth > 0:
            node.parent = current_view[-1]

        if 'children' in hierarchy_root:
            for child in hierarchy_root['children']:
                current_view.append(node)
                child_node = traverse(child, depth + 1)
                current_view.pop()
                child_node.parent = node
                node.children.append(child_node)

        if 'path' in hierarchy_root:
            node.path = hierarchy_root['path'].replace('\\', '/')

        return node
    ans = traverse(json.load(open(cmd_tree_path, 'r', encoding='utf-8')))
    virtual_root = HierarchyNode()
    ans.parent = virtual_root   # 虚拟根节点成为真实根节点的父节点
    virtual_root.children.append(ans)
    virtual_root.cli = 'virtual root'
    virtual_root.is_virtual = True
    virtual_root.parent = virtual_root  # 虚拟根节点自环（会不会有其他问题？）
    return virtual_root, all_clis

def parse_rsp(rsp, fmt="json"):
    if not rsp:
        return ""
    pattern = r"```{}(.*?)```".format(fmt)  # ?表示非贪婪匹配
    matches = re.findall(pattern, rsp, re.DOTALL)
    cmd_text = matches[-1] if matches else ""
    return cmd_text

def json_str_list_print(json_str, keys_list=["Intent/Behavior", "Fragment"]):
    json_obj = json.loads(json_str)
    for item in json_obj:
        for key in keys_list:
            print(f"### {key}: \n{item[key]}")
        print("\n")

def transform_underline(text):
    # 使用正则表达式先将 '\_' 替换为占位符 '\temp_',然后替换普通的 '_'，最后将 '\temp_' 替换回 '_'
    text = re.sub(r'\\_', '\temp', text)  # 替换 '\_' 为占位符
    text = text.replace('_', ' ')         # 替换普通的 '_' 为空格
    text = text.replace('\temp', '_')    # 将占位符替换回 '_'
    return text


# def extract_config_and_paths(line):
#     # 匹配配置命令和后面中括号中的路径列表
#     pattern = r'^(.*?)\s*\[(.*?)\]\s*$'
#     match = re.search(pattern, line.strip())
#     if match:
#         command = match.group(1).strip()
#         paths = [p.strip().strip('"') for p in match.group(2).split(',')]
#         return command, paths
#     return None, None


def extract_cmd_and_manual_with_indent(line):
    # 匹配命令行和可选 manual，保留前导空格
    pattern = r'^(\s*.*?)\s*(\[(.*?)\])?\s*$'
    match = re.match(pattern, line)
    if match:
        cmd_with_indent = match.group(1)  # 带缩进的命令
        manual_block = match.group(3)     # 中括号中的内容
        if manual_block:
            manuals = [m.strip().strip('"') for m in manual_block.split(',')]
        else:
            manuals = []
        return cmd_with_indent, manuals
    return line, []

# Remove lines beginning with '#', '!' and '//', and remove empty lines
def purify_configuration(text, keep_manuals=False):
    logger.debug(f'keep_manuals: {keep_manuals}')
    lines = text.split('\n')
    res = []
    for cmd_list in lines:
        line = None
        line_stripped = cmd_list.strip()
        if line_stripped == '':
            continue
        elif line_stripped.startswith('#') or line_stripped.startswith('!') or line_stripped.startswith('//'):
            continue
        elif line_stripped == 'commit' or line_stripped == 'quit' or line_stripped == 'return' or line_stripped == 'exit':   # 去除平凡命令
            continue
        elif 'loopback' in line_stripped.lower():
            # 替换其中任意大小写的loopback为Loopback
            line = re.sub(r'loopback', 'Loopback', line_stripped, flags=re.IGNORECASE)
        elif "//" in line_stripped:
            line_stripped = line_stripped.split("//")[0]
            cmd_list = " "*(len(cmd_list) - len(cmd_list.lstrip())) + line_stripped
        line = cmd_list

        if line:
            if not keep_manuals:
                line, manual = extract_cmd_and_manual_with_indent(line)
                logger.debug(f'(purify_configuration) get manual: {manual} for line: {line}')
                # match = re.match(r'^(.*?)\s*(\[[^\]]*\])$', line)
                # if match:
                #     cmd = match.group(1)
                #     manual = match.group(2)
                #     logger.debug(f'(purify_configuration) get manual: {manual} for line: {cmd}')
            res.append(line)
                
    return '\n'.join(res)


def split_command(command):
    """
    保留引号，拆分命令
    输入：命令字符串
    输出：拆分后的命令列表
    """
    # 正则表达式：匹配引号内的内容或者非空白字符的连续片段
    pattern = r'".*?"|\S+'
    matches = re.findall(pattern, command)
    # 去掉引号
    results = [match if not (match.startswith('"') and match.endswith('"')) else match[1:-1] for match in matches]
    return results

# 提取命令中的关键字和参数
def extract_and_split_cmd(input_string):
    # 定义正则模式，匹配 {} 包裹的部分和 <> 包裹的部分
    pattern = r'{.*?}|<.*?>|[^{}<>\s]+'
    # 使用 re.findall 提取匹配部分
    matches = re.findall(pattern, input_string)
    # 去除每个部分的首尾空格，保持顺序
    return matches

def extract_uppercase(input_string):
    # 使用列表生成式提取大写字母并组合
    return ''.join([char for char in input_string if char.isupper()])


def command_match_fuzzy(cmd_str, mode_list) -> str:     # TODO: 命令语法匹配
    """
    模糊匹配命令行和命令模式
    Args:
        cmd_list: 待匹配的命令行字符串
        mode: 命令模式字符串
    Returns:
        模糊的匹配结果字符串
    """
    # 模糊匹配命令行和命令模式
    # cmd_list = cmd_list.split(' ')
    cmd_list = split_command(cmd_str)
    if not cmd_list:
        return ""
    # if cmd_list[0] == 'undo':
    #     cmd_list = cmd_list[1:]
    mode_list = extract_and_split_cmd(mode_list.split('##')[0])    
    # logger.debug(f"cmd_list: {cmd_list}")
    # logger.debug(f"mode_list: {mode_list}")
    match_res = []
    has_para = False
    for i in mode_list:
        if '<' in i or '{' in i:
            has_para = True
            break

    cmd_point = 0
    line_point = 0
    in_alternative = False
    alterbrackets = 0   # 记录被拆散的选择括号[]数目
    while cmd_point < len(mode_list) and line_point < len(cmd_list):
        # logger.debug(f"match_res: {match_res}")
        # print(cmd[cmd_point], cmd_list[line_point])
        if mode_list[cmd_point] == cmd_list[line_point]:
            match_res.append(cmd_list[line_point])
            cmd_point += 1
            line_point += 1
        elif '<' in mode_list[cmd_point]:
            match_res.append('*')
            line_point += 1
            cmd_point += 1
        elif '{' in mode_list[cmd_point]:
            if cmd_list[line_point] in mode_list[cmd_point]:
                match_res.append(cmd_list[line_point])
                line_point += 1
                cmd_point += 1
            else:
                break
        elif '[' in mode_list[cmd_point]:
            in_alternative = True
            cmd_point += 1
            alterbrackets += 1
            if mode_list[cmd_point] == cmd_list[line_point]:
                match_res.append(cmd_list[line_point])
                line_point += 1
                cmd_point += 1
        elif ']' in mode_list[cmd_point]:
            in_alternative = False
            alterbrackets += 1
            cmd_point += 1
        elif '|' in mode_list[cmd_point]:
            cmd_point += 1
        else:
            break

        
    # if len(match_res) == len(mode_str) and not has_para:
    if len(match_res) == len(cmd_list) and not has_para:
        match_res.append('(exact)')  # 避免匹配到含有前缀的其他命令
    return " ".join(match_res)


# 命令拆分【来自ConfigTrans】
def parse_vdm_cli_format(cli_format):
    ans = []
    splits = [c for c in re.split(' ', cli_format) if c]    # 拆分命令，去除空格
    for token in splits:
        if re.match(r'\<.*\>', token):
            ans.append(('var', re.sub('<|>', '', token)))
        elif re.match(r'\[|\]|\{|\}|\||(\&\<[0-9]*-[0-9]*\>)|\*', token):
            ans.append(('symbol', token))
        else:
            ans.append(('keyword', token))
    ans.append(('symbol', 'EOC'))
    return ans


class CmdGraph():
    """
    命令图的节点，类型：顺序节点、必选选择节点、可选选择节点；叶子结点
    一个节点也是顺序节点，其子节点是GraphNode，表示具体匹配的关键字或参数
    选择节点是列表，包含多个可能的选择
    命令图和命令行匹配二合一
    """
    def __init__(self, type, mode_seq, parent=None):
        """
        Args:
            type: 'seq', 'req_selector', 'opt_selector', 'end'
            mode_seq: 一个命令的模式序列
        """
        # 构建模式
        self.type = type    # Internal: 'seq', 'req_selector', 'opt_selector'; Leaf: 'keyword', 'var', 'pass', 'end'.
        self.name = None    # only for leaf node (keyword or var)
        self.value = None   # only for leaf node (var)
        self.mode_seq = mode_seq    # initial mode sequence (list)
        self.select_mode = False     # if True then selection can be all ({x|y|...}* or [x|y|...]*)
        self.repeat = 1             # if larger than 1, then repeat the mode sequence before (* or &<1-n>)
        self.is_selected = False     # if True then this node is selected, use with self.repeat > 1
        self.mode = []      # a list of sub GraphNode
        self.current_matching = 0    # 当前正在匹配的模式序列idx
        self.parent = parent
        if type == 'seq':
            self.make_graph_seq(mode_seq)
        elif type == 'req_selector':
            self.make_graph_req_selector(mode_seq)
        elif type == 'opt_selector':
            self.make_graph_opt_selector(mode_seq)
        elif type == 'keyword':
            self.name = mode_seq
        elif type == 'var':
            self.name = mode_seq
        elif type == 'end':
            pass
        elif type == 'pass':
            pass
        else:
            raise ValueError(f"Invalid type {type}")
        
    def __lt__(self, other):    # 以模式长度为比较依据
        return len(self.mode) < len(other.mode)

    def __eq__(self, other):
        if not isinstance(other, CmdGraph):
            return False
        if self.type != other.type or self.name != other.name:
            return False
        if len(self.mode) != len(other.mode):
            return False
        return all(a == b for a, b in zip(self.mode, other.mode))

    def __hash__(self):
        # This is a simplified hash - you might need a more robust one
        return hash((self.type, self.name, tuple(self.mode) if hasattr(self, 'mode') else None))
    
    def reset(self):
        """Reset the internal state of the graph for a fresh matching."""
        self.current_matching = 0
        self.is_selected = False
        if hasattr(self, 'value'):
            self.value = None
        # Recursively reset all child nodes
        if hasattr(self, 'mode'):
            for child in self.mode:
                child.reset()
    
    def make_graph_seq(self, mode_seq):
        i = 0   # 当前正要处理的模式序列
        bracket_stack = [] 
        # 处理所有最外层括号
        for j, item in enumerate(mode_seq): # j 当前正在探索的模式序列
            # j += 1
            if len(bracket_stack) == 0:
                if item[0] == 'symbol' and item[1] == 'EOC':
                    self.mode.append(CmdGraph('end', ('symbol', 'EOC'), self))
                    break
                # if item[0] == 'keyword' or item[0] == 'var':
                #     self.mode.append(CmdGraph(item[0], item[1], self))
                #     i += 1
                if item[0] == 'keyword':
                    self.mode.append(CmdGraph('keyword', item[1], self))
                    i += 1
                if item[0] == 'var':
                    repeat = 1  # &<1-n>的n
                    logger.debug(f"find var: {item[1]} in {mode_seq}")
                    if j < len(mode_seq) - 1:
                        if mode_seq[j+1][0] == 'symbol' and mode_seq[j+1][1].startswith('&'):
                            logger.debug(f"try repeat: {mode_seq[j+1][1]} in {mode_seq}")
                            matches = re.match(r'&<([0-9]*)-([0-9]*)>', mode_seq[j+1][1])
                            if matches:
                                repeat = int(matches.group(2))
                            else:
                                raise ValueError(f"Repeat symbol error of {mode_seq[j+1][1]}")
                    if repeat > 1:
                        logger.debug(f"find repeat: {repeat} in {mode_seq}")
                    self.mode.append(CmdGraph('var', item[1], self))
                    self.mode[-1].repeat = repeat
                    i += 1
                if item[0] == 'symbol' and item[1] == '*':
                    try:
                        # self.mode[-1].select_mode = True
                        self.mode[-1].repeat = 5     # select_mode == True，可选择多个
                    except:
                        # raise ValueError("No previous mode before *")
                        self.mode.append(CmdGraph('keyword', ('keyword', '*'), self))
                    i += 1
                if item[0] == 'symbol' and item[1].startswith('&'):
                    matches = re.match(r'&<([0-9]*)-([0-9]*)>', item[1])
                    if matches:
                        self.mode[-1].repeat = int(matches.group(2))
                        pass
                    else:
                        raise ValueError(f"Repeat symbol error of {item[1]}")
                    i += 1
                elif item[0] == 'symbol':
                    if item[1] == '[':
                        bracket_stack.append('[')
                    elif item[1] == '{':
                        bracket_stack.append('{')
                    elif item[1] == '|':
                        raise NotImplementedError("Not support '|' in seq mode")
                    elif item[1] == '}':
                        raise ValueError("Bracket not match")
                    elif item[1] == ']':
                        raise ValueError("Bracket not match")
                # logger.debug(item, 'match')
            else:
                if item[0] == 'symbol' and item[1] == '[':
                    bracket_stack.append('[')
                elif item[0] == 'symbol' and item[1] == ']':
                    if bracket_stack[-1] == '[':
                        bracket_stack.pop()
                    else:
                        raise ValueError("Bracket not match")
                elif item[0] == 'symbol' and item[1] == '{':
                    bracket_stack.append('{')
                elif item[0] == 'symbol' and item[1] == '}':
                    if bracket_stack[-1] == '{':
                        bracket_stack.pop()
                    else:
                        raise ValueError("Bracket not match")
                if len(bracket_stack) == 0:
                    if mode_seq[i][1] == '{':
                        self.mode.append(CmdGraph('req_selector', mode_seq[i+1:j], self))
                    elif mode_seq[i][1] == '[':
                        self.mode.append(CmdGraph('opt_selector', mode_seq[i+1:j], self))
                    else:
                        # logger.debug(mode_seq[i][1])
                        # logger.debug(mode_seq[i:j+1])
                        raise ValueError("Bracket Error")
                    # logger.debug(str(mode_seq[i:j+1]) + ' bracket match') # python 的 list 切片是左闭右开区间
                    i = j + 1
    
    def make_graph_req_selector(self, mode_seq):
        """
        可选节点的每一条都是一个seq，所有可选seq都是并列的，纳入req的mode中
        """
        # logger.debug("make req_selector")
        # logger.debug(mode_seq)
        i = 0   # 当前正要处理的模式序列
        bracket_stack = []
        for j, item in enumerate(mode_seq):
            if len(bracket_stack) == 0:
                if item[0] == 'symbol' and item[1] == '|':
                    self.mode.append(CmdGraph('seq', mode_seq[i:j], self))
                    i = j + 1
                elif j == len(mode_seq) - 1:
                    self.mode.append(CmdGraph('seq', mode_seq[i:], self))
                elif item[0] == 'keyword' or item[0] == 'var':
                    pass
                elif item[0] == 'symbol':
                    if item[1] == '[' or item[1] == '{':
                        bracket_stack.append(item[1])
                        # if j > i:
                        #     self.mode.append(CmdGraph('seq', mode_seq[i:j], self))
                        #     i = j
                    elif item[1] == '}':
                        raise ValueError("Bracket not match")
                    elif item[1] == ']':
                        raise ValueError("Bracket not match")
            else:
                if item[0] == 'symbol' and item[1] == '[':
                    bracket_stack.append('[')
                elif item[0] == 'symbol' and item[1] == ']':
                    if bracket_stack[-1] == '[':
                        bracket_stack.pop()
                    else:
                        raise ValueError("Bracket not match")
                elif item[0] == 'symbol' and item[1] == '{':
                    bracket_stack.append('{')
                elif item[0] == 'symbol' and item[1] == '}':
                    if bracket_stack[-1] == '{':
                        bracket_stack.pop()
                    else:
                        raise ValueError("Bracket not match")
                if j == len(mode_seq) - 1:
                    if len(bracket_stack) != 0:
                        raise ValueError("Bracket not match")
                    self.mode.append(CmdGraph('seq', mode_seq[i:], self))
                    # if mode_seq[i][1] == '{':
                    #     self.mode.append(CmdGraph('req_selector', mode_seq[i+1:j], self))
                    # elif mode_seq[i][1] == '[':
                    #     self.mode.append(CmdGraph('opt_selector', mode_seq[i+1:j], self))
                    # else:
                    #     logger.debug(mode_seq[i][1])
                    #     raise ValueError(f"Bracket Error of {item} in {j}")
        # logger.debug(f"req_selector: {self.mode}")
        self.mode = sorted(self.mode, reverse=True)    # 优先匹配最长的模式
        # logger.debug(f"req_selector: {self.mode}")
        # logger.debug("make req_selector end")
        

    def make_graph_opt_selector(self, mode_seq):
        # logger.debug("make opt_selector")
        self.make_graph_req_selector(mode_seq)      # 可选选择节点和必选选择节点的主要实现相同
        self.mode.append(CmdGraph('pass', None, self))    # 增加可选项：opt_selector 匹配失败时，跳过
        # logger.debug("make opt_selector end")

                        
    def print(self):
        if self.type == 'seq':
            self.print_seq()
        elif self.type == 'req_selector':
            self.print_req_selector()
        elif self.type == 'opt_selector':
            self.print_opt_selector()
        elif self.type == 'keyword':
            logger.info(self.name)
        elif self.type == 'var':
            if self.value:
                logger.info(f"<{self.name}>: {self.value}")
            else:
                logger.info(f"<{self.name}>")
        elif self.type == 'pass':
            logger.info('(pass optional)')
        elif self.type == 'end':
            logger.info('cmd finished')
        else:
            raise ValueError("Invalid type")

    def print_seq(self):
        for item in self.mode:
            if item.type == 'keyword':
                logger.info(item.name)
            elif item.type == 'var':
                logger.info(f"<{item.name}>")
            elif item.type == 'req_selector' or item.type == 'opt_selector':
                item.print()
            elif item.type == 'end':
                logger.info('cmd finished')
            else:
                raise ValueError("Invalid type")
            
    def print_req_selector(self):
        logger.info('req_selector')
        # if self.select_mode:
        #     logger.info(f'select_mode {self.select_mode}')

        if self.repeat > 1:
            logger.info(f'repeat {self.repeat}')
        for i, item in enumerate(self.mode):
            logger.info("Item:")
            item.print()
            if i < len(self.mode) - 1:
                logger.info("or")
        logger.info('req_selector end')

    def print_opt_selector(self):
        logger.info('opt_selector')
        if self.repeat > 1:
            logger.info(f'repeat {self.repeat}')
        self.print_req_selector()
        logger.info('opt_selector end')
        
    
    # 考虑多种情况的匹配，match的结果可以是多条路径（【TODO】）
    # 也可以考虑给节点
    # 目前的设计：输入逆序的待匹配字段列表；输出匹配的模式序列（关键字及赋值了的参数节点）及更新的待匹配字段列表
    # TODO：实现*和&<1-n>的匹配
    def match(self, cmd_list, traceback=False):
        """
        Args:
            cmd_list: 待匹配的命令行字符串
            traceback: 是否回溯
        Returns:
            匹配的模式序列（关键字及赋值了的参数节点）及更新的待匹配字段列表
        """
        logger.debug(f"match() {cmd_list}")
        if len(cmd_list) == 0:
            return [], cmd_list
        
        if cmd_list[-1] == 'EOC':
            if self.type == 'end' or self.type == 'pass':
                return [self], cmd_list
            elif self.type == 'opt_selector':
                return [self.mode[-1]], cmd_list    # 可选选择节点，直接匹配到pass节点
            else:
                # logger.debug(f"Unexpected end of command")
                return [], cmd_list                 # 未匹配到结束符
        

        matched_list = []
        if self.repeat > 1:
            logger.debug(f"repeat {self.repeat} in {self.type}")
            self_copy = copy.deepcopy(self)   # 复制一份当前节点
        type_hit = False
        for i in range(self.repeat):
            _matched_list = None
            matcher = self if i == 0 else copy.deepcopy(self_copy)

            if matcher.type == 'seq':
                _matched_list, cmd_list = matcher.match_seq(cmd_list, traceback)
                matched_list.extend(_matched_list)
                type_hit = True
            elif matcher.type == 'req_selector':
                _matched_list, cmd_list = matcher.match_req_selector(cmd_list, traceback)
                matched_list.extend(_matched_list)
                type_hit = True
            elif matcher.type == 'opt_selector':
                _matched_list, cmd_list = matcher.match_opt_selector(cmd_list)
                matched_list.extend(_matched_list)
                type_hit = True
            if not _matched_list:
                if self.repeat > 1:
                    logger.debug(f"Mismatched cmd_list {cmd_list} in repeat {i+1}")
                break
            if self.repeat > 1:
                logger.debug(f"Matched {matched_list} with cmd_list {cmd_list} in repeat {i+1}")
            # if self.type == 'seq':
            #     return self.match_seq(cmd_list)
            # elif self.type == 'req_selector':
            #     return self.match_req_selector(cmd_list)
            # elif self.type == 'opt_selector':
            #     return self.match_opt_selector(cmd_list)
            #     # return self.match_req_selector(cmd_list)  # 可选选择节点和必选选择节点的主要实现相同
        if type_hit:
            logger.debug(f"matched_list: {matched_list}, cmd_list: {cmd_list}")
            return matched_list, cmd_list
        
        # 由于关键字和参数的叶子节点并不是seq类型，因此在这里处理
        if self.type == 'keyword':
            if self.name == cmd_list[-1]:
                cmd_list.pop()
                # logger.debug(f"match keyword: {self.name}")
                return [self], cmd_list
            else:
                return [], cmd_list
        elif self.type == 'var':
            # 目前无法识别谁是真的变量，因此只能支持 &<1-32> 在最后的模式
            # self.value = cmd_list[-1]
            # cmd_list.pop()
            # # logger.debug(f"match var: {self.name} = {self.value}")
            # return [self], cmd_list
            values = ""
            for i in range(self.repeat):
                if cmd_list:
                    values = cmd_list[-1] if not values else values + ", " + cmd_list[-1]
                    cmd_list.pop()
                else:
                    break
            self.value = values.strip()
            # logger.debug(f"match var: {self.name} = {self.value}")
            return [self], cmd_list
        elif self.type == 'pass':
            return [self], cmd_list
        elif self.type == 'end':
            if cmd_list[-1] == 'EOC':
                cmd_list.pop()
                return [self], cmd_list
            else:
                return [], cmd_list         # 未匹配到结束符    
        else:
            raise ValueError(f"Invalid type {self.type}")

    def match_seq(self, cmd_list, traceback=False):
        cmd_list_0 = cmd_list.copy()                # 用于回溯
        matched_list = []
        while self.current_matching < len(self.mode):
            res, cmd_list = self.mode[self.current_matching].match(cmd_list)
            if res:
                matched_list.extend(res)
                self.current_matching += 1
            else:
                break
        if self.current_matching == len(self.mode): # 序列匹配完毕
            return matched_list, cmd_list
        else:
            return [], cmd_list_0                   # 匹配失败，回溯

    def match_req_selector(self, cmd_list, traceback=False):
        # 选择节点的匹配，只要有一个匹配成功即可
        res = []
        idx = 0
        repeated = 0
        while True:
            if idx >= len(self.mode):
                break
            if self.mode[idx].is_selected:
                idx += 1
                continue
            res_, cmd_list = self.mode[idx].match(cmd_list)
            if res_:
                res.extend(res_)
                # res.append(res_)
                self.mode[idx].is_selected = True
                repeated += 1
                if repeated < self.repeat:    # 带星号的选择节点，可以多次选择
                    idx = 0
                else:
                    return res, cmd_list
            else:
                idx += 1
        return res, cmd_list

    def match_opt_selector(self, cmd_list):
        # 选择节点的匹配，只要有一个匹配成功即可（因为pass节点的存在，理论上不会出现无法匹配的情况）
        res = []
        idx = 0
        repeated = 0
        while True:
            if idx >= len(self.mode) - 1:     # 最后一个节点是pass节点
                break
            if self.mode[idx].is_selected:
                idx += 1
                continue
            res_, cmd_list = self.mode[idx].match(cmd_list)
            if res_:
                res.extend(res_)
                # res.append(res_)
                self.mode[idx].is_selected = True
                repeated += 1
                if repeated < self.repeat:    # 带星号的选择节点，可以多次选择
                    idx = 0
                else:
                    return res, cmd_list
            else:
                idx += 1
        if not res:
            res_, cmd_list = self.mode[-1].match(cmd_list)
            if res_:
                res.extend(res_)
        if not res:
            raise ValueError("Opt selector should always match")
        return res, cmd_list

    def get_cmd(self):
        """
        获取主Command
        """
        cmd_list = []
        if self.type == 'seq':
            for item in self.mode:
                if item.type == 'keyword':
                    cmd_list.append(item.name)
                else:
                    break
        else:
            logger.error(f"Invalid type {self.type}")
        return " ".join(cmd_list)


# 配置模型：多叉树
# 目前：唯一匹配，不考虑模棱两可的情况（因此实际还要结合最长前缀匹配，给置信度）
def match_cmd_graph(cmd_str, mode_str):
    """
    精确匹配命令行和命令模式
    Args:
        cmd_str: 待匹配的命令行字符串
        mode_str: 命令模式字符串
    Returns:
        精确的匹配结果列表 List[CmdGraph]
    """
    # logger.info(f"Begin to match cmd: {cmd_str} of mode: {mode_str}")
    # 构建命令图
    modes = parse_vdm_cli_format(mode_str.split('##')[0])
    logger.debug(f" matching cmd: {cmd_str} of mode: {modes}")
    # match graph cache by hash
    if hash(tuple(modes)) in CMD_GRAPH_CACHE:
        graph = CMD_GRAPH_CACHE[hash(tuple(modes))]
        logger.debug("cache hit!")
        graph.reset()
        # print(f"old = new? : {str(modes) == VERIFY_CACHE[hash(tuple(modes))]}")
    else:
        graph = CmdGraph('seq', modes)
        CMD_GRAPH_CACHE[hash(tuple(modes))] = graph
        # VERIFY_CACHE[hash(tuple(modes))] = str(modes)
    graph = CmdGraph('seq', modes)
    # graph.print()
    # 匹配命令
    # cmd_list = cmd_str.split(' ')
    cmd_list = split_command(cmd_str)
    cmd_list.append('EOC')
    cmd_list.reverse()
    res, _ = graph.match(cmd_list)
    return res
        
def get_matched_str(matched_cmds):
    res = []
    for cmd in matched_cmds:
        if cmd.type == 'keyword':
            res.append(cmd.name)
        elif cmd.type == 'var':
            res.append(f"{cmd.value} (<{cmd.name}>)")
        elif cmd.type == 'pass':
            # res.append('(pass optional)')
            pass
        elif cmd.type == 'end':
            # res.append('cmd finished')
            pass
        else:
            raise ValueError("Invalid type")
    return " ".join(res)

def get_all_syntax_matches(cmd_str, all_clis):
    matches = []
    for cli in all_clis:
        matched = match_cmd_graph(cmd_str.strip(), cli)
        if matched:
            matches.append(cli)
    return matches

def get_syntax_correctness(config, all_clis):
    configs = [line.strip() for line in config.split('\n') if line.strip()]
    if not configs:
        return 0
    matched_n = 0
    for line in configs:
        matches = get_all_syntax_matches(line, all_clis)
        if matches:
            matched_n += 1
            # print(f"Matched: {line} -> {matches}")
    # print(f"Matched {matched_n} out of {len(configs)} lines")
    return matched_n / len(configs)

# 获取列表lst中index的排序位置
def get_sorted_index(lst, index):
    # 获取列表中所有元素的排序位置
    sorted_indices = sorted(range(len(lst)), key=lambda i: lst[i], reverse=True)
    # 找到指定下标对应值的排序位置
    sorted_index = sorted_indices.index(index)
    return sorted_index

def find_cmds(file_path):
    """
    从config文件中提取cmd
    Args:
        file_path: config文件路径
    Returns:
        result: 提取到的cmd列表（set）
    """

    # 需要过滤的命令
    cmds_to_filter = ["system-view", "commit", "quit", "return", "exit", "display"]

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    # 匹配形如 [**标签**]内容 的结构
    pattern = r'\[\*\*(.*?)\*\*\](.*?)(?=\[\*\*|$)'
    matches = re.findall(pattern, text, re.DOTALL)
    result = {label.strip().replace("\_", "_") for label, _ in matches if label.strip() not in cmds_to_filter}
    return result

def get_json_content(manual_path, extra_info_limits=150) -> str:
    manual_fields = ["FuncDef", "CLIs", "ParentView", "ParaDef"] # ["PageTitle", "FuncDef", "CLIs", "ParentView", "ParaDef", "Example", "ExtraInfo"]
    logger.debug(f"Extracting manual from {manual_path}")
    manual_retrieved = ""
    
    with open(manual_path, 'r', encoding='utf-8') as f:
        try:
            manual = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e} in {manual_path}")
            return ""
        manual_retrieved += f"{manual['PageTitle']}\n"
        for field in manual_fields:
            manual_retrieved += f"#### {field}\n{manual[field]}\n"
        if "ExtraInfo" in manual and manual["ExtraInfo"]:
            ExtraInfos = manual["ExtraInfo"].split(" ")
            if len(ExtraInfos) > extra_info_limits:
                ExtraInfo = " ".join(ExtraInfos[:extra_info_limits])
                manual_retrieved += f"#### ExtraInfo\n{ExtraInfo}...\n"
            else:
                manual_retrieved += f"#### ExtraInfo\n{manual['ExtraInfo']}\n"
        return manual_retrieved
        
if __name__ == "__main__":
  
    # parser test
    mode = "undo synchronization##BGP view"
    cmd = "undo synchronization"
   
    print("Exact: ", get_matched_str(match_cmd_graph(cmd, mode)))
    print("Fuzzy: ", command_match_fuzzy(cmd, mode))
