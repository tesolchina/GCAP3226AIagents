#!/usr/bin/env python3
"""
Simple MTR API Example

A minimal example showing how to use the MTR Next Train API.
Perfect for learning or as a starting point for your own project.
"""

import requests
import json

# API endpoint
API_URL = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php"

def get_next_trains(line_code, station_code):
    """
    Get next train arrivals for a station
    
    Args:
        line_code: MTR line code (e.g., 'TML', 'ISL')
        station_code: Station code (e.g., 'TUM', 'CEN')
    """
    # Set up parameters
    params = {
        'line': line_code,
        'sta': station_code
    }
    
    # Make the API request
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    # Check if successful
    if data.get('status') == 1:
        print(f"\n✓ Success! Data retrieved at {data['curr_time']}")
        print(f"Service delayed: {'Yes' if data['isdelay'] == 'Y' else 'No'}")
        
        # Get station data
        station_key = f"{line_code}-{station_code}"
        station_data = data['data'].get(station_key, {})
        
        # Show DOWN direction trains
        down_trains = station_data.get('DOWN', [])
        if down_trains:
            print(f"\n🚇 Trains going DOWN:")
            for train in down_trains:
                print(f"   → To {train['dest']}: {train['ttnt']} minutes (Platform {train['plat']})")
        
        # Show UP direction trains
        up_trains = station_data.get('UP', [])
        if up_trains:
            print(f"\n🚇 Trains going UP:")
            for train in up_trains:
                print(f"   → To {train['dest']}: {train['ttnt']} minutes (Platform {train['plat']})")
        
        return data
    else:
        print(f"✗ Error: {data.get('message', 'Unknown error')}")
        return None


def main():
    """Main function - try it out!"""
    
    print("=" * 60)
    print("MTR Next Train API - Simple Example")
    print("=" * 60)
    
    # Example 1: Tuen Mun station on Tuen Ma Line
    print("\n📍 Example 1: Tuen Mun Station (Tuen Ma Line)")
    print("-" * 60)
    get_next_trains('TML', 'TUM')
    
    # Example 2: Central station on Island Line
    print("\n📍 Example 2: Central Station (Island Line)")
    print("-" * 60)
    get_next_trains('ISL', 'CEN')
    
    # Example 3: Mong Kok station on Kwun Tong Line
    print("\n📍 Example 3: Mong Kok Station (Kwun Tong Line)")
    print("-" * 60)
    get_next_trains('KTL', 'MOK')
    
    print("\n" + "=" * 60)
    print("✓ Examples completed!")
    print("=" * 60)
    
    # Bonus: Try your own!
    print("\n💡 Try it yourself!")
    print("   Modify the code above to check your favorite station!")
    print("   Common line codes: TML, ISL, KTL, EAL, TWL, TKL")
    print("   Find station codes in README.md")


if __name__ == "__main__":
    main()
