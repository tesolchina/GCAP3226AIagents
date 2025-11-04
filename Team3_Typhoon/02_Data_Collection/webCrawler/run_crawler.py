#!/usr/bin/env python3
"""
HKO Typhoon Crawler Runner
==========================
Simple runner script for the HKO Typhoon Signal 8 Web Crawler

Usage: python run_crawler.py
"""

import sys
import os
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from hko_typhoon_crawler import HKOTyphoonCrawler, main
except ImportError as e:
    print(f"❌ Error importing crawler: {e}")
    print("Please ensure hko_typhoon_crawler.py is in the same directory")
    sys.exit(1)

def run_crawler():
    """Run the HKO typhoon crawler"""
    print("🚀 Starting HKO Typhoon Signal 8 Web Crawler")
    print("=" * 60)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Working Directory: {os.getcwd()}")
    print("=" * 60)
    
    try:
        # Run the main crawler
        main()
        
        print("\n🎉 Crawler execution completed!")
        print("📊 Check the output directories for results:")
        print("   - data/     : Collected data files")
        print("   - output/   : Generated reports")
        print("   - logs/     : Crawling logs")
        
    except Exception as e:
        print(f"\n❌ Crawler execution failed: {e}")
        print("📝 Check the logs directory for error details")
        return False
    
    return True

if __name__ == "__main__":
    success = run_crawler()
    sys.exit(0 if success else 1)
