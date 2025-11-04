#!/usr/bin/env python3
"""
Comprehensive Overlap Analysis Script
Analyze route overlaps between KMB and Citybus based on collected data
"""

import pandas as pd
import json
from datetime import datetime
import os

print("🔍 COMPREHENSIVE OVERLAP ANALYSIS")
print("=" * 80)
print(f"📅 Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

# Create output directory
os.makedirs("analysis_results", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def load_data():
    """Load all available data files"""
    print("📊 Loading data files...")
    
    # Load KMB data
    kmb_routes = pd.read_csv("data/collected_data/kmb_all_routes_20251019_142825.csv")
    kmb_stops = pd.read_csv("data/collected_data/kmb_all_stops_20251019_142825.csv")
    kmb_mappings = pd.read_csv("data/collected_data/route_stop_mappings_20251019_142825.csv")
    
    # Load Citybus data
    citybus_routes = pd.read_csv("data/collected_data/citybus_all_routes_20251019_144031.csv")
    citybus_mappings = pd.read_csv("data/collected_data/citybus_route_stop_mappings_20251019_144031.csv")
    
    print(f"✅ KMB Routes: {len(kmb_routes)} routes")
    print(f"✅ KMB Stops: {len(kmb_stops)} stops")
    print(f"✅ KMB Mappings: {len(kmb_mappings)} mappings")
    print(f"✅ Citybus Routes: {len(citybus_routes)} routes")
    print(f"✅ Citybus Mappings: {len(citybus_mappings)} mappings")
    
    return kmb_routes, kmb_stops, kmb_mappings, citybus_routes, citybus_mappings

def analyze_kmb_overlaps(kmb_mappings):
    """Analyze KMB route overlaps"""
    print("\n🚌 ANALYZING KMB ROUTE OVERLAPS")
    print("=" * 50)
    
    # Get unique routes
    kmb_routes = kmb_mappings['route'].unique()
    print(f"📊 Analyzing {len(kmb_routes)} KMB routes")
    
    overlaps = []
    
    for i, route1 in enumerate(kmb_routes):
        for j, route2 in enumerate(kmb_routes):
            if i < j:  # Avoid duplicates
                # Get stops for each route
                stops1 = set(kmb_mappings[kmb_mappings['route'] == route1]['stop_id'])
                stops2 = set(kmb_mappings[kmb_mappings['route'] == route2]['stop_id'])
                
                # Find common stops
                common_stops = stops1.intersection(stops2)
                
                if len(common_stops) > 0:
                    overlap_percentage = (len(common_stops) / min(len(stops1), len(stops2))) * 100
                    overlaps.append({
                        'route1': route1,
                        'route2': route2,
                        'common_stops': len(common_stops),
                        'overlap_percentage': round(overlap_percentage, 2),
                        'stops1_total': len(stops1),
                        'stops2_total': len(stops2)
                    })
    
    # Sort by overlap percentage
    overlaps.sort(key=lambda x: x['overlap_percentage'], reverse=True)
    
    print(f"📊 Found {len(overlaps)} overlapping KMB route pairs")
    
    # Show top overlaps
    print("\n🔝 TOP KMB OVERLAPS:")
    for i, overlap in enumerate(overlaps[:10]):
        print(f"   {i+1}. {overlap['route1']} ↔ {overlap['route2']}: {overlap['overlap_percentage']}% ({overlap['common_stops']} stops)")
    
    return overlaps

def analyze_citybus_overlaps(citybus_mappings):
    """Analyze Citybus route overlaps"""
    print("\n🚌 ANALYZING CITYBUS ROUTE OVERLAPS")
    print("=" * 50)
    
    # Get unique routes
    citybus_routes = citybus_mappings['route'].unique()
    print(f"📊 Analyzing {len(citybus_routes)} Citybus routes")
    
    overlaps = []
    
    for i, route1 in enumerate(citybus_routes):
        for j, route2 in enumerate(citybus_routes):
            if i < j:  # Avoid duplicates
                # Get stops for each route
                stops1 = set(citybus_mappings[citybus_mappings['route'] == route1]['stop_id'])
                stops2 = set(citybus_mappings[citybus_mappings['route'] == route2]['stop_id'])
                
                # Find common stops
                common_stops = stops1.intersection(stops2)
                
                if len(common_stops) > 0:
                    overlap_percentage = (len(common_stops) / min(len(stops1), len(stops2))) * 100
                    overlaps.append({
                        'route1': route1,
                        'route2': route2,
                        'common_stops': len(common_stops),
                        'overlap_percentage': round(overlap_percentage, 2),
                        'stops1_total': len(stops1),
                        'stops2_total': len(stops2)
                    })
    
    # Sort by overlap percentage
    overlaps.sort(key=lambda x: x['overlap_percentage'], reverse=True)
    
    print(f"📊 Found {len(overlaps)} overlapping Citybus route pairs")
    
    # Show top overlaps
    print("\n🔝 TOP CITYBUS OVERLAPS:")
    for i, overlap in enumerate(overlaps[:10]):
        print(f"   {i+1}. {overlap['route1']} ↔ {overlap['route2']}: {overlap['overlap_percentage']}% ({overlap['common_stops']} stops)")
    
    return overlaps

def analyze_cross_operator_overlaps(kmb_mappings, citybus_mappings):
    """Analyze overlaps between KMB and Citybus routes"""
    print("\n🚌 ANALYZING CROSS-OPERATOR OVERLAPS")
    print("=" * 50)
    
    # Get unique routes
    kmb_routes = kmb_mappings['route'].unique()
    citybus_routes = citybus_mappings['route'].unique()
    
    print(f"📊 Analyzing {len(kmb_routes)} KMB routes vs {len(citybus_routes)} Citybus routes")
    
    overlaps = []
    
    for kmb_route in kmb_routes:
        for citybus_route in citybus_routes:
            # Get stops for each route
            kmb_stops = set(kmb_mappings[kmb_mappings['route'] == kmb_route]['stop_id'])
            citybus_stops = set(citybus_mappings[citybus_mappings['route'] == citybus_route]['stop_id'])
            
            # Find common stops
            common_stops = kmb_stops.intersection(citybus_stops)
            
            if len(common_stops) > 0:
                overlap_percentage = (len(common_stops) / min(len(kmb_stops), len(citybus_stops))) * 100
                overlaps.append({
                    'kmb_route': kmb_route,
                    'citybus_route': citybus_route,
                    'common_stops': len(common_stops),
                    'overlap_percentage': round(overlap_percentage, 2),
                    'kmb_stops_total': len(kmb_stops),
                    'citybus_stops_total': len(citybus_stops)
                })
    
    # Sort by overlap percentage
    overlaps.sort(key=lambda x: x['overlap_percentage'], reverse=True)
    
    print(f"📊 Found {len(overlaps)} cross-operator overlapping route pairs")
    
    # Show top overlaps
    print("\n🔝 TOP CROSS-OPERATOR OVERLAPS:")
    for i, overlap in enumerate(overlaps[:10]):
        print(f"   {i+1}. KMB {overlap['kmb_route']} ↔ Citybus {overlap['citybus_route']}: {overlap['overlap_percentage']}% ({overlap['common_stops']} stops)")
    
    return overlaps

def save_results(kmb_overlaps, citybus_overlaps, cross_operator_overlaps):
    """Save analysis results to CSV files"""
    print("\n💾 SAVING ANALYSIS RESULTS")
    print("=" * 50)
    
    # Save KMB overlaps
    if kmb_overlaps:
        kmb_df = pd.DataFrame(kmb_overlaps)
        kmb_file = f"analysis_results/kmb_overlaps_{timestamp}.csv"
        kmb_df.to_csv(kmb_file, index=False)
        print(f"✅ KMB overlaps saved: {kmb_file}")
    
    # Save Citybus overlaps
    if citybus_overlaps:
        citybus_df = pd.DataFrame(citybus_overlaps)
        citybus_file = f"analysis_results/citybus_overlaps_{timestamp}.csv"
        citybus_df.to_csv(citybus_file, index=False)
        print(f"✅ Citybus overlaps saved: {citybus_file}")
    
    # Save cross-operator overlaps
    if cross_operator_overlaps:
        cross_df = pd.DataFrame(cross_operator_overlaps)
        cross_file = f"analysis_results/cross_operator_overlaps_{timestamp}.csv"
        cross_df.to_csv(cross_file, index=False)
        print(f"✅ Cross-operator overlaps saved: {cross_file}")

def generate_summary_report(kmb_overlaps, citybus_overlaps, cross_operator_overlaps):
    """Generate comprehensive summary report"""
    print("\n📊 GENERATING SUMMARY REPORT")
    print("=" * 50)
    
    report_file = f"analysis_results/overlap_analysis_summary_{timestamp}.md"
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# 🔍 COMPREHENSIVE OVERLAP ANALYSIS SUMMARY\n")
        f.write(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## 📊 **ANALYSIS OVERVIEW**\n\n")
        f.write(f"- **KMB Route Overlaps:** {len(kmb_overlaps)} pairs\n")
        f.write(f"- **Citybus Route Overlaps:** {len(citybus_overlaps)} pairs\n")
        f.write(f"- **Cross-Operator Overlaps:** {len(cross_operator_overlaps)} pairs\n\n")
        
        f.write("## 🚌 **KMB ROUTE OVERLAPS**\n\n")
        if kmb_overlaps:
            f.write("### Top 10 KMB Overlaps:\n")
            for i, overlap in enumerate(kmb_overlaps[:10]):
                f.write(f"{i+1}. **{overlap['route1']} ↔ {overlap['route2']}**: {overlap['overlap_percentage']}% ({overlap['common_stops']} stops)\n")
        else:
            f.write("No significant KMB overlaps found.\n")
        f.write("\n")
        
        f.write("## 🚌 **CITYBUS ROUTE OVERLAPS**\n\n")
        if citybus_overlaps:
            f.write("### Top 10 Citybus Overlaps:\n")
            for i, overlap in enumerate(citybus_overlaps[:10]):
                f.write(f"{i+1}. **{overlap['route1']} ↔ {overlap['route2']}**: {overlap['overlap_percentage']}% ({overlap['common_stops']} stops)\n")
        else:
            f.write("No significant Citybus overlaps found.\n")
        f.write("\n")
        
        f.write("## 🚌 **CROSS-OPERATOR OVERLAPS**\n\n")
        if cross_operator_overlaps:
            f.write("### Top 10 Cross-Operator Overlaps:\n")
            for i, overlap in enumerate(cross_operator_overlaps[:10]):
                f.write(f"{i+1}. **KMB {overlap['kmb_route']} ↔ Citybus {overlap['citybus_route']}**: {overlap['overlap_percentage']}% ({overlap['common_stops']} stops)\n")
        else:
            f.write("No significant cross-operator overlaps found.\n")
        f.write("\n")
        
        f.write("## 💡 **RECOMMENDATIONS**\n\n")
        f.write("### High Priority Coordination Opportunities:\n")
        
        # Find high overlap routes
        high_overlap_routes = []
        for overlap in kmb_overlaps + citybus_overlaps + cross_operator_overlaps:
            if overlap['overlap_percentage'] > 50:
                high_overlap_routes.append(overlap)
        
        if high_overlap_routes:
            f.write("Routes with >50% overlap:\n")
            for overlap in high_overlap_routes[:5]:
                if 'kmb_route' in overlap:
                    f.write(f"- KMB {overlap['kmb_route']} ↔ Citybus {overlap['citybus_route']}\n")
                else:
                    f.write(f"- {overlap['route1']} ↔ {overlap['route2']}\n")
        else:
            f.write("No routes with >50% overlap found.\n")
        
        f.write("\n### Coordination Benefits:\n")
        f.write("- **Reduced Redundancy**: Eliminate duplicate services\n")
        f.write("- **Improved Efficiency**: Optimize route coverage\n")
        f.write("- **Better Service**: Enhanced passenger experience\n")
        f.write("- **Cost Savings**: Reduced operational costs\n")
    
    print(f"✅ Summary report saved: {report_file}")

def main():
    """Main analysis function"""
    try:
        # Load data
        kmb_routes, kmb_stops, kmb_mappings, citybus_routes, citybus_mappings = load_data()
        
        # Analyze overlaps
        kmb_overlaps = analyze_kmb_overlaps(kmb_mappings)
        citybus_overlaps = analyze_citybus_overlaps(citybus_mappings)
        cross_operator_overlaps = analyze_cross_operator_overlaps(kmb_mappings, citybus_mappings)
        
        # Save results
        save_results(kmb_overlaps, citybus_overlaps, cross_operator_overlaps)
        
        # Generate summary report
        generate_summary_report(kmb_overlaps, citybus_overlaps, cross_operator_overlaps)
        
        print("\n" + "=" * 80)
        print("🎉 OVERLAP ANALYSIS COMPLETED!")
        print("=" * 80)
        print("📊 Check analysis_results/ folder for detailed results")
        print("📁 CSV files: kmb_overlaps, citybus_overlaps, cross_operator_overlaps")
        print("📄 Summary report: overlap_analysis_summary")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()
