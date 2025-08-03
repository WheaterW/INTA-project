# test for qwen
nohup python run.py \
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
    > run_test_qwen.log \
    2>&1 &




# Minibenchmark Test of GPT-4o
nohup python run.py \
    -s datasets/Nokia-hw-router/Nokia2Huawei-minibenchmark/Nokia-with-manual-config-with-division-4o \
    --src-config-path-cmd datasets/Nokia-hw-router/Nokia2Huawei-minibenchmark/Nokia-with-manual-cmd \
    --senario minibenchmark \
    --base-model gpt-4o \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --use-ext-config-division \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_minibenchmark_gpt-4o.log \
    2>&1 &

# Human-eval Test of GPT-4o
nohup python run.py \
    -s datasets/Nokia-hw-router/human_eval/nokia \
    --senario human-eval \
    --base-model gpt-4o \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_human-eval_gpt-4o.log \
    2>&1 &

# GPT-4o
nohup python run.py \
    -s datasets/Nokia-hw-router/dataset-merge-revised/nokia \
    --senario all \
    --base-model gpt-4o \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_gpt-4o.log \
    2>&1 &

# Qwen
# all for qwen-pure
nohup python run.py \
    -s datasets/Nokia-hw-router/dataset-merge-revised/nokia \
    --senario all \
    --base-model qwen-max-latest \
    --method LLM \
    --emb-model bge-m3 \
    --use-view \
    --use-mix \
    > run_e2e_all_qwen_pure.log \
    2>&1 &

# all for qwen-rag
nohup python run.py \
    -s datasets/Nokia-hw-router/dataset-merge-revised/nokia \
    --senario all \
    --base-model qwen-max-latest \
    --method INTA \
    --emb-model bge-m3 \
    --no-sLoop \
    --no-lLoop \
    --use-view \
    --use-mix \
    > run_e2e_all_qwen_rag.log \
    2>&1 &

# 8refs for qwen
nohup python run.py \
    -s datasets/Nokia-hw-router/8refs_all/nokia \
    --senario 8refs \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_8refs_qwen.log \
    2>&1 &

# configtrans for qwen
nohup python run.py \
    -s datasets/Nokia-hw-router/configtrans_all/nokia \
    --senario configtrans \
    --base-model qwen-max-latest \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_configtrans_qwen.log \
    2>&1 &


# generation for qwen
nohup python run.py \
    -s datasets/Nokia-hw-router/generation_all/nokia \
    --senario generation \
    --base-model qwen-max-latest \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_generation_qwen.log \
    2>&1 &

# deepseek-chat
# all for deepseek-pure
nohup python run.py \
    -s datasets/Nokia-hw-router/dataset-merge-revised/nokia\
    --senario all \
    --base-model deepseek-chat \
    --method LLM \
    --emb-model bge-m3 \
    --use-view \
    --use-mix \
    > run_e2e_all_deepseek_pure.log \
    2>&1 &

# all for deepseek-rag
nohup python run.py \
    -s datasets/Nokia-hw-router/dataset-merge-revised/nokia \
    --senario all \
    --base-model deepseek-chat \
    --method INTA \
    --emb-model bge-m3 \
    --no-sLoop \
    --no-lLoop \
    --use-view \
    --use-mix \
    > run_e2e_all_deepseek_rag.log \
    2>&1 &

# 8refs for deepseek-chat
nohup python run.py \
    -s datasets/Nokia-hw-router/8refs_all/nokia \
    --senario 8refs \
    --base-model deepseek-chat \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_8refs_deepseek-chat.log \
    2>&1 &

# configtrans for deepseek-chat
nohup python run.py \
    -s datasets/Nokia-hw-router/configtrans_all/nokia \
    --senario configtrans \
    --base-model deepseek-chat \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-view \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_configtrans_deepseek-chat.log \
    2>&1 &

# generation for deepseek-chat
nohup python run.py \
    -s datasets/Nokia-hw-router/generation_all/nokia \
    --senario generation \
    --base-model deepseek-chat \
    --method INTA \
    --emb-model bge-m3 \
    --use-view \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    --use-cmd-manuals \
    > run_e2e_generation_deepseek-chat.log \
    2>&1 &

# all for deepseek-pure
nohup python run.py \
    -s datasets/Nokia-hw-router/dataset-merge-revised/nokia\
    --senario all \
    --base-model deepseek-chat \
    --method LLM \
    --emb-model bge-m3 \
    --use-view \
    --use-mix \
    > run_e2e_configtrans_deepseek-chat_pure.log \
    2>&1 &

# cisco for deepseek-chat
nohup python run.py \
    -s datasets/Cisco-hw-switch/cisco-new \
    --senario cisco \
    --src-vendor cisco-catalyst6800 \
    --tgt-vendor huawei-ce6800 \
    --base-model deepseek-chat \
    --method INTA \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_cisco_deepseek-chat.log \
    2>&1 &


nohup python run.py \
    -s datasets/Cisco-hw-switch/cisco-new \
    --senario cisco \
    --src-vendor cisco-catalyst6800 \
    --tgt-vendor huawei-ce6800 \
    --base-model deepseek-chat \
    --method LLM \
    --emb-model bge-m3 \
    --use-cmd-manuals \
    --use-mix \
    --selector-config llm \
    --selector-cmd bm25 \
    > run_e2e_cisco_deepseek-chat_pure.log \
    2>&1 &