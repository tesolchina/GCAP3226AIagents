#!/usr/bin/env python3
"""
Sample API Access Script - TEMPLATE

This is a dummy file showing the structure your real code might have.
DO NOT use this directly - let AI generate proper code based on your instructions!

Replace this file with AI-generated code specific to your dataset.
"""

import requests
import json
from datetime import datetime


class DataAPIClient:
    """
    Template class for API access
    
    Your actual class will be customized by AI for your specific dataset
    """
    
    def __init__(self, base_url):
        """
        Initialize the API client
        
        Args:
            base_url: The base URL of your chosen API
        """
        self.base_url = base_url
        print(f"✓ Initialized API client for: {base_url}")
    
    def fetch_data(self, **params):
        """
        Fetch data from the API
        
        Args:
            **params: API parameters specific to your dataset
            
        Returns:
            dict: API response data
        """
        print(f"📡 Fetching data with parameters: {params}")
        
        try:
            # This is just a template - AI will write the actual API call
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            print("✓ Data fetched successfully")
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Error fetching data: {e}")
            return None
    
    def save_data(self, data, filename):
        """
        Save data to a JSON file
        
        Args:
            data: The data to save
            filename: Output filename
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Data saved to: {filename}")


def main():
    """
    Main function - this is where your data collection happens
    
    AI will customize this based on your specific needs
    """
    print("=" * 60)
    print("DATA COLLECTION SCRIPT")
    print("=" * 60)
    
    # Step 1: Initialize API client
    # TODO: Replace with your actual API endpoint
    api_url = "https://data.gov.hk/YOUR_API_ENDPOINT_HERE"
    client = DataAPIClient(api_url)
    
    # Step 2: Define parameters
    # TODO: AI will customize these for your dataset
    params = {
        "parameter1": "value1",
        "parameter2": "value2",
        # Add more parameters as needed
    }
    
    # Step 3: Fetch data
    print("\n📊 Collecting data...")
    data = client.fetch_data(**params)
    
    if data:
        # Step 4: Save raw data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"output/raw_data_{timestamp}.json"
        client.save_data(data, output_file)
        
        # Step 5: Basic statistics
        print("\n📈 Basic Statistics:")
        print(f"   Data timestamp: {timestamp}")
        # TODO: AI will add relevant statistics for your data
        
        print("\n✓ Data collection complete!")
    else:
        print("\n✗ Data collection failed!")


if __name__ == "__main__":
    # NOTE: This is a TEMPLATE file
    print("\n" + "!" * 60)
    print("⚠️  WARNING: This is a template file!")
    print("⚠️  Replace this with AI-generated code for your project!")
    print("!" * 60 + "\n")
    
    # Uncomment the line below after AI generates your real code
    # main()
    
    print("\n💡 To get started:")
    print("   1. Fill out project_instructions.md")
    print("   2. Give it to the AI agent")
    print("   3. AI will generate your custom code")
    print("   4. Replace this file with the AI-generated code")
