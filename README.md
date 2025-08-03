# INTA: 网络设备配置翻译多智能体框架

INTA 是一个强大的多智能体框架，专门用于实现不同网络设备之间的配置翻译，例如从诺基亚到华为路由器的CLI配置翻译。该框架结合了大型语言模型(LLM)、配置解析、语义理解和知识检索等技术，实现高效准确的网络配置迁移。

## 功能描述

### 输入输出
- **输入**: 源设备配置文件 (如Nokia SR OS路由器配置)
- **输出**: 目标设备配置文件 (如Huawei NE40E路由器配置)

### 核心功能
- 配置自动拆分与意图提取
- 跨厂商配置语义映射
- 基于知识检索的精确翻译
- 多轮验证与优化
- 支持多种网络设备类型

## 系统架构

INTA由以下核心智能体组成：

1. **ConfigDivideAgent**: 负责配置文件的结构化拆分和功能意图提取
2. **LLMTranslatorAgent**: 基于大型语言模型的配置翻译核心组件
3. **ContentTraverseAgent**: 遍历和分析配置内容
4. **CriticAgent**: 对翻译结果进行评估和优化
5. **EmbeddingModel**: 用于语义相似度计算和知识检索

## 安装要求

### 依赖项

已测试python版本：3.9.20

其他主要依赖项：

```
openai==1.39.0
nltk==3.9.1
rouge-score==0.1.2
rank-bm25==0.2.2
markdownify==0.14.1
sentence-transformers==3.3.1
flagembedding==1.3.3
jsonschema==4.23.0
numpy==1.26.4
torch==2.0.1
```

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本命令格式
```bash
python run.py -s <源配置目录> [其他参数]
```

### 主要命令参数说明
- `-s`, `--source`: 源配置文件目录
- `--senario`: 运行场景 (configtrans, minibenchmark, human-eval, all, 8refs)，仅作为标注
- `--base-model`: 基础语言模型 (qwen-max-latest, gpt-4o, deepseek-v3等)
- `--method`: 翻译方法 (INTA, LLM)
- `--emb-model`: 嵌入模型 (bge-m3等)
- `--use-cmd-manuals`: 是否使用命令手册
- `--use-view`: 是否使用视图信息
- `--use-mix`: 是否使用混合检索策略
- `--selector-config`: 配置选择器 (llm, bm25)
- `--selector-cmd`: 命令选择器 (llm, bm25)

### 示例

#### 基于Qwen-max模型的测试
```bash
python run.py \
    -s datasets/test/nokia \
    --senario configtrans \
    --base-model qwen-max-latest \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_test_qwen.log
```

## 项目结构
```
INTA-project/
├── Readme.md                   # 项目说明文档
├── Result/                     # 翻译结果目录
├── collect_corpus.py           # 语料收集脚本
├── config_parser.py            # 配置解析器
├── datasets/                   # 数据集目录
├── generate_embeddings.py      # 嵌入生成脚本
├── individual_critics.py       # 独立评估器
├── logs/                       # 日志目录
├── multi_agent.py              # 多智能体实现
├── run.new.sh                  # 运行脚本示例
├── run.py                      # 主运行脚本
└── utils.py                    # 工具函数
```

## 支持的设备类型
- Huawei NE40E router
- Nokia SR OS router
- Huawei CE6800 switch
- Cisco Catalyst 6800 switch


## 注意事项
1. 运行前请确保在环境变量中设置了正确的API密钥(如OpenAI, DashScope等)
2. Embedding模型需要本地部署
3. 大型配置文件翻译可能需要较长时间
