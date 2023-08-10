#!/bin/bash

PRE_SEQ_LEN=96
LR=1e-1

CUDA_VISIBLE_DEVICES=0,1,2 python3 main.py \
    --do_train \
    --train_file cleaned_2_data.json \
    --validation_file dev.json \
    --prompt_column input \
    --response_column output \
    --overwrite_cache \
    --model_name_or_path /root/autodl-tmp/chatglm/ChatGLM2-6B/ChatGLM2-model/chatglm2-6b \
    --ptuning_checkpoint /root/autodl-tmp/chatglm/ChatGLM2-6B/ptuning/output/chatglm-6b-pt-96-2e-2/checkpoint-2000 \
    --output_dir ./output/chatglm-6b-pt-$PRE_SEQ_LEN-$LR \
    --overwrite_output_dir \
    --max_source_length 256 \
    --max_target_length 256 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --predict_with_generate \
    --max_steps 2000 \
    --logging_steps 10 \
    --save_steps 200 \
    --learning_rate $LR \
    --pre_seq_len $PRE_SEQ_LEN \
    --quantization_bit 4