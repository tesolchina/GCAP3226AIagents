#!/usr/bin/env python3
"""
Team 2: Bus Route Coordination - Data Collection Script Template
Author: [TEAM MEMBER NAME]
Date: [DATE]
Purpose: Collect real-time bus data from Hong Kong Government Open Data APIs
"""

import requests
import json
import time
import pandas as pd
from datetime import datetime, timedelta
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BusDataCollector:
    """
    Data collector for Hong Kong bus route coordination analysis
    Collects data from Citybus and KMB/LWB APIs
    """
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.ensure_data_directories()
        
        # API endpoints
        self.citybus_base = "https://data.etabus.gov.hk/v1/transport/citybus"
        self.kmb_base = "https://data.etabus.gov.hk/v1/transport/kmb"
        
        # Target routes
        self.target_routes = {
            "kmb_272a": "272A",
            "citybus_582": "582"
        }
        
        # Overlapping stops (to be identified and updated)
        self.overlapping_stops = []
        
    def ensure_data_directories(self):
        """Create necessary data directories"""
        directories = [
            f"{self.data_dir}/raw_data/kmb_272a/route_data",
            f"{self.data_dir}/raw_data/kmb_272a/stop_data", 
            f"{self.data_dir}/raw_data/kmb_272a/eta_data",
            f"{self.data_dir}/raw_data/kmb_272a/performance_data",
            f"{self.data_dir}/raw_data/citybus_582/route_data",
            f"{self.data_dir}/raw_data/citybus_582/stop_data",
            f"{self.data_dir}/raw_data/citybus_582/eta_data", 
            f"{self.data_dir}/raw_data/citybus_582/performance_data",
            f"{self.data_dir}/raw_data/overlapping_stops/coordination_analysis",
            f"{self.data_dir}/raw_data/overlapping_stops/passenger_flow",
            f"{self.data_dir}/processed_data/performance_metrics",
            f"{self.data_dir}/processed_data/coordination_analysis",
            f"{self.data_dir}/processed_data/optimization_models"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Created directory: {directory}")
    
    def collect_citybus_data(self, route_id="582"):
        """
        Collect Citybus route data
        """
        try:
            # Get route information
            route_url = f"{self.citybus_base}/route/{route_id}"
            response = requests.get(route_url)
            
            if response.status_code == 200:
                route_data = response.json()
                self.save_data(route_data, f"citybus_582/route_data/route_{route_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
                logger.info(f"Collected Citybus route {route_id} data")
                
                # Get route stops
                stops_url = f"{self.citybus_base}/route-stop/{route_id}"
                stops_response = requests.get(stops_url)
                
                if stops_response.status_code == 200:
                    stops_data = stops_response.json()
                    self.save_data(stops_data, f"citybus_582/stop_data/stops_{route_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
                    logger.info(f"Collected Citybus route {route_id} stops data")
                
                return route_data, stops_data if 'stops_data' in locals() else None
            else:
                logger.error(f"Failed to collect Citybus route {route_id} data: {response.status_code}")
                return None, None
                
        except Exception as e:
            logger.error(f"Error collecting Citybus data: {str(e)}")
            return None, None
    
    def collect_kmb_data(self, route_id="272A"):
        """
        Collect KMB route data
        """
        try:
            # Get route information
            route_url = f"{self.kmb_base}/route/{route_id}"
            response = requests.get(route_url)
            
            if response.status_code == 200:
                route_data = response.json()
                self.save_data(route_data, f"kmb_272a/route_data/route_{route_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
                logger.info(f"Collected KMB route {route_id} data")
                
                # Get route stops
                stops_url = f"{self.kmb_base}/route-stop/{route_id}"
                stops_response = requests.get(stops_url)
                
                if stops_response.status_code == 200:
                    stops_data = stops_response.json()
                    self.save_data(stops_data, f"kmb_272a/stop_data/stops_{route_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
                    logger.info(f"Collected KMB route {route_id} stops data")
                
                return route_data, stops_data if 'stops_data' in locals() else None
            else:
                logger.error(f"Failed to collect KMB route {route_id} data: {response.status_code}")
                return None, None
                
        except Exception as e:
            logger.error(f"Error collecting KMB data: {str(e)}")
            return None, None
    
    def collect_eta_data(self, route_id, operator="citybus"):
        """
        Collect real-time ETA data for a route
        """
        try:
            if operator == "citybus":
                eta_url = f"{self.citybus_base}/eta/{route_id}"
                data_path = f"citybus_582/eta_data/eta_{route_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            else:  # kmb
                eta_url = f"{self.kmb_base}/eta/{route_id}"
                data_path = f"kmb_272a/eta_data/eta_{route_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            response = requests.get(eta_url)
            
            if response.status_code == 200:
                eta_data = response.json()
                self.save_data(eta_data, data_path)
                logger.info(f"Collected ETA data for {operator} route {route_id}")
                return eta_data
            else:
                logger.error(f"Failed to collect ETA data for {operator} route {route_id}: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error collecting ETA data: {str(e)}")
            return None
    
    def collect_overlapping_stops_data(self):
        """
        Collect data for overlapping stops between KMB 272A and Citybus 582
        """
        try:
            # This function will be implemented once overlapping stops are identified
            logger.info("Collecting overlapping stops data...")
            
            # TODO: Implement overlapping stops data collection
            # 1. Identify overlapping stops from route data
            # 2. Collect ETA data for overlapping stops
            # 3. Analyze coordination between routes
            
            pass
            
        except Exception as e:
            logger.error(f"Error collecting overlapping stops data: {str(e)}")
    
    def analyze_coordination(self, kmb_data, citybus_data):
        """
        Analyze coordination between KMB 272A and Citybus 582
        """
        try:
            # TODO: Implement coordination analysis
            # 1. Compare headways at overlapping stops
            # 2. Analyze passenger waiting times
            # 3. Assess coordination effectiveness
            
            logger.info("Analyzing route coordination...")
            
            # Placeholder for coordination analysis
            coordination_analysis = {
                "timestamp": datetime.now().isoformat(),
                "kmb_route": "272A",
                "citybus_route": "582",
                "overlapping_stops": len(self.overlapping_stops),
                "coordination_effectiveness": "TBD",
                "average_waiting_time": "TBD",
                "headway_consistency": "TBD"
            }
            
            self.save_data(coordination_analysis, f"overlapping_stops/coordination_analysis/coordination_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
            
        except Exception as e:
            logger.error(f"Error analyzing coordination: {str(e)}")
    
    def save_data(self, data, filepath):
        """
        Save data to JSON file
        """
        try:
            full_path = os.path.join(self.data_dir, "raw_data", filepath)
            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved data to: {full_path}")
        except Exception as e:
            logger.error(f"Error saving data: {str(e)}")
    
    def run_data_collection_cycle(self):
        """
        Run a complete data collection cycle
        """
        logger.info("Starting data collection cycle...")
        
        # Collect route data
        kmb_route_data, kmb_stops_data = self.collect_kmb_data("272A")
        citybus_route_data, citybus_stops_data = self.collect_citybus_data("582")
        
        # Collect ETA data
        kmb_eta_data = self.collect_eta_data("272A", "kmb")
        citybus_eta_data = self.collect_eta_data("582", "citybus")
        
        # Analyze coordination
        if kmb_eta_data and citybus_eta_data:
            self.analyze_coordination(kmb_eta_data, citybus_eta_data)
        
        logger.info("Data collection cycle completed")
    
    def run_continuous_collection(self, duration_hours=1, interval_minutes=5):
        """
        Run continuous data collection for specified duration
        """
        logger.info(f"Starting continuous data collection for {duration_hours} hours with {interval_minutes} minute intervals")
        
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=duration_hours)
        
        while datetime.now() < end_time:
            self.run_data_collection_cycle()
            time.sleep(interval_minutes * 60)  # Convert to seconds
        
        logger.info("Continuous data collection completed")

def main():
    """
    Main function to run data collection
    """
    collector = BusDataCollector()
    
    # Run single data collection cycle
    collector.run_data_collection_cycle()
    
    # Uncomment to run continuous collection
    # collector.run_continuous_collection(duration_hours=2, interval_minutes=5)

if __name__ == "__main__":
    main()
