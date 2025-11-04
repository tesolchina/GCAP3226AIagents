#!/usr/bin/env python3
"""
Comprehensive Bus Data Collector
Collects all route and stop data from KMB and Citybus APIs
Creates CSV files for comprehensive analysis
"""

import requests
import json
import csv
import time
from datetime import datetime
import os
import sys

class BusDataCollector:
    def __init__(self):
        self.kmb_base_url = "https://data.etabus.gov.hk/v1/transport/kmb"
        self.citybus_base_url = "https://rt.data.gov.hk/v2/transport/citybus"
        self.results_dir = "data/comprehensive_analysis"
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create results directory
        os.makedirs(self.results_dir, exist_ok=True)
        os.makedirs(f"{self.results_dir}/raw_data", exist_ok=True)
        os.makedirs(f"{self.results_dir}/csv_files", exist_ok=True)
        os.makedirs(f"{self.results_dir}/analysis", exist_ok=True)
        
    def collect_kmb_routes(self):
        """Collect all KMB routes"""
        print("🚌 Collecting KMB routes...")
        
        try:
            response = requests.get(f"{self.kmb_base_url}/route", timeout=30)
            if response.status_code == 200:
                data = response.json()
                routes = data.get('data', [])
                print(f"✅ Collected {len(routes)} KMB routes")
                
                # Save raw data
                with open(f"{self.results_dir}/raw_data/kmb_routes_{self.timestamp}.json", 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                return routes
            else:
                print(f"❌ KMB routes API error: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error collecting KMB routes: {str(e)}")
            return []
    
    def collect_citybus_routes(self):
        """Collect all Citybus routes"""
        print("🚌 Collecting Citybus routes...")
        
        try:
            response = requests.get(f"{self.citybus_base_url}/route/ctb", timeout=30)
            if response.status_code == 200:
                data = response.json()
                routes = data.get('data', [])
                print(f"✅ Collected {len(routes)} Citybus routes")
                
                # Save raw data
                with open(f"{self.results_dir}/raw_data/citybus_routes_{self.timestamp}.json", 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                return routes
            else:
                print(f"❌ Citybus routes API error: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error collecting Citybus routes: {str(e)}")
            return []
    
    def collect_kmb_stops(self):
        """Collect all KMB stops"""
        print("🚌 Collecting KMB stops...")
        
        try:
            response = requests.get(f"{self.kmb_base_url}/stop", timeout=30)
            if response.status_code == 200:
                data = response.json()
                stops = data.get('data', [])
                print(f"✅ Collected {len(stops)} KMB stops")
                
                # Save raw data
                with open(f"{self.results_dir}/raw_data/kmb_stops_{self.timestamp}.json", 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                return stops
            else:
                print(f"❌ KMB stops API error: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error collecting KMB stops: {str(e)}")
            return []
    
    def collect_kmb_route_stops(self, routes, max_routes=50):
        """Collect route-stop mappings for KMB routes"""
        print(f"🚌 Collecting KMB route-stop mappings (max {max_routes} routes)...")
        
        route_stops = []
        successful = 0
        failed = 0
        
        for i, route in enumerate(routes[:max_routes]):
            route_id = route.get('route', '')
            if not route_id:
                continue
                
            try:
                # Get route-stop data for both directions
                for bound in ['O', 'I']:  # Outbound and Inbound
                    response = requests.get(f"{self.kmb_base_url}/route-stop", 
                                          params={'route': route_id, 'bound': bound}, 
                                          timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        stops = data.get('data', [])
                        
                        for stop in stops:
                            route_stops.append({
                                'route': route_id,
                                'bound': bound,
                                'stop': stop.get('stop', ''),
                                'seq': stop.get('seq', 0),
                                'service_type': stop.get('service_type', '')
                            })
                        successful += 1
                    else:
                        failed += 1
                        
                # Rate limiting
                time.sleep(0.1)
                
            except Exception as e:
                print(f"❌ Error collecting route-stops for {route_id}: {str(e)}")
                failed += 1
                
            if (i + 1) % 10 == 0:
                print(f"   Processed {i + 1}/{min(len(routes), max_routes)} routes...")
        
        print(f"✅ Collected route-stops for {successful} routes, {failed} failed")
        
        # Save raw data
        with open(f"{self.results_dir}/raw_data/kmb_route_stops_{self.timestamp}.json", 'w', encoding='utf-8') as f:
            json.dump(route_stops, f, ensure_ascii=False, indent=2)
        
        return route_stops
    
    def create_kmb_routes_csv(self, routes):
        """Create CSV file for KMB routes"""
        print("📊 Creating KMB routes CSV...")
        
        csv_file = f"{self.results_dir}/csv_files/kmb_routes_{self.timestamp}.csv"
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'route', 'bound', 'service_type', 'orig_en', 'orig_tc', 'orig_sc',
                'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp'
            ])
            
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
        
        print(f"✅ KMB routes CSV created: {csv_file}")
        return csv_file
    
    def create_kmb_stops_csv(self, stops):
        """Create CSV file for KMB stops"""
        print("📊 Creating KMB stops CSV...")
        
        csv_file = f"{self.results_dir}/csv_files/kmb_stops_{self.timestamp}.csv"
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'stop', 'name_en', 'name_tc', 'name_sc', 'lat', 'long', 'data_timestamp'
            ])
            
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
        
        print(f"✅ KMB stops CSV created: {csv_file}")
        return csv_file
    
    def create_kmb_route_stops_csv(self, route_stops):
        """Create CSV file for KMB route-stops"""
        print("📊 Creating KMB route-stops CSV...")
        
        csv_file = f"{self.results_dir}/csv_files/kmb_route_stops_{self.timestamp}.csv"
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'route', 'bound', 'stop', 'seq', 'service_type'
            ])
            
            for route_stop in route_stops:
                writer.writerow([
                    route_stop.get('route', ''),
                    route_stop.get('bound', ''),
                    route_stop.get('stop', ''),
                    route_stop.get('seq', ''),
                    route_stop.get('service_type', '')
                ])
        
        print(f"✅ KMB route-stops CSV created: {csv_file}")
        return csv_file
    
    def create_citybus_routes_csv(self, routes):
        """Create CSV file for Citybus routes"""
        print("📊 Creating Citybus routes CSV...")
        
        csv_file = f"{self.results_dir}/csv_files/citybus_routes_{self.timestamp}.csv"
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'co', 'route', 'orig_en', 'orig_tc', 'orig_sc',
                'dest_en', 'dest_tc', 'dest_sc', 'data_timestamp'
            ])
            
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
        
        print(f"✅ Citybus routes CSV created: {csv_file}")
        return csv_file
    
    def run_comprehensive_collection(self):
        """Run comprehensive data collection"""
        print("🚌 Starting Comprehensive Bus Data Collection")
        print("=" * 60)
        
        # Collect KMB data
        print("\n📊 COLLECTING KMB DATA")
        print("-" * 30)
        kmb_routes = self.collect_kmb_routes()
        kmb_stops = self.collect_kmb_stops()
        kmb_route_stops = self.collect_kmb_route_stops(kmb_routes)
        
        # Collect Citybus data
        print("\n📊 COLLECTING CITYBUS DATA")
        print("-" * 30)
        citybus_routes = self.collect_citybus_routes()
        
        # Create CSV files
        print("\n📊 CREATING CSV FILES")
        print("-" * 30)
        kmb_routes_csv = self.create_kmb_routes_csv(kmb_routes)
        kmb_stops_csv = self.create_kmb_stops_csv(kmb_stops)
        kmb_route_stops_csv = self.create_kmb_route_stops_csv(kmb_route_stops)
        citybus_routes_csv = self.create_citybus_routes_csv(citybus_routes)
        
        # Summary
        print("\n🎯 COLLECTION SUMMARY")
        print("=" * 60)
        print(f"KMB Routes: {len(kmb_routes)}")
        print(f"KMB Stops: {len(kmb_stops)}")
        print(f"KMB Route-Stops: {len(kmb_route_stops)}")
        print(f"Citybus Routes: {len(citybus_routes)}")
        print(f"\nCSV Files Created:")
        print(f"  - {kmb_routes_csv}")
        print(f"  - {kmb_stops_csv}")
        print(f"  - {kmb_route_stops_csv}")
        print(f"  - {citybus_routes_csv}")
        
        return {
            'kmb_routes': kmb_routes,
            'kmb_stops': kmb_stops,
            'kmb_route_stops': kmb_route_stops,
            'citybus_routes': citybus_routes,
            'csv_files': {
                'kmb_routes': kmb_routes_csv,
                'kmb_stops': kmb_stops_csv,
                'kmb_route_stops': kmb_route_stops_csv,
                'citybus_routes': citybus_routes_csv
            }
        }

def main():
    """Main function"""
    collector = BusDataCollector()
    results = collector.run_comprehensive_collection()
    
    print(f"\n🎉 Data collection completed!")
    print(f"📁 Results saved in: {collector.results_dir}")
    
    return results

if __name__ == "__main__":
    results = main()
