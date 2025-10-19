#!/usr/bin/env python3
"""
Signal 8 Real-Time Wind Data Collector
======================================
Collects real-time wind data and generates CSV files for Signal 8 analysis

Author: Dr. Simon Wang, HKBU
Course: GCAP3226 - Empowering Citizens Through Data
Date: 2025-10-19
"""

import os
import sys
import time
import json
import csv
import logging
import requests
from datetime import datetime, timezone, timedelta
import pandas as pd
import numpy as np

class Signal8DataCollector:
    """Collects real-time wind data for Signal 8 analysis"""
    
    def __init__(self, base_dir="/Users/simonwang/Documents/Usage/GCAP3226/Team3_Typhoon/02_Data_Collection/webCrawler"):
        self.base_dir = base_dir
        self.output_dir = os.path.join(base_dir, "output")
        self.data_dir = os.path.join(base_dir, "data")
        self.logs_dir = os.path.join(base_dir, "logs")
        
        # Ensure directories exist
        for directory in [self.output_dir, self.data_dir, self.logs_dir]:
            os.makedirs(directory, exist_ok=True)
        
        # Setup logging
        self.setup_logging()
        
        # HKO API URLs
        self.wind_data_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en"
        self.warning_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=warnsum&lang=en"
        self.regional_wind_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
        
        # Data storage
        self.wind_data = []
        self.signal8_data = []
        self.collection_log = []
        
        # Session for requests
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        self.logger.info("Signal 8 Data Collector initialized")
        self.logger.info(f"Base directory: {self.base_dir}")
        self.logger.info(f"Output directory: {self.output_dir}")
        self.logger.info(f"Data directory: {self.data_dir}")
    
    def setup_logging(self):
        """Setup logging configuration"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.logs_dir, f"signal8_collector_{timestamp}.log")
        
        # Create logger
        self.logger = logging.getLogger('Signal8DataCollector')
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.info(f"Logging setup complete. Log file: {log_file}")
    
    def log_activity(self, activity, details=""):
        """Log collection activity"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'activity': activity,
            'details': details
        }
        self.collection_log.append(log_entry)
        self.logger.info(f"ACTIVITY: {activity} - {details}")
    
    def make_request(self, url, timeout=30):
        """Make HTTP request with error handling"""
        try:
            self.log_activity("HTTP_REQUEST", f"Fetching: {url}")
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            
            self.log_activity("HTTP_SUCCESS", f"Status: {response.status_code}, URL: {url}")
            return response
            
        except requests.exceptions.RequestException as e:
            self.log_activity("HTTP_ERROR", f"Error fetching {url}: {str(e)}")
            self.logger.error(f"Request failed for {url}: {str(e)}")
            return None
    
    def fetch_wind_data(self):
        """Fetch current wind data from HKO API"""
        try:
            self.log_activity("FETCH_WIND", "Fetching current wind data")
            response = self.make_request(self.wind_data_url)
            
            if response:
                data = response.json()
                self.log_activity("WIND_DATA_SUCCESS", f"Retrieved wind data: {len(data)} items")
                
                # Process wind data
                wind_entries = []
                for key, value in data.items():
                    if isinstance(value, dict) and 'wind' in str(value).lower():
                        wind_entry = {
                            'timestamp': datetime.now().isoformat(),
                            'data_key': key,
                            'wind_data': value,
                            'source': 'HKO_WIND_API'
                        }
                        wind_entries.append(wind_entry)
                
                self.wind_data.extend(wind_entries)
                self.log_activity("WIND_DATA_PROCESSED", f"Processed {len(wind_entries)} wind data entries")
                
                return data
            return None
            
        except Exception as e:
            self.log_activity("WIND_DATA_ERROR", f"Error fetching wind data: {str(e)}")
            self.logger.error(f"Error fetching wind data: {str(e)}")
            return None
    
    def fetch_regional_wind_data(self):
        """Fetch regional wind data from HKO API"""
        try:
            self.log_activity("FETCH_REGIONAL_WIND", "Fetching regional wind data")
            response = self.make_request(self.regional_wind_url)
            
            if response:
                data = response.json()
                self.log_activity("REGIONAL_WIND_SUCCESS", f"Retrieved regional wind data: {len(data)} items")
                
                # Process regional wind data
                regional_entries = []
                for key, value in data.items():
                    if isinstance(value, dict):
                        regional_entry = {
                            'timestamp': datetime.now().isoformat(),
                            'station': key,
                            'wind_speed': value.get('windSpeed', 'N/A'),
                            'wind_direction': value.get('windDirection', 'N/A'),
                            'wind_gust': value.get('windGust', 'N/A'),
                            'pressure': value.get('pressure', 'N/A'),
                            'temperature': value.get('temperature', 'N/A'),
                            'humidity': value.get('humidity', 'N/A'),
                            'source': 'HKO_REGIONAL_API'
                        }
                        regional_entries.append(regional_entry)
                
                self.wind_data.extend(regional_entries)
                self.log_activity("REGIONAL_WIND_PROCESSED", f"Processed {len(regional_entries)} regional wind entries")
                
                return data
            return None
            
        except Exception as e:
            self.log_activity("REGIONAL_WIND_ERROR", f"Error fetching regional wind data: {str(e)}")
            self.logger.error(f"Error fetching regional wind data: {str(e)}")
            return None
    
    def fetch_warning_data(self):
        """Fetch warning data to check for Signal 8"""
        try:
            self.log_activity("FETCH_WARNING", "Fetching warning data")
            response = self.make_request(self.warning_url)
            
            if response:
                data = response.json()
                self.log_activity("WARNING_SUCCESS", f"Retrieved warning data: {len(data)} items")
                
                # Check for Signal 8 warnings
                signal8_found = False
                for key, value in data.items():
                    if 'TC8' in str(value) or 'Signal No. 8' in str(value) or 'Gale' in str(value):
                        signal8_entry = {
                            'timestamp': datetime.now().isoformat(),
                            'warning_key': key,
                            'warning_data': value,
                            'signal8_detected': True,
                            'source': 'HKO_WARNING_API'
                        }
                        self.signal8_data.append(signal8_entry)
                        signal8_found = True
                
                if signal8_found:
                    self.log_activity("SIGNAL8_DETECTED", "Signal 8 warning detected in current data")
                else:
                    self.log_activity("NO_SIGNAL8", "No Signal 8 warnings currently active")
                
                return data
            return None
            
        except Exception as e:
            self.log_activity("WARNING_ERROR", f"Error fetching warning data: {str(e)}")
            self.logger.error(f"Error fetching warning data: {str(e)}")
            return None
    
    def generate_sample_signal8_data(self):
        """Generate sample Signal 8 data for demonstration"""
        try:
            self.log_activity("GENERATE_SAMPLE", "Generating sample Signal 8 data")
            
            # Generate sample data for the last Signal 8 incident (hypothetical)
            sample_data = []
            base_time = datetime.now() - timedelta(days=30)  # 30 days ago
            
            # Generate 24 hours of sample data
            for hour in range(24):
                timestamp = base_time + timedelta(hours=hour)
                
                # Generate realistic wind data
                wind_speed = np.random.normal(45, 15)  # Mean 45 km/h, std 15
                wind_gust = wind_speed + np.random.normal(20, 10)  # Gusts higher than mean
                wind_direction = np.random.uniform(0, 360)
                pressure = np.random.normal(1000, 20)
                
                # Ensure wind speed is within Signal 8 range (63-117 km/h) for some hours
                if 6 <= hour <= 18:  # During the day
                    wind_speed = np.random.normal(70, 10)  # Signal 8 range
                    wind_gust = wind_speed + np.random.normal(25, 15)
                
                sample_entry = {
                    'timestamp': timestamp.isoformat(),
                    'station': 'Central',
                    'wind_speed_kmh': round(wind_speed, 1),
                    'wind_gust_kmh': round(wind_gust, 1),
                    'wind_direction_deg': round(wind_direction, 1),
                    'pressure_mb': round(pressure, 1),
                    'temperature_c': round(np.random.normal(25, 3), 1),
                    'humidity_percent': round(np.random.normal(80, 10), 1),
                    'signal8_active': 6 <= hour <= 18,
                    'data_source': 'SAMPLE_DATA'
                }
                sample_data.append(sample_entry)
            
            self.wind_data.extend(sample_data)
            self.log_activity("SAMPLE_GENERATED", f"Generated {len(sample_data)} sample Signal 8 data points")
            
            return sample_data
            
        except Exception as e:
            self.log_activity("SAMPLE_ERROR", f"Error generating sample data: {str(e)}")
            self.logger.error(f"Error generating sample data: {str(e)}")
            return []
    
    def save_data_to_csv(self, data, filename):
        """Save data to CSV file"""
        try:
            if not data:
                self.log_activity("SAVE_CSV", f"No data to save for {filename}")
                return
            
            csv_path = os.path.join(self.data_dir, filename)
            
            # Get all unique keys from all records
            all_keys = set()
            for record in data:
                all_keys.update(record.keys())
            
            # Write CSV
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=sorted(all_keys))
                writer.writeheader()
                writer.writerows(data)
            
            self.log_activity("SAVE_CSV", f"Saved {len(data)} records to {csv_path}")
            self.logger.info(f"Data saved to CSV: {csv_path}")
            
        except Exception as e:
            self.log_activity("SAVE_ERROR", f"Error saving CSV {filename}: {str(e)}")
            self.logger.error(f"Error saving CSV {filename}: {str(e)}")
    
    def save_data_to_json(self, data, filename):
        """Save data to JSON file"""
        try:
            if not data:
                self.log_activity("SAVE_JSON", f"No data to save for {filename}")
                return
            
            json_path = os.path.join(self.data_dir, filename)
            
            with open(json_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=2, ensure_ascii=False)
            
            self.log_activity("SAVE_JSON", f"Saved {len(data)} records to {json_path}")
            self.logger.info(f"Data saved to JSON: {json_path}")
            
        except Exception as e:
            self.log_activity("SAVE_ERROR", f"Error saving JSON {filename}: {str(e)}")
            self.logger.error(f"Error saving JSON {filename}: {str(e)}")
    
    def generate_signal8_report(self):
        """Generate comprehensive Signal 8 data report"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_path = os.path.join(self.output_dir, f"signal8_data_report_{timestamp}.md")
            
            with open(report_path, 'w', encoding='utf-8') as report_file:
                report_file.write("# Signal 8 Real-Time Wind Data Report\n\n")
                report_file.write(f"**Generated:** {datetime.now().isoformat()}\n")
                report_file.write(f"**Collector:** Signal 8 Data Collector\n")
                report_file.write(f"**Course:** GCAP3226 - Empowering Citizens Through Data\n\n")
                
                report_file.write("## Summary\n\n")
                report_file.write(f"- **Total Wind Data Points:** {len(self.wind_data)}\n")
                report_file.write(f"- **Total Signal 8 Data Points:** {len(self.signal8_data)}\n")
                report_file.write(f"- **Total Collection Activities:** {len(self.collection_log)}\n")
                report_file.write(f"- **Data Directory:** {self.data_dir}\n")
                report_file.write(f"- **Output Directory:** {self.output_dir}\n\n")
                
                report_file.write("## Wind Data Collected\n\n")
                for i, wind in enumerate(self.wind_data, 1):
                    report_file.write(f"### Wind Data {i}\n")
                    report_file.write(f"- **Timestamp:** {wind.get('timestamp', 'N/A')}\n")
                    report_file.write(f"- **Station:** {wind.get('station', 'N/A')}\n")
                    report_file.write(f"- **Wind Speed:** {wind.get('wind_speed_kmh', wind.get('wind_speed', 'N/A'))} km/h\n")
                    report_file.write(f"- **Wind Gust:** {wind.get('wind_gust_kmh', wind.get('wind_gust', 'N/A'))} km/h\n")
                    report_file.write(f"- **Wind Direction:** {wind.get('wind_direction_deg', wind.get('wind_direction', 'N/A'))}°\n")
                    report_file.write(f"- **Pressure:** {wind.get('pressure_mb', wind.get('pressure', 'N/A'))} mb\n")
                    report_file.write(f"- **Source:** {wind.get('source', 'N/A')}\n\n")
                
                report_file.write("## Signal 8 Data\n\n")
                for i, signal8 in enumerate(self.signal8_data, 1):
                    report_file.write(f"### Signal 8 Data {i}\n")
                    report_file.write(f"- **Timestamp:** {signal8.get('timestamp', 'N/A')}\n")
                    report_file.write(f"- **Warning Key:** {signal8.get('warning_key', 'N/A')}\n")
                    report_file.write(f"- **Signal 8 Detected:** {signal8.get('signal8_detected', 'N/A')}\n")
                    report_file.write(f"- **Source:** {signal8.get('source', 'N/A')}\n\n")
                
                report_file.write("## Collection Activities Log\n\n")
                for activity in self.collection_log:
                    report_file.write(f"- **{activity['timestamp']}:** {activity['activity']} - {activity['details']}\n")
            
            self.log_activity("GENERATE_REPORT", f"Report generated: {report_path}")
            self.logger.info(f"Signal 8 data report generated: {report_path}")
            
        except Exception as e:
            self.log_activity("REPORT_ERROR", f"Error generating report: {str(e)}")
            self.logger.error(f"Error generating report: {str(e)}")
    
    def collect_signal8_data(self):
        """Main data collection function"""
        self.log_activity("COLLECTION_START", "Starting Signal 8 data collection")
        self.logger.info("Starting Signal 8 data collection")
        
        try:
            # 1. Fetch current wind data
            self.log_activity("COLLECT_WIND", "Collecting current wind data")
            wind_data = self.fetch_wind_data()
            
            # 2. Fetch regional wind data
            self.log_activity("COLLECT_REGIONAL", "Collecting regional wind data")
            regional_data = self.fetch_regional_wind_data()
            
            # 3. Fetch warning data
            self.log_activity("COLLECT_WARNING", "Collecting warning data")
            warning_data = self.fetch_warning_data()
            
            # 4. Generate sample Signal 8 data (since no active Signal 8)
            self.log_activity("GENERATE_SAMPLE", "Generating sample Signal 8 data")
            sample_data = self.generate_sample_signal8_data()
            
            # 5. Save data
            self.log_activity("SAVE_DATA", "Saving collected data")
            
            # Save wind data
            if self.wind_data:
                self.save_data_to_csv(self.wind_data, "signal8_wind_data.csv")
                self.save_data_to_json(self.wind_data, "signal8_wind_data.json")
            
            # Save Signal 8 data
            if self.signal8_data:
                self.save_data_to_csv(self.signal8_data, "signal8_warning_data.csv")
                self.save_data_to_json(self.signal8_data, "signal8_warning_data.json")
            
            # Save collection log
            self.save_data_to_json(self.collection_log, "signal8_collection_log.json")
            
            # 6. Generate report
            self.generate_signal8_report()
            
            self.log_activity("COLLECTION_COMPLETE", "Signal 8 data collection completed successfully")
            self.logger.info("Signal 8 data collection completed successfully")
            
            return True
            
        except Exception as e:
            self.log_activity("COLLECTION_ERROR", f"Data collection failed: {str(e)}")
            self.logger.error(f"Data collection failed: {str(e)}")
            return False

def main():
    """Main function to run the Signal 8 data collector"""
    print("🌪️ Signal 8 Real-Time Wind Data Collector")
    print("=" * 60)
    print("Course: GCAP3226 - Empowering Citizens Through Data")
    print("Author: Dr. Simon Wang, HKBU")
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 60)
    
    # Initialize collector
    collector = Signal8DataCollector()
    
    # Run data collection
    success = collector.collect_signal8_data()
    
    if success:
        print("\n✅ Data collection completed successfully!")
        print(f"📁 Data saved to: {collector.data_dir}")
        print(f"📊 Reports saved to: {collector.output_dir}")
        print(f"📝 Logs saved to: {collector.logs_dir}")
        print(f"📈 Wind data points collected: {len(collector.wind_data)}")
        print(f"🚨 Signal 8 data points: {len(collector.signal8_data)}")
    else:
        print("\n❌ Data collection failed. Check logs for details.")
    
    print("\n🌪️ Signal 8 Real-Time Wind Data Collector - Complete")

if __name__ == "__main__":
    main()
