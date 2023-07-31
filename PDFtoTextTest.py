import PyPDF2
import os

def convert_pdf_to_text(pdf_file_path, output_text_file):
    try:
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            all_text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                all_text += page.extract_text()

            all_text = all_text.replace('\n', ' ')

            downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
            
            output_file_path = os.path.join(downloads_folder, output_text_file)
            with open(output_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(all_text)

            print("Text extraction and save successful!")
    except Exception as e:
        print("Error during text extraction:", str(e))

if __name__ == "__main__":
    pdf_file_path = '/Users/rdas/Downloads/pdf_file.pdf'
    output_text_file = 'output_text.txt'
    convert_pdf_to_text(pdf_file_path, output_text_file)
