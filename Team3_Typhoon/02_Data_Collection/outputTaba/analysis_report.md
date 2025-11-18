```markdown
# Typhoon Taba (塔巴) Wind Speed Analysis Report

## Analysis Period
- **Signal No. 8 Effective Period**: 2025-09-07 21:20 to 2025-09-08 13:20
- **Duration**: 16.0 hours

## HKO Signal No. 8 Criteria
According to Hong Kong Observatory guidelines:
- **Wind Speed Range**: 63-117 km/h (sustained winds)
- **Issuance Criterion**: Signal is issued when **half or more** (4 or more out of 8) reference anemometers register or are expected to register sustained winds within the prescribed range and the wind condition is expected to persist.

## 8 Reference Stations
The following 8 reference anemometers are used by HKO for tropical cyclone warnings:

1. **Ta Kwu Ling** (打鼓嶺)
2. **Lau Fau Shan** (流浮山)
3. **Sha Tin** (沙田)
4. **Tsing Yi** (青衣)
5. **Kai Tak** (啓德)
6. **Cheung Chau** (長洲)
7. **Sai Kung** (西貢)
8. **Chek Lap Kok** (赤鱲角)

## Key Findings

### 1. Overall Wind Speed Statistics (10-min means)

Based on the generated timeseries (`taba_8stations_timeseries.csv`; 97 time points):

**Ta Kwu Ling**
- Mean Speed: 17.3 km/h
- Maximum Speed: 35.0 km/h
- Times ≥ 63 km/h: 0 out of 97 readings (0.0%)

**Lau Fau Shan**
- Mean Speed: 26.9 km/h
- Maximum Speed: 53.0 km/h
- Times ≥ 63 km/h: 0 out of 97 readings (0.0%)

**Sha Tin**
- Mean Speed: 15.9 km/h
- Maximum Speed: 32.0 km/h
- Times ≥ 63 km/h: 0 out of 97 readings (0.0%)

**Tsing Yi**
- Mean Speed: 25.2 km/h
- Maximum Speed: 51.0 km/h
- Times ≥ 63 km/h: 0 out of 97 readings (0.0%)

**Kai Tak**
- Mean Speed: 31.1 km/h
- Maximum Speed: 60.0 km/h
- Times ≥ 63 km/h: 0 out of 97 readings (0.0%)

**Cheung Chau**
- Mean Speed: 61.1 km/h
- Maximum Speed: 95.0 km/h
- Times ≥ 63 km/h: 42 out of 97 readings (43.3%)

**Sai Kung**
- Mean Speed: 35.0 km/h
- Maximum Speed: 69.0 km/h
- Times ≥ 63 km/h: 5 out of 97 readings (5.2%)

**Chek Lap Kok**
- Mean Speed: 38.7 km/h
- Maximum Speed: 64.0 km/h
- Times ≥ 63 km/h: 1 out of 97 readings (1.0%)


### 2. Signal No. 8 Criterion Compliance

- **Maximum number of stations simultaneously exceeding 63 km/h**: 2 out of 8 stations
- **Times when 4+ stations met criterion**: 0 out of 97 time points (0.0%)
- **Peak wind speed recorded across stations**: 95.0 km/h (Cheung Chau)

### 3. Threshold Exceedance Summary

**Stations that never exceeded 63 km/h threshold**: Ta Kwu Ling, Lau Fau Shan, Sha Tin, Tsing Yi, Kai Tak

**Stations that frequently exceeded 63 km/h**: Cheung Chau (43% of time points)

## Visualizations Generated

1. **taba_8stations_wind_timeseries.png** - Time series showing wind speeds at all 8 stations over the Signal 8 period
2. **taba_8stations_timeseries.csv** - Pivoted timeseries (datetime × stations)

## Interpretation

The analysis indicates that while Cheung Chau experienced sustained high winds during the Taba event, the HKO criterion of at least four reference stations measuring sustained winds ≥ 63 km/h was not met in this dataset. The maximum simultaneous exceedance was 2 stations, so based solely on these 8-station measurements the pattern does not meet the HKO threshold for Signal No. 8 issuance.

## Data Source
Wind data collected from Hong Kong Observatory CSV extracts for the Taba event.
Time window: 2025-09-07 21:20 to 2025-09-08 13:20

```
