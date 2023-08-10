PRE_SEQ_LEN=96

CUDA_VISIBLE_DEVICES=0,1,2 python3 web_demo.py \
    --model_name_or_path /root/autodl-tmp/chatglm/ChatGLM2-6B/ChatGLM2-model/chatglm2-6b \
    --ptuning_checkpoint /root/autodl-tmp/chatglm/ChatGLM2-6B/ptuning/output/chatglm-6b-pt-96-2e-2/checkpoint-2000 \
    --pre_seq_len $PRE_SEQ_LEN

