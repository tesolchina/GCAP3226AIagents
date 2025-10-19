#!/usr/bin/env python3
"""
Citybus Data Collection Script
Comprehensive script to collect all Citybus data including routes, stops, and route-stop mappings
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

print("🚌 CITYBUS DATA COLLECTION SCRIPT")
print("=" * 80)
print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

# Create directories
os.makedirs("data/collected_data", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"citybus_data_collection_log_{timestamp}.txt"

# Initialize log file
with open(log_file, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("🚌 CITYBUS DATA COLLECTION LOG\n")
    f.write("=" * 80 + "\n")
    f.write(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"📁 Log File: {log_file}\n")
    f.write("=" * 80 + "\n\n")

def log_and_print(message):
    timestamp_str = datetime.now().strftime('%H:%M:%S')
    formatted_message = f"[{timestamp_str}] {message}"
    print(formatted_message)
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(formatted_message + "\n")

# STEP 1: Collect Citybus Routes
log_and_print("🚀 STEP 1: Collecting Citybus Routes")
log_and_print("=" * 50)
log_and_print("🔍 API Details:")
log_and_print("   URL: https://rt.data.gov.hk/v2/transport/citybus/route/ctb")
log_and_print("   Method: GET")
log_and_print("   Timeout: 30 seconds")

try:
    log_and_print("📡 Making Citybus routes API request...")
    start_time = time.time()
    
    response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/route/ctb", timeout=30)
    
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
        
        log_and_print(f"📊 Found {len(routes)} Citybus routes")
        log_and_print(f"📋 Data structure: {list(data.keys())}")
        
        # Save raw JSON data
        json_file = f"data/collected_data/citybus_all_routes_{timestamp}.json"
        log_and_print(f"💾 Saving raw JSON data to: {json_file}")
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        log_and_print(f"✅ Raw data saved: {json_file}")
        log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes")
        
        # Create CSV file
        csv_file = f"data/collected_data/citybus_all_routes_{timestamp}.csv"
        log_and_print(f"📊 Creating CSV file: {csv_file}")
        log_and_print("📋 CSV Headers: route, bound, service_type, orig_tc, orig_en, dest_tc, dest_en, data_timestamp")
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            headers = ['route', 'bound', 'service_type', 'orig_tc', 'orig_en', 'dest_tc', 'dest_en', 'data_timestamp']
            writer.writerow(headers)
            
            # Write data
            log_and_print("📝 Writing route data to CSV...")
            for i, route in enumerate(routes):
                writer.writerow([
                    route.get('route', ''),
                    route.get('bound', ''),
                    route.get('service_type', ''),
                    route.get('orig_tc', ''),
                    route.get('orig_en', ''),
                    route.get('dest_tc', ''),
                    route.get('dest_en', ''),
                    route.get('data_timestamp', '')
                ])
                
                # Progress update every 50 routes
                if (i + 1) % 50 == 0:
                    log_and_print(f"   📊 Processed {i + 1}/{len(routes)} routes...")
        
        log_and_print(f"✅ CSV file created: {csv_file}")
        log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes")
        log_and_print(f"📊 Total routes written: {len(routes)}")
        
        # Show sample data
        if routes:
            log_and_print("\n📋 Sample Route Data:")
            sample = routes[0]
            log_and_print(f"   Route ID: {sample.get('route', 'N/A')}")
            log_and_print(f"   Origin (TC): {sample.get('orig_tc', 'N/A')}")
            log_and_print(f"   Origin (EN): {sample.get('orig_en', 'N/A')}")
            log_and_print(f"   Destination (TC): {sample.get('dest_tc', 'N/A')}")
            log_and_print(f"   Destination (EN): {sample.get('dest_en', 'N/A')}")
            log_and_print(f"   Bound: {sample.get('bound', 'N/A')}")
            log_and_print(f"   Service Type: {sample.get('service_type', 'N/A')}")
        
        log_and_print("\n✅ STEP 1 COMPLETED: Citybus Routes Collection")
        log_and_print(f"📊 Citybus Routes: {len(routes)} routes")
        log_and_print(f"📁 CSV File: {csv_file}")
        log_and_print(f"📁 File Size: {os.path.getsize(csv_file)} bytes")
        
    else:
        log_and_print(f"❌ API request failed: {response.status_code}")
        log_and_print(f"📄 Response content: {response.text[:200]}...")
        
except Exception as e:
    log_and_print(f"❌ Error collecting Citybus routes: {str(e)}")

# STEP 2: Collect Citybus Stops
log_and_print("\n🚀 STEP 2: Collecting Citybus Stops")
log_and_print("=" * 50)
log_and_print("🔍 API Details:")
log_and_print("   URL: https://rt.data.gov.hk/v2/transport/citybus/stop")
log_and_print("   Method: GET")
log_and_print("   Timeout: 30 seconds")

try:
    log_and_print("📡 Making Citybus stops API request...")
    start_time = time.time()
    
    response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/stop", timeout=30)
    
    request_time = time.time() - start_time
    log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds")
    log_and_print(f"📊 Status Code: {response.status_code}")
    log_and_print(f"📏 Response Size: {len(response.content)} bytes")
    
    if response.status_code == 200:
        log_and_print("✅ API request successful!")
        
        # Parse JSON response
        log_and_print("🔍 Parsing JSON response...")
        data = response.json()
        stops = data.get('data', [])
        
        log_and_print(f"📊 Found {len(stops)} Citybus stops")
        log_and_print(f"📋 Data structure: {list(data.keys())}")
        
        # Save raw JSON data
        json_file = f"data/collected_data/citybus_all_stops_{timestamp}.json"
        log_and_print(f"💾 Saving raw JSON data to: {json_file}")
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        log_and_print(f"✅ Raw data saved: {json_file}")
        log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes")
        
        # Create CSV file
        csv_file = f"data/collected_data/citybus_all_stops_{timestamp}.csv"
        log_and_print(f"📊 Creating CSV file: {csv_file}")
        log_and_print("📋 CSV Headers: stop, name_en, name_tc, name_sc, lat, long, data_timestamp")
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            headers = ['stop', 'name_en', 'name_tc', 'name_sc', 'lat', 'long', 'data_timestamp']
            writer.writerow(headers)
            
            # Write data
            log_and_print("📝 Writing stop data to CSV...")
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
                    log_and_print(f"   📊 Processed {i + 1}/{len(stops)} stops...")
        
        log_and_print(f"✅ CSV file created: {csv_file}")
        log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes")
        log_and_print(f"📊 Total stops written: {len(stops)}")
        
        # Show sample data
        if stops:
            log_and_print("\n📋 Sample Stop Data:")
            sample = stops[0]
            log_and_print(f"   Stop ID: {sample.get('stop', 'N/A')}")
            log_and_print(f"   Name (EN): {sample.get('name_en', 'N/A')}")
            log_and_print(f"   Name (TC): {sample.get('name_tc', 'N/A')}")
            log_and_print(f"   Latitude: {sample.get('lat', 'N/A')}")
            log_and_print(f"   Longitude: {sample.get('long', 'N/A')}")
        
        log_and_print("\n✅ STEP 2 COMPLETED: Citybus Stops Collection")
        log_and_print(f"📊 Citybus Stops: {len(stops)} stops")
        log_and_print(f"📁 CSV File: {csv_file}")
        log_and_print(f"📁 File Size: {os.path.getsize(csv_file)} bytes")
        
    else:
        log_and_print(f"❌ API request failed: {response.status_code}")
        log_and_print(f"📄 Response content: {response.text[:200]}...")
        
except Exception as e:
    log_and_print(f"❌ Error collecting Citybus stops: {str(e)}")

# STEP 3: Collect Route-Stop Mappings (Sample Routes)
log_and_print("\n🚀 STEP 3: Collecting Route-Stop Mappings (Sample Routes)")
log_and_print("=" * 50)

# Test specific routes for stop mappings
test_routes = ["582", "581", "580", "1", "2", "3", "5", "6", "9", "10", "101", "102", "103", "104", "105"]
log_and_print(f"🔍 Testing routes: {', '.join(test_routes)}")

all_mappings = []

def citybus_bus_stop_info(stop_id):
    """Get Citybus stop information"""
    url = f"https://rt.data.gov.hk/v2/transport/citybus/stop/{stop_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json().get('data', {})
        return [data.get('name_tc', 'Unknown stop'), data.get('name_en', 'Unknown stop'), data.get('lat', 'Unknown stop'), data.get('long', 'Unknown stop')]
    except Exception as e:
        log_and_print(f"Failed to get Citybus stop {stop_id} name: {e}")
        return None

def citybus_stop_info(company_id, route, direction):
    """Get Citybus stop information for a route"""
    url = f"https://rt.data.gov.hk/v2/transport/citybus/route-stop/{company_id}/{route}/{direction}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        stops = sorted(data.get('data', []), key=lambda x: x.get('seq', 0))
        stops = [stop['stop'] for stop in stops]
        stops_name = {key: citybus_bus_stop_info(key) for key in stops}
        return stops, stops_name
    except Exception as e:
        log_and_print(f"Failed to get Citybus stop IDs: {e}")
        return None, None

for route in test_routes:
    log_and_print(f"\n🔍 Processing Citybus route: {route}")
    
    # Try Citybus
    try:
        for direction in ["inbound", "outbound"]:
            log_and_print(f"   🚌 Testing {direction}...")
            stops, stops_name = citybus_stop_info("CTB", route, direction)
            if stops and stops_name:
                log_and_print(f"   ✅ Found {len(stops)} stops for {route} {direction}")
                for i, stop_id in enumerate(stops):
                    stop_info = stops_name.get(stop_id, ['Unknown', 'Unknown', '0', '0'])
                    all_mappings.append({
                        'route': route,
                        'operator': 'Citybus',
                        'direction': direction,
                        'service_type': 'N/A',
                        'stop_id': stop_id,
                        'stop_name_tc': stop_info[0],
                        'stop_name_en': stop_info[1],
                        'lat': stop_info[2],
                        'long': stop_info[3],
                        'sequence': i + 1
                    })
                break
        log_and_print(f"   ✅ Citybus route {route} processed")
    except Exception as e:
        log_and_print(f"   ❌ Citybus route {route} failed: {str(e)}")

# Save route-stop mappings
if all_mappings:
    csv_file = f"data/collected_data/citybus_route_stop_mappings_{timestamp}.csv"
    log_and_print(f"\n📊 Creating route-stop mappings CSV: {csv_file}")
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['route', 'operator', 'direction', 'service_type', 'stop_id', 'stop_name_tc', 'stop_name_en', 'lat', 'long', 'sequence'])
        
        for mapping in all_mappings:
            writer.writerow([
                mapping['route'],
                mapping['operator'],
                mapping['direction'],
                mapping['service_type'],
                mapping['stop_id'],
                mapping['stop_name_tc'],
                mapping['stop_name_en'],
                mapping['lat'],
                mapping['long'],
                mapping['sequence']
            ])
    
    log_and_print(f"✅ Route-stop mappings saved: {csv_file}")
    log_and_print(f"📊 Total mappings: {len(all_mappings)}")
    
    # Show summary by route
    route_summary = {}
    for mapping in all_mappings:
        route = mapping['route']
        if route not in route_summary:
            route_summary[route] = 0
        route_summary[route] += 1
    
    log_and_print("\n📋 Route Summary:")
    for route, count in route_summary.items():
        log_and_print(f"   {route}: {count} stop mappings")

# Final Summary
log_and_print("\n" + "=" * 80)
log_and_print("🎉 CITYBUS DATA COLLECTION COMPLETED!")
log_and_print("=" * 80)

# List all created files
log_and_print("📁 Created Files:")
for file in os.listdir("data/collected_data"):
    if file.endswith(f"_{timestamp}.csv") or file.endswith(f"_{timestamp}.json"):
        file_path = f"data/collected_data/{file}"
        file_size = os.path.getsize(file_path)
        log_and_print(f"   📄 {file} ({file_size} bytes)")

log_and_print(f"\n📁 Log file: {log_file}")
log_and_print("📊 Check data/collected_data/ for all CSV files")
log_and_print("=" * 80)

print("\n" + "=" * 80)
print("🎉 CITYBUS DATA COLLECTION COMPLETED!")
print("=" * 80)
print(f"📁 Log file: {log_file}")
print("📊 Check data/collected_data/ for all CSV files")
print("=" * 80)
