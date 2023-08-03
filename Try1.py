import re
import os

def extract_sections(text_content):
    section_pattern = r"Code Title Units([\s\S]*?)(?=\n\n[A-Z&]+\s\d+\s[A-Z\s\d]+|$)"

    sections = re.findall(section_pattern, text_content, re.DOTALL)

    extracted_sections = []

    for section in sections:
        course_codes = re.findall(r"\b[A-Z&]+\s\d+\s[A-Z\d]+\b", section)
        extracted_section = "\n".join(course_codes) + "\n"

        extracted_sections.append(extracted_section)

    all_sections = '\n'.join(extracted_sections)

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file_path = os.path.join(downloads_folder, "extracted_sections.txt")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(all_sections)

    print(f"All extracted sections saved to '{output_file_path}'.")

if __name__ == "__main__":
    text_file_path = '/Users/rdas/Downloads/output_text.txt'

    with open(text_file_path, 'r', encoding='utf-8') as text_file:
        text_content = text_file.read()

    extract_sections(text_content)
