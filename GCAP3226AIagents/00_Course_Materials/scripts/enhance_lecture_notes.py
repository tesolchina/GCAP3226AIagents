#!/usr/bin/env python3
"""
Enhance lecture notes with AI processing
Uses inexpensive models to add structure, summaries, and better formatting
"""
# ORGANIZATION NOTE
# This script has been organized and moved to:
# AItools/05_Utility_Scripts/Automation/
# Original location: /Users/simonwang/Documents/Usage/ObSync/Vault4sync/GCAP3226/00_Course_Materials/enhance_lecture_notes.py
# Moved on: 2025-09-27 22:21:56
#


import os
import json
import time
from pathlib import Path
import requests
from typing import Dict, List

class LectureNoteEnhancer:
    def __init__(self, api_key: str = None):
        """Initialize the enhancer with OpenRouter API key"""
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            raise ValueError("OpenRouter API key required. Set OPENROUTER_API_KEY environment variable or pass api_key parameter.")
        
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/simonwang",  # Optional
            "X-Title": "Lecture Note Enhancer"  # Optional
        }
        
        # Use Google Gemini 2.5 Flash Lite - very cost effective
        self.model = "google/gemini-2.5-flash-lite-preview-09-2025"
    
    def enhance_lecture_content(self, content: str, week_number: str) -> Dict:
        """Enhance a single lecture's content with structure and summaries"""
        
        prompt = f"""
You are an expert educational content processor. Please enhance this lecture transcript from Week {week_number} of a university course on "Empowering Citizens through Data: Participatory Policy Analysis for Hong Kong".

TASK: Transform this raw transcript into a well-structured, educational document with:

1. **Executive Summary** (2-3 paragraphs)
2. **Key Topics Covered** (bullet points)
3. **Main Discussion Points** (organized by topic)
4. **Important Concepts** (definitions and explanations)
5. **Student Activities/Interactions** (if any)
6. **Key Takeaways** (bullet points)
7. **Questions Raised** (if any)

FORMATTING REQUIREMENTS:
- Use clear markdown headers (##, ###)
- Add bullet points for lists
- Bold important terms
- Keep the original speaker attributions
- Maintain all original content but organize it better
- Add section breaks for readability

LECTURE CONTENT:
{content}

Please process this content and return the enhanced version in markdown format.
"""

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,
            "max_tokens": 4000
        }
        
        try:
            response = requests.post(self.base_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            enhanced_content = result['choices'][0]['message']['content']
            
            return {
                'success': True,
                'enhanced_content': enhanced_content,
                'usage': result.get('usage', {}),
                'model': self.model
            }
            
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'model': self.model
            }
    
    def process_lecture_file(self, file_path: Path) -> Dict:
        """Process a single lecture file"""
        print(f"Processing {file_path.name}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract week number from filename
            week_number = file_path.stem.replace('week', 'Week ')
            
            # Enhance the content
            result = self.enhance_lecture_content(content, week_number)
            
            if result['success']:
                # Save enhanced version
                enhanced_file = file_path.parent / f"{file_path.stem}_enhanced.md"
                with open(enhanced_file, 'w', encoding='utf-8') as f:
                    f.write(result['enhanced_content'])
                
                print(f"✓ Enhanced {file_path.name} → {enhanced_file.name}")
                
                # Print usage info
                usage = result.get('usage', {})
                if usage:
                    prompt_tokens = usage.get('prompt_tokens', 0)
                    completion_tokens = usage.get('completion_tokens', 0)
                    total_tokens = usage.get('total_tokens', 0)
                    print(f"  Tokens used: {total_tokens} (prompt: {prompt_tokens}, completion: {completion_tokens})")
                
                return result
            else:
                print(f"✗ Error processing {file_path.name}: {result['error']}")
                return result
                
        except Exception as e:
            print(f"✗ Error reading {file_path.name}: {e}")
            return {'success': False, 'error': str(e)}
    
    def process_all_lectures(self, directory: Path = None):
        """Process all lecture markdown files in the directory"""
        if directory is None:
            directory = Path(__file__).parent
        
        # Find all week*.md files
        lecture_files = list(directory.glob("week*.md"))
        
        if not lecture_files:
            print("No lecture files found (week*.md)")
            return
        
        print(f"Found {len(lecture_files)} lecture files to process:")
        for file in lecture_files:
            print(f"  - {file.name}")
        
        print(f"\nUsing model: {self.model}")
        print("Starting processing...\n")
        
        results = []
        total_cost = 0
        
        for i, file_path in enumerate(lecture_files, 1):
            print(f"[{i}/{len(lecture_files)}] ", end="")
            result = self.process_lecture_file(file_path)
            results.append(result)
            
            # Add small delay to avoid rate limiting
            time.sleep(1)
        
        # Summary
        successful = sum(1 for r in results if r.get('success', False))
        print(f"\n📊 Processing Summary:")
        print(f"  Successful: {successful}/{len(lecture_files)}")
        print(f"  Failed: {len(lecture_files) - successful}/{len(lecture_files)}")
        
        return results

def main():
    """Main function to run the lecture enhancer"""
    print("🎓 Lecture Note Enhancer")
    print("=" * 50)
    
    # Check for API key
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY environment variable not set")
        print("Please set your OpenRouter API key:")
        print("export OPENROUTER_API_KEY='your-api-key-here'")
        return
    
    try:
        enhancer = LectureNoteEnhancer(api_key)
        results = enhancer.process_all_lectures()
        
        if results:
            print("\n✅ Processing complete!")
            print("Enhanced files saved with '_enhanced.md' suffix")
            print("Original files preserved unchanged")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
