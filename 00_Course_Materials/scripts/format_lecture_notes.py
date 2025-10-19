#!/usr/bin/env python3
"""
Format lecture notes with proper paragraphs and headings
Preserves all original content, only adds structure and fixes typos
"""

import os
import json
import time
from pathlib import Path
import requests
from typing import Dict, List

class LectureNoteFormatter:
    def __init__(self, api_key: str = None):
        """Initialize the formatter with OpenRouter API key"""
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            raise ValueError("OpenRouter API key required. Set OPENROUTER_API_KEY environment variable or pass api_key parameter.")
        
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/simonwang",  # Optional
            "X-Title": "Lecture Note Formatter"  # Optional
        }
        
        # Use Google Gemini 2.5 Flash Lite - very cost effective
        self.model = "google/gemini-2.5-flash-lite-preview-09-2025"
    
    def format_lecture_content(self, content: str, week_number: str) -> Dict:
        """Format a single lecture's content with proper structure while preserving all original text"""
        
        prompt = f"""
You are a text formatting expert. Please format this lecture transcript from Week {week_number} with proper structure while preserving ALL original content.

TASK: Add formatting to make this lecture transcript more readable by:

1. **Add appropriate headings** (##, ###) to break up the content into logical sections
2. **Add paragraph breaks** where natural speech pauses occur
3. **Fix obvious typos** (like "recording" instead of "recording", "government" instead of "goverment")
4. **Preserve ALL original content** - do not summarize, paraphrase, or change meaning
5. **Keep all speaker names and attributions** exactly as they are
6. **Maintain the conversational flow** of the original transcript

FORMATTING RULES:
- Use ## for main topics/sections
- Use ### for subtopics
- Add paragraph breaks between different speakers or topics
- Fix only obvious spelling errors
- Keep all original words, phrases, and expressions
- Preserve the informal, conversational tone
- Do not add summaries or analysis

LECTURE CONTENT:
{content}

Please format this content and return the enhanced version in markdown format, preserving all original text.
"""

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.1,  # Low temperature for consistent formatting
            "max_tokens": 6000
        }
        
        try:
            response = requests.post(self.base_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            formatted_content = result['choices'][0]['message']['content']
            
            return {
                'success': True,
                'formatted_content': formatted_content,
                'usage': result.get('usage', {}),
                'model': self.model
            }
            
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'model': self.model
            }
    
    def format_lecture_file(self, file_path: Path) -> Dict:
        """Format a single lecture file"""
        print(f"Formatting {file_path.name}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract week number from filename
            week_number = file_path.stem.replace('week', 'Week ')
            
            # Format the content
            result = self.format_lecture_content(content, week_number)
            
            if result['success']:
                # Save formatted version
                formatted_file = file_path.parent / f"{file_path.stem}_formatted.md"
                with open(formatted_file, 'w', encoding='utf-8') as f:
                    f.write(result['formatted_content'])
                
                print(f"✓ Formatted {file_path.name} → {formatted_file.name}")
                
                # Print usage info
                usage = result.get('usage', {})
                if usage:
                    prompt_tokens = usage.get('prompt_tokens', 0)
                    completion_tokens = usage.get('completion_tokens', 0)
                    total_tokens = usage.get('total_tokens', 0)
                    print(f"  Tokens used: {total_tokens} (prompt: {prompt_tokens}, completion: {completion_tokens})")
                
                return result
            else:
                print(f"✗ Error formatting {file_path.name}: {result['error']}")
                return result
                
        except Exception as e:
            print(f"✗ Error reading {file_path.name}: {e}")
            return {'success': False, 'error': str(e)}
    
    def format_all_lectures(self, directory: Path = None):
        """Format all lecture markdown files in the directory"""
        if directory is None:
            directory = Path(__file__).parent
        
        # Find all week*.md files (but not the enhanced ones)
        lecture_files = [f for f in directory.glob("week*.md") if not f.name.endswith('_enhanced.md') and not f.name.endswith('_formatted.md')]
        
        if not lecture_files:
            print("No lecture files found (week*.md)")
            return
        
        print(f"Found {len(lecture_files)} lecture files to format:")
        for file in lecture_files:
            print(f"  - {file.name}")
        
        print(f"\nUsing model: {self.model}")
        print("Starting formatting...\n")
        
        results = []
        
        for i, file_path in enumerate(lecture_files, 1):
            print(f"[{i}/{len(lecture_files)}] ", end="")
            result = self.format_lecture_file(file_path)
            results.append(result)
            
            # Add small delay to avoid rate limiting
            time.sleep(1)
        
        # Summary
        successful = sum(1 for r in results if r.get('success', False))
        print(f"\n📊 Formatting Summary:")
        print(f"  Successful: {successful}/{len(lecture_files)}")
        print(f"  Failed: {len(lecture_files) - successful}/{len(lecture_files)}")
        
        return results

def main():
    """Main function to run the lecture formatter"""
    print("📝 Lecture Note Formatter")
    print("=" * 50)
    
    # Check for API key
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY environment variable not set")
        print("Please set your OpenRouter API key:")
        print("export OPENROUTER_API_KEY='your-api-key-here'")
        return
    
    try:
        formatter = LectureNoteFormatter(api_key)
        results = formatter.format_all_lectures()
        
        if results:
            print("\n✅ Formatting complete!")
            print("Formatted files saved with '_formatted.md' suffix")
            print("Original files preserved unchanged")
            print("All original content preserved with added structure")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
