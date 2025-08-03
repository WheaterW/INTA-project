from markdownify import markdownify as md
import requests
import time
import json
import os
import re

# match the commands of the markdown
def find_cmds(markdown):
    pattern = r'\[\*\*(.*?)\*\*\]'
    match = re.findall(pattern, markdown)
    # print(match)
    return match
    
# match the description of the markdown
def find_desc(markdown):
    pattern = r"^\s*={3,}\s*\n(.*?)\n\s*#{3,}"
    res = ""
    match = re.findall(pattern, markdown, re.DOTALL | re.MULTILINE)
    if match:
        res = match[0].strip()
        if res.startswith("####"):
            res = ""
            print("Passing a markdown...")
    # print(match)
    res_list = res.strip().split("\n")
    res = res_list[0].strip()   # only keep the first line of the description
    res = res.replace("\_", "underline").replace("_", " ").replace("underline", "_")
    return res

def flatten_desc(desc, k=300):
    res = []
    for line in desc.split("\n"):
        if line.startswith("![]"):
            continue
        for word in line.split(" "):
            res.append(word)
    if len(res) > k:
        res = res[:k]
        res.append("...")
    return " ".join(res)

# match the description of the markdown
def extract_section(content, section_title="#### Purpose"):
    # 构造正则表达式，匹配标题和其后的段落内容
    pattern = rf'{re.escape(section_title)}\n(.*?)(?=\n#### |\Z)'  # 假设####开头为下一个段落标题
    match = re.search(pattern, content, re.DOTALL)  # 使用re.DOTALL匹配跨行内容
    if match:
        return match.group(1).strip()  # 返回匹配的内容，去除首尾空格
    return None

def contains_sublist(main_list, sub_list):
    if not sub_list:
        return True
    if len(sub_list) > len(main_list):
        return False
    for i in range(len(main_list) - len(sub_list) + 1):
        if main_list[i:i+len(sub_list)] == sub_list:
            return True
    return False

def has_duplicate_elements(lst):
    unique_elements = set()
    for element in lst:
        if element in unique_elements:
            return True
        unique_elements.add(element)
    return False

def collect_corpus(base_path, config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        configs = json.load(f)
    current_path = base_path
    parent_list = []
    cmd_manual_flat = []
    errors = []

    for dict in configs:
        timer = time.time()
        _parent_list = [parent.replace(" ", "_") for parent in dict['parent_list'][1:]]
        for i in range(len(_parent_list)):
            if '/' in _parent_list[i]:
                _parent_list[i] = _parent_list[i].replace("/", "_and_")
        for i in range(len(parent_list)):
            if '/' in parent_list[i]:
                parent_list[i] = parent_list[i].replace("/", "_and_")
                
        if len(_parent_list) > 0 and len(_parent_list) >= len(parent_list):
            if parent_list == []:
                parent_list = _parent_list
            elif len(_parent_list) > len(parent_list) and '...' not in _parent_list:
                parent_list = _parent_list
            elif _parent_list[-1] != parent_list[-1]:
                parent_list.append(_parent_list[-1])
        elif len(parent_list) == 0 or len(_parent_list) == 0:
            parent_list = _parent_list
        elif "..." == _parent_list[0] and _parent_list[-1] != parent_list[-1]:
            # parent_list.append(_parent_list[-1])
                        # 如果是进入下一级：当前的-1成为了-2
            # 如果是平级：当前的-2还是-2
            # 如果是返回：...序列之后的内容是当前真正层级列表的子序列
            # 其他：未覆盖情况。bug
            if parent_list[-1] == _parent_list[-2]: # 进入下一级
                print(f"Entering next level: {parent_list} -> {_parent_list}")
                parent_list.append(_parent_list[-1])
            elif parent_list[-2] == _parent_list[-2]: # 平级
                print(f"Entering same level: {parent_list} -> {_parent_list}")
                parent_list[-1] = _parent_list[-1]
            else:
                print(f"Returning to parent: {parent_list} -> {_parent_list}?")
                if not contains_sublist(parent_list, _parent_list[1:]):
                    print("Error: ", parent_list, _parent_list)
                    exit()
                # 寻找_parent_list[-1] 在parent_list中的位置
                # 找到位置后，进行截断
                parent_list = parent_list[:parent_list.index(_parent_list[-1])+1]
        elif "..." != _parent_list[0]:
            parent_list = _parent_list
        
        print("*" * 20)
        print(_parent_list)
        print(parent_list)
        if len(parent_list) > 3:
            if has_duplicate_elements(parent_list[3:]):
                print("Error: ", parent_list)

        current_path = base_path + '/' + "/".join(parent_list) + "/"
        current_path_url = base_path + '/src/' + "/".join(parent_list) + "/"
        print(current_path)
        print(current_path_url)
        # continue
        if not os.path.exists(current_path):
            os.makedirs(current_path)
        if not os.path.exists(current_path_url):
            os.makedirs(current_path_url)
        response = requests.get(dict['src'])
        markdown = md(response.text).lstrip()
        if "config_corpus" in base_path:
            if "####" not in markdown:  # skip the index pages (NE40E)
                print("Passing: " + dict['src'])
                continue
        if "cmd_corpus" in base_path:
            if "Format\n------" not in markdown:  # skip the index pages (CE6881)
                print("Passing: " + dict['src'])
                continue

        print("Processing: ", dict['src'])
        idx = markdown.find("Parent Topic")
        if idx != -1:
            markdown = markdown[:idx].rstrip()
        markdown = markdown.lstrip()
        # print(markdown)
        markdown = markdown.split("\n", 1)[1].strip() # split the redundant title
        markdowns = markdown.split("\n", 2)

        title = markdowns[0].replace(" ", "_")
        if '/' in title:
            title = title.replace("/", "_and_")
        # print(title)
        # print("markdown:\n", markdown)
        desc = find_desc(markdown)
        # print('desc: ', desc)
        if desc == "":
            final_markdown = "\n".join(markdowns[:2]) + "\n\n" + markdowns[0] + "\n" + markdowns[2]
        else:
            final_markdown = markdown
        # print("final_markdown:\n", final_markdown)
        # exit()
        try:
            with open(current_path + title + ".md", "w", encoding="utf-8") as f:
                f.write(final_markdown)
            with open(current_path_url + title + ".html", "w", encoding="utf-8") as f:
                f.write(response.text)
        except Exception as e:
            print("Error: ", e)
            errors.append(dict['src'])
            # continue
        # exit()
        print(current_path+title)
        cmd_manual_flat.append({
            "title": title,
            "desc": desc if desc != "" else title,
            "path": current_path + title + ".md",
            "cmds": find_cmds(final_markdown)
        })
        if time.time() - timer < 1:
            time.sleep(1)

    with open(base_path + 'cmd_manual_flat.json', 'w', encoding='utf-8') as f:
        json.dump(cmd_manual_flat, f, ensure_ascii=False, indent=4)
    print("Errors: ", errors)
    with open(base_path + 'errors.json', 'w', encoding='utf-8') as f:
        json.dump(errors, f, ensure_ascii=False, indent=4)
    


# Tree-based manual hierarchy
# 需要获得每个视图下的名字+描述
# 文件夹描述来源：About this document、Overview of ***、文件夹名字
def make_manual_tree():
    config_corpus_path = "/root/MyConfigTrans/nassim-main/corpus/hw/hw_NE40E_V800R012C10/config_corpus/Configuration"


if __name__ == '__main__':
    # NE40E config
    # config_path = 'nassim-main/corpus/hw/Configuration_NE40E_config.json'
    # base_path = 'nassim-main/corpus/hw/hw_NE40E_V800R012C10/config_corpus'
    # CE6800 cmd
    config_path = 'nassim-main/corpus/hw/Configuration_CE6800_cmd.json'
    base_path = 'nassim-main/corpus/hw/hw_CE6800_V300R023C00/cmd_corpus'
    # CE6800 config
    # config_path = 'nassim-main/corpus/hw/Configuration_CE6800_config.json'
    # base_path = 'nassim-main/corpus/hw/hw_CE6800_V300R023C00/config_corpus'
    with open(config_path, 'r', encoding='utf-8') as f:
        configs = json.load(f)
    print(len(configs))
    collect_corpus(base_path, config_path)
    # make_manual_tree()
    
# nohup python collect_corpus.py > cmd_collect_1.log 2>&1 &
# nohup python collect_corpus.py > collect_corpus_ne40e_config.log 2>&1 &
# nohup python collect_corpus.py > collect_corpus_ce6800_cmd.log 2>&1 &