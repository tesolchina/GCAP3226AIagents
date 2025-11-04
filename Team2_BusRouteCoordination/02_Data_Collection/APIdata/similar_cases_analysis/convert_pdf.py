#!/usr/bin/env python3
"""
Simple PDF to Markdown Converter
"""

import os
import sys

def install_pdf_library():
    """Install required PDF library"""
    print("📦 Installing PyPDF2...")
    os.system("pip install PyPDF2")
    print("✅ PyPDF2 installed")

def convert_pdf_to_markdown():
    """Convert PDF to markdown"""
    try:
        import PyPDF2
        print("✅ PyPDF2 available")
    except ImportError:
        print("❌ PyPDF2 not available, installing...")
        install_pdf_library()
        try:
            import PyPDF2
            print("✅ PyPDF2 installed successfully")
        except ImportError:
            print("❌ Failed to install PyPDF2")
            return False
    
    # PDF file path
    pdf_path = "/Users/simonwang/Documents/Usage/GCAP3226/Team2_BusRouteCoordination/02_Data_Collection/APIdata/documentation/bus_eta_api_specifications.pdf"
    output_path = "/Users/simonwang/Documents/Usage/GCAP3226/Team2_BusRouteCoordination/02_Data_Collection/APIdata/similar_cases_analysis/bus_eta_api_specifications.md"
    
    print(f"📄 Converting PDF: {pdf_path}")
    print(f"📄 Output: {output_path}")
    
    if not os.path.exists(pdf_path):
        print(f"❌ PDF file not found: {pdf_path}")
        return False
    
    try:
        # Extract text from PDF
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            print(f"📊 PDF has {len(pdf_reader.pages)} pages")
            
            for page_num in range(len(pdf_reader.pages)):
                print(f"📄 Processing page {page_num + 1}...")
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                text += page_text + "\n\n"
        
        print(f"✅ Extracted {len(text)} characters")
        
        # Clean up text
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line and len(line) > 2:  # Skip empty or very short lines
                cleaned_lines.append(line)
        
        # Convert to markdown
        markdown_content = "# Bus ETA API Specifications\n\n"
        markdown_content += "**Source:** bus_eta_api_specifications.pdf\n"
        markdown_content += "**Converted:** 2025-10-19\n\n"
        markdown_content += "---\n\n"
        
        for line in cleaned_lines:
            # Detect headers (all caps or start with numbers)
            if line.isupper() and len(line) > 5:
                markdown_content += f"## {line}\n\n"
            elif line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                markdown_content += f"### {line}\n\n"
            elif line.startswith(('•', '-', '*')):
                markdown_content += f"- {line[1:].strip()}\n"
            else:
                markdown_content += f"{line}\n\n"
        
        # Save to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Markdown file created: {output_path}")
        print(f"📊 File size: {os.path.getsize(output_path)} bytes")
        
        return True
        
    except Exception as e:
        print(f"❌ Error converting PDF: {str(e)}")
        return False

if __name__ == "__main__":
    print("📄 PDF to Markdown Converter")
    print("=" * 50)
    
    success = convert_pdf_to_markdown()
    
    if success:
        print("\n✅ PDF conversion completed successfully!")
    else:
        print("\n❌ PDF conversion failed!")
