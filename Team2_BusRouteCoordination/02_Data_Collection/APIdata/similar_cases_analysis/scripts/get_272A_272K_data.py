#!/usr/bin/env python3
"""
Get Real Data for KMB Routes 272A and 272K
Access actual route data via APIs to analyze overlaps
"""

import requests
import json
from datetime import datetime
import os

def get_kmb_route_data(route_id):
    """Get KMB route data from API"""
    print(f"🔍 Getting KMB route {route_id} data...")
    
    try:
        # Try KMB API endpoint
        url = f"https://data.etabus.gov.hk/v1/transport/kmb/route/{route_id}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Successfully retrieved KMB route {route_id} data")
            return data
        else:
            print(f"❌ KMB API error for route {route_id}: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error accessing KMB route {route_id}: {str(e)}")
        return None

def get_kmb_route_stops(route_id):
    """Get KMB route-stop data"""
    print(f"🔍 Getting KMB route {route_id} stops...")
    
    try:
        # Try route-stop API
        url = f"https://data.etabus.gov.hk/v1/transport/kmb/route-stop"
        params = {"route": route_id}
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Successfully retrieved KMB route {route_id} stops")
            return data
        else:
            print(f"❌ KMB route-stop API error for route {route_id}: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error accessing KMB route {route_id} stops: {str(e)}")
        return None

def get_stop_details(stop_id):
    """Get stop details"""
    print(f"🔍 Getting stop {stop_id} details...")
    
    try:
        url = f"https://data.etabus.gov.hk/v1/transport/kmb/stop/{stop_id}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Successfully retrieved stop {stop_id} details")
            return data
        else:
            print(f"❌ Stop API error for stop {stop_id}: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error accessing stop {stop_id}: {str(e)}")
        return None

def analyze_route_overlap(route1_data, route2_data, route1_stops, route2_stops):
    """Analyze overlap between two routes"""
    print("🔍 Analyzing route overlap...")
    
    if not route1_stops or not route2_stops:
        print("❌ Cannot analyze - missing stop data")
        return None
    
    # Extract stop IDs
    stops1 = set()
    stops2 = set()
    
    if 'data' in route1_stops:
        for stop in route1_stops['data']:
            if 'stop' in stop:
                stops1.add(stop['stop'])
    
    if 'data' in route2_stops:
        for stop in route2_stops['data']:
            if 'stop' in stop:
                stops2.add(stop['stop'])
    
    # Find common stops
    common_stops = stops1 & stops2
    
    overlap_analysis = {
        'route1': {
            'route_id': route1_data.get('route', 'Unknown') if route1_data else 'Unknown',
            'total_stops': len(stops1),
            'stops': list(stops1)
        },
        'route2': {
            'route_id': route2_data.get('route', 'Unknown') if route2_data else 'Unknown',
            'total_stops': len(stops2),
            'stops': list(stops2)
        },
        'overlap_count': len(common_stops),
        'overlap_percentage': len(common_stops) / min(len(stops1), len(stops2)) if min(len(stops1), len(stops2)) > 0 else 0,
        'common_stops': list(common_stops),
        'analysis_timestamp': datetime.now().isoformat()
    }
    
    return overlap_analysis

def main():
    """Main function to get and analyze 272A and 272K data"""
    print("🚌 Getting Real Data for KMB Routes 272A and 272K")
    print("=" * 60)
    
    # Get route data
    route_272A_data = get_kmb_route_data("272A")
    route_272K_data = get_kmb_route_data("272K")
    
    print()
    
    # Get route stops
    route_272A_stops = get_kmb_route_stops("272A")
    route_272K_stops = get_kmb_route_stops("272K")
    
    print()
    
    # Display route information
    if route_272A_data:
        print("📊 Route 272A Information:")
        if 'data' in route_272A_data:
            route_info = route_272A_data['data']
            print(f"   Route: {route_info.get('route', 'N/A')}")
            print(f"   Origin: {route_info.get('orig_en', 'N/A')} ({route_info.get('orig_tc', 'N/A')})")
            print(f"   Destination: {route_info.get('dest_en', 'N/A')} ({route_info.get('dest_tc', 'N/A')})")
            print(f"   Service Type: {route_info.get('service_type', 'N/A')}")
        else:
            print("   No route data available")
    
    if route_272K_data:
        print("📊 Route 272K Information:")
        if 'data' in route_272K_data:
            route_info = route_272K_data['data']
            print(f"   Route: {route_info.get('route', 'N/A')}")
            print(f"   Origin: {route_info.get('orig_en', 'N/A')} ({route_info.get('orig_tc', 'N/A')})")
            print(f"   Destination: {route_info.get('dest_en', 'N/A')} ({route_info.get('dest_tc', 'N/A')})")
            print(f"   Service Type: {route_info.get('service_type', 'N/A')}")
        else:
            print("   No route data available")
    
    print()
    
    # Analyze overlap
    if route_272A_stops and route_272K_stops:
        overlap_analysis = analyze_route_overlap(
            route_272A_data, route_272K_data,
            route_272A_stops, route_272K_stops
        )
        
        if overlap_analysis:
            print("📊 OVERLAP ANALYSIS RESULTS:")
            print("-" * 40)
            print(f"Route 1: {overlap_analysis['route1']['route_id']} ({overlap_analysis['route1']['total_stops']} stops)")
            print(f"Route 2: {overlap_analysis['route2']['route_id']} ({overlap_analysis['route2']['total_stops']} stops)")
            print(f"Overlap Count: {overlap_analysis['overlap_count']} stops")
            print(f"Overlap Percentage: {overlap_analysis['overlap_percentage']:.1%}")
            print(f"Common Stops: {', '.join(overlap_analysis['common_stops'])}")
            
            # Save results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            results_file = f"data/overlap_analysis/272A_272K_analysis_{timestamp}.json"
            os.makedirs(os.path.dirname(results_file), exist_ok=True)
            
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(overlap_analysis, f, ensure_ascii=False, indent=2)
            
            print(f"\n💾 Results saved to: {results_file}")
        else:
            print("❌ Could not analyze overlap - insufficient data")
    else:
        print("❌ Could not get stop data for overlap analysis")
    
    print("\n🎯 Analysis Complete!")

if __name__ == "__main__":
    main()
