from multi_agent import CriticAgent
from utils import *
from config_parser import build_config_tree_huawei, build_config_tree_nokia
import argparse
import ast

def build_config_tree(config, hierarchy_root, parser_type='nokia'):
    if parser_type == 'huawei':
        config_root = build_config_tree_huawei(config, hierarchy_root)
    elif parser_type == 'nokia':
        config_root = build_config_tree_nokia(config, hierarchy_root)
    logger.info(f"{parser_type}_config_tree:")

    config_unit = None


    return config_root, config_unit

def basic_evaluation(translation, label):
    """
    Get EM, BLEU, ROUGE scores
    """
    translation = purify_configuration(translation)
    label = purify_configuration(label)
    lines = len(translation.split('\n'))
    critic = CriticAgent()
    EM = critic.exact_match(label, translation)
    logger.info(f"Exact Match: {EM}")
    BLEU_1, BLEU_2, BLEU_3, BLEU_4 = critic.bleu(label, translation)
    logger.info(f"BLEU-1: {BLEU_1}, BLEU-2: {BLEU_2}, BLEU-3: {BLEU_3}, BLEU-4: {BLEU_4}")
    ROUGE_1, ROUGE_2, ROUGE_L = critic.rouge(label, translation)
    logger.info(f"ROUGE-1: {ROUGE_1}, ROUGE-2: {ROUGE_2}, ROUGE-L: {ROUGE_L}")
    # exit()
    return EM, BLEU_1, BLEU_2, BLEU_3, BLEU_4, ROUGE_1, ROUGE_2, ROUGE_L, lines

def view_and_syntax_evaluation(translation_config_root, hw_all_clis):
    """
    Get TM, TM+ scores
    Args:
        config_root: config tree of the translation
        hw_all_clis: all commands in the hierarchy tree
    """
    config_lines = translation_config_root.get_lines()
    mismatched_lines_ = translation_config_root.get_mismatched_lines(pure=True)


    matching_str = ""
    Tree_match = translation_config_root.print_to_str()
    matching_str += Tree_match + '\n'
    rematched = []
    mismatched_lines = []
    for cmd in mismatched_lines_:
        if cmd.strip() == 'undo shutdown':
            continue
        matching_str += "Mismatched (view): " + cmd + '\n'
        mismatched_lines.append(cmd)
        rematched_cmds = get_all_syntax_matches(cmd, hw_all_clis)
        if rematched_cmds:
            matching_str += "Rematched (syntax): " + str(rematched_cmds) + '\n'
            rematched.append(cmd)
        else:
            matching_str += "No rematched (syntax): " + cmd + '\n'

    logger.info(f"Mismatched lines: {mismatched_lines}")
    TM_real = 1 - len(mismatched_lines) / lines_

    TM_plus = TM_real + len(rematched) / lines_

    logger.info(f"TM: {TM_real}, TM+: {TM_plus}")

    return TM_real, TM_plus, matching_str

def command_evaluation(translation, baseline, hierarchy_root):
    """
    Get Command Match
    """
    
    if hierarchy_root:
        baseline_config_root, _ = build_config_tree(baseline, hierarchy_root, 'huawei')

        # 首先获取config tree的所有command（每个节点加一个command字段，对于有hierarchy的，直接提取；对于没有hierarchy的，取前缀）；最后以打标记的方式进行最长前缀匹配
        baseline_config_root.reset_is_chosen()

        translation = purify_configuration(translation).split('\n')

        for line in translation:
            if not line.strip():
                continue
            _ = baseline_config_root.get_matched_cmd(line)  # 利用baseline_config_root记录匹配状态
        cnt_match, cnt_all = baseline_config_root.get_matched_cli_lines()
    else:
        print("No hierarchy tree, using command match")
        baseline = purify_configuration(baseline).split('\n')
        translation = purify_configuration(translation).split('\n')
        # 选择第一个单词作为Command的kwd，考察translation对baseline的kwd的覆盖率
        baseline_cmd = [[line.strip().split()[0], 0] for line in baseline if line.strip()]
        for line in translation:
            for cmd_score in baseline_cmd:
                if cmd_score[0] in line and cmd_score[1] == 0:
                    cmd_score[1] = 1
                    print(f"Matched: {cmd_score[0]}")
                    break
        cnt_all = len(baseline_cmd)
        cnt_match = sum([1 for cmd_score in baseline_cmd if cmd_score[1] == 1])
        print(baseline_cmd)
        print(f"cnt_all: {cnt_all}, cnt_match: {cnt_match}")
    return cnt_match / cnt_all



if __name__ == '__main__':

    hw_hierarchy_file_path = 'nassim-main/corpus/hierarchy/cmd_tree_hw_system_view.json'
    nokia_hierarchy_file_path = 'nassim-main/corpus/hierarchy/cmd_tree_nokia_opt.json'
    
    hw_hierarchy_root, hw_all_clis = build_hierarchy_tree(hw_hierarchy_file_path)
    nokia_hierarchy_root, nokia_all_clis = build_hierarchy_tree(nokia_hierarchy_file_path)

    argparser = argparse.ArgumentParser()  
    argparser.add_argument('-v', '--vendor', type=str, default='huawei', choices=['huawei', 'nokia', 'huawei-ce'], help='vendor type')
    argparser.add_argument('-s', '--dst_config_path', type=str, default=None)   # 待检查翻译结果配置文件夹
    argparser.add_argument('-b', '--baseline', type=str, default=None)          # 参考翻译结果配置文件夹
    argparser.add_argument('--not-use-tree', action='store_true')
    args = argparser.parse_args()

    if args.vendor == 'huawei-ce':
        with open("nassim-main/corpus/hw/hw_CE6800_V300R023C00/cmd_all_flat.json", 'r') as fp:
            hw_all_clis = ast.literal_eval(fp.read())
            hw_hierarchy_root = None

    print(f"all_clis: {len(hw_all_clis)}")


    res_path = os.path.join(args.dst_config_path, 'results')
    if not os.path.exists(res_path):
        os.makedirs(res_path)

    files = os.listdir(args.dst_config_path)
    filters = []
    files = [f for f in files if (f.endswith('.txt') or f.endswith('.cfg')) and f not in filters]

    EMs = []
    TMs = []
    TM_pluss = []   # TM_plus = Syntax match
    BLEU_1s = []
    BLEU_2s = []
    BLEU_3s = []
    BLEU_4s = []
    ROUGE_Lr = []
    ROUGE_Lf = []
    ROUGE_Lp = []
    CMD_scores = []
    lines =  []
    full_lines = []
    lines_with_manuals = []
    for fname in files:
        logger.info('#'*10 + f" Processing {fname} " + '#'*10)
        lines_with_manuals_ = 0
        with open(os.path.join(args.dst_config_path, fname), 'r', encoding='utf-8') as f:
            config = f.read()
            if not config.startswith('system-view') and args.vendor == 'huawei':
                config = 'system-view\n' + config
            full_lines.append(len(config.split('\n')))
            for line_manual in config.split('\n'):
                if '[' in line_manual:
                    lines_with_manuals_ += 1
            lines_with_manuals.append(lines_with_manuals_)
            translation = purify_configuration(config)
        EM, BLEU_1, BLEU_2, BLEU_3, BLEU_4, lines_ = 0, 0, 0, 0, 0, 0
        if args.baseline:
            with open(os.path.join(args.baseline, fname), 'r', encoding='utf-8') as f:
                baseline = f.read()
                baseline = purify_configuration(baseline)
            EM, BLEU_1, BLEU_2, BLEU_3, BLEU_4, ROUGE_1, ROUGE_2, ROUGE_L, lines_ = basic_evaluation(translation, baseline)
            EMs.append(EM)
            BLEU_1s.append(BLEU_1)
            BLEU_2s.append(BLEU_2)
            BLEU_3s.append(BLEU_3)
            BLEU_4s.append(BLEU_4)
            ROUGE_Lr.append(ROUGE_L['r'])
            ROUGE_Lf.append(ROUGE_L['f'])
            ROUGE_Lp.append(ROUGE_L['p'])
            lines.append(lines_)
            logger.info(f"EM: {EM}, BLEU-1: {BLEU_1}, BLEU-2: {BLEU_2}, BLEU-3: {BLEU_3}, BLEU-4: {BLEU_4}, ROUGE-L: {ROUGE_L}")
            # baseline_config_root, _ = build_config_tree(baseline, hw_hierarchy_root, args.vendor)
            # baseline_config_root.print()
            cmd_score = command_evaluation(translation, baseline, hw_hierarchy_root)
            CMD_scores.append(cmd_score)
            logger.info(f"Command Match: {cmd_score}")
        else:
            lines_ = len(translation.split('\n'))
            lines.append(lines_)

        if args.not_use_tree:
            SC = get_syntax_correctness(translation, hw_all_clis)
            TM_pluss.append(SC)
            logger.info(f"Syntax Correctness: {SC}")    
            matching_str = f"EM: {EM}, BLEU-1: {BLEU_1}, BLEU-2: {BLEU_2}, BLEU-3: {BLEU_3}, BLEU-4: {BLEU_4}, ROUGE-L(r,f,p): {ROUGE_Lr, ROUGE_Lf, ROUGE_Lp}, CMD: {cmd_score}\n"
            matching_str += f"Syntax Correctness: {SC}\n"
            with open(os.path.join(res_path, fname), 'w', encoding='utf-8') as f:
                f.write(matching_str)
            continue
        
        if args.vendor == 'huawei':
            config_root, config_unit = build_config_tree(translation, hw_hierarchy_root, args.vendor)
        elif args.vendor == 'nokia':
            config_root, config_unit = build_config_tree(translation, nokia_hierarchy_root, args.vendor)
        config_root.print()


        TM_real, TM_plus, matching_str = view_and_syntax_evaluation(config_root, hw_all_clis)

        TMs.append(TM_real)
        TM_pluss.append(TM_plus)

        matching_str += f"TM: {TM_real}, TM+: {TM_plus}\n"
        if args.baseline:
            matching_str += f"EM: {EM}, BLEU-1: {BLEU_1}, BLEU-2: {BLEU_2}, BLEU-3: {BLEU_3}, BLEU-4: {BLEU_4}, ROUGE-L: {ROUGE_L}"
        with open(os.path.join(res_path, fname), 'w', encoding='utf-8') as f:
            f.write(matching_str)



    total_lines = sum(lines)
    total_lines_full = sum(full_lines)
    # average scores
    TM = sum([TMs[i] * lines[i] for i in range(len(TMs))]) / total_lines
    TM_plus = sum([TM_pluss[i] * lines[i] for i in range(len(TM_pluss))]) / total_lines
    if args.baseline:
        # 使用lines作为权重，仅EM加权
        EM = sum([EMs[i] * lines[i] for i in range(len(EMs))]) / total_lines
        cmd_score = sum([CMD_scores[i] * lines[i] for i in range(len(CMD_scores))]) / total_lines
        BLEU_1 = np.mean(BLEU_1s)
        BLEU_2 = np.mean(BLEU_2s)
        BLEU_3 = np.mean(BLEU_3s)
        BLEU_4 = np.mean(BLEU_4s)
        ROUGE_Lr = np.mean(ROUGE_Lr)
        ROUGE_Lf = np.mean(ROUGE_Lf)
        ROUGE_Lp = np.mean(ROUGE_Lp)
        # BLEU_1 = sum([BLEU_1s[i] * lines[i] for i in range(len(BLEU_1s))]) / total_lines
        # BLEU_2 = sum([BLEU_2s[i] * lines[i] for i in range(len(BLEU_2s))]) / total_lines
        # BLEU_3 = sum([BLEU_3s[i] * lines[i] for i in range(len(BLEU_3s))]) / total_lines
        # BLEU_4 = sum([BLEU_4s[i] * lines[i] for i in range(len(BLEU_4s))]) / total_lines
        # ROUGE_Lr = sum([ROUGE_Lr[i] * lines[i] for i in range(len(ROUGE_Lr))]) / total_lines
        # ROUGE_Lf = sum([ROUGE_Lf[i] * lines[i] for i in range(len(ROUGE_Lf))]) / total_lines
        # ROUGE_Lp = sum([ROUGE_Lp[i] * lines[i] for i in range(len(ROUGE_Lp))]) / total_lines
        logger.info(f"Average EM: {EM}, TM: {TM}, TMp: {TM_plus}, BLEU-1: {BLEU_1}, BLEU-2: {BLEU_2}, BLEU-3: {BLEU_3}, BLEU-4: {BLEU_4}, ROUGE-L(r,f,p): {ROUGE_Lr, ROUGE_Lf, ROUGE_Lp}, CMD: {cmd_score}")
        logger.info(f"Total lines: {total_lines}, Full lines: {total_lines_full}, Lines with manuals: {sum(lines_with_manuals)}")
        # 输出挑选的结果：Total lines	TM	TM+	BLEU-2	ROUGE-L(r)	EM
        logger.info(f"Total lines: {total_lines}, TM: {TM}, TM+: {TM_plus}, BLEU-2: {BLEU_2}, ROUGE-L(r): {ROUGE_Lr}, EM: {EM}, CMD: {cmd_score}")

        # 输出最终结果到文件
        with open(os.path.join(res_path, 'final_result.txt'), 'w', encoding='utf-8') as f:
            f.write(f"Total lines: {total_lines}, TM: {TM}, TM+: {TM_plus}, BLEU-2: {BLEU_2}, ROUGE-L(r): {ROUGE_Lr}, EM: {EM}, CMD: {cmd_score}\n")

    else:
        logger.info(f"Average TM: {TM}, TM+: {TM_plus}")
        logger.info(f"Total lines: {total_lines}, Full lines: {total_lines_full}, Lines with manuals: {sum(lines_with_manuals)}")
        # 输出挑选的结果：Total lines	TM	TM+	BLEU-2	ROUGE-L(r)	EM
        logger.info(f"Total lines: {total_lines}, TM: {TM}, TM+: {TM_plus}")

        # 输出最终结果到文件
        with open(os.path.join(res_path, 'final_result.txt'), 'w', encoding='utf-8') as f:
            f.write(f"Total lines: {total_lines}, TM: {TM}, TM+: {TM_plus}\n")

# Usage Example
# python individual_critics.py -s Final_result/gpt-4o/full -b datasets/Nokia-hw-router/dataset-merge-revised/hw
