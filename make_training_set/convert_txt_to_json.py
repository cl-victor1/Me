# 以下代码负责提取聊天记录中“我”作为回答者的对话（一组两句），并将这些对话存进json文件。

import os
import json

def extract_conversations(input_file):
    conversations = []
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        prev_line = None
        for line in lines:
            current_line = line.strip()
            try:
                if current_line.startswith("你自己的昵称"):
                    if "):" in prev_line and not prev_line.startswith("你自己的昵称"):
                        conversation_pair = {
                            "input": prev_line.split("):")[1],
                            "output": current_line.split("):")[1]
                        }
                        conversations.append(conversation_pair)
            except IndexError:
                print("can't parse", current_line)

            prev_line = current_line

    return conversations

def main():
    input_directory = "txt_files"
    output_file = "output2.json"

    all_conversations = []

    for filename in os.listdir(input_directory):
        input_file = os.path.join(input_directory, filename)
        conversations = extract_conversations(input_file)
        all_conversations.extend(conversations)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(all_conversations, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
