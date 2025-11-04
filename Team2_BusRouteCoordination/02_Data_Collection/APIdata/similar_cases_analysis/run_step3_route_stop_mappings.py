#!/usr/bin/env python3
"""
Step 3: Collect Route-Stop Mappings
Script to collect route-stop mappings for specific routes
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

print("🚌 STEP 3: ROUTE-STOP MAPPINGS COLLECTION")
print("=" * 50)
print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

# Create directories
os.makedirs("data/collected_data", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def kmb_stopid_info(stop_id):
    """Get KMB stop information"""
    url = f"https://data.etabus.gov.hk/v1/transport/kmb/stop/{stop_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json().get('data', {})
        return [data.get('name_tc', 'Unknown stop'), data.get('name_en', 'Unknown stop'), data.get('lat', 'Unknown stop'), data.get('long', 'Unknown stop')]
    except Exception as e:
        print(f"Failed to get KMB stop {stop_id} name: {e}")
        return None

def kmb_stop_info(direction, service_type, route):
    """Get KMB stop information for a route"""
    url = f"https://data.etabus.gov.hk/v1/transport/kmb/route-stop/{route}/{direction}/{service_type}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        stops = data.get('data', [])
        stops = [stop['stop'] for stop in stops]
        stops_name = {key: kmb_stopid_info(key) for key in stops}
        return stops, stops_name
    except Exception as e:
        print(f"Failed to get KMB stop IDs: {e}")
        return None, None

def citybus_bus_stop_info(stop_id):
    """Get Citybus stop information"""
    url = f"https://rt.data.gov.hk/v2/transport/citybus/stop/{stop_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json().get('data', {})
        return [data.get('name_tc', 'Unknown stop'), data.get('name_en', 'Unknown stop'), data.get('lat', 'Unknown stop'), data.get('long', 'Unknown stop')]
    except Exception as e:
        print(f"Failed to get Citybus stop {stop_id} name: {e}")
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
        print(f"Failed to get Citybus stop IDs: {e}")
        return None, None

# Test with specific routes
test_routes = ["272A", "272K", "582", "581", "1", "2", "3", "5", "6", "9"]
print(f"🔍 Testing routes: {', '.join(test_routes)}")

all_mappings = []

for route in test_routes:
    print(f"\n🔍 Processing route: {route}")
    
    # Try KMB first
    print(f"   🚌 Trying KMB route {route}...")
    try:
        for direction in ["inbound", "outbound"]:
            for service_type in range(1, 5):
                print(f"      Testing {direction} service type {service_type}...")
                stops, stops_name = kmb_stop_info(direction, service_type, route)
                if stops and stops_name:
                    print(f"      ✅ Found {len(stops)} stops for {route} {direction} service type {service_type}")
                    for i, stop_id in enumerate(stops):
                        stop_info = stops_name.get(stop_id, ['Unknown', 'Unknown', '0', '0'])
                        all_mappings.append({
                            'route': route,
                            'operator': 'KMB',
                            'direction': direction,
                            'service_type': service_type,
                            'stop_id': stop_id,
                            'stop_name_tc': stop_info[0],
                            'stop_name_en': stop_info[1],
                            'lat': stop_info[2],
                            'long': stop_info[3],
                            'sequence': i + 1
                        })
                    break
        print(f"   ✅ KMB route {route} processed")
    except Exception as e:
        print(f"   ❌ KMB route {route} failed: {str(e)}")
    
    # Try Citybus
    print(f"   🚌 Trying Citybus route {route}...")
    try:
        for direction in ["inbound", "outbound"]:
            print(f"      Testing {direction}...")
            stops, stops_name = citybus_stop_info("CTB", route, direction)
            if stops and stops_name:
                print(f"      ✅ Found {len(stops)} stops for {route} {direction}")
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
        print(f"   ✅ Citybus route {route} processed")
    except Exception as e:
        print(f"   ❌ Citybus route {route} failed: {str(e)}")

# Save to CSV
csv_file = f"data/collected_data/route_stop_mappings_{timestamp}.csv"
print(f"\n📊 Creating CSV file: {csv_file}")

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

print(f"✅ Route-stop mappings CSV created: {csv_file}")
print(f"📊 Total mappings: {len(all_mappings)}")

# Show summary by route
route_summary = {}
for mapping in all_mappings:
    route = mapping['route']
    if route not in route_summary:
        route_summary[route] = {'KMB': 0, 'Citybus': 0}
    route_summary[route][mapping['operator']] += 1

print("\n📋 Route Summary:")
for route, counts in route_summary.items():
    print(f"   {route}: KMB={counts['KMB']}, Citybus={counts['Citybus']}")

print("\n✅ STEP 3 COMPLETED: Route-Stop Mappings Collection")
print(f"📊 Total Mappings: {len(all_mappings)}")
print(f"📁 CSV File: {csv_file}")

print("\n" + "=" * 80)
print("🎉 STEP 3 COMPLETED!")
print("=" * 80)
print("📊 Route-stop mappings data collection completed")
print("📁 Check data/collected_data/ for CSV files")
print("=" * 80)
