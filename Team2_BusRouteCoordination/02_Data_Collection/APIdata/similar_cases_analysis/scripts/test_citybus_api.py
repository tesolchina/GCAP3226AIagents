#!/usr/bin/env python3
"""
Citybus API Testing Script
Tests all Citybus API endpoints to verify data retrieval capabilities
"""

import requests
import json
from datetime import datetime
import time

def test_citybus_api():
    """Test all Citybus API endpoints"""
    
    print('=== TESTING CITYBUS API DATA RETRIEVAL ===')
    print(f'Test Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print()
    
    base_url = 'https://rt.data.gov.hk/v2/transport/citybus'
    results = {}
    
    # Test 1: Company API
    print('1. Testing Company API...')
    try:
        response = requests.get(f'{base_url}/company/CTB', timeout=10)
        print(f'   Status: {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            print(f'   ✅ Company: {data["data"]["name_en"]}')
            print(f'   📊 Data timestamp: {data["data"]["data_timestamp"]}')
            results['company'] = {'status': 'success', 'data': data}
        else:
            print(f'   ❌ Error: {response.text}')
            results['company'] = {'status': 'error', 'code': response.status_code}
    except Exception as e:
        print(f'   ❌ Exception: {str(e)}')
        results['company'] = {'status': 'exception', 'error': str(e)}
    
    print()
    
    # Test 2: Route API (specific route)
    print('2. Testing Route API (specific route)...')
    try:
        response = requests.get(f'{base_url}/route/CTB/1', timeout=10)
        print(f'   Status: {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            route_data = data['data']
            print(f'   ✅ Route: {route_data["route"]} - {route_data["orig_en"]} to {route_data["dest_en"]}')
            print(f'   📊 Data timestamp: {route_data["data_timestamp"]}')
            results['route_specific'] = {'status': 'success', 'data': data}
        else:
            print(f'   ❌ Error: {response.text}')
            results['route_specific'] = {'status': 'error', 'code': response.status_code}
    except Exception as e:
        print(f'   ❌ Exception: {str(e)}')
        results['route_specific'] = {'status': 'exception', 'error': str(e)}
    
    print()
    
    # Test 3: Route API (all routes)
    print('3. Testing Route API (all routes)...')
    try:
        response = requests.get(f'{base_url}/route/CTB', timeout=15)
        print(f'   Status: {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            routes = data['data']
            print(f'   ✅ Total routes: {len(routes)}')
            print(f'   📊 Sample routes:')
            for i, route in enumerate(routes[:5]):
                print(f'      {i+1}. Route {route["route"]}: {route["orig_en"]} → {route["dest_en"]}')
            print(f'   📊 Generated timestamp: {data["generated_timestamp"]}')
            results['route_all'] = {'status': 'success', 'count': len(routes), 'data': data}
        else:
            print(f'   ❌ Error: {response.text}')
            results['route_all'] = {'status': 'error', 'code': response.status_code}
    except Exception as e:
        print(f'   ❌ Exception: {str(e)}')
        results['route_all'] = {'status': 'exception', 'error': str(e)}
    
    print()
    
    # Test 4: Stop API
    print('4. Testing Stop API...')
    try:
        response = requests.get(f'{base_url}/stop/002403', timeout=10)
        print(f'   Status: {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            stop_data = data['data']
            print(f'   ✅ Stop: {stop_data["stop"]} - {stop_data["name_en"]}')
            print(f'   📍 Coordinates: {stop_data["lat"]}, {stop_data["long"]}')
            print(f'   📊 Data timestamp: {stop_data["data_timestamp"]}')
            results['stop'] = {'status': 'success', 'data': data}
        else:
            print(f'   ❌ Error: {response.text}')
            results['stop'] = {'status': 'error', 'code': response.status_code}
    except Exception as e:
        print(f'   ❌ Exception: {str(e)}')
        results['stop'] = {'status': 'exception', 'error': str(e)}
    
    print()
    
    # Test 5: Route-Stop API
    print('5. Testing Route-Stop API...')
    try:
        response = requests.get(f'{base_url}/route-stop/CTB/1/inbound', timeout=10)
        print(f'   Status: {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            stops = data['data']
            print(f'   ✅ Route 1 inbound stops: {len(stops)}')
            print(f'   📊 Sample stops:')
            for i, stop in enumerate(stops[:3]):
                print(f'      {i+1}. Stop {stop["stop"]} (seq: {stop["seq"]})')
            results['route_stop'] = {'status': 'success', 'count': len(stops), 'data': data}
        else:
            print(f'   ❌ Error: {response.text}')
            results['route_stop'] = {'status': 'error', 'code': response.status_code}
    except Exception as e:
        print(f'   ❌ Exception: {str(e)}')
        results['route_stop'] = {'status': 'exception', 'error': str(e)}
    
    print()
    
    # Test 6: ETA API
    print('6. Testing ETA API...')
    try:
        response = requests.get(f'{base_url}/eta/CTB/002403/1', timeout=10)
        print(f'   Status: {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            etas = data['data']
            print(f'   ✅ ETAs available: {len(etas)}')
            if etas:
                print(f'   📊 Sample ETA: {etas[0]["eta"]}')
            print(f'   📊 Generated timestamp: {data["generated_timestamp"]}')
            results['eta'] = {'status': 'success', 'count': len(etas), 'data': data}
        else:
            print(f'   ❌ Error: {response.text}')
            results['eta'] = {'status': 'error', 'code': response.status_code}
    except Exception as e:
        print(f'   ❌ Exception: {str(e)}')
        results['eta'] = {'status': 'exception', 'error': str(e)}
    
    print()
    print('=== SUMMARY ===')
    
    # Count successful tests
    successful_tests = sum(1 for result in results.values() if result['status'] == 'success')
    total_tests = len(results)
    
    print(f'✅ Successful tests: {successful_tests}/{total_tests}')
    print(f'📊 API endpoints working: {successful_tests}/{total_tests}')
    
    # Save results to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f'data/api_test_results_{timestamp}.json'
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f'📁 Results saved to: {results_file}')
    
    return results

if __name__ == "__main__":
    test_citybus_api()
