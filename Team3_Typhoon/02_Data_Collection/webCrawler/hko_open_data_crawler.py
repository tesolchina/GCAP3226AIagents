#!/usr/bin/env python3
"""
HKO Open Data Crawler
=====================
Web crawler for collecting data from HKO open datasets and tropical cyclone impact data
Focus: Signal 8 data, wind measurements, and tropical cyclone information

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
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import hashlib

class HKOOpenDataCrawler:
    """Web crawler for HKO open datasets and tropical cyclone impact data"""
    
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
        
        # HKO Open Data URLs
        self.open_data_url = "https://www.hko.gov.hk/en/abouthko/opendata_intro.htm"
        self.tc_impact_url = "https://www.hko.gov.hk/en/informtc/tc_impact.html"
        self.base_url = "https://www.hko.gov.hk"
        
        # Data storage
        self.open_data_info = []
        self.tc_impact_data = []
        self.available_datasets = []
        self.crawl_log = []
        
        # Session for requests
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        self.logger.info("HKO Open Data Crawler initialized")
        self.logger.info(f"Base directory: {self.base_dir}")
        self.logger.info(f"Output directory: {self.output_dir}")
        self.logger.info(f"Logs directory: {self.logs_dir}")
        self.logger.info(f"Data directory: {self.data_dir}")
    
    def setup_logging(self):
        """Setup logging configuration"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.logs_dir, f"hko_open_data_crawler_{timestamp}.log")
        
        # Create logger
        self.logger = logging.getLogger('HKOOpenDataCrawler')
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
    
    def parse_open_data_page(self, html_content):
        """Parse HKO open data introduction page"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            datasets = []
            
            # Look for dataset information
            # Find all links that might lead to datasets
            links = soup.find_all('a', href=True)
            
            for link in links:
                href = link.get('href')
                text = link.get_text().strip()
                
                if href and text:
                    # Check if it's a dataset link
                    if any(keyword in text.lower() for keyword in ['data', 'dataset', 'csv', 'json', 'xml', 'wind', 'typhoon', 'signal']):
                        dataset_info = {
                            'timestamp': datetime.now().isoformat(),
                            'title': text,
                            'url': urljoin(self.base_url, href) if href.startswith('/') else href,
                            'description': self.extract_description(link),
                            'source': 'HKO_OPEN_DATA'
                        }
                        datasets.append(dataset_info)
            
            # Look for specific Signal 8 and typhoon data
            signal_8_patterns = [
                r'Signal No\.?\s*8',
                r'TC8',
                r'Tropical Cyclone Warning Signal No\.?\s*8',
                r'Gale or Storm',
                r'No\.?\s*8.*?Gale',
                r'No\.?\s*8.*?Storm'
            ]
            
            text_content = soup.get_text()
            
            for pattern in signal_8_patterns:
                matches = re.finditer(pattern, text_content, re.IGNORECASE)
                for match in matches:
                    context = text_content[max(0, match.start()-100):match.end()+100].strip()
                    
                    signal_info = {
                        'timestamp': datetime.now().isoformat(),
                        'pattern_matched': pattern,
                        'context': context,
                        'source': 'HKO_OPEN_DATA'
                    }
                    datasets.append(signal_info)
            
            self.log_crawl_activity("PARSE_OPEN_DATA", f"Found {len(datasets)} dataset references")
            return datasets
            
        except Exception as e:
            self.log_crawl_activity("PARSE_ERROR", f"Error parsing open data page: {str(e)}")
            self.logger.error(f"Error parsing open data page: {str(e)}")
            return []
    
    def parse_tc_impact_page(self, html_content):
        """Parse tropical cyclone impact data page"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            impact_data = []
            
            # Look for tropical cyclone impact information
            tc_patterns = [
                r'Tropical Cyclone.*?(\w+)',
                r'Typhoon.*?(\w+)',
                r'Signal No\.?\s*8',
                r'TC8',
                r'Gale or Storm',
                r'Wind.*?(\d+)\s*km/h',
                r'Wind.*?(\d+)\s*knots',
                r'Pressure.*?(\d+)\s*mb'
            ]
            
            text_content = soup.get_text()
            
            for pattern in tc_patterns:
                matches = re.finditer(pattern, text_content, re.IGNORECASE)
                for match in matches:
                    impact_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'pattern_matched': pattern,
                        'matches': match.groups() if match.groups() else [match.group()],
                        'context': text_content[max(0, match.start()-100):match.end()+100].strip(),
                        'source': 'HKO_TC_IMPACT'
                    }
                    impact_data.append(impact_entry)
            
            # Look for data download links
            links = soup.find_all('a', href=True)
            for link in links:
                href = link.get('href')
                text = link.get_text().strip()
                
                if href and text and any(keyword in text.lower() for keyword in ['download', 'data', 'csv', 'json', 'xml']):
                    download_info = {
                        'timestamp': datetime.now().isoformat(),
                        'title': text,
                        'url': urljoin(self.base_url, href) if href.startswith('/') else href,
                        'source': 'HKO_TC_IMPACT'
                    }
                    impact_data.append(download_info)
            
            self.log_crawl_activity("PARSE_TC_IMPACT", f"Found {len(impact_data)} TC impact data points")
            return impact_data
            
        except Exception as e:
            self.log_crawl_activity("PARSE_ERROR", f"Error parsing TC impact page: {str(e)}")
            self.logger.error(f"Error parsing TC impact page: {str(e)}")
            return []
    
    def extract_description(self, element):
        """Extract description from element"""
        try:
            # Try to find description in parent or sibling elements
            parent = element.parent
            if parent:
                # Look for description in nearby text
                text_content = parent.get_text().strip()
                if len(text_content) > len(element.get_text().strip()):
                    return text_content[:200] + "..." if len(text_content) > 200 else text_content
            return ""
        except:
            return ""
    
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
            report_path = os.path.join(self.output_dir, f"hko_open_data_report_{timestamp}.md")
            
            with open(report_path, 'w', encoding='utf-8') as report_file:
                report_file.write("# HKO Open Data Crawling Report\n\n")
                report_file.write(f"**Generated:** {datetime.now().isoformat()}\n")
                report_file.write(f"**Crawler:** HKO Open Data Crawler\n")
                report_file.write(f"**Course:** GCAP3226 - Empowering Citizens Through Data\n\n")
                
                report_file.write("## Summary\n\n")
                report_file.write(f"- **Total Open Data References:** {len(self.open_data_info)}\n")
                report_file.write(f"- **Total TC Impact Data Points:** {len(self.tc_impact_data)}\n")
                report_file.write(f"- **Total Crawl Activities:** {len(self.crawl_log)}\n")
                report_file.write(f"- **Data Directory:** {self.data_dir}\n")
                report_file.write(f"- **Output Directory:** {self.output_dir}\n\n")
                
                report_file.write("## Available Datasets\n\n")
                for i, dataset in enumerate(self.open_data_info, 1):
                    report_file.write(f"### Dataset {i}\n")
                    report_file.write(f"- **Title:** {dataset.get('title', 'N/A')}\n")
                    report_file.write(f"- **URL:** {dataset.get('url', 'N/A')}\n")
                    report_file.write(f"- **Description:** {dataset.get('description', 'N/A')}\n")
                    report_file.write(f"- **Source:** {dataset.get('source', 'N/A')}\n\n")
                
                report_file.write("## TC Impact Data\n\n")
                for i, impact in enumerate(self.tc_impact_data, 1):
                    report_file.write(f"### Impact Data {i}\n")
                    report_file.write(f"- **Timestamp:** {impact.get('timestamp', 'N/A')}\n")
                    report_file.write(f"- **Pattern:** {impact.get('pattern_matched', 'N/A')}\n")
                    report_file.write(f"- **Matches:** {impact.get('matches', 'N/A')}\n")
                    report_file.write(f"- **Context:** {impact.get('context', 'N/A')[:200]}...\n")
                    report_file.write(f"- **Source:** {impact.get('source', 'N/A')}\n\n")
                
                report_file.write("## Crawl Activities Log\n\n")
                for activity in self.crawl_log:
                    report_file.write(f"- **{activity['timestamp']}:** {activity['activity']} - {activity['details']}\n")
            
            self.log_crawl_activity("GENERATE_REPORT", f"Report generated: {report_path}")
            self.logger.info(f"Crawling report generated: {report_path}")
            
        except Exception as e:
            self.log_crawl_activity("REPORT_ERROR", f"Error generating report: {str(e)}")
            self.logger.error(f"Error generating report: {str(e)}")
    
    def crawl_hko_open_data(self):
        """Main crawling function"""
        self.log_crawl_activity("CRAWL_START", "Starting HKO open data crawling")
        self.logger.info("Starting HKO open data crawling")
        
        try:
            # 1. Crawl open data introduction page
            self.log_crawl_activity("CRAWL_OPEN_DATA", "Crawling HKO open data introduction page")
            open_data_response = self.make_request(self.open_data_url)
            if open_data_response:
                datasets = self.parse_open_data_page(open_data_response.text)
                self.open_data_info.extend(datasets)
                self.log_crawl_activity("CRAWL_OPEN_DATA", f"Found {len(datasets)} dataset references")
            
            # 2. Crawl tropical cyclone impact page
            self.log_crawl_activity("CRAWL_TC_IMPACT", "Crawling tropical cyclone impact data page")
            tc_impact_response = self.make_request(self.tc_impact_url)
            if tc_impact_response:
                impact_data = self.parse_tc_impact_page(tc_impact_response.text)
                self.tc_impact_data.extend(impact_data)
                self.log_crawl_activity("CRAWL_TC_IMPACT", f"Found {len(impact_data)} TC impact data points")
            
            # 3. Save data
            self.log_crawl_activity("SAVE_DATA", "Saving collected data")
            
            # Save open data information
            if self.open_data_info:
                self.save_data_to_csv(self.open_data_info, "hko_open_data_info.csv")
                self.save_data_to_json(self.open_data_info, "hko_open_data_info.json")
            
            # Save TC impact data
            if self.tc_impact_data:
                self.save_data_to_csv(self.tc_impact_data, "hko_tc_impact_data.csv")
                self.save_data_to_json(self.tc_impact_data, "hko_tc_impact_data.json")
            
            # Save crawl log
            self.save_data_to_json(self.crawl_log, "hko_open_data_crawl_log.json")
            
            # 4. Generate report
            self.generate_report()
            
            self.log_crawl_activity("CRAWL_COMPLETE", "HKO open data crawling completed successfully")
            self.logger.info("HKO open data crawling completed successfully")
            
            return True
            
        except Exception as e:
            self.log_crawl_activity("CRAWL_ERROR", f"Crawling failed: {str(e)}")
            self.logger.error(f"Crawling failed: {str(e)}")
            return False

def main():
    """Main function to run the HKO open data crawler"""
    print("📊 HKO Open Data Crawler")
    print("=" * 50)
    print("Course: GCAP3226 - Empowering Citizens Through Data")
    print("Author: Dr. Simon Wang, HKBU")
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 50)
    
    # Initialize crawler
    crawler = HKOOpenDataCrawler()
    
    # Run crawling
    success = crawler.crawl_hko_open_data()
    
    if success:
        print("\n✅ Crawling completed successfully!")
        print(f"📁 Data saved to: {crawler.data_dir}")
        print(f"📊 Reports saved to: {crawler.output_dir}")
        print(f"📝 Logs saved to: {crawler.logs_dir}")
    else:
        print("\n❌ Crawling failed. Check logs for details.")
    
    print("\n📊 HKO Open Data Crawler - Complete")

if __name__ == "__main__":
    main()
