#!/usr/bin/env python3
"""
Team 2: Bus Route Coordination - Route Overlap Analyzer
Author: Team 2 - Bus Route Coordination
Date: 2024
Purpose: Find bus routes with overlapping stops across different operators
"""

import requests
import json
import time
import pandas as pd
from datetime import datetime, timedelta
import os
import logging
from typing import Dict, List, Tuple, Set
from collections import defaultdict
import itertools

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RouteOverlapAnalyzer:
    """
    Analyzer for finding bus routes with overlapping stops
    """
    
    def __init__(self, data_dir="data", results_dir="results"):
        self.data_dir = data_dir
        self.results_dir = results_dir
        self.ensure_directories()
        
        # API endpoints
        self.citybus_base = "https://data.etabus.gov.hk/v1/transport/citybus"
        self.kmb_base = "https://data.etabus.gov.hk/v1/transport/kmb"
        
        # Data storage
        self.all_routes = {}
        self.route_stops = {}
        self.overlap_results = []
        
    def ensure_directories(self):
        """Create necessary directories"""
        directories = [
            f"{self.data_dir}/raw_routes",
            f"{self.data_dir}/route_stops", 
            f"{self.data_dir}/overlap_analysis",
            f"{self.results_dir}/high_overlap",
            f"{self.results_dir}/medium_overlap",
            f"{self.results_dir}/low_overlap",
            f"{self.results_dir}/coordination_analysis"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Created directory: {directory}")
    
    def collect_all_routes(self):
        """
        Collect all routes from all operators
        """
        logger.info("Starting comprehensive route collection...")
        
        # Collect KMB routes
        kmb_routes = self.collect_kmb_routes()
        if kmb_routes:
            self.all_routes['kmb'] = kmb_routes
            logger.info(f"Collected {len(kmb_routes)} KMB routes")
        
        # Collect Citybus routes
        citybus_routes = self.collect_citybus_routes()
        if citybus_routes:
            self.all_routes['citybus'] = citybus_routes
            logger.info(f"Collected {len(citybus_routes)} Citybus routes")
        
        # Save all routes data
        self.save_data(self.all_routes, f"raw_routes/all_routes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        return self.all_routes
    
    def collect_kmb_routes(self):
        """
        Collect all KMB routes
        """
        try:
            url = f"{self.kmb_base}/route"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                routes = data.get('data', [])
                logger.info(f"Successfully collected {len(routes)} KMB routes")
                return routes
            else:
                logger.error(f"Failed to collect KMB routes: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error collecting KMB routes: {str(e)}")
            return None
    
    def collect_citybus_routes(self):
        """
        Collect all Citybus routes
        """
        try:
            url = f"{self.citybus_base}/route"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                routes = data.get('data', [])
                logger.info(f"Successfully collected {len(routes)} Citybus routes")
                return routes
            else:
                logger.error(f"Failed to collect Citybus routes: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error collecting Citybus routes: {str(e)}")
            return None
    
    def collect_route_stops(self, route_id, operator):
        """
        Collect stops for a specific route
        """
        try:
            if operator == "kmb":
                url = f"{self.kmb_base}/route-stop/{route_id}"
            else:  # citybus
                url = f"{self.citybus_base}/route-stop/{route_id}"
            
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                stops = data.get('data', [])
                return stops
            else:
                logger.warning(f"Failed to collect stops for {operator} route {route_id}: {response.status_code}")
                return []
                
        except Exception as e:
            logger.warning(f"Error collecting stops for {operator} route {route_id}: {str(e)}")
            return []
    
    def collect_all_route_stops(self):
        """
        Collect stops for all routes
        """
        logger.info("Starting route stops collection...")
        
        for operator, routes in self.all_routes.items():
            logger.info(f"Collecting stops for {len(routes)} {operator} routes...")
            
            for route in routes:
                route_id = route.get('route')
                if route_id:
                    stops = self.collect_route_stops(route_id, operator)
                    if stops:
                        self.route_stops[f"{operator}_{route_id}"] = {
                            'operator': operator,
                            'route_id': route_id,
                            'route_name': route.get('dest_tc', ''),
                            'stops': stops
                        }
                    
                    # Rate limiting
                    time.sleep(0.1)
        
        # Save route stops data
        self.save_data(self.route_stops, f"route_stops/all_route_stops_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        logger.info(f"Collected stops for {len(self.route_stops)} routes")
        return self.route_stops
    
    def find_route_overlaps(self, min_overlap=5):
        """
        Find routes with overlapping stops
        """
        logger.info(f"Starting overlap analysis with minimum {min_overlap} stops...")
        
        overlap_results = []
        route_pairs = list(itertools.combinations(self.route_stops.keys(), 2))
        
        logger.info(f"Analyzing {len(route_pairs)} route pairs...")
        
        for i, (route1_key, route2_key) in enumerate(route_pairs):
            if i % 100 == 0:
                logger.info(f"Processed {i}/{len(route_pairs)} route pairs...")
            
            route1_data = self.route_stops[route1_key]
            route2_data = self.route_stops[route2_key]
            
            # Skip if same operator
            if route1_data['operator'] == route2_data['operator']:
                continue
            
            # Find overlapping stops
            stops1 = set(stop.get('stop', '') for stop in route1_data['stops'])
            stops2 = set(stop.get('stop', '') for stop in route2_data['stops'])
            
            common_stops = stops1 & stops2
            
            if len(common_stops) >= min_overlap:
                overlap_analysis = {
                    'route1': {
                        'operator': route1_data['operator'],
                        'route_id': route1_data['route_id'],
                        'route_name': route1_data['route_name'],
                        'total_stops': len(stops1)
                    },
                    'route2': {
                        'operator': route2_data['operator'],
                        'route_id': route2_data['route_id'],
                        'route_name': route2_data['route_name'],
                        'total_stops': len(stops2)
                    },
                    'overlap_count': len(common_stops),
                    'overlap_percentage': len(common_stops) / min(len(stops1), len(stops2)),
                    'common_stops': list(common_stops),
                    'analysis_timestamp': datetime.now().isoformat()
                }
                
                overlap_results.append(overlap_analysis)
        
        # Sort by overlap count
        overlap_results.sort(key=lambda x: x['overlap_count'], reverse=True)
        
        # Save results
        self.save_data(overlap_results, f"overlap_analysis/route_overlaps_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        logger.info(f"Found {len(overlap_results)} route pairs with {min_overlap}+ overlapping stops")
        return overlap_results
    
    def categorize_overlaps(self, overlap_results):
        """
        Categorize overlaps by severity
        """
        high_overlap = [r for r in overlap_results if r['overlap_count'] >= 10]
        medium_overlap = [r for r in overlap_results if 5 <= r['overlap_count'] < 10]
        low_overlap = [r for r in overlap_results if 3 <= r['overlap_count'] < 5]
        
        categories = {
            'high_overlap': high_overlap,
            'medium_overlap': medium_overlap,
            'low_overlap': low_overlap
        }
        
        # Save categorized results
        for category, results in categories.items():
            if results:
                self.save_data(results, f"{category}/{category}_routes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
                logger.info(f"Saved {len(results)} {category} routes")
        
        return categories
    
    def analyze_coordination_patterns(self, overlap_results):
        """
        Analyze coordination patterns in overlapping routes
        """
        logger.info("Analyzing coordination patterns...")
        
        coordination_analysis = {
            'total_overlapping_pairs': len(overlap_results),
            'operator_combinations': defaultdict(int),
            'geographic_distribution': defaultdict(int),
            'overlap_statistics': {
                'max_overlap': max(r['overlap_count'] for r in overlap_results) if overlap_results else 0,
                'min_overlap': min(r['overlap_count'] for r in overlap_results) if overlap_results else 0,
                'avg_overlap': sum(r['overlap_count'] for r in overlap_results) / len(overlap_results) if overlap_results else 0
            }
        }
        
        # Analyze operator combinations
        for result in overlap_results:
            combo = f"{result['route1']['operator']}-{result['route2']['operator']}"
            coordination_analysis['operator_combinations'][combo] += 1
        
        # Save coordination analysis
        self.save_data(coordination_analysis, f"coordination_analysis/coordination_patterns_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        return coordination_analysis
    
    def generate_summary_report(self, overlap_results, coordination_analysis):
        """
        Generate a comprehensive summary report
        """
        report = {
            'analysis_timestamp': datetime.now().isoformat(),
            'summary': {
                'total_routes_analyzed': len(self.route_stops),
                'total_overlapping_pairs': len(overlap_results),
                'top_overlapping_routes': overlap_results[:10] if overlap_results else [],
                'coordination_patterns': coordination_analysis
            },
            'recommendations': {
                'high_priority_coordination': [r for r in overlap_results if r['overlap_count'] >= 10],
                'medium_priority_coordination': [r for r in overlap_results if 5 <= r['overlap_count'] < 10],
                'coordination_opportunities': len([r for r in overlap_results if r['overlap_count'] >= 5])
            }
        }
        
        # Save report
        self.save_data(report, f"results/summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        return report
    
    def save_data(self, data, filepath):
        """
        Save data to JSON file
        """
        try:
            full_path = os.path.join(self.data_dir, filepath)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved data to: {full_path}")
        except Exception as e:
            logger.error(f"Error saving data: {str(e)}")
    
    def run_complete_analysis(self, min_overlap=5):
        """
        Run complete overlap analysis
        """
        logger.info("Starting complete route overlap analysis...")
        
        # Step 1: Collect all routes
        self.collect_all_routes()
        
        # Step 2: Collect route stops
        self.collect_all_route_stops()
        
        # Step 3: Find overlaps
        overlap_results = self.find_route_overlaps(min_overlap)
        
        # Step 4: Categorize overlaps
        categories = self.categorize_overlaps(overlap_results)
        
        # Step 5: Analyze coordination patterns
        coordination_analysis = self.analyze_coordination_patterns(overlap_results)
        
        # Step 6: Generate summary report
        report = self.generate_summary_report(overlap_results, coordination_analysis)
        
        logger.info("Complete analysis finished!")
        return {
            'overlap_results': overlap_results,
            'categories': categories,
            'coordination_analysis': coordination_analysis,
            'report': report
        }

def main():
    """
    Main function to run route overlap analysis
    """
    analyzer = RouteOverlapAnalyzer()
    
    # Run complete analysis with minimum 5 overlapping stops
    results = analyzer.run_complete_analysis(min_overlap=5)
    
    print(f"\n=== ANALYSIS COMPLETE ===")
    print(f"Total overlapping route pairs found: {len(results['overlap_results'])}")
    print(f"High overlap routes (10+ stops): {len(results['categories']['high_overlap'])}")
    print(f"Medium overlap routes (5-9 stops): {len(results['categories']['medium_overlap'])}")
    print(f"Low overlap routes (3-4 stops): {len(results['categories']['low_overlap'])}")

if __name__ == "__main__":
    main()
