#!/usr/bin/env python3
"""
Comprehensive Bus Route Overlap Analyzer
Analyzes overlaps between KMB and Citybus routes using collected data
"""

import json
import csv
import pandas as pd
from datetime import datetime
import os
from collections import defaultdict

class OverlapAnalyzer:
    def __init__(self, data_dir="data/comprehensive_analysis"):
        self.data_dir = data_dir
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results_dir = f"{data_dir}/analysis"
        os.makedirs(self.results_dir, exist_ok=True)
        
    def load_kmb_data(self):
        """Load KMB data from CSV files"""
        print("📊 Loading KMB data...")
        
        try:
            # Load KMB routes
            kmb_routes_df = pd.read_csv(f"{self.data_dir}/csv_files/kmb_routes_*.csv")
            print(f"✅ Loaded {len(kmb_routes_df)} KMB routes")
            
            # Load KMB stops
            kmb_stops_df = pd.read_csv(f"{self.data_dir}/csv_files/kmb_stops_*.csv")
            print(f"✅ Loaded {len(kmb_stops_df)} KMB stops")
            
            # Load KMB route-stops
            kmb_route_stops_df = pd.read_csv(f"{self.data_dir}/csv_files/kmb_route_stops_*.csv")
            print(f"✅ Loaded {len(kmb_route_stops_df)} KMB route-stops")
            
            return kmb_routes_df, kmb_stops_df, kmb_route_stops_df
            
        except Exception as e:
            print(f"❌ Error loading KMB data: {str(e)}")
            return None, None, None
    
    def load_citybus_data(self):
        """Load Citybus data from CSV files"""
        print("📊 Loading Citybus data...")
        
        try:
            # Load Citybus routes
            citybus_routes_df = pd.read_csv(f"{self.data_dir}/csv_files/citybus_routes_*.csv")
            print(f"✅ Loaded {len(citybus_routes_df)} Citybus routes")
            
            return citybus_routes_df
            
        except Exception as e:
            print(f"❌ Error loading Citybus data: {str(e)}")
            return None
    
    def create_route_stop_mapping(self, kmb_route_stops_df, kmb_stops_df):
        """Create route to stops mapping for KMB"""
        print("🔍 Creating KMB route-stop mapping...")
        
        route_stops = defaultdict(list)
        
        for _, row in kmb_route_stops_df.iterrows():
            route_id = row['route']
            stop_id = row['stop']
            seq = row['seq']
            
            # Get stop details
            stop_info = kmb_stops_df[kmb_stops_df['stop'] == stop_id]
            if not stop_info.empty:
                stop_details = stop_info.iloc[0]
                route_stops[route_id].append({
                    'stop': stop_id,
                    'seq': seq,
                    'name_en': stop_details.get('name_en', ''),
                    'name_tc': stop_details.get('name_tc', ''),
                    'lat': stop_details.get('lat', 0),
                    'long': stop_details.get('long', 0)
                })
        
        print(f"✅ Created route-stop mapping for {len(route_stops)} KMB routes")
        return route_stops
    
    def find_route_overlaps(self, kmb_route_stops, citybus_routes_df):
        """Find overlaps between KMB routes and Citybus routes"""
        print("🔍 Finding route overlaps...")
        
        overlaps = []
        
        # For each KMB route, find potential Citybus overlaps
        for kmb_route, kmb_stops in kmb_route_stops.items():
            kmb_stop_ids = set(stop['stop'] for stop in kmb_stops)
            
            # Check against all Citybus routes
            for _, citybus_route in citybus_routes_df.iterrows():
                citybus_route_id = citybus_route['route']
                
                # For now, we'll use route names to identify potential overlaps
                # In a real implementation, we'd need Citybus route-stop data
                kmb_orig = kmb_route  # This would be the origin from route data
                citybus_orig = citybus_route.get('orig_en', '')
                citybus_dest = citybus_route.get('dest_en', '')
                
                # Simple overlap detection based on route names
                if self.detect_potential_overlap(kmb_route, citybus_orig, citybus_dest):
                    overlap = {
                        'kmb_route': kmb_route,
                        'citybus_route': citybus_route_id,
                        'kmb_orig': kmb_orig,
                        'citybus_orig': citybus_orig,
                        'citybus_dest': citybus_dest,
                        'overlap_type': 'potential',
                        'analysis_timestamp': datetime.now().isoformat()
                    }
                    overlaps.append(overlap)
        
        print(f"✅ Found {len(overlaps)} potential overlaps")
        return overlaps
    
    def detect_potential_overlap(self, kmb_route, citybus_orig, citybus_dest):
        """Detect potential overlap based on route information"""
        # Simple heuristic: check if routes serve similar areas
        # This is a placeholder - real implementation would use stop data
        
        # Check for common keywords
        common_areas = [
            'university', 'station', 'central', 'tai po', 'tsim sha tsui',
            'causeway bay', 'mong kok', 'admirality', 'wan chai'
        ]
        
        kmb_lower = kmb_route.lower()
        citybus_orig_lower = citybus_orig.lower()
        citybus_dest_lower = citybus_dest.lower()
        
        for area in common_areas:
            if (area in kmb_lower and area in citybus_orig_lower) or \
               (area in kmb_lower and area in citybus_dest_lower):
                return True
        
        return False
    
    def analyze_kmb_kmb_overlaps(self, kmb_route_stops):
        """Analyze overlaps between KMB routes"""
        print("🔍 Analyzing KMB-KMB overlaps...")
        
        overlaps = []
        kmb_routes = list(kmb_route_stops.keys())
        
        for i in range(len(kmb_routes)):
            for j in range(i + 1, len(kmb_routes)):
                route1 = kmb_routes[i]
                route2 = kmb_routes[j]
                
                stops1 = set(stop['stop'] for stop in kmb_route_stops[route1])
                stops2 = set(stop['stop'] for stop in kmb_route_stops[route2])
                
                common_stops = stops1 & stops2
                
                if len(common_stops) >= 2:  # Minimum 2 overlapping stops
                    overlap = {
                        'route1': route1,
                        'route2': route2,
                        'route1_stops': len(stops1),
                        'route2_stops': len(stops2),
                        'overlap_count': len(common_stops),
                        'overlap_percentage': len(common_stops) / min(len(stops1), len(stops2)),
                        'common_stops': list(common_stops),
                        'overlap_type': 'kmb_kmb',
                        'analysis_timestamp': datetime.now().isoformat()
                    }
                    overlaps.append(overlap)
        
        print(f"✅ Found {len(overlaps)} KMB-KMB overlaps")
        return overlaps
    
    def create_overlap_csv(self, overlaps, filename):
        """Create CSV file for overlaps"""
        print(f"📊 Creating overlap CSV: {filename}")
        
        csv_file = f"{self.results_dir}/{filename}_{self.timestamp}.csv"
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            if overlaps:
                # Write header based on first overlap
                headers = list(overlaps[0].keys())
                writer.writerow(headers)
                
                # Write data
                for overlap in overlaps:
                    writer.writerow([overlap.get(header, '') for header in headers])
        
        print(f"✅ Overlap CSV created: {csv_file}")
        return csv_file
    
    def generate_analysis_report(self, kmb_overlaps, kmb_citybus_overlaps):
        """Generate comprehensive analysis report"""
        print("📊 Generating analysis report...")
        
        report = {
            'analysis_summary': {
                'total_kmb_overlaps': len(kmb_overlaps),
                'total_kmb_citybus_overlaps': len(kmb_citybus_overlaps),
                'high_overlap_routes': len([o for o in kmb_overlaps if o.get('overlap_percentage', 0) >= 0.75]),
                'medium_overlap_routes': len([o for o in kmb_overlaps if 0.5 <= o.get('overlap_percentage', 0) < 0.75]),
                'low_overlap_routes': len([o for o in kmb_overlaps if o.get('overlap_percentage', 0) < 0.5]),
                'analysis_date': datetime.now().isoformat()
            },
            'kmb_overlaps': kmb_overlaps,
            'kmb_citybus_overlaps': kmb_citybus_overlaps,
            'recommendations': []
        }
        
        # Generate recommendations
        for overlap in kmb_overlaps:
            if overlap.get('overlap_percentage', 0) >= 0.75:
                report['recommendations'].append({
                    'priority': 'High',
                    'routes': f"KMB {overlap['route1']} vs KMB {overlap['route2']}",
                    'overlap_percentage': overlap['overlap_percentage'],
                    'recommendation': 'Immediate coordination recommended'
                })
        
        # Save report
        report_file = f"{self.results_dir}/analysis_report_{self.timestamp}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Analysis report created: {report_file}")
        return report_file
    
    def run_comprehensive_analysis(self):
        """Run comprehensive overlap analysis"""
        print("🚌 Starting Comprehensive Overlap Analysis")
        print("=" * 60)
        
        # Load data
        kmb_routes_df, kmb_stops_df, kmb_route_stops_df = self.load_kmb_data()
        citybus_routes_df = self.load_citybus_data()
        
        if kmb_route_stops_df is None or citybus_routes_df is None:
            print("❌ Cannot proceed - missing data")
            return
        
        # Create route-stop mapping
        kmb_route_stops = self.create_route_stop_mapping(kmb_route_stops_df, kmb_stops_df)
        
        # Analyze overlaps
        print("\n🔍 ANALYZING OVERLAPS")
        print("-" * 30)
        
        # KMB-KMB overlaps
        kmb_overlaps = self.analyze_kmb_kmb_overlaps(kmb_route_stops)
        
        # KMB-Citybus overlaps (potential)
        kmb_citybus_overlaps = self.find_route_overlaps(kmb_route_stops, citybus_routes_df)
        
        # Create CSV files
        print("\n📊 CREATING CSV FILES")
        print("-" * 30)
        
        kmb_overlaps_csv = self.create_overlap_csv(kmb_overlaps, "kmb_overlaps")
        kmb_citybus_overlaps_csv = self.create_overlap_csv(kmb_citybus_overlaps, "kmb_citybus_overlaps")
        
        # Generate report
        report_file = self.generate_analysis_report(kmb_overlaps, kmb_citybus_overlaps)
        
        # Summary
        print("\n🎯 ANALYSIS SUMMARY")
        print("=" * 60)
        print(f"KMB-KMB Overlaps: {len(kmb_overlaps)}")
        print(f"KMB-Citybus Overlaps: {len(kmb_citybus_overlaps)}")
        print(f"High Priority Routes: {len([o for o in kmb_overlaps if o.get('overlap_percentage', 0) >= 0.75])}")
        print(f"\nFiles Created:")
        print(f"  - {kmb_overlaps_csv}")
        print(f"  - {kmb_citybus_overlaps_csv}")
        print(f"  - {report_file}")
        
        return {
            'kmb_overlaps': kmb_overlaps,
            'kmb_citybus_overlaps': kmb_citybus_overlaps,
            'csv_files': {
                'kmb_overlaps': kmb_overlaps_csv,
                'kmb_citybus_overlaps': kmb_citybus_overlaps_csv
            },
            'report_file': report_file
        }

def main():
    """Main function"""
    analyzer = OverlapAnalyzer()
    results = analyzer.run_comprehensive_analysis()
    
    print(f"\n🎉 Analysis completed!")
    print(f"📁 Results saved in: {analyzer.results_dir}")
    
    return results

if __name__ == "__main__":
    results = main()
