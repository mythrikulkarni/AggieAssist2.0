import re

def extract_text_between_keywords(file_path, start_keyword, end_keyword):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = re.compile(f"{re.escape(start_keyword)}(.*?){re.escape(end_keyword)}", re.DOTALL)
    extracted_texts = re.findall(pattern, content)

    return extracted_texts

# Usage example
file_path = 'output_text.txt'
start_keyword = 'Code Title Units'
end_keyword = 'Total Units'

extracted_texts = extract_text_between_keywords(file_path, start_keyword, end_keyword)

for i, text in enumerate(extracted_texts, start=1):
    print(f"Extraction {i}:\n{text.strip()}\n")
