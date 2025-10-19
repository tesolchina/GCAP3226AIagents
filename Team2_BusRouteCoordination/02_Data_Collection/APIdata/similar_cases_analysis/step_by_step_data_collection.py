#!/usr/bin/env python3
"""
Step-by-Step Data Collection
Collect API data one at a time with detailed logging
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

def log_message(message):
    """Log message with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

def collect_kmb_routes():
    """Step 1: Collect KMB routes"""
    log_message("🚌 STEP 1: Collecting KMB Routes")
    log_message("=" * 60)
    
    # Create data directory
    os.makedirs("data/collected_data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        log_message("🔍 Accessing KMB Routes API...")
        log_message("   URL: https://data.etabus.gov.hk/v1/transport/kmb/route")
        
        # Make API request
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=30)
        
        log_message(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            log_message("   ✅ API request successful!")
            
            # Parse JSON response
            data = response.json()
            routes = data.get('data', [])
            
            log_message(f"   📊 Found {len(routes)} KMB routes")
            
            # Save raw JSON data
            json_file = f"data/collected_data/kmb_routes_{timestamp}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            log_message(f"   💾 Raw data saved: {json_file}")
            
            # Create CSV file
            csv_file = f"data/collected_data/kmb_routes_{timestamp}.csv"
            log_message(f"   📊 Creating CSV file: {csv_file}")
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow([
                    'route', 'bound', 'service_type', 'orig_en', 'orig_tc', 'orig_sc',
                    'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp'
                ])
                
                # Write data
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
            
            log_message(f"   ✅ CSV file created: {csv_file}")
            log_message(f"   📊 Total routes: {len(routes)}")
            
            # Show sample data
            if routes:
                log_message("\\n📋 Sample Route Data:")
                sample = routes[0]
                log_message(f"   Route: {sample.get('route', 'N/A')}")
                log_message(f"   Origin: {sample.get('orig_en', 'N/A')}")
                log_message(f"   Destination: {sample.get('dest_en', 'N/A')}")
                log_message(f"   Bound: {sample.get('bound', 'N/A')}")
            
            return {
                'success': True,
                'routes_count': len(routes),
                'json_file': json_file,
                'csv_file': csv_file
            }
            
        else:
            log_message(f"   ❌ API request failed: {response.status_code}")
            return {'success': False, 'error': f"API request failed: {response.status_code}"}
            
    except Exception as e:
        log_message(f"   ❌ Error collecting KMB routes: {str(e)}")
        return {'success': False, 'error': str(e)}

def collect_kmb_stops():
    """Step 2: Collect KMB stops"""
    log_message("🚌 STEP 2: Collecting KMB Stops")
    log_message("=" * 60)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        log_message("🔍 Accessing KMB Stops API...")
        log_message("   URL: https://data.etabus.gov.hk/v1/transport/kmb/stop")
        
        # Make API request
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop", timeout=30)
        
        log_message(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            log_message("   ✅ API request successful!")
            
            # Parse JSON response
            data = response.json()
            stops = data.get('data', [])
            
            log_message(f"   📊 Found {len(stops)} KMB stops")
            
            # Save raw JSON data
            json_file = f"data/collected_data/kmb_stops_{timestamp}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            log_message(f"   💾 Raw data saved: {json_file}")
            
            # Create CSV file
            csv_file = f"data/collected_data/kmb_stops_{timestamp}.csv"
            log_message(f"   📊 Creating CSV file: {csv_file}")
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow(['stop', 'name_en', 'name_tc', 'name_sc', 'lat', 'long', 'data_timestamp'])
                
                # Write data
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
            
            log_message(f"   ✅ CSV file created: {csv_file}")
            log_message(f"   📊 Total stops: {len(stops)}")
            
            return {
                'success': True,
                'stops_count': len(stops),
                'json_file': json_file,
                'csv_file': csv_file
            }
            
        else:
            log_message(f"   ❌ API request failed: {response.status_code}")
            return {'success': False, 'error': f"API request failed: {response.status_code}"}
            
    except Exception as e:
        log_message(f"   ❌ Error collecting KMB stops: {str(e)}")
        return {'success': False, 'error': str(e)}

def collect_citybus_routes():
    """Step 3: Collect Citybus routes"""
    log_message("🚌 STEP 3: Collecting Citybus Routes")
    log_message("=" * 60)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        log_message("🔍 Accessing Citybus Routes API...")
        log_message("   URL: https://rt.data.gov.hk/v2/transport/citybus/route/ctb")
        
        # Make API request
        response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/route/ctb", timeout=30)
        
        log_message(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            log_message("   ✅ API request successful!")
            
            # Parse JSON response
            data = response.json()
            routes = data.get('data', [])
            
            log_message(f"   📊 Found {len(routes)} Citybus routes")
            
            # Save raw JSON data
            json_file = f"data/collected_data/citybus_routes_{timestamp}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            log_message(f"   💾 Raw data saved: {json_file}")
            
            # Create CSV file
            csv_file = f"data/collected_data/citybus_routes_{timestamp}.csv"
            log_message(f"   📊 Creating CSV file: {csv_file}")
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow(['co', 'route', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp'])
                
                # Write data
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
            
            log_message(f"   ✅ CSV file created: {csv_file}")
            log_message(f"   📊 Total routes: {len(routes)}")
            
            return {
                'success': True,
                'routes_count': len(routes),
                'json_file': json_file,
                'csv_file': csv_file
            }
            
        else:
            log_message(f"   ❌ API request failed: {response.status_code}")
            return {'success': False, 'error': f"API request failed: {response.status_code}"}
            
    except Exception as e:
        log_message(f"   ❌ Error collecting Citybus routes: {str(e)}")
        return {'success': False, 'error': str(e)}

def main():
    """Main function - run all data collection steps"""
    log_message("🚌 COMPREHENSIVE DATA COLLECTION")
    log_message("=" * 80)
    log_message(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_message("=" * 80)
    
    results = {}
    
    # Step 1: Collect KMB routes
    log_message("\\n🚀 Starting Step 1: KMB Routes Collection")
    kmb_routes_result = collect_kmb_routes()
    results['kmb_routes'] = kmb_routes_result
    
    if kmb_routes_result['success']:
        log_message("✅ Step 1 completed successfully!")
    else:
        log_message("❌ Step 1 failed!")
    
    # Wait between requests
    log_message("⏱️  Waiting 5 seconds before next request...")
    time.sleep(5)
    
    # Step 2: Collect KMB stops
    log_message("\\n🚀 Starting Step 2: KMB Stops Collection")
    kmb_stops_result = collect_kmb_stops()
    results['kmb_stops'] = kmb_stops_result
    
    if kmb_stops_result['success']:
        log_message("✅ Step 2 completed successfully!")
    else:
        log_message("❌ Step 2 failed!")
    
    # Wait between requests
    log_message("⏱️  Waiting 5 seconds before next request...")
    time.sleep(5)
    
    # Step 3: Collect Citybus routes
    log_message("\\n🚀 Starting Step 3: Citybus Routes Collection")
    citybus_routes_result = collect_citybus_routes()
    results['citybus_routes'] = citybus_routes_result
    
    if citybus_routes_result['success']:
        log_message("✅ Step 3 completed successfully!")
    else:
        log_message("❌ Step 3 failed!")
    
    # Final summary
    log_message("\\n📊 COLLECTION SUMMARY")
    log_message("=" * 80)
    
    if results['kmb_routes']['success']:
        log_message(f"✅ KMB Routes: {results['kmb_routes']['routes_count']} routes")
        log_message(f"   📊 CSV: {results['kmb_routes']['csv_file']}")
    else:
        log_message(f"❌ KMB Routes: Failed - {results['kmb_routes']['error']}")
    
    if results['kmb_stops']['success']:
        log_message(f"✅ KMB Stops: {results['kmb_stops']['stops_count']} stops")
        log_message(f"   📊 CSV: {results['kmb_stops']['csv_file']}")
    else:
        log_message(f"❌ KMB Stops: Failed - {results['kmb_stops']['error']}")
    
    if results['citybus_routes']['success']:
        log_message(f"✅ Citybus Routes: {results['citybus_routes']['routes_count']} routes")
        log_message(f"   📊 CSV: {results['citybus_routes']['csv_file']}")
    else:
        log_message(f"❌ Citybus Routes: Failed - {results['citybus_routes']['error']}")
    
    log_message("=" * 80)
    log_message("🎉 Data collection completed!")
    
    return results

if __name__ == "__main__":
    results = main()
