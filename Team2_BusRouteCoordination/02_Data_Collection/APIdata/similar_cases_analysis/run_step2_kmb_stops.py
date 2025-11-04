#!/usr/bin/env python3
"""
Step 2: Collect KMB Stops
Script to collect all KMB stops data
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

print("🚌 STEP 2: KMB STOPS COLLECTION")
print("=" * 50)
print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

# Create directories
os.makedirs("data/collected_data", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

print("🔍 API Details:")
print("   URL: https://data.etabus.gov.hk/v1/transport/kmb/stop")
print("   Method: GET")
print("   Timeout: 30 seconds")

try:
    print("📡 Making API request...")
    start_time = time.time()
    
    response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop", timeout=30)
    
    request_time = time.time() - start_time
    print(f"⏱️  Request completed in {request_time:.2f} seconds")
    print(f"📊 Status Code: {response.status_code}")
    print(f"📏 Response Size: {len(response.content)} bytes")
    
    if response.status_code == 200:
        print("✅ API request successful!")
        
        # Parse JSON response
        print("🔍 Parsing JSON response...")
        data = response.json()
        stops = data.get('data', [])
        
        print(f"📊 Found {len(stops)} KMB stops")
        print(f"📋 Data structure: {list(data.keys())}")
        
        # Save raw JSON data
        json_file = f"data/collected_data/kmb_all_stops_{timestamp}.json"
        print(f"💾 Saving raw JSON data to: {json_file}")
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Raw data saved: {json_file}")
        print(f"📁 File size: {os.path.getsize(json_file)} bytes")
        
        # Create CSV file
        csv_file = f"data/collected_data/kmb_all_stops_{timestamp}.csv"
        print(f"📊 Creating CSV file: {csv_file}")
        print("📋 CSV Headers: stop, name_en, name_tc, name_sc, lat, long, data_timestamp")
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            headers = ['stop', 'name_en', 'name_tc', 'name_sc', 'lat', 'long', 'data_timestamp']
            writer.writerow(headers)
            
            # Write data
            print("📝 Writing stop data to CSV...")
            for i, stop in enumerate(stops):
                writer.writerow([
                    stop.get('stop', ''),
                    stop.get('name_en', ''),
                    stop.get('name_tc', ''),
                    stop.get('name_sc', ''),
                    stop.get('lat', ''),
                    stop.get('long', ''),
                    stop.get('data_timestamp', '')
                ])
                
                # Progress update every 500 stops
                if (i + 1) % 500 == 0:
                    print(f"   📊 Processed {i + 1}/{len(stops)} stops...")
        
        print(f"✅ CSV file created: {csv_file}")
        print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes")
        print(f"📊 Total stops written: {len(stops)}")
        
        # Show sample data
        if stops:
            print("\n📋 Sample Stop Data:")
            sample = stops[0]
            print(f"   Stop ID: {sample.get('stop', 'N/A')}")
            print(f"   Name (EN): {sample.get('name_en', 'N/A')}")
            print(f"   Name (TC): {sample.get('name_tc', 'N/A')}")
            print(f"   Latitude: {sample.get('lat', 'N/A')}")
            print(f"   Longitude: {sample.get('long', 'N/A')}")
        
        print("\n✅ STEP 2 COMPLETED: KMB Stops Collection")
        print(f"📊 KMB Stops: {len(stops)} stops")
        print(f"📁 CSV File: {csv_file}")
        print(f"📁 File Size: {os.path.getsize(csv_file)} bytes")
        
    else:
        print(f"❌ API request failed: {response.status_code}")
        print(f"📄 Response content: {response.text[:200]}...")
        
except Exception as e:
    print(f"❌ Error collecting KMB stops: {str(e)}")

print("\n" + "=" * 80)
print("🎉 STEP 2 COMPLETED!")
print("=" * 80)
print("📊 KMB Stops data collection completed")
print("📁 Check data/collected_data/ for CSV files")
print("=" * 80)
