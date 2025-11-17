#!/usr/bin/env python3
"""
Convert VTT files to Markdown files, removing timestamps and formatting.
"""
import os
import re
from pathlib import Path

def convert_vtt_to_md(vtt_file_path, output_dir=None):
    """
    Convert a VTT file to Markdown format, removing timestamps.
    
    Args:
        vtt_file_path: Path to the input VTT file
        output_dir: Directory to save the output MD file (default: same as input)
    """
    vtt_path = Path(vtt_file_path)
    
    if output_dir:
        output_path = Path(output_dir) / f"{vtt_path.stem}.md"
    else:
        output_path = vtt_path.parent / f"{vtt_path.stem}.md"
    
    with open(vtt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines
    lines = content.split('\n')
    
    # Process lines to extract text content
    md_lines = []
    skip_next = False
    
    for i, line in enumerate(lines):
        # Skip WEBVTT header
        if line.strip() == 'WEBVTT':
            continue
        
        # Skip empty lines after WEBVTT
        if i < 2 and not line.strip():
            continue
        
        # Skip numbered segment markers (standalone numbers)
        if line.strip().isdigit():
            skip_next = True  # Next line will be timestamp
            continue
        
        # Skip timestamp lines (format: 00:00:01.340 --> 00:00:04.630)
        if re.match(r'\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}', line.strip()):
            skip_next = False
            continue
        
        # Skip if we're in skip mode
        if skip_next:
            skip_next = False
            continue
        
        # Add text content
        if line.strip():
            md_lines.append(line.strip())
        elif md_lines and md_lines[-1]:  # Add empty line only if previous line wasn't empty
            md_lines.append('')
    
    # Join lines and clean up multiple empty lines
    md_content = '\n'.join(md_lines)
    # Replace multiple empty lines with double newline
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    md_content = md_content.strip()
    
    # Write to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Converted: {vtt_path.name} -> {output_path.name}")
    return output_path

def main():
    # Directory containing VTT files
    vtt_dir = Path("/Users/simonwang/Documents/Usage/GCAP3226/Course_Docs/Presentation1")
    
    # Find all VTT files
    vtt_files = sorted(vtt_dir.glob("*.vtt"))
    
    if not vtt_files:
        print(f"No VTT files found in {vtt_dir}")
        return
    
    print(f"Found {len(vtt_files)} VTT files to convert...")
    
    # Convert each file
    converted_files = []
    for vtt_file in vtt_files:
        md_file = convert_vtt_to_md(vtt_file)
        converted_files.append(md_file)
    
    print(f"\nSuccessfully converted {len(converted_files)} files:")
    for md_file in converted_files:
        print(f"  - {md_file.name}")

if __name__ == "__main__":
    main()


