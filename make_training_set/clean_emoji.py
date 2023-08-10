import json
import re

def remove_square_bracket_content(text):
    # Define a regular expression pattern to match content embraced by square brackets
    pattern = r"\[.*?\]"
    # Use re.sub() to replace the matched pattern with an empty string
    return re.sub(pattern, '', text)

def process_json_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Apply the remove_square_bracket_content function to each JSON object in the list
    processed_data = []
    for obj in data:
        processed_obj = {key: remove_square_bracket_content(value) for key, value in obj.items()}
        processed_data.append(processed_obj)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(processed_data, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    input_file = "output.json"  # Replace with the path to your input JSON file
    output_file = "cleaned_data.json"  # Replace with the desired output file path

    process_json_file(input_file, output_file)
