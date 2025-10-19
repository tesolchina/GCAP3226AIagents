#!/usr/bin/env python3
"""
PDF to Markdown Converter
Convert the bus ETA API specifications PDF to markdown format
"""

import sys
import os

# Try to import PyPDF2 or pdfplumber
try:
    import PyPDF2
    PDF_LIBRARY = "PyPDF2"
except ImportError:
    try:
        import pdfplumber
        PDF_LIBRARY = "pdfplumber"
    except ImportError:
        print("❌ No PDF library found. Installing PyPDF2...")
        os.system("pip install PyPDF2")
        try:
            import PyPDF2
            PDF_LIBRARY = "PyPDF2"
        except ImportError:
            print("❌ Failed to install PyPDF2. Please install manually: pip install PyPDF2")
            sys.exit(1)

def extract_text_pypdf2(pdf_path):
    """Extract text using PyPDF2"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"❌ Error extracting text with PyPDF2: {e}")
    return text

def extract_text_pdfplumber(pdf_path):
    """Extract text using pdfplumber"""
    text = ""
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"❌ Error extracting text with pdfplumber: {e}")
    return text

def convert_to_markdown(text):
    """Convert extracted text to markdown format"""
    lines = text.split('\n')
    markdown_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Detect headers (lines that are all caps or start with numbers)
        if line.isupper() and len(line) > 3:
            markdown_lines.append(f"## {line}")
        elif line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            markdown_lines.append(f"### {line}")
        elif line.startswith(('•', '-', '*')):
            markdown_lines.append(f"- {line[1:].strip()}")
        else:
            markdown_lines.append(line)
    
    return '\n'.join(markdown_lines)

def main():
    pdf_path = "/Users/simonwang/Documents/Usage/GCAP3226/Team2_BusRouteCoordination/02_Data_Collection/APIdata/documentation/bus_eta_api_specifications.pdf"
    output_path = "/Users/simonwang/Documents/Usage/GCAP3226/Team2_BusRouteCoordination/02_Data_Collection/APIdata/similar_cases_analysis/bus_eta_api_specifications.md"
    
    print("📄 PDF to Markdown Converter")
    print("=" * 50)
    print(f"📁 Input: {pdf_path}")
    print(f"📁 Output: {output_path}")
    print(f"📚 Using library: {PDF_LIBRARY}")
    
    if not os.path.exists(pdf_path):
        print(f"❌ PDF file not found: {pdf_path}")
        return
    
    # Extract text
    print("🔍 Extracting text from PDF...")
    if PDF_LIBRARY == "PyPDF2":
        text = extract_text_pypdf2(pdf_path)
    else:
        text = extract_text_pdfplumber(pdf_path)
    
    if not text.strip():
        print("❌ No text extracted from PDF")
        return
    
    print(f"✅ Extracted {len(text)} characters")
    
    # Convert to markdown
    print("📝 Converting to markdown...")
    markdown_text = convert_to_markdown(text)
    
    # Save to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Bus ETA API Specifications\n\n")
        f.write("**Source:** bus_eta_api_specifications.pdf\n")
        f.write("**Converted:** " + str(datetime.now()) + "\n\n")
        f.write("---\n\n")
        f.write(markdown_text)
    
    print(f"✅ Markdown file created: {output_path}")
    print(f"📊 File size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    from datetime import datetime
    main()
