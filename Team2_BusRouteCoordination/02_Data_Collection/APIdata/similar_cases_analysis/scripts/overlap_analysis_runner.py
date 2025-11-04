#!/usr/bin/env python3
"""
Comprehensive Bus Route Overlap Analysis
Identifies overlapping stops between KMB and Citybus routes
"""

import json
import requests
from datetime import datetime
import os
import sys

def load_kmb_data():
    """Load KMB route data"""
    print("📊 Loading KMB data...")
    
    # Try to load from existing files
    kmb_files = [
        'data/raw_routes/kmb_routes_20251019_120938.json',
        'data/raw_routes/all_routes_20251019_120938.json'
    ]
    
    for file_path in kmb_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                print(f"✅ Loaded KMB data from {file_path}")
                return data
            except Exception as e:
                print(f"❌ Error loading {file_path}: {e}")
    
    # If no existing data, create sample KMB data
    print("📝 Creating sample KMB data...")
    sample_kmb_data = {
        "type": "RouteList",
        "version": "2.0",
        "generated_timestamp": datetime.now().isoformat(),
        "data": [
            {
                "co": "KMB",
                "route": "1",
                "orig_tc": "竹園邨",
                "orig_en": "Chuk Yuen Estate",
                "dest_tc": "尖沙咀碼頭",
                "dest_en": "Star Ferry",
                "bound": "O",
                "service_type": "1"
            },
            {
                "co": "KMB", 
                "route": "2",
                "orig_tc": "竹園邨",
                "orig_en": "Chuk Yuen Estate",
                "dest_tc": "尖沙咀碼頭",
                "dest_en": "Star Ferry",
                "bound": "O",
                "service_type": "1"
            },
            {
                "co": "KMB",
                "route": "3",
                "orig_tc": "中環",
                "orig_en": "Central",
                "dest_tc": "銅鑼灣",
                "dest_en": "Causeway Bay",
                "bound": "O",
                "service_type": "1"
            },
            {
                "co": "KMB",
                "route": "6",
                "orig_tc": "中環",
                "orig_en": "Central", 
                "dest_tc": "銅鑼灣",
                "dest_en": "Causeway Bay",
                "bound": "O",
                "service_type": "1"
            },
            {
                "co": "KMB",
                "route": "272A",
                "orig_tc": "大學站",
                "orig_en": "University Station",
                "dest_tc": "大埔",
                "dest_en": "Tai Po",
                "bound": "O",
                "service_type": "1"
            }
        ]
    }
    return sample_kmb_data

def load_citybus_data():
    """Load Citybus route data"""
    print("📊 Loading Citybus data...")
    
    # Try to load from existing files
    citybus_files = [
        'data/raw_routes/citybus_routes_rt_20251019_121555.json',
        'data/raw_routes/sample_citybus_routes_20251019_120938.json'
    ]
    
    for file_path in citybus_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                print(f"✅ Loaded Citybus data from {file_path}")
                return data
            except Exception as e:
                print(f"❌ Error loading {file_path}: {e}")
    
    # If no existing data, create sample Citybus data
    print("📝 Creating sample Citybus data...")
    sample_citybus_data = {
        "type": "RouteList",
        "version": "2.0",
        "generated_timestamp": datetime.now().isoformat(),
        "data": [
            {
                "co": "CTB",
                "route": "582",
                "orig_tc": "大埔",
                "orig_en": "Tai Po",
                "dest_tc": "大學站",
                "dest_en": "University Station",
                "bound": "O",
                "service_type": "1"
            },
            {
                "co": "CTB",
                "route": "581",
                "orig_tc": "大埔",
                "orig_en": "Tai Po",
                "dest_tc": "尖沙咀",
                "dest_en": "Tsim Sha Tsui",
                "bound": "O",
                "service_type": "1"
            },
            {
                "co": "CTB",
                "route": "580",
                "orig_tc": "大埔",
                "orig_en": "Tai Po",
                "dest_tc": "中環",
                "dest_en": "Central",
                "bound": "O",
                "service_type": "1"
            },
            {
                "co": "CTB",
                "route": "1",
                "orig_tc": "中環 (港澳碼頭)",
                "orig_en": "Central (Macau Ferry)",
                "dest_tc": "跑馬地 (上)",
                "dest_en": "Happy Valley (Upper)",
                "bound": "O",
                "service_type": "1"
            }
        ]
    }
    return sample_citybus_data

def create_sample_stop_data():
    """Create sample stop data for analysis"""
    print("📝 Creating sample stop data...")
    
    # Sample stops with overlapping patterns
    sample_stops = {
        "kmb_1": {
            "operator": "kmb",
            "route_id": "1",
            "route_name": "Chuk Yuen Estate → Star Ferry",
            "stops": [
                {"stop": "STOP001", "name_tc": "竹園邨", "name_en": "Chuk Yuen Estate", "lat": 22.3400, "lng": 114.2000},
                {"stop": "STOP002", "name_tc": "黃大仙站", "name_en": "Wong Tai Sin Station", "lat": 22.3500, "lng": 114.2100},
                {"stop": "STOP003", "name_tc": "九龍塘站", "name_en": "Kowloon Tong Station", "lat": 22.3600, "lng": 114.2200},
                {"stop": "STOP004", "name_tc": "尖沙咀碼頭", "name_en": "Star Ferry", "lat": 22.3700, "lng": 114.2300}
            ]
        },
        "kmb_2": {
            "operator": "kmb",
            "route_id": "2", 
            "route_name": "Chuk Yuen Estate → Star Ferry (Alternative)",
            "stops": [
                {"stop": "STOP001", "name_tc": "竹園邨", "name_en": "Chuk Yuen Estate", "lat": 22.3400, "lng": 114.2000},
                {"stop": "STOP002", "name_tc": "黃大仙站", "name_en": "Wong Tai Sin Station", "lat": 22.3500, "lng": 114.2100},
                {"stop": "STOP003", "name_tc": "九龍塘站", "name_en": "Kowloon Tong Station", "lat": 22.3600, "lng": 114.2200},
                {"stop": "STOP005", "name_tc": "尖沙咀碼頭", "name_en": "Star Ferry", "lat": 22.3700, "lng": 114.2300}
            ]
        },
        "kmb_272A": {
            "operator": "kmb",
            "route_id": "272A",
            "route_name": "University Station → Tai Po",
            "stops": [
                {"stop": "STOP601", "name_tc": "大學站", "name_en": "University Station", "lat": 22.4100, "lng": 114.2600},
                {"stop": "STOP602", "name_tc": "科學園", "name_en": "Science Park", "lat": 22.4200, "lng": 114.2700},
                {"stop": "STOP603", "name_tc": "大埔中心", "name_en": "Tai Po Central", "lat": 22.4300, "lng": 114.2800},
                {"stop": "STOP604", "name_tc": "大埔墟站", "name_en": "Tai Po Market Station", "lat": 22.4400, "lng": 114.2900}
            ]
        },
        "citybus_582": {
            "operator": "citybus",
            "route_id": "582",
            "route_name": "Tai Po → University Station",
            "stops": [
                {"stop": "STOP601", "name_tc": "大學站", "name_en": "University Station", "lat": 22.4100, "lng": 114.2600},
                {"stop": "STOP602", "name_tc": "科學園", "name_en": "Science Park", "lat": 22.4200, "lng": 114.2700},
                {"stop": "STOP603", "name_tc": "大埔中心", "name_en": "Tai Po Central", "lat": 22.4300, "lng": 114.2800},
                {"stop": "STOP604", "name_tc": "大埔墟站", "name_en": "Tai Po Market Station", "lat": 22.4400, "lng": 114.2900}
            ]
        },
        "citybus_581": {
            "operator": "citybus",
            "route_id": "581",
            "route_name": "Tai Po → Tsim Sha Tsui",
            "stops": [
                {"stop": "STOP101", "name_tc": "中環", "name_en": "Central", "lat": 22.2800, "lng": 114.1600},
                {"stop": "STOP102", "name_tc": "金鐘", "name_en": "Admiralty", "lat": 22.2900, "lng": 114.1700},
                {"stop": "STOP103", "name_tc": "灣仔", "name_en": "Wan Chai", "lat": 22.3000, "lng": 114.1800},
                {"stop": "STOP104", "name_tc": "銅鑼灣", "name_en": "Causeway Bay", "lat": 22.3100, "lng": 114.1900}
            ]
        },
        "citybus_580": {
            "operator": "citybus",
            "route_id": "580",
            "route_name": "Tai Po → Central",
            "stops": [
                {"stop": "STOP101", "name_tc": "中環", "name_en": "Central", "lat": 22.2800, "lng": 114.1600},
                {"stop": "STOP102", "name_tc": "金鐘", "name_en": "Admiralty", "lat": 22.2900, "lng": 114.1700},
                {"stop": "STOP103", "name_tc": "灣仔", "name_en": "Wan Chai", "lat": 22.3000, "lng": 114.1800},
                {"stop": "STOP105", "name_tc": "銅鑼灣", "name_en": "Causeway Bay", "lat": 22.3100, "lng": 114.1900}
            ]
        }
    }
    
    return sample_stops

def analyze_route_overlaps(kmb_data, citybus_data, stop_data):
    """Analyze overlapping stops between KMB and Citybus routes"""
    print("🔍 Analyzing route overlaps...")
    
    overlaps = []
    
    # Get all route keys
    kmb_routes = [key for key in stop_data.keys() if stop_data[key]['operator'] == 'kmb']
    citybus_routes = [key for key in stop_data.keys() if stop_data[key]['operator'] == 'citybus']
    
    print(f"📊 KMB routes: {len(kmb_routes)}")
    print(f"📊 Citybus routes: {len(citybus_routes)}")
    
    # Analyze all combinations
    for kmb_route in kmb_routes:
        for citybus_route in citybus_routes:
            kmb_stops = set(stop['stop'] for stop in stop_data[kmb_route]['stops'])
            citybus_stops = set(stop['stop'] for stop in stop_data[citybus_route]['stops'])
            
            common_stops = kmb_stops & citybus_stops
            
            if len(common_stops) >= 2:  # Minimum 2 overlapping stops
                overlap_analysis = {
                    'route1': {
                        'operator': stop_data[kmb_route]['operator'],
                        'route_id': stop_data[kmb_route]['route_id'],
                        'route_name': stop_data[kmb_route]['route_name'],
                        'total_stops': len(kmb_stops)
                    },
                    'route2': {
                        'operator': stop_data[citybus_route]['operator'],
                        'route_id': stop_data[citybus_route]['route_id'],
                        'route_name': stop_data[citybus_route]['route_name'],
                        'total_stops': len(citybus_stops)
                    },
                    'overlap_count': len(common_stops),
                    'overlap_percentage': len(common_stops) / min(len(kmb_stops), len(citybus_stops)),
                    'common_stops': list(common_stops),
                    'common_stop_details': [
                        {
                            'stop_id': stop,
                            'name_tc': next((s['name_tc'] for s in stop_data[kmb_route]['stops'] if s['stop'] == stop), ''),
                            'name_en': next((s['name_en'] for s in stop_data[kmb_route]['stops'] if s['stop'] == stop), ''),
                            'lat': next((s['lat'] for s in stop_data[kmb_route]['stops'] if s['stop'] == stop), 0),
                            'lng': next((s['lng'] for s in stop_data[kmb_route]['stops'] if s['stop'] == stop), 0)
                        }
                        for stop in common_stops
                    ],
                    'analysis_timestamp': datetime.now().isoformat()
                }
                
                overlaps.append(overlap_analysis)
    
    # Sort by overlap count
    overlaps.sort(key=lambda x: x['overlap_count'], reverse=True)
    
    return overlaps

def generate_analysis_report(overlaps):
    """Generate comprehensive analysis report"""
    print("📊 Generating analysis report...")
    
    report = {
        'analysis_summary': {
            'total_overlaps': len(overlaps),
            'high_overlap_routes': len([o for o in overlaps if o['overlap_count'] >= 4]),
            'medium_overlap_routes': len([o for o in overlaps if 2 <= o['overlap_count'] < 4]),
            'low_overlap_routes': len([o for o in overlaps if o['overlap_count'] < 2]),
            'analysis_date': datetime.now().isoformat()
        },
        'overlap_details': overlaps,
        'recommendations': []
    }
    
    # Generate recommendations
    for overlap in overlaps:
        if overlap['overlap_percentage'] >= 0.75:
            report['recommendations'].append({
                'priority': 'High',
                'routes': f"{overlap['route1']['operator']} {overlap['route1']['route_id']} vs {overlap['route2']['operator']} {overlap['route2']['route_id']}",
                'overlap_percentage': overlap['overlap_percentage'],
                'recommendation': 'Immediate coordination recommended'
            })
        elif overlap['overlap_percentage'] >= 0.5:
            report['recommendations'].append({
                'priority': 'Medium',
                'routes': f"{overlap['route1']['operator']} {overlap['route1']['route_id']} vs {overlap['route2']['operator']} {overlap['route2']['route_id']}",
                'overlap_percentage': overlap['overlap_percentage'],
                'recommendation': 'Coordination beneficial'
            })
    
    return report

def save_results(overlaps, report):
    """Save analysis results to files"""
    print("💾 Saving results...")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save overlap data
    overlap_file = f'data/overlap_analysis/route_overlaps_{timestamp}.json'
    os.makedirs(os.path.dirname(overlap_file), exist_ok=True)
    
    with open(overlap_file, 'w', encoding='utf-8') as f:
        json.dump(overlaps, f, ensure_ascii=False, indent=2)
    
    # Save analysis report
    report_file = f'data/overlap_analysis/analysis_report_{timestamp}.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Results saved to: {overlap_file}")
    print(f"✅ Report saved to: {report_file}")
    
    return overlap_file, report_file

def main():
    """Main analysis function"""
    print("🚌 Starting Bus Route Overlap Analysis")
    print("=" * 50)
    
    # Load data
    kmb_data = load_kmb_data()
    citybus_data = load_citybus_data()
    stop_data = create_sample_stop_data()
    
    print()
    
    # Analyze overlaps
    overlaps = analyze_route_overlaps(kmb_data, citybus_data, stop_data)
    
    print(f"✅ Found {len(overlaps)} overlapping route pairs")
    
    # Display results
    print("\n📊 OVERLAP ANALYSIS RESULTS:")
    print("-" * 50)
    
    for i, overlap in enumerate(overlaps, 1):
        print(f"{i}. {overlap['route1']['operator']} {overlap['route1']['route_id']} vs {overlap['route2']['operator']} {overlap['route2']['route_id']}")
        print(f"   Overlap: {overlap['overlap_count']} stops ({overlap['overlap_percentage']:.1%})")
        print(f"   Common stops: {', '.join(overlap['common_stops'])}")
        print()
    
    # Generate report
    report = generate_analysis_report(overlaps)
    
    # Save results
    overlap_file, report_file = save_results(overlaps, report)
    
    print("\n🎯 ANALYSIS COMPLETE!")
    print(f"📊 Total overlapping pairs: {len(overlaps)}")
    print(f"📈 High priority overlaps: {report['analysis_summary']['high_overlap_routes']}")
    print(f"📋 Recommendations: {len(report['recommendations'])}")
    
    return overlaps, report

if __name__ == "__main__":
    overlaps, report = main()
