#!/usr/bin/env python3
"""
Simple API Test for Bus Route Analysis
Test basic API access and log results
"""

import requests
import json
from datetime import datetime

def test_kmb_api():
    """Test KMB API access"""
    print("🔍 Testing KMB API...")
    
    try:
        # Test routes endpoint
        response = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route", timeout=10)
        print(f"   Routes API: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            print(f"   ✅ KMB Routes: {len(routes)} routes available")
            return True, len(routes)
        else:
            print(f"   ❌ KMB Routes API error: {response.status_code}")
            return False, 0
            
    except Exception as e:
        print(f"   ❌ KMB API error: {str(e)}")
        return False, 0

def test_citybus_api():
    """Test Citybus API access"""
    print("🔍 Testing Citybus API...")
    
    try:
        # Test routes endpoint
        response = requests.get("https://rt.data.gov.hk/v2/transport/citybus/route/ctb", timeout=10)
        print(f"   Routes API: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            routes = data.get('data', [])
            print(f"   ✅ Citybus Routes: {len(routes)} routes available")
            return True, len(routes)
        else:
            print(f"   ❌ Citybus Routes API error: {response.status_code}")
            return False, 0
            
    except Exception as e:
        print(f"   ❌ Citybus API error: {str(e)}")
        return False, 0

def main():
    """Main test function"""
    print("🚌 Bus Route API Test")
    print("=" * 40)
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 40)
    
    # Test KMB API
    kmb_success, kmb_count = test_kmb_api()
    
    # Test Citybus API
    citybus_success, citybus_count = test_citybus_api()
    
    # Summary
    print("\n📊 Test Summary")
    print("-" * 20)
    print(f"KMB API: {'✅ Success' if kmb_success else '❌ Failed'} ({kmb_count} routes)")
    print(f"Citybus API: {'✅ Success' if citybus_success else '❌ Failed'} ({citybus_count} routes)")
    
    if kmb_success and citybus_success:
        print("\n🎉 All APIs accessible! Ready for data collection.")
        return True
    else:
        print("\n⚠️  Some APIs not accessible. Check connectivity.")
        return False

if __name__ == "__main__":
    success = main()
    print(f"\n{'✅ Test completed successfully!' if success else '❌ Test completed with issues.'}")
