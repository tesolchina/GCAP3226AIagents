#!/usr/bin/env python3
"""
Test API Access for Bus Route Analysis
Simple script to test API access and log results
"""

import requests
import json
from datetime import datetime
import os

def test_api_access():
    """Test API access for both KMB and Citybus"""
    
    # Create logs directory
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/api_test_{timestamp}.log"
    
    print("🚌 Testing Bus Route API Access")
    print("=" * 50)
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Log File: {log_file}")
    print("=" * 50)
    
    results = {
        'test_date': datetime.now().isoformat(),
        'kmb_tests': {},
        'citybus_tests': {},
        'summary': {}
    }
    
    # Test KMB API
    print("\n🔍 Testing KMB API...")
    kmb_tests = [
        {
            'name': 'KMB Routes',
            'url': 'https://data.etabus.gov.hk/v1/transport/kmb/route',
            'description': 'Get all KMB routes'
        },
        {
            'name': 'KMB Stops',
            'url': 'https://data.etabus.gov.hk/v1/transport/kmb/stop',
            'description': 'Get all KMB stops'
        },
        {
            'name': 'KMB Route-Stop',
            'url': 'https://data.etabus.gov.hk/v1/transport/kmb/route-stop',
            'description': 'Get KMB route-stop mappings'
        }
    ]
    
    for test in kmb_tests:
        print(f"   Testing: {test['name']}")
        try:
            response = requests.get(test['url'], timeout=10)
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    count = len(data['data'])
                    print(f"   ✅ Success: {count} items")
                    results['kmb_tests'][test['name']] = {
                        'status': 'success',
                        'status_code': response.status_code,
                        'data_count': count,
                        'url': test['url']
                    }
                else:
                    print(f"   ⚠️  Success but no data array")
                    results['kmb_tests'][test['name']] = {
                        'status': 'success_no_data',
                        'status_code': response.status_code,
                        'data_count': 0,
                        'url': test['url']
                    }
            else:
                print(f"   ❌ Error: {response.status_code}")
                results['kmb_tests'][test['name']] = {
                    'status': 'error',
                    'status_code': response.status_code,
                    'data_count': 0,
                    'url': test['url']
                }
        except Exception as e:
            print(f"   ❌ Exception: {str(e)}")
            results['kmb_tests'][test['name']] = {
                'status': 'exception',
                'error': str(e),
                'url': test['url']
            }
    
    # Test Citybus API
    print("\n🔍 Testing Citybus API...")
    citybus_tests = [
        {
            'name': 'Citybus Routes',
            'url': 'https://rt.data.gov.hk/v2/transport/citybus/route/ctb',
            'description': 'Get all Citybus routes'
        },
        {
            'name': 'Citybus Company',
            'url': 'https://rt.data.gov.hk/v2/transport/citybus/company/ctb',
            'description': 'Get Citybus company info'
        }
    ]
    
    for test in citybus_tests:
        print(f"   Testing: {test['name']}")
        try:
            response = requests.get(test['url'], timeout=10)
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    count = len(data['data'])
                    print(f"   ✅ Success: {count} items")
                    results['citybus_tests'][test['name']] = {
                        'status': 'success',
                        'status_code': response.status_code,
                        'data_count': count,
                        'url': test['url']
                    }
                else:
                    print(f"   ⚠️  Success but no data array")
                    results['citybus_tests'][test['name']] = {
                        'status': 'success_no_data',
                        'status_code': response.status_code,
                        'data_count': 0,
                        'url': test['url']
                    }
            else:
                print(f"   ❌ Error: {response.status_code}")
                results['citybus_tests'][test['name']] = {
                    'status': 'error',
                    'status_code': response.status_code,
                    'data_count': 0,
                    'url': test['url']
                }
        except Exception as e:
            print(f"   ❌ Exception: {str(e)}")
            results['citybus_tests'][test['name']] = {
                'status': 'exception',
                'error': str(e),
                'url': test['url']
            }
    
    # Generate summary
    print("\n📊 TEST SUMMARY")
    print("-" * 30)
    
    kmb_success = sum(1 for test in results['kmb_tests'].values() if test['status'] == 'success')
    citybus_success = sum(1 for test in results['citybus_tests'].values() if test['status'] == 'success')
    
    print(f"KMB API Tests: {kmb_success}/{len(results['kmb_tests'])} successful")
    print(f"Citybus API Tests: {citybus_success}/{len(results['citybus_tests'])} successful")
    
    results['summary'] = {
        'kmb_success_rate': kmb_success / len(results['kmb_tests']),
        'citybus_success_rate': citybus_success / len(results['citybus_tests']),
        'total_tests': len(results['kmb_tests']) + len(results['citybus_tests']),
        'successful_tests': kmb_success + citybus_success
    }
    
    # Save results
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Results saved to: {log_file}")
    print("✅ API testing completed!")
    
    return results

if __name__ == "__main__":
    results = test_api_access()
