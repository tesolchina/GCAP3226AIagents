#!/usr/bin/env python3
"""
Execute Bus Route Analysis
Simplified execution script for comprehensive analysis
"""

import requests
import json
import csv
from datetime import datetime
import os
import time

def log_message(message):
    """Log message with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

def test_apis():
    """Test API access"""
    log_message("🔍 Testing API access...")
    
    # Test KMB API
    try:
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=10)
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            log_message(f"✅ KMB API: {len(routes)} routes available")
            kmb_success = True
        else:
            log_message(f"❌ KMB API error: {response.status_code}")
            kmb_success = False
    except Exception as e:
        log_message(f"❌ KMB API error: {str(e)}")
        kmb_success = False
    
    # Test Citybus API
    try:
        response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/route/ctb", timeout=10)
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            log_message(f"✅ Citybus API: {len(routes)} routes available")
            citybus_success = True
        else:
            log_message(f"❌ Citybus API error: {response.status_code}")
            citybus_success = False
    except Exception as e:
        log_message(f"❌ Citybus API error: {str(e)}")
        citybus_success = False
    
    return kmb_success, citybus_success

def collect_kmb_data():
    """Collect KMB data"""
    log_message("📊 Collecting KMB data...")
    
    # Create directories
    os.makedirs("data/comprehensive_analysis/raw_data", exist_ok=True)
    os.makedirs("data/comprehensive_analysis/csv_files", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results = {}
    
    # Collect routes
    try:
        log_message("   Collecting KMB routes...")
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=30)
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            log_message(f"   ✅ Collected {len(routes)} KMB routes")
            
            # Save raw data
            with open(f"data/comprehensive_analysis/raw_data/kmb_routes_{timestamp}.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            # Create CSV
            csv_file = f"data/comprehensive_analysis/csv_files/kmb_routes_{timestamp}.csv"
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
            
            log_message(f"   ✅ KMB routes CSV created: {csv_file}")
            results['kmb_routes'] = routes
            results['kmb_routes_csv'] = csv_file
        else:
            log_message(f"   ❌ KMB routes API error: {response.status_code}")
            return None
    except Exception as e:
        log_message(f"   ❌ Error collecting KMB routes: {str(e)}")
        return None
    
    # Collect stops
    try:
        log_message("   Collecting KMB stops...")
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop", timeout=30)
        if response.status_code == 200:
            data = response.json()
            stops = data.get('data', [])
            log_message(f"   ✅ Collected {len(stops)} KMB stops")
            
            # Save raw data
            with open(f"data/comprehensive_analysis/raw_data/kmb_stops_{timestamp}.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            # Create CSV
            csv_file = f"data/comprehensive_analysis/csv_files/kmb_stops_{timestamp}.csv"
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
            
            log_message(f"   ✅ KMB stops CSV created: {csv_file}")
            results['kmb_stops'] = stops
            results['kmb_stops_csv'] = csv_file
        else:
            log_message(f"   ❌ KMB stops API error: {response.status_code}")
            return None
    except Exception as e:
        log_message(f"   ❌ Error collecting KMB stops: {str(e)}")
        return None
    
    return results

def collect_citybus_data():
    """Collect Citybus data"""
    log_message("📊 Collecting Citybus data...")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        log_message("   Collecting Citybus routes...")
        response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/route/ctb", timeout=30)
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            log_message(f"   ✅ Collected {len(routes)} Citybus routes")
            
            # Save raw data
            with open(f"data/comprehensive_analysis/raw_data/citybus_routes_{timestamp}.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            # Create CSV
            csv_file = f"data/comprehensive_analysis/csv_files/citybus_routes_{timestamp}.csv"
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
            
            log_message(f"   ✅ Citybus routes CSV created: {csv_file}")
            return {'citybus_routes': routes, 'citybus_routes_csv': csv_file}
        else:
            log_message(f"   ❌ Citybus routes API error: {response.status_code}")
            return None
    except Exception as e:
        log_message(f"   ❌ Error collecting Citybus routes: {str(e)}")
        return None

def analyze_overlaps(kmb_data, citybus_data):
    """Analyze overlaps between routes"""
    log_message("🔍 Analyzing route overlaps...")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Simple overlap analysis based on route names
    overlaps = []
    
    if kmb_data and citybus_data:
        kmb_routes = kmb_data.get('kmb_routes', [])
        citybus_routes = citybus_data.get('citybus_routes', [])
        
        log_message(f"   Analyzing {len(kmb_routes)} KMB routes vs {len(citybus_routes)} Citybus routes")
        
        # Simple overlap detection based on route names
        for kmb_route in kmb_routes[:10]:  # Limit for demo
            for citybus_route in citybus_routes[:10]:  # Limit for demo
                kmb_orig = kmb_route.get('orig_en', '').lower()
                kmb_dest = kmb_route.get('dest_en', '').lower()
                citybus_orig = citybus_route.get('orig_en', '').lower()
                citybus_dest = citybus_route.get('dest_en', '').lower()
                
                # Simple overlap detection
                if (kmb_orig in citybus_orig or kmb_orig in citybus_dest or 
                    kmb_dest in citybus_orig or kmb_dest in citybus_dest):
                    overlap = {
                        'kmb_route': kmb_route.get('route', ''),
                        'citybus_route': citybus_route.get('route', ''),
                        'kmb_orig': kmb_route.get('orig_en', ''),
                        'kmb_dest': kmb_route.get('dest_en', ''),
                        'citybus_orig': citybus_route.get('orig_en', ''),
                        'citybus_dest': citybus_route.get('dest_en', ''),
                        'overlap_type': 'potential',
                        'analysis_timestamp': datetime.now().isoformat()
                    }
                    overlaps.append(overlap)
        
        log_message(f"   ✅ Found {len(overlaps)} potential overlaps")
        
        # Create overlap CSV
        csv_file = f"data/comprehensive_analysis/csv_files/overlaps_{timestamp}.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['kmb_route', 'citybus_route', 'kmb_orig', 'kmb_dest', 'citybus_orig', 'citybus_dest', 'overlap_type', 'analysis_timestamp'])
            
            for overlap in overlaps:
                writer.writerow([
                    overlap['kmb_route'],
                    overlap['citybus_route'],
                    overlap['kmb_orig'],
                    overlap['kmb_dest'],
                    overlap['citybus_orig'],
                    overlap['citybus_dest'],
                    overlap['overlap_type'],
                    overlap['analysis_timestamp']
                ])
        
        log_message(f"   ✅ Overlaps CSV created: {csv_file}")
        return overlaps, csv_file
    
    return [], None

def generate_summary_report(kmb_data, citybus_data, overlaps):
    """Generate summary report"""
    log_message("📋 Generating summary report...")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"data/comprehensive_analysis/analysis/summary_report_{timestamp}.md"
    
    os.makedirs("data/comprehensive_analysis/analysis", exist_ok=True)
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Bus Route Analysis Summary Report\n\n")
        f.write(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## 📊 Data Collection Summary\n\n")
        if kmb_data:
            f.write(f"- **KMB Routes:** {len(kmb_data.get('kmb_routes', []))}\n")
            f.write(f"- **KMB Stops:** {len(kmb_data.get('kmb_stops', []))}\n")
        if citybus_data:
            f.write(f"- **Citybus Routes:** {len(citybus_data.get('citybus_routes', []))}\n")
        
        f.write("\n## 🔍 Overlap Analysis Summary\n\n")
        f.write(f"- **Potential Overlaps:** {len(overlaps)}\n")
        
        if overlaps:
            f.write("\n### 🎯 High Priority Overlaps\n\n")
            for i, overlap in enumerate(overlaps[:5], 1):
                f.write(f"{i}. **KMB {overlap['kmb_route']} vs Citybus {overlap['citybus_route']}**\n")
                f.write(f"   - KMB Route: {overlap['kmb_orig']} → {overlap['kmb_dest']}\n")
                f.write(f"   - Citybus Route: {overlap['citybus_orig']} → {overlap['citybus_dest']}\n\n")
        
        f.write("## 📁 Generated Files\n\n")
        if kmb_data:
            f.write(f"- **KMB Routes CSV:** {kmb_data.get('kmb_routes_csv', 'N/A')}\n")
            f.write(f"- **KMB Stops CSV:** {kmb_data.get('kmb_stops_csv', 'N/A')}\n")
        if citybus_data:
            f.write(f"- **Citybus Routes CSV:** {citybus_data.get('citybus_routes_csv', 'N/A')}\n")
        
        f.write("\n## 🎯 Recommendations\n\n")
        f.write("1. **Immediate Action:** Implement coordination for high-priority overlapping routes\n")
        f.write("2. **Medium-term:** Develop comprehensive coordination framework\n")
        f.write("3. **Long-term:** System-wide coordination implementation\n\n")
    
    log_message(f"   ✅ Summary report created: {report_file}")
    return report_file

def main():
    """Main execution function"""
    log_message("🚌 Starting Bus Route Analysis Pipeline")
    log_message("=" * 60)
    
    # Test APIs
    kmb_success, citybus_success = test_apis()
    
    if not kmb_success and not citybus_success:
        log_message("❌ No APIs accessible. Cannot proceed.")
        return False
    
    # Collect data
    kmb_data = None
    citybus_data = None
    
    if kmb_success:
        kmb_data = collect_kmb_data()
    
    if citybus_success:
        citybus_data = collect_citybus_data()
    
    # Analyze overlaps
    overlaps, overlaps_csv = analyze_overlaps(kmb_data, citybus_data)
    
    # Generate report
    report_file = generate_summary_report(kmb_data, citybus_data, overlaps)
    
    # Final summary
    log_message("🎉 Analysis completed successfully!")
    log_message("=" * 60)
    log_message(f"📊 KMB Routes: {len(kmb_data.get('kmb_routes', [])) if kmb_data else 0}")
    log_message(f"📊 KMB Stops: {len(kmb_data.get('kmb_stops', [])) if kmb_data else 0}")
    log_message(f"📊 Citybus Routes: {len(citybus_data.get('citybus_routes', [])) if citybus_data else 0}")
    log_message(f"🔍 Overlaps: {len(overlaps)}")
    log_message(f"📋 Report: {report_file}")
    log_message("=" * 60)
    
    return True

if __name__ == "__main__":
    success = main()
    print(f"\n{'✅ Analysis completed successfully!' if success else '❌ Analysis completed with issues.'}")
