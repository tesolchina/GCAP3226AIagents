#!/usr/bin/env python3
"""
Analyze 272A and 582 Route Overlap
Check for potential overlaps between KMB 272A and Citybus 582
"""

import pandas as pd
import json
from datetime import datetime

print("🔍 ANALYZING 272A ↔ 582 OVERLAP")
print("=" * 50)
print(f"📅 Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

def load_data():
    """Load the data files"""
    print("📊 Loading data files...")
    
    # Load KMB route mappings
    kmb_mappings = pd.read_csv("data/collected_data/route_stop_mappings_20251019_142825.csv")
    kmb_stops = pd.read_csv("data/collected_data/kmb_all_stops_20251019_142825.csv")
    
    # Load Citybus route mappings
    citybus_mappings = pd.read_csv("data/collected_data/citybus_route_stops_20251019_144804.csv")
    citybus_stops = pd.read_csv("data/collected_data/citybus_stops_20251019_144804.csv")
    
    print(f"✅ KMB mappings: {len(kmb_mappings)} records")
    print(f"✅ KMB stops: {len(kmb_stops)} records")
    print(f"✅ Citybus mappings: {len(citybus_mappings)} records")
    print(f"✅ Citybus stops: {len(citybus_stops)} records")
    
    return kmb_mappings, kmb_stops, citybus_mappings, citybus_stops

def analyze_272A_582():
    """Analyze 272A and 582 routes"""
    print("\n🔍 ANALYZING 272A AND 582 ROUTES")
    print("=" * 50)
    
    kmb_mappings, kmb_stops, citybus_mappings, citybus_stops = load_data()
    
    # Get 272A stops
    kmb_272A = kmb_mappings[kmb_mappings['route'] == '272A']
    print(f"📊 KMB 272A: {len(kmb_272A)} stops")
    
    # Get 582 stops
    citybus_582 = citybus_mappings[citybus_mappings['route'] == '582']
    print(f"📊 Citybus 582: {len(citybus_582)} stops")
    
    # Get stop details for 272A
    print("\n🚌 KMB 272A STOPS:")
    kmb_272A_stops = []
    for _, stop in kmb_272A.iterrows():
        stop_id = stop['stop_id']
        stop_info = kmb_stops[kmb_stops['stop'] == stop_id]
        if not stop_info.empty:
            stop_data = stop_info.iloc[0]
            kmb_272A_stops.append({
                'stop_id': stop_id,
                'name_en': stop_data['name_en'],
                'name_tc': stop_data['name_tc'],
                'lat': stop_data['lat'],
                'long': stop_data['long'],
                'sequence': stop['sequence']
            })
            print(f"   {stop['sequence']}. {stop_data['name_en']} ({stop_data['name_tc']})")
    
    # Get stop details for 582
    print("\n🚌 CITYBUS 582 STOPS:")
    citybus_582_stops = []
    for _, stop in citybus_582.iterrows():
        stop_id = stop['stop_id']
        stop_info = citybus_stops[citybus_stops['stop_id'] == stop_id]
        if not stop_info.empty:
            stop_data = stop_info.iloc[0]
            citybus_582_stops.append({
                'stop_id': stop_id,
                'name_en': stop_data['name_en'],
                'name_tc': stop_data['name_tc'],
                'lat': stop_data['lat'],
                'long': stop_data['long'],
                'sequence': stop['sequence']
            })
            print(f"   {stop['sequence']}. {stop_data['name_en']} ({stop_data['name_tc']})")
    
    # Check for coordinate-based overlaps
    print("\n🔍 CHECKING FOR COORDINATE-BASED OVERLAPS:")
    overlaps = []
    
    for kmb_stop in kmb_272A_stops:
        for citybus_stop in citybus_582_stops:
            # Check if coordinates are very close (within ~50 meters)
            try:
                kmb_lat = float(kmb_stop['lat'])
                kmb_long = float(kmb_stop['long'])
                citybus_lat = float(citybus_stop['lat'])
                citybus_long = float(citybus_stop['long'])
                
                # Calculate distance (rough approximation)
                lat_diff = abs(kmb_lat - citybus_lat)
                long_diff = abs(kmb_long - citybus_long)
                
                # If coordinates are very close (within ~0.0005 degrees ≈ 50m)
                if lat_diff < 0.0005 and long_diff < 0.0005:
                    overlaps.append({
                        'kmb_stop': kmb_stop,
                        'citybus_stop': citybus_stop,
                        'lat_diff': lat_diff,
                        'long_diff': long_diff
                    })
                    print(f"   🎯 Potential overlap:")
                    print(f"      KMB: {kmb_stop['name_en']} ({kmb_stop['name_tc']})")
                    print(f"      Citybus: {citybus_stop['name_en']} ({citybus_stop['name_tc']})")
                    print(f"      Coordinates: KMB({kmb_lat}, {kmb_long}) vs Citybus({citybus_lat}, {citybus_long})")
            except (ValueError, TypeError):
                continue
    
    print(f"\n📊 Found {len(overlaps)} potential coordinate-based overlaps")
    
    # Check for name-based overlaps
    print("\n🔍 CHECKING FOR NAME-BASED OVERLAPS:")
    name_overlaps = []
    
    for kmb_stop in kmb_272A_stops:
        for citybus_stop in citybus_582_stops:
            # Check for similar names (case insensitive)
            kmb_name = kmb_stop['name_en'].lower()
            citybus_name = citybus_stop['name_en'].lower()
            
            # Check for common words or similar names
            if any(word in citybus_name for word in kmb_name.split() if len(word) > 3):
                name_overlaps.append({
                    'kmb_stop': kmb_stop,
                    'citybus_stop': citybus_stop
                })
                print(f"   🎯 Potential name overlap:")
                print(f"      KMB: {kmb_stop['name_en']} ({kmb_stop['name_tc']})")
                print(f"      Citybus: {citybus_stop['name_en']} ({citybus_stop['name_tc']})")
    
    print(f"\n📊 Found {len(name_overlaps)} potential name-based overlaps")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 272A ↔ 582 OVERLAP ANALYSIS SUMMARY")
    print("=" * 50)
    print(f"KMB 272A stops: {len(kmb_272A_stops)}")
    print(f"Citybus 582 stops: {len(citybus_582_stops)}")
    print(f"Coordinate overlaps: {len(overlaps)}")
    print(f"Name overlaps: {len(name_overlaps)}")
    
    if overlaps or name_overlaps:
        print("\n✅ POTENTIAL OVERLAPS FOUND!")
        print("These routes may share common stops or serve similar areas.")
    else:
        print("\n❌ NO OVERLAPS FOUND")
        print("These routes appear to serve different areas with no common stops.")
    
    return overlaps, name_overlaps

if __name__ == "__main__":
    try:
        overlaps, name_overlaps = analyze_272A_582()
        
        print("\n" + "=" * 80)
        print("🎉 272A ↔ 582 ANALYSIS COMPLETED!")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")
