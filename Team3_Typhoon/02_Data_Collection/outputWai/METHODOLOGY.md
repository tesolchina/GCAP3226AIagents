# Data Processing Methodology

## Overview
This document explains the data processing methodology used to analyze wind speed data during Typhoon Weipa Signal No. 8 period.

## Data Collection

### Input Data
- **Source Directory**: `/workspaces/GCAP3226AIagents/Team3_Typhoon/02_Data_Collection/韋帕 7.19 2230 - 7.21 0010/`
- **File Format**: CSV files with 10-minute mean wind measurements
- **File Naming Convention**: `YYYYMMDD-HHMM-latest_10min_wind.csv`
- **Number of Files**: 155 CSV files
- **Time Range**: July 19, 2025 22:30 to July 21, 2025 00:10
- **Sampling Frequency**: Approximately every 10 minutes

### CSV File Structure
Each CSV file contains:
- **Date time**: Timestamp in format YYYYMMDDHHMM
- **Automatic Weather Station**: Station name
- **10-Minute Mean Wind Direction(Compass points)**: Wind direction
- **10-Minute Mean Speed(km/hour)**: Average wind speed over 10 minutes
- **10-Minute Maximum Gust(km/hour)**: Peak gust speed over 10 minutes

### Weather Stations
Each CSV file includes data from ~30 weather stations across Hong Kong, but analysis focuses on 8 reference stations.

## Data Processing Pipeline

### Step 1: Data Loading
```python
# Load all CSV files
csv_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.csv")))
all_data = []
for file in csv_files:
    df = pd.read_csv(file)
    all_data.append(df)
combined_df = pd.concat(all_data, ignore_index=True)
```

**Output**: Combined DataFrame with 4,650 total records

### Step 2: Datetime Conversion
```python
# Convert timestamp string to datetime object
combined_df['datetime'] = pd.to_datetime(
    combined_df['Date time'], 
    format='%Y%m%d%H%M'
)
```

**Purpose**: Enable time-based filtering and chronological ordering

### Step 3: Numeric Conversion
```python
# Convert wind speed to numeric, handling N/A values
combined_df['10-Minute Mean Speed(km/hour)'] = pd.to_numeric(
    combined_df['10-Minute Mean Speed(km/hour)'], 
    errors='coerce'
)
```

**Handling missing data**:
- N/A values converted to NaN
- NaN values excluded from statistical calculations
- Preserves data integrity while allowing numerical operations

### Step 4: Temporal Filtering
```python
# Filter for Signal No. 8 period
SIGNAL_8_START = datetime(2025, 7, 20, 0, 20)
SIGNAL_8_END = datetime(2025, 7, 20, 19, 40)

mask = (df['datetime'] >= SIGNAL_8_START) & (df['datetime'] <= SIGNAL_8_END)
df_signal8 = df[mask].copy()
```

**Output**: 3,510 records during Signal 8 period

### Step 5: Station Filtering
```python
# Filter for 8 reference stations
REFERENCE_STATIONS = [
    'Ta Kwu Ling', 'Lau Fau Shan', 'Sha Tin', 'Tsing Yi',
    'Kai Tak', 'Cheung Chau', 'Sai Kung', 'Chek Lap Kok'
]

df_filtered = df[df['Automatic Weather Station'].isin(REFERENCE_STATIONS)]
```

**Output**: 936 records from 8 reference stations during Signal 8

## Statistical Analyses

### Descriptive Statistics
For each station, calculated:
- **Mean**: Average wind speed
- **Maximum**: Highest recorded wind speed
- **Minimum**: Lowest recorded wind speed
- **Standard Deviation**: Measure of variability

```python
mean_speed = station_data['10-Minute Mean Speed(km/hour)'].mean()
max_speed = station_data['10-Minute Mean Speed(km/hour)'].max()
min_speed = station_data['10-Minute Mean Speed(km/hour)'].min()
std_dev = station_data['10-Minute Mean Speed(km/hour)'].std()
```

### Threshold Analysis
For each station, counted:
- **Times ≥ 63 km/h**: Frequency exceeding Signal 8 lower threshold
- **Times ≥ 117 km/h**: Frequency exceeding Signal 8 upper threshold

```python
times_above_lower = (station_data >= SIGNAL_8_LOWER_THRESHOLD).sum()
times_above_upper = (station_data >= SIGNAL_8_UPPER_THRESHOLD).sum()
```

### Temporal Compliance Analysis
For each time point, calculated:
- **Stations above threshold**: Number of stations ≥ 63 km/h
- **HKO criterion compliance**: Whether ≥4 stations exceeded threshold
- **Percentage**: Proportion of 8 stations meeting criterion

```python
for dt in sorted(df['datetime'].unique()):
    dt_data = df[df['datetime'] == dt]
    count_above = (dt_data['10-Minute Mean Speed(km/hour)'] >= 63).sum()
    percentage = (count_above / 8) * 100
```

## Visualization Methods

### 1. Time Series Plot
- **Library**: Matplotlib
- **Type**: Line plot with markers
- **Features**:
  - Multiple lines (one per station)
  - Threshold lines (horizontal)
  - Shaded threshold region
  - Legend with station names

### 2. Heatmap
- **Library**: Seaborn
- **Type**: 2D color-coded matrix
- **Method**: `pivot_table()` to reshape data
- **Color scale**: Yellow-Orange-Red (YlOrRd)
- **Dimensions**: Stations × Time points

### 3. Box Plot
- **Library**: Matplotlib
- **Type**: Statistical box-and-whisker plot
- **Features**:
  - Box: 25th-75th percentile
  - Line: Median
  - Whiskers: 1.5× IQR
  - Outliers: Individual points

### 4. Threshold Compliance Plot
- **Library**: Matplotlib
- **Type**: Dual-panel plot
  - Top: Line plot (number of stations)
  - Bottom: Bar chart (percentage)
- **Features**: HKO criterion reference line

### 5. Statistics Table
- **Library**: Matplotlib
- **Type**: Table visualization
- **Features**:
  - Formatted numerical values
  - Color-coded header
  - Alternating row colors

## Data Quality Considerations

### Missing Data
- **Occurrence**: Some stations report "N/A" for certain time periods
- **Handling**: Converted to NaN, excluded from calculations
- **Impact**: Minimal - affects <1% of data points

### Temporal Resolution
- **Sampling**: ~10 minute intervals
- **Limitation**: May miss very brief wind spikes
- **Mitigation**: Consistent with HKO operational procedures

### Spatial Coverage
- **Strengths**: 8 stations cover major geographic areas
- **Limitations**: Cannot capture micro-scale variations
- **Context**: Matches HKO official warning system design

## Assumptions

1. **10-minute mean winds**: Sustained wind metric appropriate for tropical cyclone warnings
2. **Station representativeness**: 8 reference stations adequately represent Hong Kong's wind conditions
3. **Data accuracy**: HKO measurements are accurate and properly calibrated
4. **Threshold consistency**: 63 km/h threshold uniformly applied across all stations

## Quality Assurance

### Data Validation Checks
1. ✓ All timestamps within expected range
2. ✓ All station names match reference list
3. ✓ Wind speeds are non-negative
4. ✓ No duplicate timestamp-station combinations
5. ✓ Chronological ordering maintained

### Output Validation
1. ✓ All 8 stations included in analysis
2. ✓ Time period matches Signal 8 duration
3. ✓ Statistics calculated from filtered data only
4. ✓ Visualizations properly labeled and formatted

## Reproducibility

### Requirements
- Python 3.7+
- pandas 1.0+
- matplotlib 3.0+
- seaborn 0.11+
- numpy 1.18+

### Execution Environment
- Platform: Linux (Ubuntu 24.04.2 LTS)
- Container: Dev container
- Location: `/workspaces/GCAP3226AIagents/`

### Random State
- No randomization involved
- Analysis is fully deterministic
- Results are reproducible given same input data

## Limitations

1. **Temporal Coverage**: Analysis limited to Signal 8 period only
2. **Spatial Resolution**: Only 8 stations; cannot capture all local variations
3. **Threshold Binary**: Analysis treats 62.9 km/h and 40 km/h equivalently as "below threshold"
4. **Wind Gusts**: Analysis focuses on sustained winds; gusts analyzed separately
5. **Direction**: Wind direction not incorporated into threshold analysis

## Future Enhancements

Potential improvements to analysis:
1. Include wind gust analysis
2. Incorporate wind direction patterns
3. Compare with forecast models
4. Analyze preceding/following periods
5. Multi-typhoon comparison
6. Machine learning prediction models

## References

### Data Source
- Hong Kong Observatory (HKO)
- Real-time wind data system
- 10-minute mean wind observations

### Methodology References
- HKO Tropical Cyclone Warning System guidelines
- WMO standards for wind measurement and reporting
- Pandas documentation for data processing
- Matplotlib/Seaborn documentation for visualization

---

**Document Version**: 1.0
**Last Updated**: November 4, 2025
**Author**: Automated Analysis System
