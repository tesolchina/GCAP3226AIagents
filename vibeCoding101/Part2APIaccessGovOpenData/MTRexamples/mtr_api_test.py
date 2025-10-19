#!/usr/bin/env python3
"""
MTR Next Train API Test Script

This script demonstrates how to access the Hong Kong MTR Next Train API
and retrieve real-time train arrival information.

Author: Generated for GCAP3226 Course
Date: 2025-10-13
"""

import requests
import json
from datetime import datetime
from typing import Dict, List, Any


class MTRAPIClient:
    """Client for accessing MTR Next Train API"""
    
    BASE_URL = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php"
    
    def __init__(self, language: str = "EN"):
        """
        Initialize the MTR API client
        
        Args:
            language: Response language (EN, TC, or SC)
        """
        self.language = language
        
    def get_next_train(self, line: str, station: str) -> Dict[str, Any]:
        """
        Get next train information for a specific line and station
        
        Args:
            line: MTR line code (e.g., 'TML', 'ISL', 'KTL')
            station: Station code (e.g., 'TUM', 'CEN', 'MOK')
            
        Returns:
            Dictionary containing train schedule data
        """
        params = {
            "line": line,
            "sta": station,
            "lang": self.language
        }
        
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "status": 0,
                "message": f"Error: {str(e)}",
                "error": str(e)
            }
    
    def parse_train_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse and format train data for easier consumption
        
        Args:
            data: Raw API response data
            
        Returns:
            Formatted train information
        """
        if data.get("status") != 1:
            return {
                "success": False,
                "message": data.get("message", "Unknown error"),
                "error": data.get("error", {})
            }
        
        result = {
            "success": True,
            "system_time": data.get("sys_time"),
            "current_time": data.get("curr_time"),
            "is_delayed": data.get("isdelay") == "Y",
            "stations": {}
        }
        
        # Parse station data
        for station_key, station_data in data.get("data", {}).items():
            station_info = {
                "up_trains": [],
                "down_trains": []
            }
            
            # Process UP direction trains
            for train in station_data.get("UP", []):
                station_info["up_trains"].append({
                    "sequence": train.get("seq"),
                    "destination": train.get("dest"),
                    "platform": train.get("plat"),
                    "time": train.get("time"),
                    "minutes_to_arrival": train.get("ttnt"),
                    "valid": train.get("valid") == "Y"
                })
            
            # Process DOWN direction trains
            for train in station_data.get("DOWN", []):
                station_info["down_trains"].append({
                    "sequence": train.get("seq"),
                    "destination": train.get("dest"),
                    "platform": train.get("plat"),
                    "time": train.get("time"),
                    "minutes_to_arrival": train.get("ttnt"),
                    "valid": train.get("valid") == "Y"
                })
            
            result["stations"][station_key] = station_info
        
        return result


def test_single_station():
    """Test API with a single station"""
    print("=" * 80)
    print("Test 1: Single Station Query")
    print("=" * 80)
    
    client = MTRAPIClient()
    
    # Test with Tuen Mun station on Tuen Ma Line
    line = "TML"
    station = "TUM"
    
    print(f"\nQuerying: Line {line}, Station {station}")
    print("-" * 80)
    
    data = client.get_next_train(line, station)
    parsed = client.parse_train_data(data)
    
    if parsed["success"]:
        print(f"✓ Success!")
        print(f"System Time: {parsed['system_time']}")
        print(f"Current Time: {parsed['current_time']}")
        print(f"Service Delayed: {'Yes' if parsed['is_delayed'] else 'No'}")
        
        for station_key, station_info in parsed["stations"].items():
            print(f"\n{station_key}:")
            
            if station_info["down_trains"]:
                print("  DOWN direction:")
                for train in station_info["down_trains"]:
                    print(f"    Train to {train['destination']}: "
                          f"{train['minutes_to_arrival']} min (Platform {train['platform']})")
            
            if station_info["up_trains"]:
                print("  UP direction:")
                for train in station_info["up_trains"]:
                    print(f"    Train to {train['destination']}: "
                          f"{train['minutes_to_arrival']} min (Platform {train['platform']})")
    else:
        print(f"✗ Failed: {parsed['message']}")
    
    return data


def test_multiple_stations():
    """Test API with multiple stations"""
    print("\n" + "=" * 80)
    print("Test 2: Multiple Stations Query")
    print("=" * 80)
    
    client = MTRAPIClient()
    
    # Test stations on different lines
    test_cases = [
        ("TML", "TUM", "Tuen Ma Line - Tuen Mun"),
        ("TML", "TIS", "Tuen Ma Line - Tin Shui Wai"),
        ("TML", "MEF", "Tuen Ma Line - Mei Foo"),
        ("TML", "HUH", "Tuen Ma Line - Hung Hom"),
        ("ISL", "CEN", "Island Line - Central"),
        ("TWL", "TSW", "Tsuen Wan Line - Tsim Sha Tsui"),
    ]
    
    results = []
    
    for line, station, description in test_cases:
        print(f"\nQuerying: {description}")
        print("-" * 80)
        
        data = client.get_next_train(line, station)
        parsed = client.parse_train_data(data)
        
        if parsed["success"]:
            train_count = sum(
                len(info["up_trains"]) + len(info["down_trains"])
                for info in parsed["stations"].values()
            )
            print(f"✓ Success! Found {train_count} upcoming trains")
            results.append({
                "line": line,
                "station": station,
                "description": description,
                "data": data,
                "parsed": parsed
            })
        else:
            print(f"✗ Failed: {parsed['message']}")
            results.append({
                "line": line,
                "station": station,
                "description": description,
                "error": parsed.get("message")
            })
    
    return results


def generate_summary_report(results: List[Dict[str, Any]]) -> str:
    """Generate a summary report of all API tests"""
    report = []
    report.append("=" * 80)
    report.append("MTR API TEST SUMMARY REPORT")
    report.append("=" * 80)
    report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    
    successful = sum(1 for r in results if "parsed" in r and r["parsed"]["success"])
    total = len(results)
    
    report.append(f"Tests Completed: {total}")
    report.append(f"Successful: {successful}")
    report.append(f"Failed: {total - successful}")
    report.append("")
    
    report.append("Detailed Results:")
    report.append("-" * 80)
    
    for i, result in enumerate(results, 1):
        report.append(f"\n{i}. {result['description']} ({result['line']}-{result['station']})")
        
        if "parsed" in result and result["parsed"]["success"]:
            parsed = result["parsed"]
            report.append(f"   Status: ✓ SUCCESS")
            report.append(f"   System Time: {parsed['system_time']}")
            report.append(f"   Delayed: {'Yes' if parsed['is_delayed'] else 'No'}")
            
            for station_key, station_info in parsed["stations"].items():
                total_trains = len(station_info["up_trains"]) + len(station_info["down_trains"])
                report.append(f"   Trains Found: {total_trains}")
                
                if station_info["down_trains"]:
                    report.append(f"   DOWN: {len(station_info['down_trains'])} trains")
                if station_info["up_trains"]:
                    report.append(f"   UP: {len(station_info['up_trains'])} trains")
        else:
            report.append(f"   Status: ✗ FAILED")
            report.append(f"   Error: {result.get('error', 'Unknown error')}")
    
    report.append("\n" + "=" * 80)
    report.append("END OF REPORT")
    report.append("=" * 80)
    
    return "\n".join(report)


def main():
    """Main test function"""
    print("\n" + "=" * 80)
    print("MTR NEXT TRAIN API TEST SCRIPT")
    print("=" * 80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Test 1: Single station
    single_result = test_single_station()
    
    # Test 2: Multiple stations
    multiple_results = test_multiple_stations()
    
    # Combine all results
    all_results = [
        {
            "line": "TML",
            "station": "TUM",
            "description": "Tuen Ma Line - Tuen Mun (Single Test)",
            "data": single_result,
            "parsed": MTRAPIClient().parse_train_data(single_result)
        }
    ] + multiple_results
    
    # Generate summary report
    report = generate_summary_report(all_results)
    print("\n" + report)
    
    # Save output to JSON file
    output_file = "mtr_api_output.json"
    output_data = {
        "test_timestamp": datetime.now().isoformat(),
        "total_tests": len(all_results),
        "results": all_results
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Full output saved to: {output_file}")
    
    # Save summary report to text file
    report_file = "mtr_api_report.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✓ Summary report saved to: {report_file}")
    
    print("\n" + "=" * 80)
    print("ALL TESTS COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    main()
