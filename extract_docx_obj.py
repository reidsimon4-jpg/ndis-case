import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def extract_docx_text(docx_path, output_path):
    try:
        if not os.path.exists(docx_path):
            print(f"Error: File not found: {docx_path}")
            sys.exit(1)

        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read('word/document.xml')
        
        tree = ET.fromstring(xml_content)
        text = []
        # XML namespace for Word
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        for p in tree.findall('.//w:p', ns):
            p_text = ''
            for t in p.findall('.//w:t', ns):
                if t.text:
                    p_text += t.text
            text.append(p_text)
            
        full_text = '\n'.join(text)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"Extracted {len(full_text)} characters to {output_path}")
    except Exception as e:
        print(f"Error extracting docx: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_docx_obj.py <input> <output>")
        sys.exit(1)
    extract_docx_text(sys.argv[1], sys.argv[2])
