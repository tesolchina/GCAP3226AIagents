#!/usr/bin/env python3
"""
Convert VTT files to Markdown format
Cleans up timestamps and speaker labels while preserving content
"""
# ORGANIZATION NOTE
# This script has been organized and moved to:
# AItools/01_Data_Processing_Analysis/Document_Analysis/
# Original location: /Users/simonwang/Documents/Usage/ObSync/Vault4sync/GCAP3226/00_Course_Materials/convert_vtt_to_md.py
# Moved on: 2025-09-27 22:21:56
#


import os
import re
from pathlib import Path

def clean_vtt_content(vtt_content):
    """Clean VTT content and convert to markdown format"""
    lines = vtt_content.split('\n')
    markdown_lines = []
    
    # Skip WEBVTT header
    if lines and lines[0].strip() == 'WEBVTT':
        lines = lines[1:]
    
    current_speaker = None
    current_text = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Skip timestamp lines (format: 00:00:00.000 --> 00:00:00.000)
        if re.match(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', line):
            continue
            
        # Skip cue numbers
        if line.isdigit():
            continue
            
        # Check if line contains speaker name (format: "Speaker Name: text")
        if ':' in line and not line.startswith('http'):
            parts = line.split(':', 1)
            if len(parts) == 2:
                speaker = parts[0].strip()
                text = parts[1].strip()
                
                # If speaker changed, add previous content and start new
                if current_speaker != speaker:
                    if current_speaker and current_text:
                        markdown_lines.append(f"**{current_speaker}:** {' '.join(current_text)}")
                        markdown_lines.append("")
                    current_speaker = speaker
                    current_text = [text] if text else []
                else:
                    if text:
                        current_text.append(text)
            else:
                # No speaker, just text - append to current speaker
                if current_speaker:
                    current_text.append(line)
        else:
            # No speaker identified, append to current speaker
            if current_speaker:
                current_text.append(line)
    
    # Add final speaker content
    if current_speaker and current_text:
        markdown_lines.append(f"**{current_speaker}:** {' '.join(current_text)}")
    
    return '\n'.join(markdown_lines)

def convert_vtt_to_markdown(vtt_file_path, output_file_path):
    """Convert a single VTT file to Markdown"""
    try:
        with open(vtt_file_path, 'r', encoding='utf-8') as f:
            vtt_content = f.read()
        
        markdown_content = clean_vtt_content(vtt_content)
        
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✓ Converted {vtt_file_path.name} to {output_file_path.name}")
        return True
        
    except Exception as e:
        print(f"✗ Error converting {vtt_file_path.name}: {e}")
        return False

def main():
    """Main function to process all VTT files in the directory"""
    current_dir = Path(__file__).parent
    
    # Find all VTT files
    vtt_files = list(current_dir.glob("*.vtt"))
    
    if not vtt_files:
        print("No VTT files found in the current directory")
        return
    
    print(f"Found {len(vtt_files)} VTT files to convert:")
    for vtt_file in vtt_files:
        print(f"  - {vtt_file.name}")
    
    print("\nConverting files...")
    
    success_count = 0
    for vtt_file in vtt_files:
        # Create output filename by replacing .vtt with .md
        output_file = vtt_file.with_suffix('.md')
        
        if convert_vtt_to_markdown(vtt_file, output_file):
            success_count += 1
    
    print(f"\nConversion complete! {success_count}/{len(vtt_files)} files converted successfully.")

if __name__ == "__main__":
    main()
