#!/usr/bin/env python3
"""
Cross-Operator Overlap Analysis
Identify similar cases between KMB and Citybus routes
"""

import pandas as pd
import json
from datetime import datetime
import re

print("🔍 CROSS-OPERATOR OVERLAP ANALYSIS")
print("=" * 80)
print(f"📅 Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("🚌 Identifying KMB ↔ Citybus overlaps")
print("=" * 80)

def load_data():
    """Load all data files"""
    print("📊 Loading data files...")
    
    # Load KMB data
    kmb_routes = pd.read_csv("data/collected_data/kmb_all_routes_20251019_142825.csv")
    kmb_stops = pd.read_csv("data/collected_data/kmb_all_stops_20251019_142825.csv")
    kmb_mappings = pd.read_csv("data/collected_data/route_stop_mappings_20251019_142825.csv")
    
    # Load Citybus data
    citybus_routes = pd.read_csv("data/collected_data/citybus_routes_20251019_144804.csv")
    citybus_stops = pd.read_csv("data/collected_data/citybus_stops_20251019_144804.csv")
    citybus_mappings = pd.read_csv("data/collected_data/citybus_route_stops_20251019_144804.csv")
    
    print(f"✅ KMB routes: {len(kmb_routes)}")
    print(f"✅ KMB stops: {len(kmb_stops)}")
    print(f"✅ KMB mappings: {len(kmb_mappings)}")
    print(f"✅ Citybus routes: {len(citybus_routes)}")
    print(f"✅ Citybus stops: {len(citybus_stops)}")
    print(f"✅ Citybus mappings: {len(citybus_mappings)}")
    
    return kmb_routes, kmb_stops, kmb_mappings, citybus_routes, citybus_stops, citybus_mappings

def analyze_route_names(kmb_routes, citybus_routes):
    """Analyze route names for similarities"""
    print("\n🔍 ANALYZING ROUTE NAMES")
    print("=" * 50)
    
    similarities = []
    
    for _, kmb_route in kmb_routes.iterrows():
        kmb_route_num = kmb_route['route']
        kmb_orig_en = str(kmb_route['orig_en']).lower()
        kmb_dest_en = str(kmb_route['dest_en']).lower()
        kmb_orig_tc = str(kmb_route['orig_tc']).lower()
        kmb_dest_tc = str(kmb_route['dest_tc']).lower()
        
        for _, citybus_route in citybus_routes.iterrows():
            citybus_route_num = citybus_route['route']
            citybus_orig_en = str(citybus_route['orig_en']).lower()
            citybus_dest_en = str(citybus_route['dest_en']).lower()
            citybus_orig_tc = str(citybus_route['orig_tc']).lower()
            citybus_dest_tc = str(citybus_route['dest_tc']).lower()
            
            # Check for origin matches
            origin_match = False
            if (kmb_orig_en in citybus_orig_en or citybus_orig_en in kmb_orig_en or
                kmb_orig_tc in citybus_orig_tc or citybus_orig_tc in kmb_orig_tc):
                origin_match = True
            
            # Check for destination matches
            dest_match = False
            if (kmb_dest_en in citybus_dest_en or citybus_dest_en in kmb_dest_en or
                kmb_dest_tc in citybus_dest_tc or citybus_dest_tc in kmb_dest_tc):
                dest_match = True
            
            # Check for cross matches (KMB origin with Citybus destination)
            cross_match = False
            if (kmb_orig_en in citybus_dest_en or citybus_dest_en in kmb_orig_en or
                kmb_orig_tc in citybus_dest_tc or citybus_dest_tc in kmb_orig_tc):
                cross_match = True
            
            if origin_match or dest_match or cross_match:
                similarities.append({
                    'kmb_route': kmb_route_num,
                    'citybus_route': citybus_route_num,
                    'kmb_orig_en': kmb_route['orig_en'],
                    'kmb_dest_en': kmb_route['dest_en'],
                    'citybus_orig_en': citybus_route['orig_en'],
                    'citybus_dest_en': citybus_route['dest_en'],
                    'origin_match': origin_match,
                    'dest_match': dest_match,
                    'cross_match': cross_match,
                    'match_type': 'name_similarity'
                })
    
    print(f"📊 Found {len(similarities)} route name similarities")
    return similarities

def analyze_geographic_areas(kmb_routes, citybus_routes):
    """Analyze geographic areas served"""
    print("\n🔍 ANALYZING GEOGRAPHIC AREAS")
    print("=" * 50)
    
    # Define key geographic areas
    areas = {
        'university': ['university', '大學', '大学'],
        'science_park': ['science park', '科學園', '科学园', 'pak shek kok', '白石角'],
        'sai_sha': ['sai sha', '西沙', 'shap sze heung', '十四鄉', '十四乡'],
        'central': ['central', '中環', '中环'],
        'tsim_sha_tsui': ['tsim sha tsui', '尖沙咀', '尖沙咀'],
        'kowloon_bay': ['kowloon bay', '九龍灣', '九龙湾'],
        'kwun_tong': ['kwun tong', '觀塘', '观塘'],
        'mei_foo': ['mei foo', '美孚'],
        'sham_shui_po': ['sham shui po', '深水埗', '深水埗']
    }
    
    geographic_matches = []
    
    for _, kmb_route in kmb_routes.iterrows():
        kmb_route_num = kmb_route['route']
        kmb_orig = str(kmb_route['orig_en']).lower()
        kmb_dest = str(kmb_route['dest_en']).lower()
        
        for _, citybus_route in citybus_routes.iterrows():
            citybus_route_num = citybus_route['route']
            citybus_orig = str(citybus_route['orig_en']).lower()
            citybus_dest = str(citybus_route['dest_en']).lower()
            
            # Check for area matches
            for area, keywords in areas.items():
                kmb_orig_match = any(keyword in kmb_orig for keyword in keywords)
                kmb_dest_match = any(keyword in kmb_dest for keyword in keywords)
                citybus_orig_match = any(keyword in citybus_orig for keyword in keywords)
                citybus_dest_match = any(keyword in citybus_dest for keyword in keywords)
                
                if (kmb_orig_match and citybus_orig_match) or (kmb_dest_match and citybus_dest_match) or \
                   (kmb_orig_match and citybus_dest_match) or (kmb_dest_match and citybus_orig_match):
                    geographic_matches.append({
                        'kmb_route': kmb_route_num,
                        'citybus_route': citybus_route_num,
                        'area': area,
                        'kmb_orig_en': kmb_route['orig_en'],
                        'kmb_dest_en': kmb_route['dest_en'],
                        'citybus_orig_en': citybus_route['orig_en'],
                        'citybus_dest_en': citybus_route['dest_en'],
                        'match_type': 'geographic_area'
                    })
    
    print(f"📊 Found {len(geographic_matches)} geographic area matches")
    return geographic_matches

def analyze_route_numbers(kmb_routes, citybus_routes):
    """Analyze route numbers for similarities"""
    print("\n🔍 ANALYZING ROUTE NUMBERS")
    print("=" * 50)
    
    number_matches = []
    
    # Get all route numbers
    kmb_numbers = set(kmb_routes['route'].unique())
    citybus_numbers = set(citybus_routes['route'].unique())
    
    # Find common route numbers
    common_numbers = kmb_numbers.intersection(citybus_numbers)
    
    for route_num in common_numbers:
        kmb_route = kmb_routes[kmb_routes['route'] == route_num].iloc[0]
        citybus_route = citybus_routes[citybus_routes['route'] == route_num].iloc[0]
        
        number_matches.append({
            'route_number': route_num,
            'kmb_orig_en': kmb_route['orig_en'],
            'kmb_dest_en': kmb_route['dest_en'],
            'citybus_orig_en': citybus_route['orig_en'],
            'citybus_dest_en': citybus_route['dest_en'],
            'match_type': 'same_route_number'
        })
    
    print(f"📊 Found {len(number_matches)} common route numbers")
    return number_matches

def analyze_specific_cases():
    """Analyze specific known cases"""
    print("\n🔍 ANALYZING SPECIFIC CASES")
    print("=" * 50)
    
    specific_cases = []
    
    # Case 1: 272A ↔ 582 (University Station ↔ Pak Shek Kok ↔ Sai Sha)
    specific_cases.append({
        'kmb_route': '272A',
        'citybus_route': '582',
        'description': 'University Station ↔ Pak Shek Kok ↔ Sai Sha connection',
        'kmb_route_info': 'University Station → Pak Shek Kok',
        'citybus_route_info': 'Pak Shek Kok → Sai Sha and Shap Sze Heung',
        'coordination_type': 'transfer_connection',
        'priority': 'high'
    })
    
    # Case 2: Routes serving similar areas
    specific_cases.append({
        'kmb_route': '1',
        'citybus_route': '1',
        'description': 'Both serve Central area',
        'kmb_route_info': 'Chuk Yuen Estate ↔ Star Ferry',
        'citybus_route_info': 'Central (Macau Ferry) ↔ Happy Valley (Upper)',
        'coordination_type': 'area_overlap',
        'priority': 'medium'
    })
    
    print(f"📊 Identified {len(specific_cases)} specific cases")
    return specific_cases

def save_results(name_similarities, geographic_matches, number_matches, specific_cases):
    """Save analysis results"""
    print("\n💾 SAVING RESULTS")
    print("=" * 50)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save name similarities
    if name_similarities:
        df = pd.DataFrame(name_similarities)
        csv_file = f"analysis_results/cross_operator_name_similarities_{timestamp}.csv"
        df.to_csv(csv_file, index=False)
        print(f"✅ Name similarities saved: {csv_file}")
    
    # Save geographic matches
    if geographic_matches:
        df = pd.DataFrame(geographic_matches)
        csv_file = f"analysis_results/cross_operator_geographic_matches_{timestamp}.csv"
        df.to_csv(csv_file, index=False)
        print(f"✅ Geographic matches saved: {csv_file}")
    
    # Save number matches
    if number_matches:
        df = pd.DataFrame(number_matches)
        csv_file = f"analysis_results/cross_operator_number_matches_{timestamp}.csv"
        df.to_csv(csv_file, index=False)
        print(f"✅ Number matches saved: {csv_file}")
    
    # Save specific cases
    if specific_cases:
        df = pd.DataFrame(specific_cases)
        csv_file = f"analysis_results/cross_operator_specific_cases_{timestamp}.csv"
        df.to_csv(csv_file, index=False)
        print(f"✅ Specific cases saved: {csv_file}")
    
    # Create summary report
    report_file = f"analysis_results/cross_operator_analysis_summary_{timestamp}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# 🔍 CROSS-OPERATOR OVERLAP ANALYSIS SUMMARY\n")
        f.write(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## 📊 **ANALYSIS OVERVIEW**\n\n")
        f.write(f"- **Name Similarities:** {len(name_similarities)} pairs\n")
        f.write(f"- **Geographic Matches:** {len(geographic_matches)} pairs\n")
        f.write(f"- **Common Route Numbers:** {len(number_matches)} pairs\n")
        f.write(f"- **Specific Cases:** {len(specific_cases)} cases\n\n")
        
        f.write("## 🚌 **KEY FINDINGS**\n\n")
        
        if specific_cases:
            f.write("### High Priority Cases:\n")
            for case in specific_cases:
                f.write(f"- **{case['kmb_route']} ↔ {case['citybus_route']}**: {case['description']}\n")
                f.write(f"  - KMB: {case['kmb_route_info']}\n")
                f.write(f"  - Citybus: {case['citybus_route_info']}\n")
                f.write(f"  - Type: {case['coordination_type']}\n\n")
        
        if number_matches:
            f.write("### Common Route Numbers:\n")
            for match in number_matches:
                f.write(f"- **Route {match['route_number']}**:\n")
                f.write(f"  - KMB: {match['kmb_orig_en']} ↔ {match['kmb_dest_en']}\n")
                f.write(f"  - Citybus: {match['citybus_orig_en']} ↔ {match['citybus_dest_en']}\n\n")
        
        f.write("## 💡 **COORDINATION OPPORTUNITIES**\n\n")
        f.write("### Transfer Connections:\n")
        f.write("- **272A ↔ 582**: University Station → Pak Shek Kok → Sai Sha\n")
        f.write("  - Creates seamless connection from University to Sai Sha area\n")
        f.write("  - Pak Shek Kok serves as transfer point\n\n")
        
        f.write("### Area Coordination:\n")
        f.write("- Routes serving similar geographic areas\n")
        f.write("- Potential for coordinated scheduling\n")
        f.write("- Reduced service gaps in key areas\n\n")
        
        f.write("### Benefits:\n")
        f.write("- **Enhanced Connectivity**: Better transfer options\n")
        f.write("- **Reduced Travel Time**: Seamless connections\n")
        f.write("- **Improved Service**: Coordinated operations\n")
        f.write("- **Cost Efficiency**: Optimized route coverage\n")
    
    print(f"✅ Summary report saved: {report_file}")

def main():
    """Main analysis function"""
    try:
        # Load data
        kmb_routes, kmb_stops, kmb_mappings, citybus_routes, citybus_stops, citybus_mappings = load_data()
        
        # Run analyses
        name_similarities = analyze_route_names(kmb_routes, citybus_routes)
        geographic_matches = analyze_geographic_areas(kmb_routes, citybus_routes)
        number_matches = analyze_route_numbers(kmb_routes, citybus_routes)
        specific_cases = analyze_specific_cases()
        
        # Save results
        save_results(name_similarities, geographic_matches, number_matches, specific_cases)
        
        print("\n" + "=" * 80)
        print("🎉 CROSS-OPERATOR ANALYSIS COMPLETED!")
        print("=" * 80)
        print("📊 Check analysis_results/ folder for detailed results")
        print("📁 CSV files: name_similarities, geographic_matches, number_matches, specific_cases")
        print("📄 Summary report: cross_operator_analysis_summary")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()
