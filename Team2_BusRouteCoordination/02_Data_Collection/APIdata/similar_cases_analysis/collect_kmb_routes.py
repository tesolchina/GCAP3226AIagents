#!/usr/bin/env python3
"""
Collect KMB Routes Data
Access KMB API and create CSV file with all routes
"""

import requests
import json
import csv
from datetime import datetime
import time
import os

def collect_kmb_routes():
    """Collect all KMB routes from API"""
    print("🚌 Collecting KMB Routes Data")
    print("=" * 50)
    print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Create data directory
    os.makedirs("data/collected_data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        print("🔍 Accessing KMB Routes API...")
        print("   URL: https://data.etabus.gov.hk/v1/transport/kmb/route")
        
        # Make API request
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=30)
        
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ API request successful!")
            
            # Parse JSON response
            data = response.json()
            routes = data.get('data', [])
            
            print(f"   📊 Found {len(routes)} KMB routes")
            
            # Save raw JSON data
            json_file = f"data/collected_data/kmb_routes_{timestamp}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"   💾 Raw data saved: {json_file}")
            
            # Create CSV file
            csv_file = f"data/collected_data/kmb_routes_{timestamp}.csv"
            print(f"   📊 Creating CSV file: {csv_file}")
            
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
            
            print(f"   ✅ CSV file created: {csv_file}")
            print(f"   📊 Total routes: {len(routes)}")
            
            # Show sample data
            if routes:
                print("\n📋 Sample Route Data:")
                sample = routes[0]
                print(f"   Route: {sample.get('route', 'N/A')}")
                print(f"   Origin: {sample.get('orig_en', 'N/A')}")
                print(f"   Destination: {sample.get('dest_en', 'N/A')}")
                print(f"   Bound: {sample.get('bound', 'N/A')}")
            
            return {
                'success': True,
                'routes_count': len(routes),
                'json_file': json_file,
                'csv_file': csv_file,
                'routes': routes
            }
            
        else:
            print(f"   ❌ API request failed: {response.status_code}")
            print(f"   Response: {response.text[:200]}...")
            return {
                'success': False,
                'error': f"API request failed: {response.status_code}",
                'routes_count': 0
            }
            
    except Exception as e:
        print(f"   ❌ Error collecting KMB routes: {str(e)}")
        return {
            'success': False,
            'error': str(e),
            'routes_count': 0
        }

def main():
    """Main function"""
    print("🚌 KMB Routes Data Collection")
    print("=" * 60)
    
    # Collect KMB routes
    result = collect_kmb_routes()
    
    # Summary
    print("\n📊 COLLECTION SUMMARY")
    print("=" * 50)
    
    if result['success']:
        print(f"✅ Status: SUCCESS")
        print(f"📊 Routes Collected: {result['routes_count']}")
        print(f"💾 JSON File: {result['json_file']}")
        print(f"📊 CSV File: {result['csv_file']}")
        print(f"⏱️  Collection Time: {datetime.now().strftime('%H:%M:%S')}")
    else:
        print(f"❌ Status: FAILED")
        print(f"❌ Error: {result['error']}")
        print(f"📊 Routes Collected: {result['routes_count']}")
    
    print("=" * 50)
    print("🎉 KMB Routes collection completed!")
    
    return result

if __name__ == "__main__":
    result = main()
