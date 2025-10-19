#!/usr/bin/env python3
"""
Simple Data Collection Script
Collect API data with detailed terminal output
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

def main():
    print("🚌 COMPREHENSIVE DATA COLLECTION")
    print("=" * 80)
    print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Create directories
    os.makedirs("data/collected_data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # STEP 1: KMB Routes
    print("\n🚌 STEP 1: KMB ROUTES COLLECTION")
    print("=" * 50)
    print("🔍 API Details:")
    print("   URL: https://data.etabus.gov.hk/v1/transport/kmb/route")
    print("   Method: GET")
    print("   Timeout: 30 seconds")
    
    try:
        print("📡 Making API request...")
        start_time = time.time()
        
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=30)
        
        request_time = time.time() - start_time
        print(f"⏱️  Request completed in {request_time:.2f} seconds")
        print(f"📊 Status Code: {response.status_code}")
        print(f"📏 Response Size: {len(response.content)} bytes")
        
        if response.status_code == 200:
            print("✅ API request successful!")
            
            # Parse JSON response
            print("🔍 Parsing JSON response...")
            data = response.json()
            routes = data.get('data', [])
            
            print(f"📊 Found {len(routes)} KMB routes")
            print(f"📋 Data structure: {list(data.keys())}")
            
            # Save raw JSON data
            json_file = f"data/collected_data/kmb_routes_{timestamp}.json"
            print(f"💾 Saving raw JSON data to: {json_file}")
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"✅ Raw data saved: {json_file}")
            print(f"📁 File size: {os.path.getsize(json_file)} bytes")
            
            # Create CSV file
            csv_file = f"data/collected_data/kmb_routes_{timestamp}.csv"
            print(f"📊 Creating CSV file: {csv_file}")
            print("📋 CSV Headers: route, bound, service_type, orig_en, orig_tc, orig_sc, dest_en, dest_tc, dest_sc, data_timestamp")
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                headers = ['route', 'bound', 'service_type', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp']
                writer.writerow(headers)
                
                # Write data
                print("📝 Writing route data to CSV...")
                for i, route in enumerate(routes):
                    writer.writerow([
                        route.get('route', ''),
                        route.get('bound', ''),
                        route.get('service_type', ''),
                        route.get('orig_en', ''),
                        route.get('orig_tc', ''),
                        route.get('orig_sc', ''),
                        route.get('dest_en', ''),
                        route.get('dest_tc', ''),
                        route.get('dest_sc', ''),
                        route.get('data_timestamp', '')
                    ])
                    
                    # Progress update every 100 routes
                    if (i + 1) % 100 == 0:
                        print(f"   📊 Processed {i + 1}/{len(routes)} routes...")
            
            print(f"✅ CSV file created: {csv_file}")
            print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes")
            print(f"📊 Total routes written: {len(routes)}")
            
            # Show sample data
            if routes:
                print("\n📋 Sample Route Data:")
                sample = routes[0]
                print(f"   Route ID: {sample.get('route', 'N/A')}")
                print(f"   Origin (EN): {sample.get('orig_en', 'N/A')}")
                print(f"   Origin (TC): {sample.get('orig_tc', 'N/A')}")
                print(f"   Destination (EN): {sample.get('dest_en', 'N/A')}")
                print(f"   Destination (TC): {sample.get('dest_tc', 'N/A')}")
                print(f"   Bound: {sample.get('bound', 'N/A')}")
                print(f"   Service Type: {sample.get('service_type', 'N/A')}")
            
            print("\n✅ STEP 1 COMPLETED: KMB Routes Collection")
            print(f"📊 KMB Routes: {len(routes)} routes")
            print(f"📁 CSV File: {csv_file}")
            print(f"📁 File Size: {os.path.getsize(csv_file)} bytes")
            
        else:
            print(f"❌ API request failed: {response.status_code}")
            print(f"📄 Response content: {response.text[:200]}...")
            
    except Exception as e:
        print(f"❌ Error collecting KMB routes: {str(e)}")
    
    print("\n" + "=" * 80)
    print("🎉 STEP 1 COMPLETED!")
    print("=" * 80)
    print("📊 KMB Routes data collection completed")
    print("📁 Check data/collected_data/ for CSV files")
    print("=" * 80)

if __name__ == "__main__":
    main()
