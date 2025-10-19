#!/usr/bin/env python3
"""
Quick crawl focusing on download pages which likely have quantitative data
"""

import sys
sys.path.append('/workspaces/GCAP3226AIagents/vibeCoding101/Part3WebCrawler/cyberdefender/scripts')

from crawler import CyberDefenderCrawler
import xml.etree.ElementTree as ET

def main():
    crawler = CyberDefenderCrawler(output_dir="data")
    
    # Fetch just the downloads sitemap
    crawler.log("Focusing on downloads sitemap...")
    downloads_sitemap = "https://cyberdefender.hk/sdm_downloads-sitemap.xml"
    
    urls = crawler.fetch_sitemap(downloads_sitemap)
    crawler.log(f"Found {len(urls)} download pages")
    
    # Crawl each download page
    results = []
    for i, url in enumerate(urls, 1):
        crawler.log(f"\n--- Download Page {i}/{len(urls)} ---")
        has_data, metadata = crawler.crawl_page(url)
        results.append({
            'url': url,
            'has_data': has_data,
            'metadata': metadata
        })
        
        import time
        time.sleep(2)  # Rate limiting
    
    crawler.save_results(results)
    crawler.log_summary()

if __name__ == '__main__':
    main()
