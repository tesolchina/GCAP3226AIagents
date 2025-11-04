#!/usr/bin/env python3
"""
Execute Data Collection
Simple execution script for data collection
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

# Create directories
os.makedirs("data/collected_data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"data_collection_log_{timestamp}.txt"

# Initialize log file
with open(log_file, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("🚌 COMPREHENSIVE DATA COLLECTION LOG\n")
    f.write("=" * 80 + "\n")
    f.write(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"📁 Log File: {log_file}\n")
    f.write("=" * 80 + "\n\n")

def log_and_print(message):
    timestamp_str = datetime.now().strftime("%H:%M:%S")
    formatted_message = f"[{timestamp_str}] {message}"
    print(formatted_message)
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(formatted_message + "\n")

print("🚌 COMPREHENSIVE DATA COLLECTION WITH DETAILED LOGGING")
print("=" * 80)
print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

# STEP 1: KMB Routes
log_and_print("🚌 STEP 1: KMB ROUTES COLLECTION")
log_and_print("=" * 50)
log_and_print("🔍 API Details:")
log_and_print("   URL: https://data.etabus.gov.hk/v1/transport/kmb/route")
log_and_print("   Method: GET")
log_and_print("   Timeout: 30 seconds")

try:
    log_and_print("📡 Making API request...")
    start_time = time.time()
    
    response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=30)
    
    request_time = time.time() - start_time
    log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds")
    log_and_print(f"📊 Status Code: {response.status_code}")
    log_and_print(f"📏 Response Size: {len(response.content)} bytes")
    
    if response.status_code == 200:
        log_and_print("✅ API request successful!")
        
        # Parse JSON response
        log_and_print("🔍 Parsing JSON response...")
        data = response.json()
        routes = data.get('data', [])
        
        log_and_print(f"📊 Found {len(routes)} KMB routes")
        log_and_print(f"📋 Data structure: {list(data.keys())}")
        
        # Save raw JSON data
        json_file = f"data/collected_data/kmb_routes_{timestamp}.json"
        log_and_print(f"💾 Saving raw JSON data to: {json_file}")
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        log_and_print(f"✅ Raw data saved: {json_file}")
        log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes")
        
        # Create CSV file
        csv_file = f"data/collected_data/kmb_routes_{timestamp}.csv"
        log_and_print(f"📊 Creating CSV file: {csv_file}")
        log_and_print("📋 CSV Headers: route, bound, service_type, orig_en, orig_tc, orig_sc, dest_en, dest_tc, dest_sc, data_timestamp")
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            headers = ['route', 'bound', 'service_type', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp']
            writer.writerow(headers)
            
            # Write data
            log_and_print("📝 Writing route data to CSV...")
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
                    log_and_print(f"   📊 Processed {i + 1}/{len(routes)} routes...")
        
        log_and_print(f"✅ CSV file created: {csv_file}")
        log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes")
        log_and_print(f"📊 Total routes written: {len(routes)}")
        
        # Show sample data
        if routes:
            log_and_print("\n📋 Sample Route Data:")
            sample = routes[0]
            log_and_print(f"   Route ID: {sample.get('route', 'N/A')}")
            log_and_print(f"   Origin (EN): {sample.get('orig_en', 'N/A')}")
            log_and_print(f"   Origin (TC): {sample.get('orig_tc', 'N/A')}")
            log_and_print(f"   Destination (EN): {sample.get('dest_en', 'N/A')}")
            log_and_print(f"   Destination (TC): {sample.get('dest_tc', 'N/A')}")
            log_and_print(f"   Bound: {sample.get('bound', 'N/A')}")
            log_and_print(f"   Service Type: {sample.get('service_type', 'N/A')}")
        
        log_and_print("\n✅ STEP 1 COMPLETED: KMB Routes Collection")
        log_and_print(f"📊 KMB Routes: {len(routes)} routes")
        log_and_print(f"📁 CSV File: {csv_file}")
        log_and_print(f"📁 File Size: {os.path.getsize(csv_file)} bytes")
        
    else:
        log_and_print(f"❌ API request failed: {response.status_code}")
        log_and_print(f"📄 Response content: {response.text[:200]}...")
        
except Exception as e:
    log_and_print(f"❌ Error collecting KMB routes: {str(e)}")

print("\n" + "=" * 80)
print("🎉 STEP 1 COMPLETED!")
print("=" * 80)
print(f"📁 Log file: {log_file}")
print("📊 Check the log file for detailed results")
print("=" * 80)
