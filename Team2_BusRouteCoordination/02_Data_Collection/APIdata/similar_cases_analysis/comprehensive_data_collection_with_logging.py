#!/usr/bin/env python3
"""
Comprehensive Data Collection with Detailed Logging
Collect API data step by step with full terminal output and logging
"""

import requests
import json
import csv
from datetime import datetime
import time
import os
import sys

class DataCollector:
    def __init__(self):
        self.start_time = datetime.now()
        self.timestamp = self.start_time.strftime("%Y%m%d_%H%M%S")
        self.log_file = f"data_collection_log_{self.timestamp}.txt"
        self.results = {}
        
        # Create directories
        os.makedirs("data/collected_data", exist_ok=True)
        os.makedirs("logs", exist_ok=True)
        
        # Initialize log file
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("🚌 COMPREHENSIVE DATA COLLECTION LOG\n")
            f.write("=" * 80 + "\n")
            f.write(f"📅 Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"📁 Log File: {self.log_file}\n")
            f.write("=" * 80 + "\n\n")
    
    def log_and_print(self, message, level="INFO"):
        """Log message to file and print to terminal"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {level}: {message}"
        
        # Print to terminal
        print(formatted_message)
        
        # Log to file
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(formatted_message + "\n")
    
    def log_separator(self, title=""):
        """Log separator line"""
        separator = "=" * 60
        if title:
            separator = f"=== {title} ==="
        
        print(separator)
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(separator + "\n")
    
    def collect_kmb_routes(self):
        """Step 1: Collect KMB routes with detailed logging"""
        self.log_separator("STEP 1: KMB ROUTES COLLECTION")
        
        self.log_and_print("🚌 Starting KMB Routes Collection")
        self.log_and_print("=" * 50)
        self.log_and_print("🔍 API Details:")
        self.log_and_print("   URL: https://data.etabus.gov.hk/v1/transport/kmb/route")
        self.log_and_print("   Method: GET")
        self.log_and_print("   Timeout: 30 seconds")
        
        try:
            self.log_and_print("📡 Making API request...")
            start_time = time.time()
            
            response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=30)
            
            request_time = time.time() - start_time
            self.log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds")
            self.log_and_print(f"📊 Status Code: {response.status_code}")
            self.log_and_print(f"📏 Response Size: {len(response.content)} bytes")
            
            if response.status_code == 200:
                self.log_and_print("✅ API request successful!")
                
                # Parse JSON response
                self.log_and_print("🔍 Parsing JSON response...")
                data = response.json()
                routes = data.get('data', [])
                
                self.log_and_print(f"📊 Found {len(routes)} KMB routes")
                self.log_and_print(f"📋 Data structure: {list(data.keys())}")
                
                # Save raw JSON data
                json_file = f"data/collected_data/kmb_routes_{self.timestamp}.json"
                self.log_and_print(f"💾 Saving raw JSON data to: {json_file}")
                
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                self.log_and_print(f"✅ Raw data saved: {json_file}")
                self.log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes")
                
                # Create CSV file
                csv_file = f"data/collected_data/kmb_routes_{self.timestamp}.csv"
                self.log_and_print(f"📊 Creating CSV file: {csv_file}")
                self.log_and_print("📋 CSV Headers: route, bound, service_type, orig_en, orig_tc, orig_sc, dest_en, dest_tc, dest_sc, data_timestamp")
                
                with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    
                    # Write header
                    headers = ['route', 'bound', 'service_type', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp']
                    writer.writerow(headers)
                    
                    # Write data
                    self.log_and_print("📝 Writing route data to CSV...")
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
                            self.log_and_print(f"   📊 Processed {i + 1}/{len(routes)} routes...")
                
                self.log_and_print(f"✅ CSV file created: {csv_file}")
                self.log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes")
                self.log_and_print(f"📊 Total routes written: {len(routes)}")
                
                # Show sample data
                if routes:
                    self.log_and_print("\\n📋 Sample Route Data:")
                    sample = routes[0]
                    self.log_and_print(f"   Route ID: {sample.get('route', 'N/A')}")
                    self.log_and_print(f"   Origin (EN): {sample.get('orig_en', 'N/A')}")
                    self.log_and_print(f"   Origin (TC): {sample.get('orig_tc', 'N/A')}")
                    self.log_and_print(f"   Destination (EN): {sample.get('dest_en', 'N/A')}")
                    self.log_and_print(f"   Destination (TC): {sample.get('dest_tc', 'N/A')}")
                    self.log_and_print(f"   Bound: {sample.get('bound', 'N/A')}")
                    self.log_and_print(f"   Service Type: {sample.get('service_type', 'N/A')}")
                
                # Show route statistics
                bound_counts = {}
                service_types = {}
                for route in routes:
                    bound = route.get('bound', 'Unknown')
                    service_type = route.get('service_type', 'Unknown')
                    bound_counts[bound] = bound_counts.get(bound, 0) + 1
                    service_types[service_type] = service_types.get(service_type, 0) + 1
                
                self.log_and_print("\\n📊 Route Statistics:")
                self.log_and_print("   Bound Distribution:")
                for bound, count in bound_counts.items():
                    self.log_and_print(f"     {bound}: {count} routes")
                self.log_and_print("   Service Type Distribution:")
                for service_type, count in service_types.items():
                    self.log_and_print(f"     {service_type}: {count} routes")
                
                return {
                    'success': True,
                    'routes_count': len(routes),
                    'json_file': json_file,
                    'csv_file': csv_file,
                    'request_time': request_time,
                    'file_size': os.path.getsize(csv_file)
                }
                
            else:
                self.log_and_print(f"❌ API request failed: {response.status_code}")
                self.log_and_print(f"📄 Response content: {response.text[:200]}...")
                return {
                    'success': False,
                    'error': f"API request failed: {response.status_code}",
                    'response_text': response.text[:200]
                }
                
        except Exception as e:
            self.log_and_print(f"❌ Error collecting KMB routes: {str(e)}", "ERROR")
            return {
                'success': False,
                'error': str(e)
            }
    
    def collect_kmb_stops(self):
        """Step 2: Collect KMB stops with detailed logging"""
        self.log_separator("STEP 2: KMB STOPS COLLECTION")
        
        self.log_and_print("🚌 Starting KMB Stops Collection")
        self.log_and_print("=" * 50)
        self.log_and_print("🔍 API Details:")
        self.log_and_print("   URL: https://data.etabus.gov.hk/v1/transport/kmb/stop")
        self.log_and_print("   Method: GET")
        self.log_and_print("   Timeout: 30 seconds")
        
        try:
            self.log_and_print("📡 Making API request...")
            start_time = time.time()
            
            response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop", timeout=30)
            
            request_time = time.time() - start_time
            self.log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds")
            self.log_and_print(f"📊 Status Code: {response.status_code}")
            self.log_and_print(f"📏 Response Size: {len(response.content)} bytes")
            
            if response.status_code == 200:
                self.log_and_print("✅ API request successful!")
                
                # Parse JSON response
                self.log_and_print("🔍 Parsing JSON response...")
                data = response.json()
                stops = data.get('data', [])
                
                self.log_and_print(f"📊 Found {len(stops)} KMB stops")
                self.log_and_print(f"📋 Data structure: {list(data.keys())}")
                
                # Save raw JSON data
                json_file = f"data/collected_data/kmb_stops_{self.timestamp}.json"
                self.log_and_print(f"💾 Saving raw JSON data to: {json_file}")
                
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                self.log_and_print(f"✅ Raw data saved: {json_file}")
                self.log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes")
                
                # Create CSV file
                csv_file = f"data/collected_data/kmb_stops_{self.timestamp}.csv"
                self.log_and_print(f"📊 Creating CSV file: {csv_file}")
                self.log_and_print("📋 CSV Headers: stop, name_en, name_tc, name_sc, lat, long, data_timestamp")
                
                with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    
                    # Write header
                    headers = ['stop', 'name_en', 'name_tc', 'name_sc', 'lat', 'long', 'data_timestamp']
                    writer.writerow(headers)
                    
                    # Write data
                    self.log_and_print("📝 Writing stop data to CSV...")
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
                            self.log_and_print(f"   📊 Processed {i + 1}/{len(stops)} stops...")
                
                self.log_and_print(f"✅ CSV file created: {csv_file}")
                self.log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes")
                self.log_and_print(f"📊 Total stops written: {len(stops)}")
                
                # Show sample data
                if stops:
                    self.log_and_print("\\n📋 Sample Stop Data:")
                    sample = stops[0]
                    self.log_and_print(f"   Stop ID: {sample.get('stop', 'N/A')}")
                    self.log_and_print(f"   Name (EN): {sample.get('name_en', 'N/A')}")
                    self.log_and_print(f"   Name (TC): {sample.get('name_tc', 'N/A')}")
                    self.log_and_print(f"   Latitude: {sample.get('lat', 'N/A')}")
                    self.log_and_print(f"   Longitude: {sample.get('long', 'N/A')}")
                
                return {
                    'success': True,
                    'stops_count': len(stops),
                    'json_file': json_file,
                    'csv_file': csv_file,
                    'request_time': request_time,
                    'file_size': os.path.getsize(csv_file)
                }
                
            else:
                self.log_and_print(f"❌ API request failed: {response.status_code}")
                self.log_and_print(f"📄 Response content: {response.text[:200]}...")
                return {
                    'success': False,
                    'error': f"API request failed: {response.status_code}",
                    'response_text': response.text[:200]
                }
                
        except Exception as e:
            self.log_and_print(f"❌ Error collecting KMB stops: {str(e)}", "ERROR")
            return {
                'success': False,
                'error': str(e)
            }
    
    def collect_citybus_routes(self):
        """Step 3: Collect Citybus routes with detailed logging"""
        self.log_separator("STEP 3: CITYBUS ROUTES COLLECTION")
        
        self.log_and_print("🚌 Starting Citybus Routes Collection")
        self.log_and_print("=" * 50)
        self.log_and_print("🔍 API Details:")
        self.log_and_print("   URL: https://rt.data.gov.hk/v2/transport/citybus/route/ctb")
        self.log_and_print("   Method: GET")
        self.log_and_print("   Timeout: 30 seconds")
        
        try:
            self.log_and_print("📡 Making API request...")
            start_time = time.time()
            
            response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/route/ctb", timeout=30)
            
            request_time = time.time() - start_time
            self.log_and_print(f"⏱️  Request completed in {request_time:.2f} seconds")
            self.log_and_print(f"📊 Status Code: {response.status_code}")
            self.log_and_print(f"📏 Response Size: {len(response.content)} bytes")
            
            if response.status_code == 200:
                self.log_and_print("✅ API request successful!")
                
                # Parse JSON response
                self.log_and_print("🔍 Parsing JSON response...")
                data = response.json()
                routes = data.get('data', [])
                
                self.log_and_print(f"📊 Found {len(routes)} Citybus routes")
                self.log_and_print(f"📋 Data structure: {list(data.keys())}")
                
                # Save raw JSON data
                json_file = f"data/collected_data/citybus_routes_{self.timestamp}.json"
                self.log_and_print(f"💾 Saving raw JSON data to: {json_file}")
                
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                self.log_and_print(f"✅ Raw data saved: {json_file}")
                self.log_and_print(f"📁 File size: {os.path.getsize(json_file)} bytes")
                
                # Create CSV file
                csv_file = f"data/collected_data/citybus_routes_{self.timestamp}.csv"
                self.log_and_print(f"📊 Creating CSV file: {csv_file}")
                self.log_and_print("📋 CSV Headers: co, route, orig_en, orig_tc, orig_sc, dest_en, dest_tc, dest_sc, data_timestamp")
                
                with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    
                    # Write header
                    headers = ['co', 'route', 'orig_en', 'orig_tc', 'orig_sc', 'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp']
                    writer.writerow(headers)
                    
                    # Write data
                    self.log_and_print("📝 Writing route data to CSV...")
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
                            self.log_and_print(f"   📊 Processed {i + 1}/{len(routes)} routes...")
                
                self.log_and_print(f"✅ CSV file created: {csv_file}")
                self.log_and_print(f"📁 CSV file size: {os.path.getsize(csv_file)} bytes")
                self.log_and_print(f"📊 Total routes written: {len(routes)}")
                
                # Show sample data
                if routes:
                    self.log_and_print("\\n📋 Sample Route Data:")
                    sample = routes[0]
                    self.log_and_print(f"   Company: {sample.get('co', 'N/A')}")
                    self.log_and_print(f"   Route ID: {sample.get('route', 'N/A')}")
                    self.log_and_print(f"   Origin (EN): {sample.get('orig_en', 'N/A')}")
                    self.log_and_print(f"   Origin (TC): {sample.get('orig_tc', 'N/A')}")
                    self.log_and_print(f"   Destination (EN): {sample.get('dest_en', 'N/A')}")
                    self.log_and_print(f"   Destination (TC): {sample.get('dest_tc', 'N/A')}")
                
                return {
                    'success': True,
                    'routes_count': len(routes),
                    'json_file': json_file,
                    'csv_file': csv_file,
                    'request_time': request_time,
                    'file_size': os.path.getsize(csv_file)
                }
                
            else:
                self.log_and_print(f"❌ API request failed: {response.status_code}")
                self.log_and_print(f"📄 Response content: {response.text[:200]}...")
                return {
                    'success': False,
                    'error': f"API request failed: {response.status_code}",
                    'response_text': response.text[:200]
                }
                
        except Exception as e:
            self.log_and_print(f"❌ Error collecting Citybus routes: {str(e)}", "ERROR")
            return {
                'success': False,
                'error': str(e)
            }
    
    def run_comprehensive_collection(self):
        """Run all data collection steps with detailed logging"""
        self.log_separator("COMPREHENSIVE DATA COLLECTION STARTED")
        
        self.log_and_print("🚌 COMPREHENSIVE DATA COLLECTION")
        self.log_and_print("=" * 80)
        self.log_and_print(f"📅 Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        self.log_and_print(f"📁 Log File: {self.log_file}")
        self.log_and_print("=" * 80)
        
        # Step 1: Collect KMB routes
        self.log_and_print("\\n🚀 Starting Step 1: KMB Routes Collection")
        kmb_routes_result = self.collect_kmb_routes()
        self.results['kmb_routes'] = kmb_routes_result
        
        if kmb_routes_result['success']:
            self.log_and_print("✅ Step 1 completed successfully!")
            self.log_and_print(f"📊 KMB Routes: {kmb_routes_result['routes_count']} routes")
            self.log_and_print(f"📁 CSV File: {kmb_routes_result['csv_file']}")
            self.log_and_print(f"📁 File Size: {kmb_routes_result['file_size']} bytes")
        else:
            self.log_and_print("❌ Step 1 failed!")
            self.log_and_print(f"❌ Error: {kmb_routes_result['error']}")
        
        # Wait between requests
        self.log_and_print("\\n⏱️  Waiting 10 seconds before next request...")
        for i in range(10, 0, -1):
            self.log_and_print(f"   ⏳ {i} seconds remaining...")
            time.sleep(1)
        
        # Step 2: Collect KMB stops
        self.log_and_print("\\n🚀 Starting Step 2: KMB Stops Collection")
        kmb_stops_result = self.collect_kmb_stops()
        self.results['kmb_stops'] = kmb_stops_result
        
        if kmb_stops_result['success']:
            self.log_and_print("✅ Step 2 completed successfully!")
            self.log_and_print(f"📊 KMB Stops: {kmb_stops_result['stops_count']} stops")
            self.log_and_print(f"📁 CSV File: {kmb_stops_result['csv_file']}")
            self.log_and_print(f"📁 File Size: {kmb_stops_result['file_size']} bytes")
        else:
            self.log_and_print("❌ Step 2 failed!")
            self.log_and_print(f"❌ Error: {kmb_stops_result['error']}")
        
        # Wait between requests
        self.log_and_print("\\n⏱️  Waiting 10 seconds before next request...")
        for i in range(10, 0, -1):
            self.log_and_print(f"   ⏳ {i} seconds remaining...")
            time.sleep(1)
        
        # Step 3: Collect Citybus routes
        self.log_and_print("\\n🚀 Starting Step 3: Citybus Routes Collection")
        citybus_routes_result = self.collect_citybus_routes()
        self.results['citybus_routes'] = citybus_routes_result
        
        if citybus_routes_result['success']:
            self.log_and_print("✅ Step 3 completed successfully!")
            self.log_and_print(f"📊 Citybus Routes: {citybus_routes_result['routes_count']} routes")
            self.log_and_print(f"📁 CSV File: {citybus_routes_result['csv_file']}")
            self.log_and_print(f"📁 File Size: {citybus_routes_result['file_size']} bytes")
        else:
            self.log_and_print("❌ Step 3 failed!")
            self.log_and_print(f"❌ Error: {citybus_routes_result['error']}")
        
        # Final summary
        self.log_separator("FINAL COLLECTION SUMMARY")
        
        end_time = datetime.now()
        total_time = (end_time - self.start_time).total_seconds()
        
        self.log_and_print(f"⏱️  Total Collection Time: {total_time:.2f} seconds")
        self.log_and_print(f"📅 End Time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Summary of results
        self.log_and_print("\\n📊 COLLECTION RESULTS:")
        self.log_and_print("=" * 50)
        
        if self.results['kmb_routes']['success']:
            self.log_and_print(f"✅ KMB Routes: {self.results['kmb_routes']['routes_count']} routes")
            self.log_and_print(f"   📁 CSV: {self.results['kmb_routes']['csv_file']}")
            self.log_and_print(f"   📁 Size: {self.results['kmb_routes']['file_size']} bytes")
        else:
            self.log_and_print(f"❌ KMB Routes: Failed - {self.results['kmb_routes']['error']}")
        
        if self.results['kmb_stops']['success']:
            self.log_and_print(f"✅ KMB Stops: {self.results['kmb_stops']['stops_count']} stops")
            self.log_and_print(f"   📁 CSV: {self.results['kmb_stops']['csv_file']}")
            self.log_and_print(f"   📁 Size: {self.results['kmb_stops']['file_size']} bytes")
        else:
            self.log_and_print(f"❌ KMB Stops: Failed - {self.results['kmb_stops']['error']}")
        
        if self.results['citybus_routes']['success']:
            self.log_and_print(f"✅ Citybus Routes: {self.results['citybus_routes']['routes_count']} routes")
            self.log_and_print(f"   📁 CSV: {self.results['citybus_routes']['csv_file']}")
            self.log_and_print(f"   📁 Size: {self.results['citybus_routes']['file_size']} bytes")
        else:
            self.log_and_print(f"❌ Citybus Routes: Failed - {self.results['citybus_routes']['error']}")
        
        # Success rate
        successful_steps = sum(1 for result in self.results.values() if result['success'])
        total_steps = len(self.results)
        success_rate = (successful_steps / total_steps) * 100
        
        self.log_and_print(f"\\n📈 Success Rate: {success_rate:.1f}% ({successful_steps}/{total_steps} steps)")
        
        self.log_separator("COLLECTION COMPLETED")
        self.log_and_print("🎉 Comprehensive data collection completed!")
        self.log_and_print(f"📁 All logs saved to: {self.log_file}")
        
        return self.results

def main():
    """Main function"""
    collector = DataCollector()
    results = collector.run_comprehensive_collection()
    
    print("\\n" + "=" * 80)
    print("🎉 DATA COLLECTION COMPLETED!")
    print("=" * 80)
    print(f"📁 Log file: {collector.log_file}")
    print("📊 Check the log file for detailed results")
    print("=" * 80)
    
    return results

if __name__ == "__main__":
    results = main()
