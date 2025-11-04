#!/usr/bin/env python3
"""
Enhanced Citybus Data Collector
Based on official API specifications v2.01 (July 2023)
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

print("🚌 ENHANCED CITYBUS DATA COLLECTOR")
print("=" * 80)
print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("📚 Based on API Specifications v2.01 (July 2023)")
print("=" * 80)

# Create directories
os.makedirs("data/collected_data", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"enhanced_citybus_collection_log_{timestamp}.txt"

# Initialize log file
with open(log_file, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("🚌 ENHANCED CITYBUS DATA COLLECTION LOG\n")
    f.write("=" * 80 + "\n")
    f.write(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"📚 Based on API Specifications v2.01 (July 2023)\n")
    f.write(f"📁 Log File: {log_file}\n")
    f.write("=" * 80 + "\n\n")

def log_and_print(message):
    timestamp_str = datetime.now().strftime('%H:%M:%S')
    formatted_message = f"[{timestamp_str}] {message}"
    print(formatted_message)
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(formatted_message + "\n")

# API Configuration based on official specifications
BASE_URL = "https://rt.data.gov.hk/v2/transport/citybus"
COMPANY_ID = "CTB"

def get_citybus_company_info():
    """Get Citybus company information"""
    log_and_print("🚀 STEP 1: Getting Citybus Company Information")
    log_and_print("=" * 50)
    
    url = f"{BASE_URL}/company/{COMPANY_ID}"
    log_and_print(f"🔍 API Endpoint: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        log_and_print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            log_and_print("✅ Company information retrieved successfully")
            log_and_print(f"📋 Company: {data.get('data', {}).get('name_en', 'N/A')}")
            log_and_print(f"📋 Company TC: {data.get('data', {}).get('name_tc', 'N/A')}")
            return data
        else:
            log_and_print(f"❌ API request failed: {response.status_code}")
            log_and_print(f"📄 Response: {response.text[:200]}...")
            return None
    except Exception as e:
        log_and_print(f"❌ Error getting company info: {str(e)}")
        return None

def get_all_citybus_routes():
    """Get all Citybus routes"""
    log_and_print("\n🚀 STEP 2: Getting All Citybus Routes")
    log_and_print("=" * 50)
    
    url = f"{BASE_URL}/route/{COMPANY_ID}"
    log_and_print(f"🔍 API Endpoint: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        log_and_print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            log_and_print(f"✅ Found {len(routes)} Citybus routes")
            
            # Save raw JSON
            json_file = f"data/collected_data/citybus_routes_{timestamp}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            log_and_print(f"💾 Raw data saved: {json_file}")
            
            # Create CSV
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
            
            log_and_print(f"✅ CSV file created: {csv_file}")
            log_and_print(f"📁 File size: {os.path.getsize(csv_file)} bytes")
            
            return routes
        else:
            log_and_print(f"❌ API request failed: {response.status_code}")
            return None
    except Exception as e:
        log_and_print(f"❌ Error getting routes: {str(e)}")
        return None

def get_route_stops(route, direction):
    """Get stops for a specific route and direction"""
    url = f"{BASE_URL}/route-stop/{COMPANY_ID}/{route}/{direction}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', [])
        else:
            return None
    except Exception as e:
        log_and_print(f"❌ Error getting stops for {route} {direction}: {str(e)}")
        return None

def get_stop_info(stop_id):
    """Get detailed stop information"""
    url = f"{BASE_URL}/stop/{stop_id}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {})
        else:
            return None
    except Exception as e:
        return None

def collect_route_stop_mappings(routes):
    """Collect route-stop mappings for all routes"""
    log_and_print("\n🚀 STEP 3: Collecting Route-Stop Mappings")
    log_and_print("=" * 50)
    
    all_mappings = []
    all_stops = set()
    
    # Test with sample routes first
    test_routes = ["582", "581", "580", "1", "2", "3", "5", "6", "9", "10", "101", "102", "103", "104", "105"]
    
    log_and_print(f"🔍 Testing {len(test_routes)} sample routes")
    
    for route in test_routes:
        log_and_print(f"\n🔍 Processing route: {route}")
        
        for direction in ["inbound", "outbound"]:
            log_and_print(f"   🚌 Testing {direction}...")
            stops = get_route_stops(route, direction)
            
            if stops:
                log_and_print(f"   ✅ Found {len(stops)} stops for {route} {direction}")
                
                for stop in stops:
                    stop_id = stop.get('stop', '')
                    all_stops.add(stop_id)
                    
                    all_mappings.append({
                        'route': route,
                        'direction': direction,
                        'stop_id': stop_id,
                        'sequence': stop.get('seq', 0),
                        'company': stop.get('co', 'CTB')
                    })
            else:
                log_and_print(f"   ❌ No stops found for {route} {direction}")
    
    # Save route-stop mappings
    if all_mappings:
        csv_file = f"data/collected_data/citybus_route_stops_{timestamp}.csv"
        log_and_print(f"\n📊 Creating route-stop mappings CSV: {csv_file}")
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['route', 'direction', 'stop_id', 'sequence', 'company'])
            
            for mapping in all_mappings:
                writer.writerow([
                    mapping['route'],
                    mapping['direction'],
                    mapping['stop_id'],
                    mapping['sequence'],
                    mapping['company']
                ])
        
        log_and_print(f"✅ Route-stop mappings saved: {csv_file}")
        log_and_print(f"📊 Total mappings: {len(all_mappings)}")
        log_and_print(f"📊 Unique stops: {len(all_stops)}")
    
    return all_mappings, all_stops

def collect_stop_details(stop_ids):
    """Collect detailed stop information"""
    log_and_print("\n🚀 STEP 4: Collecting Stop Details")
    log_and_print("=" * 50)
    
    log_and_print(f"🔍 Collecting details for {len(stop_ids)} stops")
    
    all_stops = []
    processed = 0
    
    for stop_id in list(stop_ids)[:100]:  # Limit to first 100 stops for testing
        log_and_print(f"   📍 Processing stop {stop_id}...")
        
        stop_info = get_stop_info(stop_id)
        if stop_info:
            all_stops.append({
                'stop_id': stop_id,
                'name_en': stop_info.get('name_en', ''),
                'name_tc': stop_info.get('name_tc', ''),
                'name_sc': stop_info.get('name_sc', ''),
                'lat': stop_info.get('lat', ''),
                'long': stop_info.get('long', ''),
                'data_timestamp': stop_info.get('data_timestamp', '')
            })
            processed += 1
            
            if processed % 10 == 0:
                log_and_print(f"   📊 Processed {processed} stops...")
        else:
            log_and_print(f"   ❌ Failed to get info for stop {stop_id}")
    
    # Save stop details
    if all_stops:
        csv_file = f"data/collected_data/citybus_stops_{timestamp}.csv"
        log_and_print(f"\n📊 Creating stops CSV: {csv_file}")
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['stop_id', 'name_en', 'name_tc', 'name_sc', 'lat', 'long', 'data_timestamp'])
            
            for stop in all_stops:
                writer.writerow([
                    stop['stop_id'],
                    stop['name_en'],
                    stop['name_tc'],
                    stop['name_sc'],
                    stop['lat'],
                    stop['long'],
                    stop['data_timestamp']
                ])
        
        log_and_print(f"✅ Stops CSV created: {csv_file}")
        log_and_print(f"📊 Total stops: {len(all_stops)}")
    
    return all_stops

def main():
    """Main collection function"""
    try:
        # Step 1: Company info
        company_info = get_citybus_company_info()
        
        # Step 2: All routes
        routes = get_all_citybus_routes()
        
        if routes:
            # Step 3: Route-stop mappings
            mappings, stop_ids = collect_route_stop_mappings(routes)
            
            # Step 4: Stop details
            if stop_ids:
                stops = collect_stop_details(stop_ids)
            
            # Final summary
            log_and_print("\n" + "=" * 80)
            log_and_print("🎉 ENHANCED CITYBUS DATA COLLECTION COMPLETED!")
            log_and_print("=" * 80)
            
            # List created files
            log_and_print("📁 Created Files:")
            for file in os.listdir("data/collected_data"):
                if file.endswith(f"_{timestamp}.csv") or file.endswith(f"_{timestamp}.json"):
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
