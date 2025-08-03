# ====================================================
# Author: Yunze Wei <yunzewei@outlook.com>
# Date: 2025-08-03
# Description: Parser for network device configurations.
# ====================================================

from utils import *
import argparse

class Candidate(object):
    def __init__(self, matched_str, node):
        self.matched_len = len(matched_str)
        self.matched_str = matched_str
        self.node = node

    # 重载比较运算符，把小顶堆变成大顶堆
    def __lt__(self, other):
        return self.matched_len < other.matched_len

# 构建配置树
def build_config_tree_nokia(config, hierarchy_node_root, hierarchy_node_dict=None):
    # 从root节点开始匹配，优先匹配子节点，再递归地匹配父节点中的子节点、爷爷节点中的子节点...
    config = config.split('\n')
    # 取消虚拟根节点匹配
    # if not config[0].strip().startswith('config'):    # 确保根节点匹配
    #     config = ['config\n'] + config
    current_hierarchy_node = hierarchy_node_root      # 初始化为虚拟hierarchy节点
    previous_hierarchy_node = current_hierarchy_node  # 用于记录上一个匹配的节点
    config_root = ConfigNode('virtual root', current_hierarchy_node)
    config_root.parent = config_root    # 虚拟根节点的父节点同样自环
    current_config_node = config_root
    previous_config_node = current_config_node     # 用于记录上一个匹配的节点
    logger.debug('root: ' + config_root.cli + ', current_hierarchy_node:' + current_hierarchy_node.cli)
    # 总体思路：current_***_node表示当前匹配的视图（即匹配命令的父节点），每次搜索贪婪地往深度方向搜索，若匹配失败则回溯到上一层
    for line_ in config:
        line_ = line_.strip()
        logger.debug('line: ' + line_ + ', current_hierarchy_node:' + current_hierarchy_node.cli + ", current_config_node:" + current_config_node.cli)
        manual = None
        if not line_:
            continue
        # depart manual from line
        match = re.match(r'^(.*?)\s*(\[[^\]]*\])$', line_.strip())
        if match:
            line = match.group(1)
            manual = match.group(2)
            logger.debug(f'get manual: {manual} for line: {line}')
            if manual:
                _manuals = json.loads(manual)
                for _manual in _manuals:
                    if not os.path.exists(_manual):
                        logger.error(f'Error: manual file not exist: {_manual}')
                        continue
                    else:
                        logger.info(f"Manual file: {_manual} exists")
        else:
            line = line_
        logger.debug(f"line: {line}, manual: {manual}")
        # continue
        # 特判
        if "exit" == line:
            continue
        # 从当前节点的儿子开始，逐个匹配，若没有匹配去父级节点及儿子进行匹配
        while True:
            curr_match_view = ""
            curr_match_cli = ""
            cmd_graph_view = None        # exact match
            cmd_graph_cli = None
            view_match_node = None
            cli_match_node = None
            cli_fuzzy_match = []
            is_cli_match = False
            logger.debug('  current_hierarchy_node:' + current_hierarchy_node.cli)
            # 匹配view节点，必须单词匹配
            for child in current_hierarchy_node.children:
                if child.type == 'view' or child.type == 'cli_' and "##" not in child.cli:
                    view_name = child.cli.split('>')[-1]
                    logger.debug('    view: ' + view_name)
                    if line.find(view_name) != -1:
                        view_match_node_ = child
                        # curr_match_ = view_name
                        cmd_graph_ = match_cmd_graph(line, view_name)
                        curr_match_ = get_matched_str(cmd_graph_)
                        logger.debug('  prefix:' + curr_match_ + ', len:' + str(len(curr_match_)) + ", cli:" + child.cli)
                        if len(curr_match_) > len(curr_match_view): # 精确匹配
                            cmd_graph_view = cmd_graph_
                            curr_match_view = curr_match_
                            view_match_node = view_match_node_
                        elif len(view_name) > len(curr_match_view): # 模糊匹配
                            curr_match_view = view_name
                            view_match_node = view_match_node_
            logger.debug('    view_match_node:' + view_match_node.cli if view_match_node else "None")
            # 匹配cli节点
            for child in current_hierarchy_node.children:
                if child.type == 'cli' or child.type == 'cli_' and "##" in child.cli:
                    logger.debug('    cli:' + child.cli)

                    if "[ no ] " in child.cli:
                        active_cli = child.cli.replace("[ no ] ", "")
                        passive_cli = child.cli.replace("[ no ] ", "no ")
                        logger.debug('    active_cli:' + active_cli + ', passive_cli:' + passive_cli)
                        curr_match_ = max([command_match_fuzzy(line, active_cli), command_match_fuzzy(line, passive_cli)], key=len, default="")
                        logger.debug('    prefix:' + curr_match_ + ', len:' + str(len(curr_match_)) + ", cli:" + child.cli)
                    else:
                        curr_match_ = command_match_fuzzy(line, child.cli)
                    if curr_match_:
                        logger.debug('  prefix:' + curr_match_ + ', len:' + str(len(curr_match_)) + ", cli:" + child.cli)
                        cli_fuzzy_match.append(Candidate(curr_match_, child))

                        is_cli_match = True
            cli_fuzzy_match = sorted(cli_fuzzy_match, reverse=True)
            if cli_fuzzy_match:
                for i in range(len(cli_fuzzy_match)):
                    logger.debug(cli_fuzzy_match[i].matched_str)
            if cli_fuzzy_match:
                for i in range(len(cli_fuzzy_match)):
                    candidate = cli_fuzzy_match[i]
                    if i == 0:  # 先取最长的匹配结果
                        curr_match_cli = candidate.matched_str
                        cli_match_node = candidate.node
                    cmd_graph_cli_ = match_cmd_graph(line, candidate.node.cli)
                    exact_match_ = get_matched_str(cmd_graph_cli_)
                    if exact_match_:    # 再取精确匹配结果
                        curr_match_cli = exact_match_
                        cli_match_node = candidate.node
                        cmd_graph_cli = cmd_graph_cli_
                        break

            logger.debug(cli_match_node.cli if cli_match_node else "None")
            logger.debug(view_match_node.cli if view_match_node else "None")

            if cli_match_node or view_match_node:      # 匹配成功
                use_cli_match = True if cli_match_node else False
                if cli_match_node: logger.debug('  max_match_node:' + cli_match_node.cli)
                if view_match_node: logger.debug('  view_match_node:' + view_match_node.cli)
                if cli_match_node:
                    if not cli_match_node.children and view_match_node: # 视图和cli都匹配成功，但cli没有子节点且视图有子节点
                        current_hierarchy_node = view_match_node
                        previous_hierarchy_node = current_hierarchy_node
                        current_config_node.children.append(ConfigNode(line, current_hierarchy_node, current_config_node, curr_match_view, cmd_graph_cli, cli_match_node, manuals=json.loads(manual) if manual else None)) # 用视图节点，cli节点作为附节点
                        use_cli_match = False
                    else:   # cli匹配成功
                        current_hierarchy_node = cli_match_node
                        previous_hierarchy_node = current_hierarchy_node
                        current_config_node.children.append(ConfigNode(line, current_hierarchy_node, current_config_node, curr_match_cli, cmd_graph_cli, manuals=json.loads(manual) if manual else None))
                else:   # 仅视图匹配成功
                    current_hierarchy_node = view_match_node
                    previous_hierarchy_node = current_hierarchy_node
                    current_config_node.children.append(ConfigNode(line, current_hierarchy_node, current_config_node, curr_match_view, cmd_graph_view, manuals=json.loads(manual) if manual else None))
                current_config_node = current_config_node.children[-1]  # 更新配置视图
                previous_config_node = current_config_node  # 更新上一个匹配的节点
                if is_cli_match and use_cli_match:
                    # 如果是cli节点，查找其中的视图子节点第一个是否是view节点，如果是，则一定是层级关系
                    for child in current_hierarchy_node.children:
                        if child.type == 'view':
                            view_name = child.cli.split('>')[-1]
                            if line.find(view_name) != -1:
                                current_hierarchy_node = child
                                previous_hierarchy_node = current_hierarchy_node
                                current_config_node.children.append(ConfigNode(line, current_hierarchy_node, current_config_node, curr_match_cli, cmd_graph_cli, manuals=json.loads(manual) if manual else None))   # 假设视图不会嵌套
                                current_config_node = current_config_node.children[-1]
                                previous_config_node = current_config_node
                                break
                break   # 匹配成功，跳出循环
            else:
                # if current_hierarchy_node.parent:   # 递归匹配父节点。存在视图回探问题，例如视图的父节点才是精准匹配，但视图的子节点是模糊匹配；可以在实际使用时窥探父节点解决该问题
                if not current_hierarchy_node.is_virtual:
                    current_hierarchy_node = current_hierarchy_node.parent
                    current_config_node = current_config_node.parent
                else:
                    logger.error('  No match for line:' + line)
                    # 未匹配到任何节点，增加“虚空节点”，挂在当前节点之后
                    no_matching_hierarchy_node = HierarchyNode()
                    no_matching_hierarchy_node.type = 'blank'
                    no_matching_hierarchy_node.cli = 'blank'
                    no_matching_hierarchy_node.depth = previous_hierarchy_node.depth
                    current_config_node = previous_config_node.parent   # 恢复到上一个匹配的节点
                    current_hierarchy_node = previous_hierarchy_node.parent
                    try:
                        manuals = json.loads(manual) if manual else None
                    except Exception as e:
                        logger.error(f"manual: {manual}")
                        logger.error(e)
                        manuals = None
                    current_config_node.children.append(ConfigNode(line, no_matching_hierarchy_node, current_config_node, "", manuals=manuals))      # 增加虚空节点
                    break
    # config_root.print()

    return config_root

# 1201: 增加虚空节点（非匹配节点）
# - 挂载位置：为了保序，应当挂载在上一节点之后
# - 标记为虚空即可，无需单独处理

# 华为解析器
def match_node(line, current_hierarchy_node):
    """ match current cmd line with current hierarchy node
    Args:
        line: current cmd line
        current_hierarchy_node: current hierarchy node
    Returns:
        curr_match_node (HierarchyNode): matched node
        curr_match_str (str): matched string
        is_cli_match (bool): whether the matched node is cli node
        cmd_graph (CmdGraph): matched cmd graph        
    """
    logger.debug(f'matching line: {line}')
    if not current_hierarchy_node:
        logger.error('current_hierarchy_node is None')
        return None, "", False, None
    max_match_len = 0
    curr_match_node = None
    curr_match_str = ""
    cmd_graph = None
    cli_fuzzy_match = []
    is_cli_match = False
    is_undo = False
    if line.startswith('undo '):
        is_undo = True
        line = line[5:]
    for child in current_hierarchy_node.children:
        if child.type == 'view':
            view_name = child.cli.lower()
            cli_format = line.split(' ')[0].replace('-', ' ').lower()
            logger.debug('    view:' + view_name)
            # if view_name.find(cli_format) != -1:
            if cli_format == view_name:         # 先尝试严格匹配，若有问题需要宽松
                curr_match_node = child
                curr_match_str = view_name
                cmd_graph = match_cmd_graph(line, view_name)
    if not curr_match_node: 
        # 匹配cli节点
        for child in current_hierarchy_node.children:
            if child.type == 'cli' or child.type == 'cli_':
                logger.debug('    cli:' + child.cli)

                prefix = command_match_fuzzy(line, child.cli)
                if not prefix and is_undo:  # 如果没有匹配到，尝试undo命令
                    prefix = command_match_fuzzy('undo ' + line, child.cli)
                if prefix:
                    logger.debug('  prefix:' + prefix + ', len:' + str(len(prefix)) + ", cli:" + child.cli)

                    cli_fuzzy_match.append(Candidate(prefix, child))
                    is_cli_match = True
    logger.debug('    cli_fuzzy_match:' + str(cli_fuzzy_match))
    if cli_fuzzy_match:
        cli_fuzzy_match = sorted(cli_fuzzy_match, reverse=True)
        for i in range(len(cli_fuzzy_match)):
            candidate = cli_fuzzy_match[i]
            # 对华为不做FUZZY匹配，只取精确匹配

            cmd_graph_ = match_cmd_graph(line, candidate.node.cli)
            if not cmd_graph_ and is_undo:  # 如果没有匹配到，尝试undo命令
                cmd_graph_ = match_cmd_graph('undo ' + line, candidate.node.cli)

            exact_match_ = get_matched_str(cmd_graph_)
            if exact_match_:
                curr_match_str = exact_match_
                curr_match_node = candidate.node
                cmd_graph = cmd_graph_
                break
    logger.debug('    cli_match_node:' + (curr_match_node.cli if curr_match_node else "None"))
    return curr_match_node, curr_match_str, is_cli_match, cmd_graph  # 如果cmd_graph为空，表示没有精确匹配


# 构建配置树
def build_config_tree_huawei(config, hierarchy_node_root, hierarchy_node_dict=None):
    # 从root节点开始匹配，优先匹配子节点，再递归地匹配父节点中的子节点、爷爷节点中的子节点...
    # if not config.startswith('system-view'):    # 确保根节点匹配
    #     config = 'system-view\n' + config
    config = config.split('\n')
    current_hierarchy_node = hierarchy_node_root
    previous_hierarchy_node = current_hierarchy_node  # 用于记录上一个匹配的节点
    config_root = ConfigNode('virtual root', current_hierarchy_node)
    config_root.parent = config_root    # 虚拟根节点自环
    current_config_node = config_root
    previous_config_node = current_config_node     # 用于记录上一个匹配的节点
    logger.debug('root: ' + config_root.cli + ', current_hierarchy_node:' + current_hierarchy_node.cli)
    current_interface = None
    previous_interface = None
    is_sub_interface = False
    previous_is_sub_interface = False
    for line_ in config:
        line_ = line_.strip()
        manual = None
        if not line_:
            continue
        # depart manual from line
        match = re.match(r'^(.*?)\s*(\[[^\]]*\])$', line_.strip())
        if match:
            line = match.group(1)
            manual = match.group(2)
            logger.debug(f'get manual: {manual} for line: {line}')
        else:
            line = line_
        logger.debug('line: ' + line + ', current_hierarchy_node:' + current_hierarchy_node.cli + ", current_config_node:" + current_config_node.cli)

        # 从当前节点的儿子开始，逐个匹配，若没有匹配去父级节点及儿子进行匹配
        while True:
            curr_match_node = None
            curr_match_str = ""
            is_cli_match = False
            cmd_graph = None
            is_undo = False
            logger.debug('  current_hierarchy_node:' + current_hierarchy_node.cli)
            # 不同Interface需要分开处理
            if current_interface:
                if current_interface == 'Loopback' or current_interface == "Tunnel" or current_interface == "Eth-Trunk":
                    interface_type = f"{current_interface} interface view"
                elif current_interface == 'GE':  
                    interface_type = f"{current_interface} sub-interface view" if is_sub_interface else f"{current_interface} electrical interface view"
                else:
                    interface_type = f"{current_interface} sub-interface view" if is_sub_interface else f"{current_interface} interface view"
                logger.debug('  current_interface:' + current_interface)
                logger.debug('  interface_type:' + interface_type)
                all_interface_view = current_hierarchy_node.find_child("all-interface view")
                if all_interface_view:
                    curr_match_node, curr_match_str, is_cli_match, cmd_graph = match_node(line, all_interface_view)
                if not curr_match_node:
                    specific_interface_view = current_hierarchy_node.find_child(interface_type)    # hard code
                    curr_match_node, curr_match_str, is_cli_match, cmd_graph = match_node(line, specific_interface_view)
            else:
                curr_match_node, curr_match_str, is_cli_match, cmd_graph = match_node(line, current_hierarchy_node)
            
            # if curr_match_node and 'interface' in line:  # 检查当前匹配的interface节点是否包含所需接口类型
            if curr_match_node and line.strip().startswith('interface'):    # 避免匹配到内含interface的节点，例如 bfd all-interfaces enable 
                interface_name = extract_uppercase(line)
                if 'loopback' in line.lower():
                    interface_name = 'Loopback'
                logger.debug('curr_match_node.cli: ' + curr_match_node.cli)
                logger.debug("INTERFACE_TYPE: " + interface_name)
                interface_match = False
                for views in curr_match_node.renderview:
                    if interface_name in views:
                        interface_match = True
                        break
                if not interface_match:
                    curr_match_node = None

            # 优先匹配view节点，必须单词匹配
            if curr_match_node:
                logger.debug('  max_match_node:' + curr_match_node.cli)
                current_config_node.children.append(ConfigNode(line, curr_match_node, current_config_node, curr_match_str, cmd_graph, manuals=json.loads(manual) if manual else None))
                if not current_interface:   # 假设接口视图的cli节点不会有子节点
                    current_hierarchy_node = curr_match_node     # 更新模型视图
                    previous_hierarchy_node = current_hierarchy_node
                    current_config_node = current_config_node.children[-1]  # 更新配置视图为新增的节点
                    previous_config_node = current_config_node
                if is_cli_match and not current_interface:  # 假设接口视图的cli节点不会有子节点
                    if current_hierarchy_node.cli.startswith('interface'):   # 记录当前接口规格，不进入特定视图
                        if 'Loopback' in line or 'LoopBack' in line:  # Loopback接口debug
                            current_interface = 'Loopback'
                        elif 'Tunnel' in line:
                            current_interface = 'Tunnel'
                        elif 'Eth-Trunk' in line:
                            current_interface = 'Eth-Trunk'
                        else:
                            current_interface = extract_uppercase(line)
                        previous_interface = current_interface
                        logger.debug('  current_interface:' + current_interface)
                        if '.' in line:
                            is_sub_interface = True
                            previous_is_sub_interface = is_sub_interface
                    else:
                        # 如果是cli节点，查找其中的视图子节点第一个是否是view节点，如果是，则一定是层级关系
                        view_children = []
                        for child in current_hierarchy_node.children:
                            if child.type == 'view':
                                view_children.append(child)
                        if len(view_children) == 1 or current_hierarchy_node.cli == 'domain <domain-name>##AAA view': # 假设只有一个子视图节点就是本身；特判
                            child = view_children[0]
                            view_name = child.cli.lower().replace('-', ' ')
                            cli_format = line.split(' ')[0].replace('-', ' ').lower()
                            logger.debug('  view_name:' + view_name + ', cli_format:' + cli_format)
                            current_hierarchy_node = child
                            previous_hierarchy_node = current_hierarchy_node
                            current_config_node.children.append(ConfigNode(line, current_hierarchy_node, current_config_node, view_name, manuals=json.loads(manual) if manual else None))
                            current_config_node = current_config_node.children[-1]
                            previous_config_node = current_config_node
                            break
                        else:
                            logger.debug('  view_children:' + str(view_children))
                break   # 匹配成功，跳出循环
            else:
                # if current_hierarchy_node.parent:   # 递归匹配父节点
                if not current_hierarchy_node.is_virtual:
                    if "interface" in current_hierarchy_node.cli and current_hierarchy_node.type == 'cli':
                        current_interface = None
                        # previous_interface = None
                        is_sub_interface = False
                        # previous_is_sub_interface = False
                    logger.debug('  current_hierarchy_node:' + current_hierarchy_node.cli)

                    current_hierarchy_node = current_hierarchy_node.parent
                    logger.debug('  new_hierarchy_node:' + current_hierarchy_node.cli)
                    current_config_node = current_config_node.parent
                    if "interface view" in current_hierarchy_node.cli and current_hierarchy_node.type == 'view':  # 退出接口视图
                        current_hierarchy_node = current_hierarchy_node.parent
                        current_config_node = current_config_node.parent
                else:
                    logger.error('  No match for line:' + line)
                    # 未匹配到任何节点，增加“虚空节点”，挂在当前节点之后
                    no_matching_hierarchy_node = HierarchyNode()
                    no_matching_hierarchy_node.cli = 'blank'
                    no_matching_hierarchy_node.type = 'blank'
                    no_matching_hierarchy_node.depth = previous_hierarchy_node.depth
                    current_interface = previous_interface
                    is_sub_interface = previous_is_sub_interface
                    if previous_interface:      # 接口下没有进入父视图
                        current_config_node = previous_config_node
                        current_hierarchy_node = previous_hierarchy_node
                    else:
                        current_config_node = previous_config_node.parent   # 恢复到上一个匹配的节点
                        current_hierarchy_node = previous_hierarchy_node.parent
                    try:
                        manuals = json.loads(manual) if manual else None
                    except Exception as e:
                        logger.error(f"manual: {manual}")
                        logger.error(e)
                        manuals = None
                    current_config_node.children.append(ConfigNode(line, no_matching_hierarchy_node, current_config_node, "", manuals=manuals))      # 增加虚空节点
                    break
    # config_root.print()
    return config_root


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-p", "--path", help="config file path")
    argparser.add_argument("-m", "--model", default="huawei", help="model type, huawei or nokia")
    args = argparser.parse_args()

    hw_hierarchy_file_path = 'nassim-main/corpus/hierarchy/cmd_tree_hw_system_view.json'
    nokia_hierarchy_file_path = 'nassim-main/corpus/hierarchy/cmd_tree_nokia_opt.json'

    with open(args.path, 'r') as f:
        config = purify_configuration(f.read())

    if args.model == 'huawei':
        hw_hierarchy_root, hw_hierarchy_node_dict = build_hierarchy_tree(hw_hierarchy_file_path)
        config_tree = build_config_tree_huawei(config, hw_hierarchy_root, hw_hierarchy_node_dict)
    elif args.model == 'nokia':
        nokia_hierarchy_root, nokia_hierarchy_node_dict = build_hierarchy_tree(nokia_hierarchy_file_path)
        config_tree = build_config_tree_nokia(config, nokia_hierarchy_root, nokia_hierarchy_node_dict)

    config_tree.print()

# Test
# python parser.py -m nokia -p 'test_dataset/spark/ALU_validation_set(no_answer)v2/1.txt'
# python parser.py -m huawei -p Result/test_dataset/dataset-merge-revised/nokia/LLM_2025-02-10-16-19-54_deepseek-v3_irag/8ref_exd_4.txt