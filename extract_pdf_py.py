import fitz  # PyMuPDF
import sys

def extract_pdf_text(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    page_count = doc.page_count
    all_text = ""
    for page_num in range(page_count):
        page = doc[page_num]
        text = page.get_text()
        all_text += f"\n\n===== PAGE {page_num + 1} =====\n\n"
        all_text += text
    doc.close()
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(all_text)
    
    print(f"Extracted {len(all_text)} chars from {page_count} pages to {output_path}")

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    output_path = sys.argv[2]
    extract_pdf_text(pdf_path, output_path)
