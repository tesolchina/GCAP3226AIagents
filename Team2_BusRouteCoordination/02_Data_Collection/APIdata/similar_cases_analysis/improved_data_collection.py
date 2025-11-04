#!/usr/bin/env python3
"""
Improved Data Collection Script
Based on existing API.ipynb code with comprehensive logging
"""

import requests
import json
import csv
from datetime import datetime
import time
import os
import pandas as pd

# API Configuration
kmb_base_url = "https://data.etabus.gov.hk/v1/transport/kmb"
citybus_base_url = "https://rt.data.gov.hk/v2/transport/citybus"

def log_and_print(message, log_file):
    """Log message to file and print to terminal"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    formatted_message = f"[{timestamp}] {message}"
    print(formatted_message)
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(formatted_message + "\n")

def kmb_route_info(direction, service_type, route):
    """Get KMB route information"""
    url = f"{kmb_base_url}/route/{route}/{direction}/{service_type}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json().get('data', "Unknown route")
    except Exception as e:
        print(f"Failed to get KMB route information: {e}")
        return None

def kmb_stopid_info(stop_id):
    """Get KMB stop information"""
    url = f"{kmb_base_url}/stop/{stop_id}"
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
    url = f"{kmb_base_url}/route-stop/{route}/{direction}/{service_type}"
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

def citybus_route_info(company_id, route):
    """Get Citybus route information"""
    url = f"{citybus_base_url}/route/{company_id}/{route}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json().get('data', "Unknown route")
    except Exception as e:
        print(f"Failed to get Citybus route information: {e}")
        return None

def citybus_bus_stop_info(stop_id):
    """Get Citybus stop information"""
    url = f"{citybus_base_url}/stop/{stop_id}"
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
    url = f"{citybus_base_url}/route-stop/{company_id}/{route}/{direction}"
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

def collect_all_kmb_routes():
    """Collect all KMB routes"""
    print("🚌 Collecting All KMB Routes")
    print("=" * 50)
    
    try:
        # Get all routes
        url = f"{kmb_base_url}/route"
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            print(f"✅ Found {len(routes)} KMB routes")
            
            # Save to CSV
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
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
            
            print(f"📊 CSV file created: {csv_file}")
            return routes, csv_file
        else:
            print(f"❌ API request failed: {response.status_code}")
            return None, None
            
    except Exception as e:
        print(f"❌ Error collecting KMB routes: {str(e)}")
        return None, None

def collect_all_kmb_stops():
    """Collect all KMB stops"""
    print("🚌 Collecting All KMB Stops")
    print("=" * 50)
    
    try:
        # Get all stops
        url = f"{kmb_base_url}/stop"
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            stops = data.get('data', [])
            print(f"✅ Found {len(stops)} KMB stops")
            
            # Save to CSV
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
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
            
            print(f"📊 CSV file created: {csv_file}")
            return stops, csv_file
        else:
            print(f"❌ API request failed: {response.status_code}")
            return None, None
            
    except Exception as e:
        print(f"❌ Error collecting KMB stops: {str(e)}")
        return None, None

def collect_all_citybus_routes():
    """Collect all Citybus routes"""
    print("🚌 Collecting All Citybus Routes")
    print("=" * 50)
    
    try:
        # Get all routes
        url = f"{citybus_base_url}/route/ctb"
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            print(f"✅ Found {len(routes)} Citybus routes")
            
            # Save to CSV
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            csv_file = f"data/collected_data/citybus_all_routes_{timestamp}.csv"
            
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
            
            print(f"📊 CSV file created: {csv_file}")
            return routes, csv_file
        else:
            print(f"❌ API request failed: {response.status_code}")
            return None, None
            
    except Exception as e:
        print(f"❌ Error collecting Citybus routes: {str(e)}")
        return None, None

def collect_route_stop_mappings():
    """Collect route-stop mappings for specific routes"""
    print("🚌 Collecting Route-Stop Mappings")
    print("=" * 50)
    
    # Test with specific routes
    test_routes = ["272A", "272K", "582", "581"]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = f"data/collected_data/route_stop_mappings_{timestamp}.csv"
    
    all_mappings = []
    
    for route in test_routes:
        print(f"🔍 Processing route: {route}")
        
        # Try KMB first
        try:
            for direction in ["inbound", "outbound"]:
                for service_type in range(1, 5):
                    stops, stops_name = kmb_stop_info(direction, service_type, route)
                    if stops and stops_name:
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
                        print(f"   ✅ Found {len(stops)} stops for {route} {direction} service type {service_type}")
                        break
        except:
            pass
        
        # Try Citybus
        try:
            for direction in ["inbound", "outbound"]:
                stops, stops_name = citybus_stop_info("CTB", route, direction)
                if stops and stops_name:
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
                    print(f"   ✅ Found {len(stops)} stops for {route} {direction}")
                    break
        except:
            pass
    
    # Save to CSV
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
    
    print(f"📊 Route-stop mappings CSV created: {csv_file}")
    print(f"📊 Total mappings: {len(all_mappings)}")
    return all_mappings, csv_file

def main():
    """Main data collection function"""
    print("🚌 IMPROVED DATA COLLECTION WITH EXISTING API CODE")
    print("=" * 80)
    print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Create directories
    os.makedirs("data/collected_data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"improved_data_collection_log_{timestamp}.txt"
    
    # Initialize log file
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("🚌 IMPROVED DATA COLLECTION LOG\n")
        f.write("=" * 80 + "\n")
        f.write(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"📁 Log File: {log_file}\n")
        f.write("=" * 80 + "\n\n")
    
    results = {}
    
    # Step 1: Collect all KMB routes
    log_and_print("🚀 STEP 1: Collecting All KMB Routes", log_file)
    kmb_routes, kmb_routes_csv = collect_all_kmb_routes()
    if kmb_routes:
        log_and_print(f"✅ KMB Routes: {len(kmb_routes)} routes", log_file)
        log_and_print(f"📁 CSV File: {kmb_routes_csv}", log_file)
        results['kmb_routes'] = {'count': len(kmb_routes), 'csv': kmb_routes_csv}
    else:
        log_and_print("❌ KMB Routes collection failed", log_file)
        results['kmb_routes'] = {'count': 0, 'csv': None}
    
    # Wait between requests
    log_and_print("⏱️  Waiting 5 seconds before next request...", log_file)
    time.sleep(5)
    
    # Step 2: Collect all KMB stops
    log_and_print("🚀 STEP 2: Collecting All KMB Stops", log_file)
    kmb_stops, kmb_stops_csv = collect_all_kmb_stops()
    if kmb_stops:
        log_and_print(f"✅ KMB Stops: {len(kmb_stops)} stops", log_file)
        log_and_print(f"📁 CSV File: {kmb_stops_csv}", log_file)
        results['kmb_stops'] = {'count': len(kmb_stops), 'csv': kmb_stops_csv}
    else:
        log_and_print("❌ KMB Stops collection failed", log_file)
        results['kmb_stops'] = {'count': 0, 'csv': None}
    
    # Wait between requests
    log_and_print("⏱️  Waiting 5 seconds before next request...", log_file)
    time.sleep(5)
    
    # Step 3: Collect all Citybus routes
    log_and_print("🚀 STEP 3: Collecting All Citybus Routes", log_file)
    citybus_routes, citybus_routes_csv = collect_all_citybus_routes()
    if citybus_routes:
        log_and_print(f"✅ Citybus Routes: {len(citybus_routes)} routes", log_file)
        log_and_print(f"📁 CSV File: {citybus_routes_csv}", log_file)
        results['citybus_routes'] = {'count': len(citybus_routes), 'csv': citybus_routes_csv}
    else:
        log_and_print("❌ Citybus Routes collection failed", log_file)
        results['citybus_routes'] = {'count': 0, 'csv': None}
    
    # Wait between requests
    log_and_print("⏱️  Waiting 5 seconds before next request...", log_file)
    time.sleep(5)
    
    # Step 4: Collect route-stop mappings
    log_and_print("🚀 STEP 4: Collecting Route-Stop Mappings", log_file)
    mappings, mappings_csv = collect_route_stop_mappings()
    if mappings:
        log_and_print(f"✅ Route-Stop Mappings: {len(mappings)} mappings", log_file)
        log_and_print(f"📁 CSV File: {mappings_csv}", log_file)
        results['mappings'] = {'count': len(mappings), 'csv': mappings_csv}
    else:
        log_and_print("❌ Route-Stop Mappings collection failed", log_file)
        results['mappings'] = {'count': 0, 'csv': None}
    
    # Final summary
    log_and_print("\\n📊 COLLECTION SUMMARY", log_file)
    log_and_print("=" * 80, log_file)
    
    log_and_print(f"📊 KMB Routes: {results['kmb_routes']['count']} routes", log_file)
    log_and_print(f"📊 KMB Stops: {results['kmb_stops']['count']} stops", log_file)
    log_and_print(f"📊 Citybus Routes: {results['citybus_routes']['count']} routes", log_file)
    log_and_print(f"📊 Route-Stop Mappings: {results['mappings']['count']} mappings", log_file)
    
    log_and_print("\\n🎉 IMPROVED DATA COLLECTION COMPLETED!", log_file)
    log_and_print(f"📁 All logs saved to: {log_file}", log_file)
    log_and_print("📊 Check data/collected_data/ for CSV files", log_file)
    
    print("\\n" + "=" * 80)
    print("🎉 IMPROVED DATA COLLECTION COMPLETED!")
    print("=" * 80)
    print(f"📁 Log file: {log_file}")
    print("📊 Check the log file for detailed results")
    print("📁 Check data/collected_data/ for CSV files")
    print("=" * 80)
    
    return results

if __name__ == "__main__":
    results = main()
