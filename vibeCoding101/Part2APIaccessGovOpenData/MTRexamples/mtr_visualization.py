#!/usr/bin/env python3
"""
MTR API with Visualization Example

This script demonstrates how to fetch MTR data and create visualizations.
Perfect for Jupyter notebooks and data analysis.
"""

import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, List, Any

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')


def fetch_mtr_data(line: str, station: str) -> Dict[str, Any]:
    """Fetch data from MTR API"""
    url = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php"
    params = {"line": line, "sta": station}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {}


def extract_train_times(api_response: Dict[str, Any]) -> pd.DataFrame:
    """Extract train arrival times into a DataFrame"""
    trains = []
    
    if api_response.get("status") != 1:
        return pd.DataFrame()
    
    for station_key, station_data in api_response.get("data", {}).items():
        # Process DOWN direction
        for train in station_data.get("DOWN", []):
            trains.append({
                "direction": "DOWN",
                "destination": train.get("dest"),
                "platform": train.get("plat"),
                "minutes": int(train.get("ttnt", 0)),
                "sequence": int(train.get("seq", 0))
            })
        
        # Process UP direction
        for train in station_data.get("UP", []):
            trains.append({
                "direction": "UP",
                "destination": train.get("dest"),
                "platform": train.get("plat"),
                "minutes": int(train.get("ttnt", 0)),
                "sequence": int(train.get("seq", 0))
            })
    
    return pd.DataFrame(trains)


def plot_train_frequency(df: pd.DataFrame, station_name: str):
    """Create a bar chart of train arrival times"""
    if df.empty:
        print("No data to plot")
        return
    
    plt.figure(figsize=(12, 6))
    
    # Separate by direction
    down_trains = df[df['direction'] == 'DOWN']
    up_trains = df[df['direction'] == 'UP']
    
    # Create bar chart
    x_down = down_trains['sequence'] if not down_trains.empty else []
    y_down = down_trains['minutes'] if not down_trains.empty else []
    
    x_up = up_trains['sequence'] if not up_trains.empty else []
    y_up = up_trains['minutes'] if not up_trains.empty else []
    
    if not down_trains.empty:
        plt.bar(x_down, y_down, label='DOWN', alpha=0.7, color='blue', width=0.4)
    
    if not up_trains.empty:
        plt.bar([x + 0.4 for x in x_up], y_up, label='UP', alpha=0.7, color='green', width=0.4)
    
    plt.xlabel('Train Sequence', fontsize=12)
    plt.ylabel('Minutes Until Arrival', fontsize=12)
    plt.title(f'MTR Train Arrival Times - {station_name}', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'mtr_frequency_{station_name}.png', dpi=300, bbox_inches='tight')
    print(f"✓ Chart saved: mtr_frequency_{station_name}.png")
    plt.show()


def plot_platform_usage(df: pd.DataFrame, station_name: str):
    """Create a pie chart showing platform usage"""
    if df.empty:
        print("No data to plot")
        return
    
    plt.figure(figsize=(10, 8))
    
    # Count trains per platform
    platform_counts = df['platform'].value_counts()
    
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
    
    plt.pie(platform_counts.values, labels=[f'Platform {p}' for p in platform_counts.index],
            autopct='%1.1f%%', startangle=90, colors=colors[:len(platform_counts)])
    
    plt.title(f'Platform Usage Distribution - {station_name}', 
              fontsize=14, fontweight='bold', pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f'mtr_platforms_{station_name}.png', dpi=300, bbox_inches='tight')
    print(f"✓ Chart saved: mtr_platforms_{station_name}.png")
    plt.show()


def plot_direction_comparison(df: pd.DataFrame, station_name: str):
    """Compare train frequencies in different directions"""
    if df.empty:
        print("No data to plot")
        return
    
    plt.figure(figsize=(10, 6))
    
    # Count trains by direction
    direction_counts = df['direction'].value_counts()
    
    colors = ['#3498db', '#2ecc71']
    plt.bar(direction_counts.index, direction_counts.values, color=colors, alpha=0.8)
    
    plt.xlabel('Direction', fontsize=12)
    plt.ylabel('Number of Trains', fontsize=12)
    plt.title(f'Train Count by Direction - {station_name}', 
              fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for i, v in enumerate(direction_counts.values):
        plt.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'mtr_directions_{station_name}.png', dpi=300, bbox_inches='tight')
    print(f"✓ Chart saved: mtr_directions_{station_name}.png")
    plt.show()


def create_train_schedule_table(df: pd.DataFrame, station_name: str):
    """Create a formatted table of train schedule"""
    if df.empty:
        print("No data available")
        return
    
    print("\n" + "=" * 80)
    print(f"TRAIN SCHEDULE - {station_name}")
    print("=" * 80)
    print(f"{'Dir':<6} {'Seq':<5} {'Dest':<8} {'Platform':<10} {'Minutes':<10}")
    print("-" * 80)
    
    for _, row in df.iterrows():
        print(f"{row['direction']:<6} {row['sequence']:<5} {row['destination']:<8} "
              f"{row['platform']:<10} {row['minutes']:<10}")
    
    print("=" * 80)


def analyze_multiple_stations(stations_data: List[tuple]):
    """Analyze and compare multiple stations"""
    all_data = []
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('MTR Multi-Station Analysis', fontsize=16, fontweight='bold')
    
    for idx, (line, sta, name) in enumerate(stations_data[:4]):
        print(f"\nFetching data for {name}...")
        data = fetch_mtr_data(line, sta)
        df = extract_train_times(data)
        
        if not df.empty:
            all_data.append((name, df))
            
            # Plot in subplot
            ax = axes[idx // 2, idx % 2]
            direction_counts = df['direction'].value_counts()
            ax.bar(direction_counts.index, direction_counts.values, 
                   color=['#3498db', '#2ecc71'], alpha=0.8)
            ax.set_title(name, fontweight='bold')
            ax.set_ylabel('Number of Trains')
            ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('mtr_multi_station_comparison.png', dpi=300, bbox_inches='tight')
    print("\n✓ Multi-station chart saved: mtr_multi_station_comparison.png")
    plt.show()
    
    return all_data


def main():
    """Main visualization demo"""
    print("=" * 80)
    print("MTR API DATA VISUALIZATION DEMO")
    print("=" * 80)
    
    # Example 1: Single station analysis
    print("\n📊 Example 1: Single Station Analysis")
    print("-" * 80)
    
    station_line = "TML"
    station_code = "TUM"
    station_name = "Tuen Mun"
    
    print(f"Fetching data for {station_name} station...")
    data = fetch_mtr_data(station_line, station_code)
    
    if data.get("status") == 1:
        df = extract_train_times(data)
        
        if not df.empty:
            # Show data summary
            print(f"\n✓ Retrieved {len(df)} trains")
            print(f"  - UP direction: {len(df[df['direction'] == 'UP'])}")
            print(f"  - DOWN direction: {len(df[df['direction'] == 'DOWN'])}")
            
            # Create visualizations
            print("\n📈 Creating visualizations...")
            create_train_schedule_table(df, station_name)
            plot_train_frequency(df, station_name)
            plot_platform_usage(df, station_name)
            plot_direction_comparison(df, station_name)
        else:
            print("No train data available")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")
    
    # Example 2: Multi-station comparison
    print("\n" + "=" * 80)
    print("📊 Example 2: Multi-Station Comparison")
    print("-" * 80)
    
    stations = [
        ("TML", "TUM", "Tuen Mun"),
        ("TML", "MEF", "Mei Foo"),
        ("ISL", "CEN", "Central"),
        ("TWL", "TSW", "Tsim Sha Tsui")
    ]
    
    analyze_multiple_stations(stations)
    
    print("\n" + "=" * 80)
    print("✓ ALL VISUALIZATIONS COMPLETED")
    print("=" * 80)
    print("\nGenerated files:")
    print("  - mtr_frequency_*.png")
    print("  - mtr_platforms_*.png")
    print("  - mtr_directions_*.png")
    print("  - mtr_multi_station_comparison.png")
    print("\nYou can use these images in your reports and presentations!")


if __name__ == "__main__":
    main()
