#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts PDF files to markdown format for literature analysis
Author: Team 2 Bus Route Coordination
Date: [CURRENT DATE]
"""

import PyPDF2
import pdfplumber
import os
import sys
from pathlib import Path

def convert_pdf_to_markdown(pdf_path, output_path=None):
    """
    Convert PDF to markdown format
    """
    try:
        # Check if PDF file exists
        if not os.path.exists(pdf_path):
            print(f"Error: PDF file not found at {pdf_path}")
            return False
        
        # Set output path if not provided
        if output_path is None:
            pdf_name = Path(pdf_path).stem
            output_path = f"{pdf_name}.md"
        
        print(f"Converting PDF: {pdf_path}")
        print(f"Output file: {output_path}")
        
        # Extract text using pdfplumber (better for complex layouts)
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            
            for page_num, page in enumerate(pdf.pages, 1):
                print(f"Processing page {page_num}...")
                
                # Extract text from page
                page_text = page.extract_text()
                
                if page_text:
                    # Add page header
                    full_text += f"\n## Page {page_num}\n\n"
                    full_text += page_text
                    full_text += "\n\n---\n\n"
        
        # Write to markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Literature Analysis: {Path(pdf_path).stem}\n\n")
            f.write(f"**Source:** {pdf_path}\n")
            f.write(f"**Converted:** {os.path.basename(output_path)}\n\n")
            f.write("---\n\n")
            f.write(full_text)
        
        print(f"Successfully converted PDF to markdown: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error converting PDF: {str(e)}")
        return False

def extract_key_sections(text):
    """
    Extract key sections from the converted text
    """
    sections = {
        "abstract": "",
        "introduction": "",
        "methodology": "",
        "results": "",
        "conclusion": "",
        "references": ""
    }
    
    # Convert to lowercase for searching
    text_lower = text.lower()
    
    # Extract abstract
    if "abstract" in text_lower:
        abstract_start = text_lower.find("abstract")
        if abstract_start != -1:
            # Find next section
            next_section = text_lower.find("introduction", abstract_start)
            if next_section == -1:
                next_section = text_lower.find("1.", abstract_start)
            if next_section == -1:
                next_section = abstract_start + 2000  # Fallback
            
            sections["abstract"] = text[abstract_start:next_section].strip()
    
    # Extract introduction
    if "introduction" in text_lower:
        intro_start = text_lower.find("introduction")
        if intro_start != -1:
            # Find next section
            next_section = text_lower.find("methodology", intro_start)
            if next_section == -1:
                next_section = text_lower.find("2.", intro_start)
            if next_section == -1:
                next_section = intro_start + 3000  # Fallback
            
            sections["introduction"] = text[intro_start:next_section].strip()
    
    # Extract methodology
    if "methodology" in text_lower or "method" in text_lower:
        method_start = text_lower.find("methodology")
        if method_start == -1:
            method_start = text_lower.find("method")
        
        if method_start != -1:
            # Find next section
            next_section = text_lower.find("results", method_start)
            if next_section == -1:
                next_section = text_lower.find("3.", method_start)
            if next_section == -1:
                next_section = method_start + 3000  # Fallback
            
            sections["methodology"] = text[method_start:next_section].strip()
    
    # Extract results
    if "results" in text_lower:
        results_start = text_lower.find("results")
        if results_start != -1:
            # Find next section
            next_section = text_lower.find("conclusion", results_start)
            if next_section == -1:
                next_section = text_lower.find("4.", results_start)
            if next_section == -1:
                next_section = results_start + 3000  # Fallback
            
            sections["results"] = text[results_start:next_section].strip()
    
    # Extract conclusion
    if "conclusion" in text_lower:
        conclusion_start = text_lower.find("conclusion")
        if conclusion_start != -1:
            # Find next section
            next_section = text_lower.find("references", conclusion_start)
            if next_section == -1:
                next_section = text_lower.find("5.", conclusion_start)
            if next_section == -1:
                next_section = conclusion_start + 2000  # Fallback
            
            sections["conclusion"] = text[conclusion_start:next_section].strip()
    
    return sections

def create_structured_analysis(pdf_path, output_path):
    """
    Create structured analysis of the PDF content
    """
    try:
        # Convert PDF to markdown
        markdown_path = f"{Path(pdf_path).stem}_converted.md"
        if not convert_pdf_to_markdown(pdf_path, markdown_path):
            return False
        
        # Read the converted text
        with open(markdown_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Extract key sections
        sections = extract_key_sections(text)
        
        # Create structured analysis
        analysis_content = f"""# Literature Analysis: {Path(pdf_path).stem}

## Source Information
- **PDF File:** {pdf_path}
- **Converted:** {markdown_path}
- **Analysis Date:** {os.path.basename(output_path)}

## Key Sections Analysis

### Abstract
{sections['abstract'] if sections['abstract'] else 'Abstract not found or extracted'}

### Introduction
{sections['introduction'] if sections['introduction'] else 'Introduction not found or extracted'}

### Methodology
{sections['methodology'] if sections['methodology'] else 'Methodology not found or extracted'}

### Results
{sections['results'] if sections['results'] else 'Results not found or extracted'}

### Conclusion
{sections['conclusion'] if sections['conclusion'] else 'Conclusion not found or extracted'}

## Relevance to Bus Route Coordination Research

### Key Insights
- [ ] **Transportation Planning:** [Key insights from the paper]
- [ ] **Data Analysis:** [Relevant data analysis methods]
- [ ] **Policy Implications:** [Policy-related findings]
- [ ] **Methodology:** [Relevant research methods]

### Research Questions Addressed
- [ ] **Decision-Making:** How does this paper inform understanding of transportation decision-making?
- [ ] **Data Utilization:** What insights about data use in transportation planning?
- [ ] **Policy Process:** How does this inform understanding of policy processes?
- [ ] **Coordination:** What insights about coordination in transportation systems?

### Methodology Relevance
- [ ] **Data Collection:** Relevant data collection methods
- [ ] **Analysis Techniques:** Applicable analysis techniques
- [ ] **Evaluation Methods:** Relevant evaluation approaches
- [ ] **Policy Assessment:** Policy assessment methods

### Implications for Team 2 Research
- [ ] **Transportation Decision-Making:** How this informs understanding of TD decisions
- [ ] **Data-Driven Approaches:** Relevance to data-driven decision-making
- [ ] **Coordination Analysis:** Insights for route coordination analysis
- [ ] **Policy Recommendations:** Implications for policy recommendations

## Notes for Report Writing
- [ ] **Literature Review:** Key points to include in literature review
- [ ] **Methodology:** Relevant methods to reference
- [ ] **Analysis:** Relevant analysis approaches
- [ ] **Policy Implications:** Key policy insights

---
*This analysis was generated automatically. Please review and refine the content for accuracy and relevance.*
"""
        
        # Write structured analysis
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(analysis_content)
        
        print(f"Structured analysis created: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error creating structured analysis: {str(e)}")
        return False

def main():
    """
    Main function to convert PDF and create analysis
    """
    # PDF file path
    pdf_path = "/Users/simonwang/Documents/Usage/GCAP3226/GCAP3226AIagents/Team2_BusRouteCoordination/Literature/1-s2.0-S2352146517304842-main.pdf"
    
    # Output paths
    markdown_path = "/Users/simonwang/Documents/Usage/GCAP3226/GCAP3226AIagents/Team2_BusRouteCoordination/Literature/1-s2.0-S2352146517304842-main_converted.md"
    analysis_path = "/Users/simonwang/Documents/Usage/GCAP3226/GCAP3226AIagents/Team2_BusRouteCoordination/Literature/1-s2.0-S2352146517304842-main_analysis.md"
    
    print("PDF to Markdown Converter")
    print("=" * 50)
    
    # Check if PDF exists
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        print("Please check the file path and try again.")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(markdown_path), exist_ok=True)
    
    # Convert PDF to markdown
    print("Step 1: Converting PDF to markdown...")
    if convert_pdf_to_markdown(pdf_path, markdown_path):
        print("✓ PDF converted successfully")
    else:
        print("✗ PDF conversion failed")
        return
    
    # Create structured analysis
    print("\nStep 2: Creating structured analysis...")
    if create_structured_analysis(pdf_path, analysis_path):
        print("✓ Structured analysis created successfully")
    else:
        print("✗ Structured analysis creation failed")
        return
    
    print("\n" + "=" * 50)
    print("Conversion completed successfully!")
    print(f"Markdown file: {markdown_path}")
    print(f"Analysis file: {analysis_path}")

if __name__ == "__main__":
    main()
