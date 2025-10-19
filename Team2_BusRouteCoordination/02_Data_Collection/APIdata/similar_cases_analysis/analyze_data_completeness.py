#!/usr/bin/env python3
"""
Data Completeness Analysis Script
Analyze what data we have and what's missing for overlap analysis
"""

import os
import pandas as pd
from datetime import datetime

print("📊 DATA COMPLETENESS ANALYSIS")
print("=" * 80)
print(f"📅 Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

# Check data directory
data_dir = "data/collected_data"
print(f"🔍 Checking data directory: {data_dir}")

if not os.path.exists(data_dir):
    print("❌ Data directory does not exist!")
    exit(1)

# List all files
files = os.listdir(data_dir)
print(f"\n📁 Found {len(files)} files in data directory:")

# Categorize files
kmb_routes = [f for f in files if 'kmb' in f and 'routes' in f and f.endswith('.csv')]
kmb_stops = [f for f in files if 'kmb' in f and 'stops' in f and f.endswith('.csv')]
citybus_routes = [f for f in files if 'citybus' in f and 'routes' in f and f.endswith('.csv')]
citybus_stops = [f for f in files if 'citybus' in f and 'stops' in f and f.endswith('.csv')]
route_mappings = [f for f in files if 'mappings' in f and f.endswith('.csv')]

print(f"\n📊 DATA CATEGORIZATION:")
print(f"   🚌 KMB Routes: {len(kmb_routes)} files")
print(f"   🚌 KMB Stops: {len(kmb_stops)} files")
print(f"   🚌 Citybus Routes: {len(citybus_routes)} files")
print(f"   🚌 Citybus Stops: {len(citybus_stops)} files")
print(f"   🚌 Route Mappings: {len(route_mappings)} files")

# Check data completeness
print(f"\n✅ DATA COMPLETENESS CHECK:")
print("=" * 50)

# KMB Routes
if kmb_routes:
    latest_kmb_routes = max(kmb_routes)
    print(f"✅ KMB Routes: {latest_kmb_routes}")
    try:
        df = pd.read_csv(f"{data_dir}/{latest_kmb_routes}")
        print(f"   📊 Records: {len(df)} routes")
        print(f"   📋 Columns: {list(df.columns)}")
    except Exception as e:
        print(f"   ❌ Error reading file: {e}")
else:
    print("❌ KMB Routes: MISSING")

# KMB Stops
if kmb_stops:
    latest_kmb_stops = max(kmb_stops)
    print(f"✅ KMB Stops: {latest_kmb_stops}")
    try:
        df = pd.read_csv(f"{data_dir}/{latest_kmb_stops}")
        print(f"   📊 Records: {len(df)} stops")
        print(f"   📋 Columns: {list(df.columns)}")
    except Exception as e:
        print(f"   ❌ Error reading file: {e}")
else:
    print("❌ KMB Stops: MISSING")

# Citybus Routes
if citybus_routes:
    latest_citybus_routes = max(citybus_routes)
    print(f"✅ Citybus Routes: {latest_citybus_routes}")
    try:
        df = pd.read_csv(f"{data_dir}/{latest_citybus_routes}")
        print(f"   📊 Records: {len(df)} routes")
        print(f"   📋 Columns: {list(df.columns)}")
    except Exception as e:
        print(f"   ❌ Error reading file: {e}")
else:
    print("❌ Citybus Routes: MISSING")

# Citybus Stops
if citybus_stops:
    latest_citybus_stops = max(citybus_stops)
    print(f"✅ Citybus Stops: {latest_citybus_stops}")
    try:
        df = pd.read_csv(f"{data_dir}/{latest_citybus_stops}")
        print(f"   📊 Records: {len(df)} stops")
        print(f"   📋 Columns: {list(df.columns)}")
    except Exception as e:
        print(f"   ❌ Error reading file: {e}")
else:
    print("❌ Citybus Stops: MISSING")

# Route Mappings
if route_mappings:
    latest_mappings = max(route_mappings)
    print(f"✅ Route Mappings: {latest_mappings}")
    try:
        df = pd.read_csv(f"{data_dir}/{latest_mappings}")
        print(f"   📊 Records: {len(df)} mappings")
        print(f"   📋 Columns: {list(df.columns)}")
        
        # Analyze route coverage
        unique_routes = df['route'].nunique() if 'route' in df.columns else 0
        unique_operators = df['operator'].nunique() if 'operator' in df.columns else 0
        print(f"   🚌 Unique Routes: {unique_routes}")
        print(f"   🚌 Unique Operators: {unique_operators}")
        
        if 'operator' in df.columns:
            operator_counts = df['operator'].value_counts()
            print(f"   📊 Operator Distribution:")
            for operator, count in operator_counts.items():
                print(f"      {operator}: {count} mappings")
        
    except Exception as e:
        print(f"   ❌ Error reading file: {e}")
else:
    print("❌ Route Mappings: MISSING")

# Summary
print(f"\n📊 SUMMARY:")
print("=" * 50)

missing_data = []
if not kmb_routes:
    missing_data.append("KMB Routes")
if not kmb_stops:
    missing_data.append("KMB Stops")
if not citybus_routes:
    missing_data.append("Citybus Routes")
if not citybus_stops:
    missing_data.append("Citybus Stops")
if not route_mappings:
    missing_data.append("Route Mappings")

if missing_data:
    print(f"❌ MISSING DATA:")
    for item in missing_data:
        print(f"   - {item}")
else:
    print("✅ ALL DATA AVAILABLE!")

# Check for overlap analysis readiness
print(f"\n🔍 OVERLAP ANALYSIS READINESS:")
print("=" * 50)

if kmb_routes and kmb_stops and citybus_routes and route_mappings:
    print("✅ READY FOR OVERLAP ANALYSIS!")
    print("   - KMB routes and stops available")
    print("   - Citybus routes available")
    print("   - Route-stop mappings available")
    print("   - Can identify overlapping stops between routes")
else:
    print("❌ NOT READY FOR OVERLAP ANALYSIS")
    print("   Missing required data for comprehensive analysis")

# Recommendations
print(f"\n💡 RECOMMENDATIONS:")
print("=" * 50)

if not citybus_stops:
    print("1. 🚌 Collect Citybus stops data:")
    print("   Run: python3 collect_citybus_data.py")
    print("   This will collect all Citybus stops with coordinates")

if not route_mappings:
    print("2. 🚌 Collect route-stop mappings:")
    print("   Run: python3 run_step3_route_stop_mappings.py")
    print("   This will collect stop sequences for test routes")

if kmb_routes and kmb_stops and citybus_routes and route_mappings:
    print("3. 🔍 Run overlap analysis:")
    print("   Create script to identify overlapping stops between routes")
    print("   Compare KMB and Citybus routes for common stops")

print(f"\n" + "=" * 80)
print("🎉 DATA COMPLETENESS ANALYSIS COMPLETED!")
print("=" * 80)
