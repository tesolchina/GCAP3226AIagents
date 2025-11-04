#!/usr/bin/env python3
"""
Complete Data Collection Pipeline
Script to collect all KMB and Citybus data
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

print("🚌 COMPLETE DATA COLLECTION PIPELINE")
print("=" * 80)
print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

# Create directories
os.makedirs("data/collected_data", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"complete_data_collection_log_{timestamp}.txt"

# Initialize log file
with open(log_file, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("🚌 COMPLETE DATA COLLECTION LOG\n")
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

# STEP 1: KMB Routes
log_and_print("🚀 STEP 1: Collecting KMB Routes")
log_and_print("=" * 50)

try:
    log_and_print("📡 Making KMB routes API request...")
    start_time = time.time()
    
    response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=30)
    
    request_time = time.time() - start_time
    log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds")
    log_and_print(f"📊 Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        routes = data.get('data', [])
        log_and_print(f"✅ Found {len(routes)} KMB routes")
        
        # Save KMB routes
        csv_file = f"data/collected_data/kmb_all_routes_{timestamp}.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['route', 'bound', 'service_type', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp'])
            for route in routes:
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
        
        log_and_print(f"✅ KMB routes saved: {csv_file}")
        log_and_print(f"📁 File size: {os.path.getsize(csv_file)} bytes")
    else:
        log_and_print(f"❌ KMB routes API failed: {response.status_code}")
        
except Exception as e:
    log_and_print(f"❌ Error collecting KMB routes: {str(e)}")

# STEP 2: KMB Stops
log_and_print("\n🚀 STEP 2: Collecting KMB Stops")
log_and_print("=" * 50)

try:
    log_and_print("📡 Making KMB stops API request...")
    start_time = time.time()
    
    response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop", timeout=30)
    
    request_time = time.time() - start_time
    log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds")
    log_and_print(f"📊 Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        stops = data.get('data', [])
        log_and_print(f"✅ Found {len(stops)} KMB stops")
        
        # Save KMB stops
        csv_file = f"data/collected_data/kmb_all_stops_{timestamp}.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['stop', 'name_en', 'name_tc', 'name_sc', 'lat', 'long', 'data_timestamp'])
            for stop in stops:
                writer.writerow([
                    stop.get('stop', ''),
                    stop.get('name_en', ''),
                    stop.get('name_tc', ''),
                    stop.get('name_sc', ''),
                    stop.get('lat', ''),
                    stop.get('long', ''),
                    stop.get('data_timestamp', '')
                ])
        
        log_and_print(f"✅ KMB stops saved: {csv_file}")
        log_and_print(f"📁 File size: {os.path.getsize(csv_file)} bytes")
    else:
        log_and_print(f"❌ KMB stops API failed: {response.status_code}")
        
except Exception as e:
    log_and_print(f"❌ Error collecting KMB stops: {str(e)}")

# STEP 3: Citybus Routes
log_and_print("\n🚀 STEP 3: Collecting Citybus Routes")
log_and_print("=" * 50)

try:
    log_and_print("📡 Making Citybus routes API request...")
    start_time = time.time()
    
    response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/route/ctb", timeout=30)
    
    request_time = time.time() - start_time
    log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds")
    log_and_print(f"📊 Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        routes = data.get('data', [])
        log_and_print(f"✅ Found {len(routes)} Citybus routes")
        
        # Save Citybus routes
        csv_file = f"data/collected_data/citybus_all_routes_{timestamp}.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['route', 'bound', 'service_type', 'orig_tc', 'orig_en', 'dest_tc', 'dest_en', 'data_timestamp'])
            for route in routes:
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
        
        log_and_print(f"✅ Citybus routes saved: {csv_file}")
        log_and_print(f"📁 File size: {os.path.getsize(csv_file)} bytes")
    else:
        log_and_print(f"❌ Citybus routes API failed: {response.status_code}")
        
except Exception as e:
    log_and_print(f"❌ Error collecting Citybus routes: {str(e)}")

# STEP 4: Route-Stop Mappings (Sample)
log_and_print("\n🚀 STEP 4: Collecting Route-Stop Mappings (Sample)")
log_and_print("=" * 50)

# Test specific routes for stop mappings
test_routes = ["272A", "272K", "582", "581", "1", "2", "3", "5", "6", "9"]
log_and_print(f"🔍 Testing routes: {', '.join(test_routes)}")

all_mappings = []

for route in test_routes:
    log_and_print(f"\n🔍 Processing route: {route}")
    
    # Try KMB
    try:
        for direction in ["inbound", "outbound"]:
            for service_type in range(1, 5):
                url = f"https://data.etabus.gov.hk/v1/transport/kmb/route-stop/{route}/{direction}/{service_type}"
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    stops = data.get('data', [])
                    if stops:
                        log_and_print(f"   ✅ Found {len(stops)} stops for KMB {route} {direction} service type {service_type}")
                        for i, stop in enumerate(stops):
                            all_mappings.append({
                                'route': route,
                                'operator': 'KMB',
                                'direction': direction,
                                'service_type': service_type,
                                'stop_id': stop.get('stop', ''),
                                'sequence': i + 1
                            })
                        break
    except Exception as e:
        log_and_print(f"   ❌ KMB route {route} failed: {str(e)}")
    
    # Try Citybus
    try:
        for direction in ["inbound", "outbound"]:
            url = f"https://rt.data.gov.hk/v2/transport/citybus/route-stop/CTB/{route}/{direction}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                stops = sorted(data.get('data', []), key=lambda x: x.get('seq', 0))
                if stops:
                    log_and_print(f"   ✅ Found {len(stops)} stops for Citybus {route} {direction}")
                    for i, stop in enumerate(stops):
                        all_mappings.append({
                            'route': route,
                            'operator': 'Citybus',
                            'direction': direction,
                            'service_type': 'N/A',
                            'stop_id': stop.get('stop', ''),
                            'sequence': i + 1
                        })
                    break
    except Exception as e:
        log_and_print(f"   ❌ Citybus route {route} failed: {str(e)}")

# Save route-stop mappings
if all_mappings:
    csv_file = f"data/collected_data/route_stop_mappings_{timestamp}.csv"
    log_and_print(f"\n📊 Creating route-stop mappings CSV: {csv_file}")
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['route', 'operator', 'direction', 'service_type', 'stop_id', 'sequence'])
        
        for mapping in all_mappings:
            writer.writerow([
                mapping['route'],
                mapping['operator'],
                mapping['direction'],
                mapping['service_type'],
                mapping['stop_id'],
                mapping['sequence']
            ])
    
    log_and_print(f"✅ Route-stop mappings saved: {csv_file}")
    log_and_print(f"📊 Total mappings: {len(all_mappings)}")

# Final Summary
log_and_print("\n" + "=" * 80)
log_and_print("🎉 COMPLETE DATA COLLECTION FINISHED!")
log_and_print("=" * 80)

# List all created files
log_and_print("📁 Created Files:")
for file in os.listdir("data/collected_data"):
    if file.endswith(f"_{timestamp}.csv"):
        file_path = f"data/collected_data/{file}"
        file_size = os.path.getsize(file_path)
        log_and_print(f"   📄 {file} ({file_size} bytes)")

log_and_print(f"\n📁 Log file: {log_file}")
log_and_print("📊 Check data/collected_data/ for all CSV files")
log_and_print("=" * 80)

print("\n" + "=" * 80)
print("🎉 COMPLETE DATA COLLECTION FINISHED!")
print("=" * 80)
print(f"📁 Log file: {log_file}")
print("📊 Check data/collected_data/ for all CSV files")
print("=" * 80)
