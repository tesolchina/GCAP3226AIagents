#!/usr/bin/env python3
"""
Run Data Collection with Comprehensive Logging
Execute API data collection with detailed terminal output and logging
"""

import requests
import json
import csv
from datetime import datetime
import time
import os
import sys

def log_and_print(message, log_file):
    """Log message to file and print to terminal"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    formatted_message = f"[{timestamp}] {message}"
    
    # Print to terminal
    print(formatted_message)
    
    # Log to file
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(formatted_message + "\n")

def main():
    """Main data collection function"""
    print("🚌 COMPREHENSIVE DATA COLLECTION WITH DETAILED LOGGING")
    print("=" * 80)
    print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
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
    
    # STEP 1: KMB Routes
    log_and_print("🚌 STEP 1: KMB ROUTES COLLECTION", log_file)
    log_and_print("=" * 50, log_file)
    log_and_print("🔍 API Details:", log_file)
    log_and_print("   URL: https://data.etabus.gov.hk/v1/transport/kmb/route", log_file)
    log_and_print("   Method: GET", log_file)
    log_and_print("   Timeout: 30 seconds", log_file)
    
    try:
        log_and_print("📡 Making API request...", log_file)
        start_time = time.time()
        
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=30)
        
        request_time = time.time() - start_time
        log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds", log_file)
        log_and_print(f"📊 Status Code: {response.status_code}", log_file)
        log_and_print(f"📏 Response Size: {len(response.content)} bytes", log_file)
        
        if response.status_code == 200:
            log_and_print("✅ API request successful!", log_file)
            
            # Parse JSON response
            log_and_print("🔍 Parsing JSON response...", log_file)
            data = response.json()
            routes = data.get('data', [])
            
            log_and_print(f"📊 Found {len(routes)} KMB routes", log_file)
            log_and_print(f"📋 Data structure: {list(data.keys())}", log_file)
            
            # Save raw JSON data
            json_file = f"data/collected_data/kmb_routes_{timestamp}.json"
            log_and_print(f"💾 Saving raw JSON data to: {json_file}", log_file)
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            log_and_print(f"✅ Raw data saved: {json_file}", log_file)
            log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes", log_file)
            
            # Create CSV file
            csv_file = f"data/collected_data/kmb_routes_{timestamp}.csv"
            log_and_print(f"📊 Creating CSV file: {csv_file}", log_file)
            log_and_print("📋 CSV Headers: route, bound, service_type, orig_en, orig_tc, orig_sc, dest_en, dest_tc, dest_sc, data_timestamp", log_file)
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                headers = ['route', 'bound', 'service_type', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp']
                writer.writerow(headers)
                
                # Write data
                log_and_print("📝 Writing route data to CSV...", log_file)
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
                        log_and_print(f"   📊 Processed {i + 1}/{len(routes)} routes...", log_file)
            
            log_and_print(f"✅ CSV file created: {csv_file}", log_file)
            log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes", log_file)
            log_and_print(f"📊 Total routes written: {len(routes)}", log_file)
            
            # Show sample data
            if routes:
                log_and_print("\n📋 Sample Route Data:", log_file)
                sample = routes[0]
                log_and_print(f"   Route ID: {sample.get('route', 'N/A')}", log_file)
                log_and_print(f"   Origin (EN): {sample.get('orig_en', 'N/A')}", log_file)
                log_and_print(f"   Origin (TC): {sample.get('orig_tc', 'N/A')}", log_file)
                log_and_print(f"   Destination (EN): {sample.get('dest_en', 'N/A')}", log_file)
                log_and_print(f"   Destination (TC): {sample.get('dest_tc', 'N/A')}", log_file)
                log_and_print(f"   Bound: {sample.get('bound', 'N/A')}", log_file)
                log_and_print(f"   Service Type: {sample.get('service_type', 'N/A')}", log_file)
            
            log_and_print("\n✅ STEP 1 COMPLETED: KMB Routes Collection", log_file)
            log_and_print(f"📊 KMB Routes: {len(routes)} routes", log_file)
            log_and_print(f"📁 CSV File: {csv_file}", log_file)
            log_and_print(f"📁 File Size: {os.path.getsize(csv_file)} bytes", log_file)
            
        else:
            log_and_print(f"❌ API request failed: {response.status_code}", log_file)
            log_and_print(f"📄 Response content: {response.text[:200]}...", log_file)
            
    except Exception as e:
        log_and_print(f"❌ Error collecting KMB routes: {str(e)}", log_file)
    
    # Wait between requests
    log_and_print("\n⏱️  Waiting 10 seconds before next request...", log_file)
    for i in range(10, 0, -1):
        log_and_print(f"   ⏳ {i} seconds remaining...", log_file)
        time.sleep(1)
    
    # STEP 2: KMB Stops
    log_and_print("\n🚌 STEP 2: KMB STOPS COLLECTION", log_file)
    log_and_print("=" * 50, log_file)
    log_and_print("🔍 API Details:", log_file)
    log_and_print("   URL: https://data.etabus.gov.hk/v1/transport/kmb/stop", log_file)
    log_and_print("   Method: GET", log_file)
    log_and_print("   Timeout: 30 seconds", log_file)
    
    try:
        log_and_print("📡 Making API request...", log_file)
        start_time = time.time()
        
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop", timeout=30)
        
        request_time = time.time() - start_time
        log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds", log_file)
        log_and_print(f"📊 Status Code: {response.status_code}", log_file)
        log_and_print(f"📏 Response Size: {len(response.content)} bytes", log_file)
        
        if response.status_code == 200:
            log_and_print("✅ API request successful!", log_file)
            
            # Parse JSON response
            log_and_print("🔍 Parsing JSON response...", log_file)
            data = response.json()
            stops = data.get('data', [])
            
            log_and_print(f"📊 Found {len(stops)} KMB stops", log_file)
            log_and_print(f"📋 Data structure: {list(data.keys())}", log_file)
            
            # Save raw JSON data
            json_file = f"data/collected_data/kmb_stops_{timestamp}.json"
            log_and_print(f"💾 Saving raw JSON data to: {json_file}", log_file)
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            log_and_print(f"✅ Raw data saved: {json_file}", log_file)
            log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes", log_file)
            
            # Create CSV file
            csv_file = f"data/collected_data/kmb_stops_{timestamp}.csv"
            log_and_print(f"📊 Creating CSV file: {csv_file}", log_file)
            log_and_print("📋 CSV Headers: stop, name_en, name_tc, name_sc, lat, long, data_timestamp", log_file)
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                headers = ['stop', 'name_en', 'name_tc', 'name_sc', 'lat', 'long', 'data_timestamp']
                writer.writerow(headers)
                
                # Write data
                log_and_print("📝 Writing stop data to CSV...", log_file)
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
                        log_and_print(f"   📊 Processed {i + 1}/{len(stops)} stops...", log_file)
            
            log_and_print(f"✅ CSV file created: {csv_file}", log_file)
            log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes", log_file)
            log_and_print(f"📊 Total stops written: {len(stops)}", log_file)
            
            # Show sample data
            if stops:
                log_and_print("\n📋 Sample Stop Data:", log_file)
                sample = stops[0]
                log_and_print(f"   Stop ID: {sample.get('stop', 'N/A')}", log_file)
                log_and_print(f"   Name (EN): {sample.get('name_en', 'N/A')}", log_file)
                log_and_print(f"   Name (TC): {sample.get('name_tc', 'N/A')}", log_file)
                log_and_print(f"   Latitude: {sample.get('lat', 'N/A')}", log_file)
                log_and_print(f"   Longitude: {sample.get('long', 'N/A')}", log_file)
            
            log_and_print("\n✅ STEP 2 COMPLETED: KMB Stops Collection", log_file)
            log_and_print(f"📊 KMB Stops: {len(stops)} stops", log_file)
            log_and_print(f"📁 CSV File: {csv_file}", log_file)
            log_and_print(f"📁 File Size: {os.path.getsize(csv_file)} bytes", log_file)
            
        else:
            log_and_print(f"❌ API request failed: {response.status_code}", log_file)
            log_and_print(f"📄 Response content: {response.text[:200]}...", log_file)
            
    except Exception as e:
        log_and_print(f"❌ Error collecting KMB stops: {str(e)}", log_file)
    
    # Wait between requests
    log_and_print("\n⏱️  Waiting 10 seconds before next request...", log_file)
    for i in range(10, 0, -1):
        log_and_print(f"   ⏳ {i} seconds remaining...", log_file)
        time.sleep(1)
    
    # STEP 3: Citybus Routes
    log_and_print("\n🚌 STEP 3: CITYBUS ROUTES COLLECTION", log_file)
    log_and_print("=" * 50, log_file)
    log_and_print("🔍 API Details:", log_file)
    log_and_print("   URL: https://rt.data.gov.hk/v2/transport/citybus/route/ctb", log_file)
    log_and_print("   Method: GET", log_file)
    log_and_print("   Timeout: 30 seconds", log_file)
    
    try:
        log_and_print("📡 Making API request...", log_file)
        start_time = time.time()
        
        response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/route/ctb", timeout=30)
        
        request_time = time.time() - start_time
        log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds", log_file)
        log_and_print(f"📊 Status Code: {response.status_code}", log_file)
        log_and_print(f"📏 Response Size: {len(response.content)} bytes", log_file)
        
        if response.status_code == 200:
            log_and_print("✅ API request successful!", log_file)
            
            # Parse JSON response
            log_and_print("🔍 Parsing JSON response...", log_file)
            data = response.json()
            routes = data.get('data', [])
            
            log_and_print(f"📊 Found {len(routes)} Citybus routes", log_file)
            log_and_print(f"📋 Data structure: {list(data.keys())}", log_file)
            
            # Save raw JSON data
            json_file = f"data/collected_data/citybus_routes_{timestamp}.json"
            log_and_print(f"💾 Saving raw JSON data to: {json_file}", log_file)
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            log_and_print(f"✅ Raw data saved: {json_file}", log_file)
            log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes", log_file)
            
            # Create CSV file
            csv_file = f"data/collected_data/citybus_routes_{timestamp}.csv"
            log_and_print(f"📊 Creating CSV file: {csv_file}", log_file)
            log_and_print("📋 CSV Headers: co, route, orig_en, orig_tc, orig_sc, dest_en, dest_tc, dest_sc, data_timestamp", log_file)
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                headers = ['co', 'route', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp']
                writer.writerow(headers)
                
                # Write data
                log_and_print("📝 Writing route data to CSV...", log_file)
                for i, route in enumerate(routes):
                    writer.writerow([
                        route.get('co', ''),
                        route.get('route', ''),
                        route.get('orig_en', ''),
                        route.get('orig_tc', ''),
                        route.get('orig_sc', ''),
                        route.get('dest_en', ''),
                        route.get('dest_tc', ''),
                        route.get('dest_sc', ''),
                        route.get('data_timestamp', '')
                    ])
                    
                    # Progress update every 50 routes
                    if (i + 1) % 50 == 0:
                        log_and_print(f"   📊 Processed {i + 1}/{len(routes)} routes...", log_file)
            
            log_and_print(f"✅ CSV file created: {csv_file}", log_file)
            log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes", log_file)
            log_and_print(f"📊 Total routes written: {len(routes)}", log_file)
            
            # Show sample data
            if routes:
                log_and_print("\n📋 Sample Route Data:", log_file)
                sample = routes[0]
                log_and_print(f"   Company: {sample.get('co', 'N/A')}", log_file)
                log_and_print(f"   Route ID: {sample.get('route', 'N/A')}", log_file)
                log_and_print(f"   Origin (EN): {sample.get('orig_en', 'N/A')}", log_file)
                log_and_print(f"   Origin (TC): {sample.get('orig_tc', 'N/A')}", log_file)
                log_and_print(f"   Destination (EN): {sample.get('dest_en', 'N/A')}", log_file)
                log_and_print(f"   Destination (TC): {sample.get('dest_tc', 'N/A')}", log_file)
            
            log_and_print("\n✅ STEP 3 COMPLETED: Citybus Routes Collection", log_file)
            log_and_print(f"📊 Citybus Routes: {len(routes)} routes", log_file)
            log_and_print(f"📁 CSV File: {csv_file}", log_file)
            log_and_print(f"📁 File Size: {os.path.getsize(csv_file)} bytes", log_file)
            
        else:
            log_and_print(f"❌ API request failed: {response.status_code}", log_file)
            log_and_print(f"📄 Response content: {response.text[:200]}...", log_file)
            
    except Exception as e:
        log_and_print(f"❌ Error collecting Citybus routes: {str(e)}", log_file)
    
    # Final summary
    log_and_print("\n📊 COLLECTION SUMMARY", log_file)
    log_and_print("=" * 80, log_file)
    
    end_time = datetime.now()
    total_time = (end_time - datetime.strptime(timestamp, "%Y%m%d_%H%M%S")).total_seconds()
    
    log_and_print(f"⏱️  Total Collection Time: {total_time:.2f} seconds", log_file)
    log_and_print(f"📅 End Time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}", log_file)
    
    log_and_print("\n🎉 COMPREHENSIVE DATA COLLECTION COMPLETED!", log_file)
    log_and_print(f"📁 All logs saved to: {log_file}", log_file)
    log_and_print("📊 Check data/collected_data/ for CSV files", log_file)
    
    print("\n" + "=" * 80)
    print("🎉 DATA COLLECTION COMPLETED!")
    print("=" * 80)
    print(f"📁 Log file: {log_file}")
    print("📊 Check the log file for detailed results")
    print("📁 Check data/collected_data/ for CSV files")
    print("=" * 80)

if __name__ == "__main__":
    main()
