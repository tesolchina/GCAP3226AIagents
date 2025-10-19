#!/usr/bin/env python3
"""
Analyze crawl results from cyberdefender.hk
"""

import json
from pathlib import Path
from collections import Counter

def analyze_results():
    """Analyze the crawl results"""
    
    # Find most recent results file
    analysis_dir = Path("analysis")
    results_files = list(analysis_dir.glob("crawl_results_*.json"))
    
    if not results_files:
        print("No results files found!")
        return
    
    latest_file = max(results_files, key=lambda p: p.stat().st_mtime)
    print(f"Analyzing: {latest_file}\n")
    
    with open(latest_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    stats = data['stats']
    results = data['results']
    
    # Print summary
    print("=" * 80)
    print("CRAWL ANALYSIS")
    print("=" * 80)
    print(f"\nOverall Statistics:")
    print(f"  Total URLs: {stats['urls_visited']}")
    print(f"  Pages with data: {stats['pages_with_data']}")
    print(f"  Files downloaded: {stats['files_downloaded']}")
    print(f"  Errors: {stats['errors']}")
    print(f"  Success rate: {(stats['pages_with_data'] / max(stats['urls_visited'], 1)) * 100:.1f}%")
    
    # Analyze detection patterns
    pages_with_data = [r for r in results if r['has_data']]
    
    if pages_with_data:
        print(f"\n\nData Detection Breakdown:")
        
        has_numbers = sum(1 for r in pages_with_data if r['metadata'] and r['metadata'].get('has_numbers'))
        has_tables = sum(1 for r in pages_with_data if r['metadata'] and r['metadata'].get('has_tables'))
        has_charts = sum(1 for r in pages_with_data if r['metadata'] and r['metadata'].get('has_charts'))
        has_stats = sum(1 for r in pages_with_data if r['metadata'] and r['metadata'].get('has_statistics'))
        
        print(f"  Pages with numbers: {has_numbers}")
        print(f"  Pages with tables: {has_tables}")
        print(f"  Pages with charts: {has_charts}")
        print(f"  Pages with statistics: {has_stats}")
        
        # Keyword analysis
        all_keywords = []
        for r in pages_with_data:
            if r['metadata'] and 'keywords_found' in r['metadata']:
                all_keywords.extend(r['metadata']['keywords_found'])
        
        if all_keywords:
            print(f"\n\nTop Keywords Found:")
            keyword_counts = Counter(all_keywords)
            for keyword, count in keyword_counts.most_common(10):
                print(f"  {keyword}: {count}")
        
        # Number distribution
        number_counts = [r['metadata']['number_count'] for r in pages_with_data if r['metadata']]
        if number_counts:
            print(f"\n\nNumber Count Distribution:")
            print(f"  Average numbers per page: {sum(number_counts) / len(number_counts):.1f}")
            print(f"  Max numbers on a page: {max(number_counts)}")
            print(f"  Min numbers on a page: {min(number_counts)}")
        
        # Show sample URLs with data
        print(f"\n\nSample Pages with Data:")
        for r in pages_with_data[:5]:
            print(f"\n  {r['url']}")
            if r['metadata']:
                print(f"    Numbers: {r['metadata'].get('number_count', 0)}, "
                      f"Tables: {r['metadata'].get('table_count', 0)}, "
                      f"Keywords: {', '.join(r['metadata'].get('keywords_found', [])[:3])}")
    
    print("\n" + "=" * 80)

if __name__ == '__main__':
    analyze_results()
