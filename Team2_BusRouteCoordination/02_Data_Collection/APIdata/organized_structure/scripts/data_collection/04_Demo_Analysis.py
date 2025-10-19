#!/usr/bin/env python3
"""
Team 2: Bus Route Coordination - Demo Analysis Script
Author: Team 2 - Bus Route Coordination
Date: 2024
Purpose: Demonstrate the similar cases analysis functionality
"""

import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def demo_route_collection():
    """
    Demonstrate route collection functionality
    """
    print("\n=== DEMO: Route Collection ===")
    
    try:
        from route_overlap_analyzer import RouteOverlapAnalyzer
        
        analyzer = RouteOverlapAnalyzer()
        
        # Test API connectivity
        print("Testing API connectivity...")
        
        # Try to collect a small sample of routes
        print("Collecting KMB routes...")
        kmb_routes = analyzer.collect_kmb_routes()
        if kmb_routes:
            print(f"✓ Successfully collected {len(kmb_routes)} KMB routes")
            print(f"  Sample route: {kmb_routes[0] if kmb_routes else 'None'}")
        else:
            print("✗ Failed to collect KMB routes")
        
        print("Collecting Citybus routes...")
        citybus_routes = analyzer.collect_citybus_routes()
        if citybus_routes:
            print(f"✓ Successfully collected {len(citybus_routes)} Citybus routes")
            print(f"  Sample route: {citybus_routes[0] if citybus_routes else 'None'}")
        else:
            print("✗ Failed to collect Citybus routes")
        
        return True
        
    except Exception as e:
        print(f"✗ Demo failed: {str(e)}")
        return False

def demo_overlap_analysis():
    """
    Demonstrate overlap analysis with sample data
    """
    print("\n=== DEMO: Overlap Analysis ===")
    
    try:
        from route_overlap_analyzer import RouteOverlapAnalyzer
        
        analyzer = RouteOverlapAnalyzer()
        
        # Create sample route data for demonstration
        sample_routes = {
            'kmb': [
                {'route': '272A', 'dest_tc': 'University Station', 'orig_tc': 'Tai Po'},
                {'route': '271', 'dest_tc': 'Tsim Sha Tsui', 'orig_tc': 'Tai Po'},
                {'route': '270A', 'dest_tc': 'Central', 'orig_tc': 'Tai Po'}
            ],
            'citybus': [
                {'route': '582', 'dest_tc': 'University Station', 'orig_tc': 'Tai Po'},
                {'route': '581', 'dest_tc': 'Tsim Sha Tsui', 'orig_tc': 'Tai Po'},
                {'route': '580', 'dest_tc': 'Central', 'orig_tc': 'Tai Po'}
            ]
        }
        
        # Create sample route stops data
        sample_route_stops = {
            'kmb_272A': {
                'operator': 'kmb',
                'route_id': '272A',
                'route_name': 'University Station',
                'stops': [
                    {'stop': 'STOP001', 'name_tc': 'Tai Po Market'},
                    {'stop': 'STOP002', 'name_tc': 'University Station'},
                    {'stop': 'STOP003', 'name_tc': 'Science Park'}
                ]
            },
            'citybus_582': {
                'operator': 'citybus',
                'route_id': '582',
                'route_name': 'University Station',
                'stops': [
                    {'stop': 'STOP001', 'name_tc': 'Tai Po Market'},
                    {'stop': 'STOP002', 'name_tc': 'University Station'},
                    {'stop': 'STOP004', 'name_tc': 'Science Park'}
                ]
            }
        }
        
        # Set sample data
        analyzer.all_routes = sample_routes
        analyzer.route_stops = sample_route_stops
        
        print("Running overlap analysis with sample data...")
        overlap_results = analyzer.find_route_overlaps(min_overlap=2)
        
        if overlap_results:
            print(f"✓ Found {len(overlap_results)} overlapping route pairs")
            for result in overlap_results:
                print(f"  - {result['route1']['operator']} {result['route1']['route_id']} vs {result['route2']['operator']} {result['route2']['route_id']}: {result['overlap_count']} stops")
        else:
            print("No overlapping routes found in sample data")
        
        return True
        
    except Exception as e:
        print(f"✗ Demo failed: {str(e)}")
        return False

def demo_coordination_analysis():
    """
    Demonstrate coordination analysis functionality
    """
    print("\n=== DEMO: Coordination Analysis ===")
    
    try:
        from coordination_analyzer import CoordinationAnalyzer
        
        analyzer = CoordinationAnalyzer()
        
        # Create sample route pair for analysis
        route1_info = {
            'operator': 'kmb',
            'route_id': '272A',
            'route_name': 'KMB 272A'
        }
        
        route2_info = {
            'operator': 'citybus',
            'route_id': '582',
            'route_name': 'Citybus 582'
        }
        
        print("Coordination analyzer initialized successfully!")
        print(f"Ready to analyze: {route1_info['operator']} {route1_info['route_id']} vs {route2_info['operator']} {route2_info['route_id']}")
        print("Note: Full coordination analysis requires real-time ETA data collection")
        
        return True
        
    except Exception as e:
        print(f"✗ Demo failed: {str(e)}")
        return False

def demo_visualization():
    """
    Demonstrate visualization functionality
    """
    print("\n=== DEMO: Visualization Generation ===")
    
    try:
        from visualization_generator import VisualizationGenerator
        
        generator = VisualizationGenerator()
        
        # Create sample overlap data for visualization
        sample_overlap_data = [
            {
                'route1': {'operator': 'kmb', 'route_id': '272A', 'route_name': 'University Station'},
                'route2': {'operator': 'citybus', 'route_id': '582', 'route_name': 'University Station'},
                'overlap_count': 8,
                'overlap_percentage': 0.67
            },
            {
                'route1': {'operator': 'kmb', 'route_id': '271', 'route_name': 'Tsim Sha Tsui'},
                'route2': {'operator': 'citybus', 'route_id': '581', 'route_name': 'Tsim Sha Tsui'},
                'overlap_count': 6,
                'overlap_percentage': 0.50
            }
        ]
        
        print("Visualization generator initialized successfully!")
        print("Sample data prepared for visualization:")
        for data in sample_overlap_data:
            print(f"  - {data['route1']['operator']} {data['route1']['route_id']} vs {data['route2']['operator']} {data['route2']['route_id']}: {data['overlap_count']} stops")
        
        print("Note: Full visualization requires matplotlib, seaborn, and plotly packages")
        
        return True
        
    except Exception as e:
        print(f"✗ Demo failed: {str(e)}")
        return False

def create_sample_data_files():
    """
    Create sample data files for demonstration
    """
    print("\n=== Creating Sample Data Files ===")
    
    try:
        # Create sample overlap data
        sample_data = {
            'analysis_timestamp': datetime.now().isoformat(),
            'total_routes_analyzed': 150,
            'total_overlapping_pairs': 25,
            'overlap_results': [
                {
                    'route1': {'operator': 'kmb', 'route_id': '272A', 'route_name': 'University Station', 'total_stops': 12},
                    'route2': {'operator': 'citybus', 'route_id': '582', 'route_name': 'University Station', 'total_stops': 12},
                    'overlap_count': 8,
                    'overlap_percentage': 0.67,
                    'common_stops': ['STOP001', 'STOP002', 'STOP003', 'STOP004', 'STOP005', 'STOP006', 'STOP007', 'STOP008']
                },
                {
                    'route1': {'operator': 'kmb', 'route_id': '271', 'route_name': 'Tsim Sha Tsui', 'total_stops': 15},
                    'route2': {'operator': 'citybus', 'route_id': '581', 'route_name': 'Tsim Sha Tsui', 'total_stops': 14},
                    'overlap_count': 6,
                    'overlap_percentage': 0.43,
                    'common_stops': ['STOP101', 'STOP102', 'STOP103', 'STOP104', 'STOP105', 'STOP106']
                }
            ]
        }
        
        # Save sample data
        data_dir = Path("data/overlap_analysis")
        data_dir.mkdir(parents=True, exist_ok=True)
        
        sample_file = data_dir / f"sample_overlap_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(sample_file, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Sample data file created: {sample_file}")
        return str(sample_file)
        
    except Exception as e:
        print(f"✗ Failed to create sample data: {str(e)}")
        return None

def main():
    """
    Run complete demonstration
    """
    print("="*60)
    print("SIMILAR CASES ANALYSIS - DEMONSTRATION")
    print("="*60)
    
    # Run demonstrations
    demos = [
        ("Route Collection", demo_route_collection),
        ("Overlap Analysis", demo_overlap_analysis),
        ("Coordination Analysis", demo_coordination_analysis),
        ("Visualization", demo_visualization)
    ]
    
    results = {}
    for name, demo_func in demos:
        print(f"\nRunning {name} demo...")
        results[name] = demo_func()
    
    # Create sample data files
    sample_file = create_sample_data_files()
    
    # Summary
    print("\n" + "="*60)
    print("DEMONSTRATION SUMMARY")
    print("="*60)
    
    for name, success in results.items():
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"{name}: {status}")
    
    if sample_file:
        print(f"\nSample data file: {sample_file}")
    
    print("\nNext Steps:")
    print("1. Install required packages: pip install -r requirements.txt")
    print("2. Run full analysis: python run_analysis.py")
    print("3. Check results in the 'results/' directory")
    print("4. View visualizations in the 'results/visualizations/' directory")

if __name__ == "__main__":
    main()
