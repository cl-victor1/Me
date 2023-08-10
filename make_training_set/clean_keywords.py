import json
import re
import torch

def process_json_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    processed_data = []
    for obj in data:        
        marker = True
        for value in obj.values():
            if value == "" or "密码" in value or "xxx" in value or "身份证" in value:
                marker = False
                break
        if marker:
            processed_data.append(obj)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(processed_data, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    input_file = "cleaned_1_data.json"  # Replace with the path to your input JSON file
    output_file = "cleaned_2_data.json"  # Replace with the desired output file path

    process_json_file(input_file, output_file)
