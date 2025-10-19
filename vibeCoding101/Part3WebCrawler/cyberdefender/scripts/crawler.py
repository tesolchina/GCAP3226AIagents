#!/usr/bin/env python3
"""
Cyberdefender.hk Web Crawler
GCAP3226 - Web Crawling for Policy Analysis

This script crawls cyberdefender.hk to extract pages and files containing
quantitative data for policy analysis.

Author: GCAP3226 Course Team
Date: October 13, 2025
"""

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re
import time
import json
import os
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin, urlparse
import hashlib

class CyberDefenderCrawler:
    """Web crawler for cyberdefender.hk with quantitative data detection"""
    
    def __init__(self, base_url="https://cyberdefender.hk", output_dir="data"):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'GCAP3226-Educational-Crawler/1.0 (Policy Analysis Research)'
        })
        
        # Create output directories
        self.pages_dir = self.output_dir / "pages"
        self.downloads_dir = self.output_dir / "downloads"
        self.sitemaps_dir = self.output_dir / "sitemaps"
        self.logs_dir = Path("logs")
        
        for directory in [self.pages_dir, self.downloads_dir, self.sitemaps_dir, self.logs_dir]:
            directory.mkdir(parents=True, exist_ok=True)
        
        # Initialize logging
        self.log_file = self.logs_dir / f"crawl_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        self.stats = {
            'urls_visited': 0,
            'pages_with_data': 0,
            'files_downloaded': 0,
            'errors': 0,
            'start_time': datetime.now().isoformat()
        }
        
    def log(self, message, level="INFO"):
        """Log message to file and console"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] [{level}] {message}"
        print(log_message)
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_message + '\n')
    
    def fetch_sitemaps(self):
        """Fetch and parse all sitemaps"""
        self.log("Fetching sitemap index...")
        sitemap_index_url = f"{self.base_url}/sitemap_index.xml"
        
        try:
            response = self.session.get(sitemap_index_url, timeout=10)
            response.raise_for_status()
            
            # Save sitemap index
            with open(self.sitemaps_dir / "sitemap_index.xml", 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            # Parse sitemap index
            root = ET.fromstring(response.content)
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            
            sitemap_urls = []
            for sitemap in root.findall('.//ns:sitemap', namespace):
                loc = sitemap.find('ns:loc', namespace)
                if loc is not None:
                    sitemap_urls.append(loc.text)
            
            self.log(f"Found {len(sitemap_urls)} sitemaps")
            
            # Fetch individual sitemaps
            all_urls = []
            for sitemap_url in sitemap_urls:
                time.sleep(1)  # Rate limiting
                urls = self.fetch_sitemap(sitemap_url)
                all_urls.extend(urls)
            
            self.log(f"Total URLs found: {len(all_urls)}")
            return all_urls
            
        except Exception as e:
            self.log(f"Error fetching sitemaps: {str(e)}", "ERROR")
            self.stats['errors'] += 1
            return []
    
    def fetch_sitemap(self, sitemap_url):
        """Fetch and parse individual sitemap"""
        try:
            sitemap_name = urlparse(sitemap_url).path.split('/')[-1]
            self.log(f"Fetching {sitemap_name}...")
            
            response = self.session.get(sitemap_url, timeout=10)
            response.raise_for_status()
            
            # Save sitemap
            with open(self.sitemaps_dir / sitemap_name, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            # Parse URLs
            root = ET.fromstring(response.content)
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            
            urls = []
            for url_elem in root.findall('.//ns:url', namespace):
                loc = url_elem.find('ns:loc', namespace)
                if loc is not None:
                    urls.append(loc.text)
            
            self.log(f"  → Found {len(urls)} URLs in {sitemap_name}")
            return urls
            
        except Exception as e:
            self.log(f"Error fetching {sitemap_url}: {str(e)}", "ERROR")
            self.stats['errors'] += 1
            return []
    
    def has_quantitative_data(self, soup, url):
        """
        Detect if page contains quantitative data
        Returns: (bool, dict) - (has_data, metadata)
        """
        metadata = {
            'url': url,
            'has_numbers': False,
            'has_tables': False,
            'has_charts': False,
            'has_statistics': False,
            'number_count': 0,
            'keywords_found': []
        }
        
        # Get text content
        text = soup.get_text()
        
        # Count numbers (looking for meaningful numbers, not just dates)
        # Match numbers with context: percentages, currency, large numbers
        number_patterns = [
            r'\d+(?:\.\d+)?%',  # Percentages
            r'\$\d+(?:,\d{3})*(?:\.\d{2})?',  # Currency
            r'HK\$\d+(?:,\d{3})*',  # HK currency
            r'\d{1,3}(?:,\d{3})+',  # Numbers with commas
            r'\b\d+(?:\.\d+)?\s*(?:million|billion|thousand)',  # Large numbers with words
        ]
        
        for pattern in number_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            metadata['number_count'] += len(matches)
        
        if metadata['number_count'] > 5:  # Threshold: at least 5 meaningful numbers
            metadata['has_numbers'] = True
        
        # Check for tables
        tables = soup.find_all('table')
        if tables:
            metadata['has_tables'] = True
            metadata['table_count'] = len(tables)
        
        # Check for chart/graph indicators
        chart_indicators = ['chart', 'graph', 'diagram', 'visualization', 'figure']
        for indicator in chart_indicators:
            if indicator.lower() in text.lower():
                metadata['has_charts'] = True
                metadata['keywords_found'].append(indicator)
                break
        
        # Check for statistical keywords
        stat_keywords = [
            'statistics', 'data', 'analysis', 'report', 'survey',
            'percentage', 'total', 'average', 'median', 'trend',
            'increase', 'decrease', 'comparison', 'growth', 'rate'
        ]
        
        for keyword in stat_keywords:
            if keyword.lower() in text.lower():
                metadata['has_statistics'] = True
                metadata['keywords_found'].append(keyword)
        
        # Check for downloadable data files
        download_links = soup.find_all('a', href=re.compile(r'\.(pdf|xlsx?|csv|doc|docx)$', re.I))
        if download_links:
            metadata['downloadable_files'] = len(download_links)
        
        # Determine if page has quantitative data
        has_data = (
            metadata['has_numbers'] or 
            metadata['has_tables'] or 
            (metadata['has_charts'] and metadata['has_statistics'])
        )
        
        return has_data, metadata
    
    def crawl_page(self, url):
        """Crawl a single page and analyze for quantitative data"""
        try:
            self.log(f"Crawling: {url}")
            self.stats['urls_visited'] += 1
            
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Check for quantitative data
            has_data, metadata = self.has_quantitative_data(soup, url)
            
            if has_data:
                self.stats['pages_with_data'] += 1
                self.log(f"  ✓ Page has quantitative data! Numbers: {metadata['number_count']}, "
                        f"Tables: {metadata.get('table_count', 0)}", "INFO")
                
                # Save page
                self.save_page(url, response.content, metadata)
                
                # Download linked files
                self.download_files(soup, url)
                
                return True, metadata
            else:
                self.log(f"  ✗ No significant quantitative data found", "DEBUG")
                return False, metadata
            
        except Exception as e:
            self.log(f"Error crawling {url}: {str(e)}", "ERROR")
            self.stats['errors'] += 1
            return False, None
    
    def save_page(self, url, content, metadata):
        """Save HTML page and metadata"""
        # Create safe filename from URL
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        path_part = urlparse(url).path.replace('/', '_').strip('_')
        if not path_part:
            path_part = "index"
        filename = f"{path_part}_{url_hash}.html"
        
        # Save HTML
        filepath = self.pages_dir / filename
        with open(filepath, 'wb') as f:
            f.write(content)
        
        # Save metadata
        metadata_file = filepath.with_suffix('.json')
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        self.log(f"  → Saved: {filename}")
    
    def download_files(self, soup, page_url):
        """Download PDF, Excel, and other data files"""
        # Find all links to downloadable files
        file_patterns = r'\.(pdf|xlsx?|csv|doc|docx|pptx?)$'
        links = soup.find_all('a', href=re.compile(file_patterns, re.I))
        
        for link in links:
            href = link.get('href')
            if not href:
                continue
            
            # Make absolute URL
            file_url = urljoin(page_url, href)
            
            try:
                self.log(f"  → Downloading file: {file_url}")
                response = self.session.get(file_url, timeout=30)
                response.raise_for_status()
                
                # Get filename
                filename = os.path.basename(urlparse(file_url).path)
                if not filename:
                    filename = f"file_{hashlib.md5(file_url.encode()).hexdigest()[:8]}"
                
                filepath = self.downloads_dir / filename
                
                # Save file
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                
                self.stats['files_downloaded'] += 1
                self.log(f"    ✓ Downloaded: {filename}")
                
                time.sleep(1)  # Rate limiting
                
            except Exception as e:
                self.log(f"    ✗ Error downloading {file_url}: {str(e)}", "ERROR")
                self.stats['errors'] += 1
    
    def crawl_site(self, max_pages=None):
        """Crawl entire site using sitemap"""
        self.log("=" * 80)
        self.log("Starting Cyberdefender.hk Crawl")
        self.log("=" * 80)
        
        # Fetch all URLs from sitemaps
        urls = self.fetch_sitemaps()
        
        if max_pages:
            urls = urls[:max_pages]
            self.log(f"Limiting crawl to {max_pages} pages (for testing)")
        
        # Crawl each URL
        results = []
        for i, url in enumerate(urls, 1):
            self.log(f"\n--- Page {i}/{len(urls)} ---")
            has_data, metadata = self.crawl_page(url)
            results.append({
                'url': url,
                'has_data': has_data,
                'metadata': metadata
            })
            
            # Rate limiting: 2 seconds between requests
            time.sleep(2)
        
        # Save final results
        self.save_results(results)
        self.log_summary()
    
    def save_results(self, results):
        """Save crawl results to JSON"""
        results_file = self.output_dir.parent / "analysis" / f"crawl_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump({
                'stats': self.stats,
                'results': results
            }, f, indent=2, ensure_ascii=False)
        
        self.log(f"Results saved to: {results_file}")
    
    def log_summary(self):
        """Log final statistics"""
        self.stats['end_time'] = datetime.now().isoformat()
        
        self.log("\n" + "=" * 80)
        self.log("CRAWL SUMMARY")
        self.log("=" * 80)
        self.log(f"URLs visited: {self.stats['urls_visited']}")
        self.log(f"Pages with quantitative data: {self.stats['pages_with_data']}")
        self.log(f"Files downloaded: {self.stats['files_downloaded']}")
        self.log(f"Errors encountered: {self.stats['errors']}")
        self.log(f"Success rate: {(self.stats['pages_with_data'] / max(self.stats['urls_visited'], 1)) * 100:.1f}%")
        self.log("=" * 80)


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Crawl cyberdefender.hk for quantitative data')
    parser.add_argument('--max-pages', type=int, help='Maximum number of pages to crawl (for testing)')
    parser.add_argument('--output-dir', default='data', help='Output directory for data')
    
    args = parser.parse_args()
    
    crawler = CyberDefenderCrawler(output_dir=args.output_dir)
    crawler.crawl_site(max_pages=args.max_pages)


if __name__ == '__main__':
    main()
