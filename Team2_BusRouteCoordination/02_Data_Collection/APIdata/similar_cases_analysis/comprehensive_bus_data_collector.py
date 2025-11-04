#!/usr/bin/env python3
"""
Comprehensive Bus Data Collector
Collects data from both KMB and Citybus APIs
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

print("🚌 COMPREHENSIVE BUS DATA COLLECTOR")
print("=" * 80)
print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("🚌 Collecting KMB + Citybus data")
print("=" * 80)

# Create directories
os.makedirs("data/collected_data", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"comprehensive_bus_collection_log_{timestamp}.txt"

# Initialize log file
with open(log_file, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("🚌 COMPREHENSIVE BUS DATA COLLECTION LOG\n")
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

# KMB API Configuration
KMB_BASE_URL = "https://data.etabus.gov.hk/v1/transport/kmb"

# Citybus API Configuration
CITYBUS_BASE_URL = "https://rt.data.gov.hk/v2/transport/citybus"
CITYBUS_COMPANY_ID = "CTB"

def collect_kmb_data():
    """Collect KMB data"""
    log_and_print("🚌 COLLECTING KMB DATA")
    log_and_print("=" * 50)
    
    # KMB Routes
    log_and_print("📡 Getting KMB routes...")
    try:
        response = requests.get(f"{KMB_BASE_URL}/route", timeout=30)
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            log_and_print(f"✅ Found {len(routes)} KMB routes")
            
            # Save KMB routes
            csv_file = f"data/collected_data/kmb_routes_{timestamp}.csv"
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
        else:
            log_and_print(f"❌ KMB routes failed: {response.status_code}")
    except Exception as e:
        log_and_print(f"❌ Error getting KMB routes: {str(e)}")
    
    # KMB Stops
    log_and_print("📡 Getting KMB stops...")
    try:
        response = requests.get(f"{KMB_BASE_URL}/stop", timeout=30)
        if response.status_code == 200:
            data = response.json()
            stops = data.get('data', [])
            log_and_print(f"✅ Found {len(stops)} KMB stops")
            
            # Save KMB stops
            csv_file = f"data/collected_data/kmb_stops_{timestamp}.csv"
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
        else:
            log_and_print(f"❌ KMB stops failed: {response.status_code}")
    except Exception as e:
        log_and_print(f"❌ Error getting KMB stops: {str(e)}")

def collect_citybus_data():
    """Collect Citybus data"""
    log_and_print("\n🚌 COLLECTING CITYBUS DATA")
    log_and_print("=" * 50)
    
    # Citybus Routes
    log_and_print("📡 Getting Citybus routes...")
    try:
        response = requests.get(f"{CITYBUS_BASE_URL}/route/{CITYBUS_COMPANY_ID}", timeout=30)
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            log_and_print(f"✅ Found {len(routes)} Citybus routes")
            
            # Save Citybus routes
            csv_file = f"data/collected_data/citybus_routes_{timestamp}.csv"
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['co', 'route', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp'])
                for route in routes:
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
            log_and_print(f"✅ Citybus routes saved: {csv_file}")
        else:
            log_and_print(f"❌ Citybus routes failed: {response.status_code}")
    except Exception as e:
        log_and_print(f"❌ Error getting Citybus routes: {str(e)}")

def collect_route_stop_mappings():
    """Collect route-stop mappings for sample routes"""
    log_and_print("\n🚌 COLLECTING ROUTE-STOP MAPPINGS")
    log_and_print("=" * 50)
    
    # Test routes
    test_routes = ["272A", "272K", "582", "581", "580", "1", "2", "3", "5", "6", "9", "10", "101", "102", "103", "104", "105"]
    
    all_mappings = []
    
    for route in test_routes:
        log_and_print(f"🔍 Processing route: {route}")
        
        # Try KMB first
        try:
            for direction in ["inbound", "outbound"]:
                for service_type in range(1, 5):
                    url = f"{KMB_BASE_URL}/route-stop/{route}/{direction}/{service_type}"
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        data = response.json()
                        stops = data.get('data', [])
                        if stops:
                            log_and_print(f"   ✅ KMB {route} {direction} service type {service_type}: {len(stops)} stops")
                            for stop in stops:
                                all_mappings.append({
                                    'route': route,
                                    'operator': 'KMB',
                                    'direction': direction,
                                    'service_type': service_type,
                                    'stop_id': stop.get('stop', ''),
                                    'sequence': stop.get('seq', 0)
                                })
                            break
        except Exception as e:
            log_and_print(f"   ❌ KMB {route} failed: {str(e)}")
        
        # Try Citybus
        try:
            for direction in ["inbound", "outbound"]:
                url = f"{CITYBUS_BASE_URL}/route-stop/{CITYBUS_COMPANY_ID}/{route}/{direction}"
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    stops = data.get('data', [])
                    if stops:
                        log_and_print(f"   ✅ Citybus {route} {direction}: {len(stops)} stops")
                        for stop in stops:
                            all_mappings.append({
                                'route': route,
                                'operator': 'Citybus',
                                'direction': direction,
                                'service_type': 'N/A',
                                'stop_id': stop.get('stop', ''),
                                'sequence': stop.get('seq', 0)
                            })
                        break
        except Exception as e:
            log_and_print(f"   ❌ Citybus {route} failed: {str(e)}")
    
    # Save mappings
    if all_mappings:
        csv_file = f"data/collected_data/route_stop_mappings_{timestamp}.csv"
        log_and_print(f"\n📊 Creating mappings CSV: {csv_file}")
        
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
        
        log_and_print(f"✅ Mappings saved: {csv_file}")
        log_and_print(f"📊 Total mappings: {len(all_mappings)}")
    
    return all_mappings

def main():
    """Main collection function"""
    try:
        # Collect KMB data
        collect_kmb_data()
        
        # Collect Citybus data
        collect_citybus_data()
        
        # Collect route-stop mappings
        mappings = collect_route_stop_mappings()
        
        # Final summary
        log_and_print("\n" + "=" * 80)
        log_and_print("🎉 COMPREHENSIVE BUS DATA COLLECTION COMPLETED!")
        log_and_print("=" * 80)
        
        # List created files
        log_and_print("📁 Created Files:")
        for file in os.listdir("data/collected_data"):
            if file.endswith(f"_{timestamp}.csv"):
                file_path = f"data/collected_data/{file}"
                file_size = os.path.getsize(file_path)
                log_and_print(f"   📄 {file} ({file_size} bytes)")
        
        log_and_print(f"\n📁 Log file: {log_file}")
        log_and_print("📊 Check data/collected_data/ for all CSV files")
        log_and_print("=" * 80)
        
    except Exception as e:
        log_and_print(f"❌ Error during collection: {str(e)}")

if __name__ == "__main__":
    main()
