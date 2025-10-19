#!/usr/bin/env python3
"""
HKO Typhoon Signal 8 Web Crawler
================================
Web crawler for collecting typhoon signal data from hko.gov.hk
Focus: Signal 8 announcements and weather data during typhoon events

Author: Dr. Simon Wang, HKBU
Course: GCAP3226 - Empowering Citizens Through Data
Date: 2025-01-08
"""

import os
import sys
import time
import json
import csv
import logging
import requests
from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import hashlib

class HKOTyphoonCrawler:
    """Web crawler for HKO typhoon signal data collection"""
    
    def __init__(self, base_dir="/Users/simonwang/Documents/Usage/GCAP3226/Team3_Typhoon/02_Data_Collection/webCrawler"):
        self.base_dir = base_dir
        self.output_dir = os.path.join(base_dir, "output")
        self.logs_dir = os.path.join(base_dir, "logs")
        self.data_dir = os.path.join(base_dir, "data")
        
        # Ensure directories exist
        for directory in [self.output_dir, self.logs_dir, self.data_dir]:
            os.makedirs(directory, exist_ok=True)
        
        # Setup logging
        self.setup_logging()
        
        # HKO URLs
        self.base_url = "https://www.hko.gov.hk"
        self.warning_url = "https://www.hko.gov.hk/en/wxinfo/currwx/tc_warning.htm"
        self.weather_url = "https://www.hko.gov.hk/en/wxinfo/currwx/weather.htm"
        self.tc_track_url = "https://www.hko.gov.hk/en/wxinfo/currwx/tc_track.htm"
        
        # Data storage
        self.collected_data = []
        self.signal_8_announcements = []
        self.weather_data = []
        self.crawl_log = []
        
        # Session for requests
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        self.logger.info("HKO Typhoon Crawler initialized")
        self.logger.info(f"Base directory: {self.base_dir}")
        self.logger.info(f"Output directory: {self.output_dir}")
        self.logger.info(f"Logs directory: {self.logs_dir}")
        self.logger.info(f"Data directory: {self.data_dir}")
    
    def setup_logging(self):
        """Setup logging configuration"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.logs_dir, f"hko_crawler_{timestamp}.log")
        
        # Create logger
        self.logger = logging.getLogger('HKOTyphoonCrawler')
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
    
    def log_crawl_activity(self, activity, details=""):
        """Log crawling activity"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'activity': activity,
            'details': details
        }
        self.crawl_log.append(log_entry)
        self.logger.info(f"CRAWL ACTIVITY: {activity} - {details}")
    
    def make_request(self, url, timeout=30):
        """Make HTTP request with error handling"""
        try:
            self.log_crawl_activity("HTTP_REQUEST", f"Fetching: {url}")
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            
            self.log_crawl_activity("HTTP_SUCCESS", f"Status: {response.status_code}, URL: {url}")
            return response
            
        except requests.exceptions.RequestException as e:
            self.log_crawl_activity("HTTP_ERROR", f"Error fetching {url}: {str(e)}")
            self.logger.error(f"Request failed for {url}: {str(e)}")
            return None
    
    def parse_warning_page(self, html_content):
        """Parse typhoon warning page for Signal 8 announcements"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            announcements = []
            
            # Look for Signal 8 specific content
            signal_8_patterns = [
                r'Signal No\.?\s*8',
                r'TC8',
                r'Tropical Cyclone Warning Signal No\.?\s*8',
                r'Gale or Storm'
            ]
            
            # Find all text content
            text_content = soup.get_text()
            
            for pattern in signal_8_patterns:
                matches = re.finditer(pattern, text_content, re.IGNORECASE)
                for match in matches:
                    # Extract context around the match
                    start = max(0, match.start() - 200)
                    end = min(len(text_content), match.end() + 200)
                    context = text_content[start:end].strip()
                    
                    announcement = {
                        'timestamp': datetime.now().isoformat(),
                        'pattern_matched': pattern,
                        'context': context,
                        'full_text': text_content,
                        'url': self.warning_url
                    }
                    announcements.append(announcement)
            
            self.log_crawl_activity("PARSE_WARNING", f"Found {len(announcements)} Signal 8 references")
            return announcements
            
        except Exception as e:
            self.log_crawl_activity("PARSE_ERROR", f"Error parsing warning page: {str(e)}")
            self.logger.error(f"Error parsing warning page: {str(e)}")
            return []
    
    def parse_weather_page(self, html_content):
        """Parse weather page for typhoon-related data"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            weather_data = []
            
            # Look for wind data, pressure, and other meteorological data
            wind_patterns = [
                r'wind.*?(\d+)\s*km/h',
                r'wind.*?(\d+)\s*knots',
                r'gust.*?(\d+)\s*km/h',
                r'pressure.*?(\d+)\s*mb'
            ]
            
            text_content = soup.get_text()
            
            for pattern in wind_patterns:
                matches = re.finditer(pattern, text_content, re.IGNORECASE)
                for match in matches:
                    weather_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'pattern_matched': pattern,
                        'value': match.group(1),
                        'context': text_content[max(0, match.start()-50):match.end()+50].strip(),
                        'url': self.weather_url
                    }
                    weather_data.append(weather_entry)
            
            self.log_crawl_activity("PARSE_WEATHER", f"Found {len(weather_data)} weather data points")
            return weather_data
            
        except Exception as e:
            self.log_crawl_activity("PARSE_ERROR", f"Error parsing weather page: {str(e)}")
            self.logger.error(f"Error parsing weather page: {str(e)}")
            return []
    
    def parse_tc_track_page(self, html_content):
        """Parse tropical cyclone track page"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            track_data = []
            
            # Look for tropical cyclone information
            tc_patterns = [
                r'Tropical Cyclone.*?(\w+)',
                r'Typhoon.*?(\w+)',
                r'position.*?(\d+\.?\d*).*?(\d+\.?\d*)',
                r'intensity.*?(\d+)\s*knots'
            ]
            
            text_content = soup.get_text()
            
            for pattern in tc_patterns:
                matches = re.finditer(pattern, text_content, re.IGNORECASE)
                for match in matches:
                    track_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'pattern_matched': pattern,
                        'matches': match.groups(),
                        'context': text_content[max(0, match.start()-100):match.end()+100].strip(),
                        'url': self.tc_track_url
                    }
                    track_data.append(track_entry)
            
            self.log_crawl_activity("PARSE_TRACK", f"Found {len(track_data)} TC track data points")
            return track_data
            
        except Exception as e:
            self.log_crawl_activity("PARSE_ERROR", f"Error parsing TC track page: {str(e)}")
            self.logger.error(f"Error parsing TC track page: {str(e)}")
            return []
    
    def save_data_to_csv(self, data, filename):
        """Save data to CSV file"""
        try:
            if not data:
                self.log_crawl_activity("SAVE_CSV", f"No data to save for {filename}")
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
            
            self.log_crawl_activity("SAVE_CSV", f"Saved {len(data)} records to {csv_path}")
            self.logger.info(f"Data saved to CSV: {csv_path}")
            
        except Exception as e:
            self.log_crawl_activity("SAVE_ERROR", f"Error saving CSV {filename}: {str(e)}")
            self.logger.error(f"Error saving CSV {filename}: {str(e)}")
    
    def save_data_to_json(self, data, filename):
        """Save data to JSON file"""
        try:
            if not data:
                self.log_crawl_activity("SAVE_JSON", f"No data to save for {filename}")
                return
            
            json_path = os.path.join(self.data_dir, filename)
            
            with open(json_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=2, ensure_ascii=False)
            
            self.log_crawl_activity("SAVE_JSON", f"Saved {len(data)} records to {json_path}")
            self.logger.info(f"Data saved to JSON: {json_path}")
            
        except Exception as e:
            self.log_crawl_activity("SAVE_ERROR", f"Error saving JSON {filename}: {str(e)}")
            self.logger.error(f"Error saving JSON {filename}: {str(e)}")
    
    def generate_report(self):
        """Generate comprehensive crawling report"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_path = os.path.join(self.output_dir, f"crawling_report_{timestamp}.md")
            
            with open(report_path, 'w', encoding='utf-8') as report_file:
                report_file.write("# HKO Typhoon Signal 8 Crawling Report\n\n")
                report_file.write(f"**Generated:** {datetime.now().isoformat()}\n")
                report_file.write(f"**Crawler:** HKO Typhoon Signal 8 Web Crawler\n")
                report_file.write(f"**Course:** GCAP3226 - Empowering Citizens Through Data\n\n")
                
                report_file.write("## Summary\n\n")
                report_file.write(f"- **Total Signal 8 Announcements:** {len(self.signal_8_announcements)}\n")
                report_file.write(f"- **Total Weather Data Points:** {len(self.weather_data)}\n")
                report_file.write(f"- **Total Crawl Activities:** {len(self.crawl_log)}\n")
                report_file.write(f"- **Data Directory:** {self.data_dir}\n")
                report_file.write(f"- **Output Directory:** {self.output_dir}\n\n")
                
                report_file.write("## Signal 8 Announcements Found\n\n")
                for i, announcement in enumerate(self.signal_8_announcements, 1):
                    report_file.write(f"### Announcement {i}\n")
                    report_file.write(f"- **Timestamp:** {announcement.get('timestamp', 'N/A')}\n")
                    report_file.write(f"- **Pattern:** {announcement.get('pattern_matched', 'N/A')}\n")
                    report_file.write(f"- **Context:** {announcement.get('context', 'N/A')[:200]}...\n")
                    report_file.write(f"- **URL:** {announcement.get('url', 'N/A')}\n\n")
                
                report_file.write("## Weather Data Collected\n\n")
                for i, weather in enumerate(self.weather_data, 1):
                    report_file.write(f"### Weather Data {i}\n")
                    report_file.write(f"- **Timestamp:** {weather.get('timestamp', 'N/A')}\n")
                    report_file.write(f"- **Pattern:** {weather.get('pattern_matched', 'N/A')}\n")
                    report_file.write(f"- **Value:** {weather.get('value', 'N/A')}\n")
                    report_file.write(f"- **Context:** {weather.get('context', 'N/A')[:200]}...\n\n")
                
                report_file.write("## Crawl Activities Log\n\n")
                for activity in self.crawl_log:
                    report_file.write(f"- **{activity['timestamp']}:** {activity['activity']} - {activity['details']}\n")
            
            self.log_crawl_activity("GENERATE_REPORT", f"Report generated: {report_path}")
            self.logger.info(f"Crawling report generated: {report_path}")
            
        except Exception as e:
            self.log_crawl_activity("REPORT_ERROR", f"Error generating report: {str(e)}")
            self.logger.error(f"Error generating report: {str(e)}")
    
    def crawl_hko_data(self):
        """Main crawling function"""
        self.log_crawl_activity("CRAWL_START", "Starting HKO typhoon data crawling")
        self.logger.info("Starting HKO typhoon data crawling")
        
        try:
            # 1. Crawl warning page
            self.log_crawl_activity("CRAWL_WARNING", "Crawling typhoon warning page")
            warning_response = self.make_request(self.warning_url)
            if warning_response:
                announcements = self.parse_warning_page(warning_response.text)
                self.signal_8_announcements.extend(announcements)
                self.log_crawl_activity("CRAWL_WARNING", f"Found {len(announcements)} Signal 8 announcements")
            
            # 2. Crawl weather page
            self.log_crawl_activity("CRAWL_WEATHER", "Crawling weather page")
            weather_response = self.make_request(self.weather_url)
            if weather_response:
                weather_data = self.parse_weather_page(weather_response.text)
                self.weather_data.extend(weather_data)
                self.log_crawl_activity("CRAWL_WEATHER", f"Found {len(weather_data)} weather data points")
            
            # 3. Crawl TC track page
            self.log_crawl_activity("CRAWL_TRACK", "Crawling tropical cyclone track page")
            track_response = self.make_request(self.tc_track_url)
            if track_response:
                track_data = self.parse_tc_track_page(track_response.text)
                self.weather_data.extend(track_data)
                self.log_crawl_activity("CRAWL_TRACK", f"Found {len(track_data)} TC track data points")
            
            # 4. Save data
            self.log_crawl_activity("SAVE_DATA", "Saving collected data")
            
            # Save Signal 8 announcements
            if self.signal_8_announcements:
                self.save_data_to_csv(self.signal_8_announcements, "signal_8_announcements.csv")
                self.save_data_to_json(self.signal_8_announcements, "signal_8_announcements.json")
            
            # Save weather data
            if self.weather_data:
                self.save_data_to_csv(self.weather_data, "weather_data.csv")
                self.save_data_to_json(self.weather_data, "weather_data.json")
            
            # Save crawl log
            self.save_data_to_json(self.crawl_log, "crawl_log.json")
            
            # 5. Generate report
            self.generate_report()
            
            self.log_crawl_activity("CRAWL_COMPLETE", "HKO typhoon data crawling completed successfully")
            self.logger.info("HKO typhoon data crawling completed successfully")
            
            return True
            
        except Exception as e:
            self.log_crawl_activity("CRAWL_ERROR", f"Crawling failed: {str(e)}")
            self.logger.error(f"Crawling failed: {str(e)}")
            return False

def main():
    """Main function to run the crawler"""
    print("🌪️ HKO Typhoon Signal 8 Web Crawler")
    print("=" * 50)
    print("Course: GCAP3226 - Empowering Citizens Through Data")
    print("Author: Dr. Simon Wang, HKBU")
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 50)
    
    # Initialize crawler
    crawler = HKOTyphoonCrawler()
    
    # Run crawling
    success = crawler.crawl_hko_data()
    
    if success:
        print("\n✅ Crawling completed successfully!")
        print(f"📁 Data saved to: {crawler.data_dir}")
        print(f"📊 Reports saved to: {crawler.output_dir}")
        print(f"📝 Logs saved to: {crawler.logs_dir}")
    else:
        print("\n❌ Crawling failed. Check logs for details.")
    
    print("\n🌪️ HKO Typhoon Signal 8 Web Crawler - Complete")

if __name__ == "__main__":
    main()
