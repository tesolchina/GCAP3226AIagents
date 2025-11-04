# Typhoon Weipa (韋帕) Wind Speed Analysis Report

## Analysis Period
- **Signal No. 8 Effective Period**: 2025-07-20 00:20 to 2025-07-20 19:40
- **Duration**: 19.3 hours

## HKO Signal No. 8 Criteria
According to Hong Kong Observatory guidelines:
- **Wind Speed Range**: 63-117 km/h (sustained winds)
- **Issuance Criterion**: Signal is issued when **half or more** (4 or more out of 8) reference anemometers register or are expected to register sustained winds within the prescribed range and the wind condition is expected to persist.

## 8 Reference Stations
The following 8 near-sea level reference anemometers are used by HKO for tropical cyclone warnings:

1. **Ta Kwu Ling** (打鼓嶺)
2. **Lau Fau Shan** (流浮山)
3. **Sha Tin** (沙田)
4. **Tsing Yi** (青衣)
5. **Kai Tak** (啓德)
6. **Cheung Chau** (長洲)
7. **Sai Kung** (西質)
8. **Chek Lap Kok** (赤鱲角)

## Key Findings

### 1. Overall Wind Speed Statistics

**Ta Kwu Ling**
- Mean Speed: 21.2 km/h
- Maximum Speed: 47.0 km/h
- Times exceeding 63 km/h threshold: 0 out of 117 readings (0.0%)

**Lau Fau Shan**
- Mean Speed: 35.5 km/h
- Maximum Speed: 72.0 km/h
- Times exceeding 63 km/h threshold: 7 out of 117 readings (6.0%)

**Sha Tin**
- Mean Speed: 17.6 km/h
- Maximum Speed: 40.0 km/h
- Times exceeding 63 km/h threshold: 0 out of 117 readings (0.0%)

**Tsing Yi**
- Mean Speed: 23.8 km/h
- Maximum Speed: 42.0 km/h
- Times exceeding 63 km/h threshold: 0 out of 117 readings (0.0%)

**Kai Tak**
- Mean Speed: 30.0 km/h
- Maximum Speed: 55.0 km/h
- Times exceeding 63 km/h threshold: 0 out of 117 readings (0.0%)

**Cheung Chau**
- Mean Speed: 60.1 km/h
- Maximum Speed: 117.0 km/h
- Times exceeding 63 km/h threshold: 35 out of 117 readings (29.9%)

**Sai Kung**
- Mean Speed: 37.9 km/h
- Maximum Speed: 89.0 km/h
- Times exceeding 63 km/h threshold: 12 out of 117 readings (10.3%)

**Chek Lap Kok**
- Mean Speed: 43.6 km/h
- Maximum Speed: 85.0 km/h
- Times exceeding 63 km/h threshold: 17 out of 117 readings (14.5%)


### 2. Signal No. 8 Criterion Compliance

- **Maximum number of stations simultaneously exceeding 63 km/h**: 4 out of 8 stations
- **Times when 4+ stations met criterion**: 1 out of 117 time points (0.9%)
- **Peak wind speed recorded**: 117.0 km/h

### 3. Threshold Exceedance Summary

**Stations that never exceeded 63 km/h threshold**: Ta Kwu Ling, Sha Tin, Tsing Yi, Kai Tak


## Visualizations Generated

1. **wind_speed_time_series.png** - Time series showing wind speeds at all 8 stations over the Signal 8 period
2. **wind_speed_heatmap.png** - Heatmap visualization of wind speeds across stations and time
3. **wind_speed_comparison.png** - Box plot comparing wind speed distributions across stations
4. **threshold_analysis.png** - Analysis of how many stations exceeded thresholds over time
5. **summary_statistics_table.png** - Summary statistics table for all stations
6. **summary_statistics.csv** - Detailed statistics in CSV format

## Interpretation

This analysis provides insight into whether the issuance of Signal No. 8 was justified based on actual wind measurements at the 8 reference stations. The visualizations show:

- How wind speeds evolved over the typhoon period
- Which stations experienced the strongest winds
- Whether the HKO criterion (4+ stations with sustained winds ≥ 63 km/h) was met
- Spatial variation in wind speeds across Hong Kong

## Data Source
Wind data collected from Hong Kong Observatory during Typhoon Weipa
Period: July 19-21, 2025
