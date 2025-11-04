#!/usr/bin/env python3
"""
Team 2: Bus Route Coordination - Coordination Analyzer
Author: Team 2 - Bus Route Coordination
Date: 2024
Purpose: Analyze coordination patterns between overlapping bus routes
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
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CoordinationAnalyzer:
    """
    Analyzer for bus route coordination patterns
    """
    
    def __init__(self, data_dir="data", results_dir="results"):
        self.data_dir = data_dir
        self.results_dir = results_dir
        self.ensure_directories()
        
        # API endpoints
        self.citybus_base = "https://data.etabus.gov.hk/v1/transport/citybus"
        self.kmb_base = "https://data.etabus.gov.hk/v1/transport/kmb"
        
    def ensure_directories(self):
        """Create necessary directories"""
        directories = [
            f"{self.data_dir}/coordination_data",
            f"{self.results_dir}/coordination_analysis",
            f"{self.results_dir}/headway_analysis",
            f"{self.results_dir}/passenger_impact"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Created directory: {directory}")
    
    def analyze_route_pair_coordination(self, route1_info, route2_info, duration_hours=2):
        """
        Analyze coordination between two specific routes
        """
        logger.info(f"Analyzing coordination between {route1_info['operator']} {route1_info['route_id']} and {route2_info['operator']} {route2_info['route_id']}")
        
        # Collect ETA data for both routes
        route1_eta_data = self.collect_eta_data(route1_info['route_id'], route1_info['operator'], duration_hours)
        route2_eta_data = self.collect_eta_data(route2_info['route_id'], route2_info['operator'], duration_hours)
        
        if not route1_eta_data or not route2_eta_data:
            logger.warning("Insufficient ETA data for coordination analysis")
            return None
        
        # Analyze headway patterns
        headway_analysis = self.analyze_headway_patterns(route1_eta_data, route2_eta_data)
        
        # Analyze overlapping stops coordination
        overlap_coordination = self.analyze_overlapping_stops_coordination(
            route1_eta_data, route2_eta_data, route1_info, route2_info
        )
        
        # Calculate coordination effectiveness
        coordination_effectiveness = self.calculate_coordination_effectiveness(
            headway_analysis, overlap_coordination
        )
        
        analysis_result = {
            'route1': route1_info,
            'route2': route2_info,
            'analysis_timestamp': datetime.now().isoformat(),
            'headway_analysis': headway_analysis,
            'overlap_coordination': overlap_coordination,
            'coordination_effectiveness': coordination_effectiveness
        }
        
        # Save analysis result
        self.save_data(analysis_result, f"coordination_data/coordination_{route1_info['operator']}_{route1_info['route_id']}_vs_{route2_info['operator']}_{route2_info['route_id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        return analysis_result
    
    def collect_eta_data(self, route_id, operator, duration_hours=2):
        """
        Collect ETA data for a route over specified duration
        """
        eta_data = []
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=duration_hours)
        
        logger.info(f"Collecting ETA data for {operator} route {route_id} for {duration_hours} hours...")
        
        while datetime.now() < end_time:
            try:
                if operator == "kmb":
                    url = f"{self.kmb_base}/eta/{route_id}"
                else:  # citybus
                    url = f"{self.citybus_base}/eta/{route_id}"
                
                response = requests.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    eta_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'data': data.get('data', [])
                    }
                    eta_data.append(eta_entry)
                    logger.info(f"Collected ETA data at {datetime.now().strftime('%H:%M:%S')}")
                else:
                    logger.warning(f"Failed to collect ETA data: {response.status_code}")
                
                # Collect every 2 minutes
                time.sleep(120)
                
            except Exception as e:
                logger.error(f"Error collecting ETA data: {str(e)}")
                time.sleep(60)
        
        return eta_data
    
    def analyze_headway_patterns(self, route1_eta_data, route2_eta_data):
        """
        Analyze headway patterns between two routes
        """
        logger.info("Analyzing headway patterns...")
        
        # Extract headways for each route
        route1_headways = self.calculate_headways(route1_eta_data)
        route2_headways = self.calculate_headways(route2_eta_data)
        
        # Analyze headway consistency
        headway_analysis = {
            'route1_headways': {
                'average': np.mean(route1_headways) if route1_headways else 0,
                'std_dev': np.std(route1_headways) if route1_headways else 0,
                'min': min(route1_headways) if route1_headways else 0,
                'max': max(route1_headways) if route1_headways else 0
            },
            'route2_headways': {
                'average': np.mean(route2_headways) if route2_headways else 0,
                'std_dev': np.std(route2_headways) if route2_headways else 0,
                'min': min(route2_headways) if route2_headways else 0,
                'max': max(route2_headways) if route2_headways else 0
            },
            'headway_correlation': self.calculate_headway_correlation(route1_headways, route2_headways)
        }
        
        return headway_analysis
    
    def calculate_headways(self, eta_data):
        """
        Calculate headways from ETA data
        """
        headways = []
        
        for entry in eta_data:
            if entry['data']:
                # Sort by ETA time
                sorted_etas = sorted(entry['data'], key=lambda x: x.get('eta', ''))
                
                # Calculate headways between consecutive buses
                for i in range(1, len(sorted_etas)):
                    prev_eta = sorted_etas[i-1].get('eta', '')
                    curr_eta = sorted_etas[i].get('eta', '')
                    
                    if prev_eta and curr_eta:
                        try:
                            prev_time = datetime.fromisoformat(prev_eta.replace('Z', '+00:00'))
                            curr_time = datetime.fromisoformat(curr_eta.replace('Z', '+00:00'))
                            headway = (curr_time - prev_time).total_seconds() / 60  # minutes
                            headways.append(headway)
                        except:
                            continue
        
        return headways
    
    def calculate_headway_correlation(self, headways1, headways2):
        """
        Calculate correlation between headways of two routes
        """
        if not headways1 or not headways2:
            return 0
        
        # Align headways by time (simplified approach)
        min_len = min(len(headways1), len(headways2))
        if min_len < 2:
            return 0
        
        try:
            correlation = np.corrcoef(headways1[:min_len], headways2[:min_len])[0, 1]
            return correlation if not np.isnan(correlation) else 0
        except:
            return 0
    
    def analyze_overlapping_stops_coordination(self, route1_eta_data, route2_eta_data, route1_info, route2_info):
        """
        Analyze coordination at overlapping stops
        """
        logger.info("Analyzing overlapping stops coordination...")
        
        # This would require identifying common stops between routes
        # For now, we'll analyze general coordination patterns
        
        coordination_analysis = {
            'total_observations': len(route1_eta_data),
            'coordination_opportunities': 0,
            'coordination_effectiveness': 'TBD',
            'passenger_waiting_impact': 'TBD'
        }
        
        return coordination_analysis
    
    def calculate_coordination_effectiveness(self, headway_analysis, overlap_coordination):
        """
        Calculate overall coordination effectiveness
        """
        effectiveness_score = 0
        
        # Factor 1: Headway consistency
        route1_consistency = 1 - (headway_analysis['route1_headways']['std_dev'] / headway_analysis['route1_headways']['average']) if headway_analysis['route1_headways']['average'] > 0 else 0
        route2_consistency = 1 - (headway_analysis['route2_headways']['std_dev'] / headway_analysis['route2_headways']['average']) if headway_analysis['route2_headways']['average'] > 0 else 0
        
        # Factor 2: Headway correlation
        correlation_score = abs(headway_analysis['headway_correlation'])
        
        # Calculate overall effectiveness
        effectiveness_score = (route1_consistency + route2_consistency + correlation_score) / 3
        
        effectiveness_level = "High" if effectiveness_score > 0.7 else "Medium" if effectiveness_score > 0.4 else "Low"
        
        return {
            'score': effectiveness_score,
            'level': effectiveness_level,
            'route1_consistency': route1_consistency,
            'route2_consistency': route2_consistency,
            'correlation': correlation_score
        }
    
    def analyze_multiple_route_pairs(self, route_pairs, duration_hours=1):
        """
        Analyze coordination for multiple route pairs
        """
        logger.info(f"Analyzing coordination for {len(route_pairs)} route pairs...")
        
        coordination_results = []
        
        for i, (route1_info, route2_info) in enumerate(route_pairs):
            logger.info(f"Analyzing pair {i+1}/{len(route_pairs)}: {route1_info['operator']} {route1_info['route_id']} vs {route2_info['operator']} {route2_info['route_id']}")
            
            result = self.analyze_route_pair_coordination(route1_info, route2_info, duration_hours)
            if result:
                coordination_results.append(result)
            
            # Rate limiting between analyses
            time.sleep(30)
        
        # Generate comparative analysis
        comparative_analysis = self.generate_comparative_analysis(coordination_results)
        
        return {
            'individual_results': coordination_results,
            'comparative_analysis': comparative_analysis
        }
    
    def generate_comparative_analysis(self, coordination_results):
        """
        Generate comparative analysis across multiple route pairs
        """
        if not coordination_results:
            return {}
        
        # Analyze coordination effectiveness distribution
        effectiveness_scores = [r['coordination_effectiveness']['score'] for r in coordination_results]
        
        comparative_analysis = {
            'total_pairs_analyzed': len(coordination_results),
            'effectiveness_distribution': {
                'high': len([s for s in effectiveness_scores if s > 0.7]),
                'medium': len([s for s in effectiveness_scores if 0.4 < s <= 0.7]),
                'low': len([s for s in effectiveness_scores if s <= 0.4])
            },
            'average_effectiveness': np.mean(effectiveness_scores),
            'best_coordination': max(coordination_results, key=lambda x: x['coordination_effectiveness']['score']),
            'worst_coordination': min(coordination_results, key=lambda x: x['coordination_effectiveness']['score'])
        }
        
        # Save comparative analysis
        self.save_data(comparative_analysis, f"coordination_analysis/comparative_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        return comparative_analysis
    
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

def main():
    """
    Main function to run coordination analysis
    """
    analyzer = CoordinationAnalyzer()
    
    # Example: Analyze coordination between KMB 272A and Citybus 582
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
    
    # Run coordination analysis
    result = analyzer.analyze_route_pair_coordination(route1_info, route2_info, duration_hours=1)
    
    if result:
        print(f"\n=== COORDINATION ANALYSIS COMPLETE ===")
        print(f"Route 1: {result['route1']['operator']} {result['route1']['route_id']}")
        print(f"Route 2: {result['route2']['operator']} {result['route2']['route_id']}")
        print(f"Coordination Effectiveness: {result['coordination_effectiveness']['level']} ({result['coordination_effectiveness']['score']:.2f})")
    else:
        print("Coordination analysis failed - insufficient data")

if __name__ == "__main__":
    main()
