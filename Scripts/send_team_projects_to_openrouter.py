#!/usr/bin/env python3
"""
Script to send comprehensive team project information to OpenRouter LLM
for roadmap completion and refinement.

This script sends all team project information to an LLM to:
1. Complete and refine the project roadmaps
2. Generate additional team-specific guidance
3. Create Google Drive folder structure recommendations
4. Provide enhanced project management tools
"""

import requests
import json
import os
from pathlib import Path

# Configuration
API_KEY_FILE = "/Users/simonwang/Documents/Usage/ObSync/Vault4sync/VibeCoding/testOpenRouterModels/key_openrouter.md"
MODEL = "google/gemini-2.5-pro"  # Premium model for comprehensive analysis
OUTPUT_FILE = "/Users/simonwang/Documents/Usage/ObSync/Vault4sync/GCAP3226/Enhanced_Team_Project_Roadmaps.md"

def read_api_key():
    """Read API key from file"""
    try:
        with open(API_KEY_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"API key file not found: {API_KEY_FILE}")
        return None

def read_comprehensive_summary():
    """Read the comprehensive team project summary"""
    summary_file = "/Users/simonwang/Documents/Usage/ObSync/Vault4sync/GCAP3226/Comprehensive_Team_Project_Summary.md"
    try:
        with open(summary_file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Summary file not found: {summary_file}")
        return None

def send_to_openrouter(api_key, content):
    """Send content to OpenRouter LLM for processing"""
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": """You are an expert academic course designer and project management specialist. You have extensive experience in:

1. Designing data-driven government research projects
2. Creating comprehensive project roadmaps for student teams
3. Developing Google Drive collaboration structures
4. Integrating mathematical modeling (regression and simulation) into research projects
5. Creating actionable project management frameworks

Your task is to analyze the comprehensive team project information and create enhanced, detailed roadmaps for each of the 6 teams. Focus on:

- Specific, actionable tasks for each team
- Detailed timelines with clear deliverables
- Google Drive folder structure recommendations
- Enhanced collaboration frameworks
- Specific government enquiry templates
- Mathematical modeling guidance
- Risk management and contingency planning
- Quality assurance frameworks

Provide practical, implementable guidance that will help each team succeed in their data-driven government research project."""
            },
            {
                "role": "user",
                "content": f"""Please analyze the following comprehensive team project information and create enhanced, detailed roadmaps for each of the 6 teams. 

The information includes:
- Course overview and mission
- 6 team projects with specific focus areas
- Detailed timeline and methodology
- Collaboration frameworks
- Government enquiry processes
- Assessment components

Please provide:

1. **Enhanced Project Roadmaps** for each team with:
   - Specific, actionable tasks
   - Detailed weekly deliverables
   - Risk management strategies
   - Quality assurance checkpoints

2. **Google Drive Folder Structure** recommendations for each team

3. **Enhanced Collaboration Frameworks** with:
   - Specific role definitions
   - Communication protocols
   - Progress tracking systems
   - Conflict resolution strategies

4. **Government Enquiry Templates** specific to each team's focus area

5. **Mathematical Modeling Guidance** tailored to each team's research question

6. **Project Management Tools** and templates

7. **Success Metrics** and evaluation criteria

Here is the comprehensive team project information:

{content}"""
            }
        ],
        "max_tokens": 8000,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to OpenRouter: {e}")
        return None

def save_response(response, output_file):
    """Save the LLM response to a file"""
    if response and 'choices' in response:
        content = response['choices'][0]['message']['content']
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Enhanced team project roadmaps saved to: {output_file}")
        return True
    else:
        print("No response received from OpenRouter")
        return False

def main():
    """Main function to execute the script"""
    print("Sending comprehensive team project information to OpenRouter LLM...")
    
    # Read API key
    api_key = read_api_key()
    if not api_key:
        print("Failed to read API key")
        return
    
    # Read comprehensive summary
    content = read_comprehensive_summary()
    if not content:
        print("Failed to read comprehensive summary")
        return
    
    print(f"Content length: {len(content)} characters")
    print(f"Using model: {MODEL}")
    
    # Send to OpenRouter
    response = send_to_openrouter(api_key, content)
    
    if response:
        # Save response
        if save_response(response, OUTPUT_FILE):
            print("✅ Successfully generated enhanced team project roadmaps!")
            print(f"📁 Output saved to: {OUTPUT_FILE}")
        else:
            print("❌ Failed to save response")
    else:
        print("❌ Failed to get response from OpenRouter")

if __name__ == "__main__":
    main()

