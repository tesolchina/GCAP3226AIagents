# Typhoon Weipa Wind Speed Analysis

## Overview
This directory contains a comprehensive analysis of wind speed data from 8 Hong Kong Observatory (HKO) reference stations during Typhoon Weipa (韋帕) Signal No. 8 period on July 20, 2025.

## Analysis Parameters

### Time Period
- **Signal No. 8 Start**: 2025-07-20 00:20
- **Signal No. 8 End**: 2025-07-20 19:40
- **Duration**: 19.3 hours

### HKO Signal No. 8 Criteria
- **Wind Speed Range**: 63-117 km/h (sustained winds)
- **Issuance Criterion**: Signal is issued when **half or more** (≥4 out of 8) reference anemometers register sustained winds within the prescribed range, and the wind condition is expected to persist

### 8 Reference Stations Analyzed
1. **Ta Kwu Ling** (打鼓嶺) - Northern New Territories
2. **Lau Fau Shan** (流浮山) - Northwestern New Territories
3. **Sha Tin** (沙田) - Central New Territories
4. **Tsing Yi** (青衣) - Western Harbor
5. **Kai Tak** (啓德) - Eastern Harbor
6. **Cheung Chau** (長洲) - Southwestern Islands
7. **Sai Kung** (西質) - Eastern New Territories
8. **Chek Lap Kok** (赤鱲角) - Airport / Western Waters

## Files in This Directory

### Python Script
- **`analyze_typhoon_wind.py`** - Main analysis script that:
  - Loads wind data from 155 CSV files spanning the typhoon period
  - Filters data for Signal No. 8 effective period
  - Extracts data for 8 reference stations
  - Generates visualizations and statistics
  - Creates comprehensive report

### Visualizations

1. **`wind_speed_time_series.png`**
   - Line chart showing wind speed evolution at all 8 stations
   - Includes Signal No. 8 threshold lines (63 km/h and 117 km/h)
   - Shows shaded region for Signal 8 range
   - Helps identify wind speed patterns and peak periods

2. **`wind_speed_heatmap.png`**
   - Heatmap visualization of wind speeds across stations and time
   - Color intensity indicates wind speed magnitude
   - Allows quick identification of high-wind periods and affected areas

3. **`wind_speed_comparison.png`**
   - Box plot comparing wind speed distributions across all 8 stations
   - Shows median, quartiles, and outliers for each station
   - Includes threshold reference lines
   - Reveals which stations experienced strongest/weakest winds

4. **`threshold_analysis.png`**
   - Two-panel visualization showing:
     - Number of stations exceeding thresholds over time
     - Percentage of stations meeting Signal 8 criterion
   - Critical for assessing whether HKO criterion was met

5. **`summary_statistics_table.png`**
   - Formatted table with key statistics for all stations
   - Professional presentation suitable for reports

### Data Files

- **`summary_statistics.csv`** - Detailed statistics in CSV format including:
  - Mean, max, min wind speeds
  - Standard deviation
  - Frequency of threshold exceedances
  - Total number of readings

- **`analysis_report.md`** - Comprehensive markdown report with:
  - Key findings and statistics
  - Interpretation of results
  - Compliance with HKO criteria

## Key Findings

### Wind Speed Distribution
- **Highest mean wind speed**: Cheung Chau (60.1 km/h)
- **Lowest mean wind speed**: Sha Tin (17.6 km/h)
- **Peak wind speed**: 117.0 km/h at Cheung Chau

### Threshold Exceedances
- **Stations exceeding 63 km/h threshold**:
  - Cheung Chau: 35/117 readings (29.9%)
  - Chek Lap Kok: 17/117 readings (14.5%)
  - Sai Kung: 12/117 readings (10.3%)
  - Lau Fau Shan: 7/117 readings (6.0%)

- **Stations never exceeding 63 km/h**: Ta Kwu Ling, Sha Tin, Tsing Yi, Kai Tak

### HKO Criterion Compliance
- **Maximum stations simultaneously ≥63 km/h**: 4 out of 8 (50%)
- **Times criterion met (≥4 stations)**: 1 out of 117 time points (0.9%)

## Interpretation

The analysis reveals interesting patterns about Typhoon Weipa's impact:

1. **Spatial Variation**: Wind speeds varied significantly across Hong Kong, with southern/western stations (Cheung Chau, Chek Lap Kok) experiencing much stronger winds than northern/inland stations (Ta Kwu Ling, Sha Tin)

2. **Threshold Compliance**: The HKO criterion of 4+ stations exceeding 63 km/h was met very briefly (only ~1% of the time), suggesting either:
   - The signal was issued based on expected conditions rather than current measurements
   - The typhoon's strongest winds affected fewer than half the reference stations
   - The signal may have been precautionary

3. **Peak Conditions**: Cheung Chau recorded winds at the upper limit of Signal 8 (117 km/h), indicating severe local conditions despite lower readings at other stations

4. **Geographic Patterns**: Coastal and island stations experienced stronger winds, while inland and sheltered locations had significantly lower wind speeds

## How to Run

### Requirements
```bash
pip install pandas matplotlib seaborn numpy
```

### Execution
```bash
cd /workspaces/GCAP3226AIagents/Team3_Typhoon/02_Data_Collection/outputWai
python analyze_typhoon_wind.py
```

The script will:
1. Load all wind data from the input directory
2. Filter for Signal No. 8 period and reference stations
3. Generate all visualizations and statistics
4. Save outputs to this directory

## Data Source
- **Source**: Hong Kong Observatory (HKO)
- **Data Type**: 10-minute mean wind speed measurements
- **Input Directory**: `韋帕 7.19 2230 - 7.21 0010/`
- **Number of CSV Files**: 155 files
- **Total Records Analyzed**: 936 records from 8 reference stations during Signal No. 8

## References
- [HKO Tropical Cyclone Warning System](https://www.hko.gov.hk/en/wservice/tsheet/pms/tcws.htm)
- HKO Reference Anemometer Network guidelines

---

**Analysis Date**: November 4, 2025
**Generated by**: Typhoon Weipa Wind Speed Analysis Script
