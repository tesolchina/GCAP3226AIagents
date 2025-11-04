# Visualization Guide - Typhoon Weipa Wind Speed Analysis

## Quick Reference for Understanding the Charts

### 1. Time Series Plot (`wind_speed_time_series.png`)

**What it shows:**
- Wind speed changes over time for all 8 stations
- Each colored line represents one station
- Red dashed lines show Signal 8 thresholds (63 km/h and 117 km/h)
- Light red shading shows the Signal 8 wind speed range

**How to read it:**
- X-axis: Date and time during Signal 8 period
- Y-axis: Wind speed in km/h
- Lines crossing above red threshold = station meets Signal 8 criterion
- Higher/steeper lines = stronger/rapidly changing winds

**Key observations:**
- Cheung Chau (長洲) line consistently highest - most exposed to typhoon
- Ta Kwu Ling and Sha Tin lines lowest - sheltered inland locations
- Few stations consistently exceed 63 km/h threshold

---

### 2. Heatmap (`wind_speed_heatmap.png`)

**What it shows:**
- Color-coded wind speeds across all stations and time points
- Rows = different weather stations
- Columns = time progression
- Color intensity = wind speed magnitude

**How to read it:**
- Yellow/Orange = Moderate winds (30-50 km/h)
- Red/Dark Red = Strong winds (>60 km/h)
- Lighter colors = Weaker winds (<30 km/h)
- Vertical red bands = periods when winds increased across multiple stations
- Horizontal red bands = stations with consistently strong winds

**Key observations:**
- Cheung Chau row shows most red coloring = consistently strong winds
- Top rows (Ta Kwu Ling, Sha Tin) mostly yellow/light = weaker winds
- Pattern shows spatial variation across Hong Kong

---

### 3. Station Comparison Box Plot (`wind_speed_comparison.png`)

**What it shows:**
- Statistical distribution of wind speeds at each station
- Box = middle 50% of data (25th to 75th percentile)
- Line inside box = median wind speed
- Whiskers = range of typical values
- Dots beyond whiskers = outlier measurements

**How to read it:**
- Taller box = more variable wind speeds
- Higher box position = generally stronger winds
- Red dashed lines = Signal 8 thresholds for reference
- Green line in box = mean, Orange line = median

**Key observations:**
- Cheung Chau box highest and widest = strongest and most variable winds
- Ta Kwu Ling, Sha Tin, Tsing Yi boxes well below threshold
- Only Cheung Chau median approaches Signal 8 lower threshold

---

### 4. Threshold Analysis (`threshold_analysis.png`)

**What it shows:**
Two panels showing threshold compliance over time:

**Top Panel - Number of Stations Exceeding Thresholds**
- Orange line: Stations with winds ≥63 km/h
- Red line: Stations with winds ≥117 km/h
- Green dashed line: HKO criterion (4+ stations)

**Bottom Panel - Percentage Meeting Criterion**
- Blue bars: Percentage of 8 stations exceeding 63 km/h
- Green line: 50% threshold (HKO criterion)

**How to read it:**
- When orange line crosses green line = criterion met
- Taller blue bars = higher percentage of stations affected
- Time periods above green line = periods justifying Signal 8

**Key observations:**
- Orange line rarely reaches 4 stations
- Most time periods show 0-3 stations exceeding threshold
- Brief spike where 4 stations simultaneously exceeded 63 km/h
- Most blue bars below 50% line

---

### 5. Summary Statistics Table (`summary_statistics_table.png`)

**What it shows:**
Tabular summary of wind speed statistics for all 8 stations

**Columns explained:**
- **Station**: Weather station name
- **Mean Speed**: Average wind speed during Signal 8 period
- **Max Speed**: Highest recorded wind speed
- **Min Speed**: Lowest recorded wind speed
- **Std Dev**: Standard deviation (measure of variability)
- **Times ≥63 km/h**: Number of readings exceeding Signal 8 lower threshold
- **Times ≥117 km/h**: Number of readings exceeding Signal 8 upper threshold
- **Total Readings**: Total number of measurements analyzed

**Key observations:**
- Cheung Chau: Highest mean (60.1 km/h), highest max (117 km/h)
- Four stations (Ta Kwu Ling, Sha Tin, Tsing Yi, Kai Tak): Never exceeded 63 km/h
- Only Cheung Chau recorded winds at upper threshold (117 km/h)
- Coastal/island stations generally higher speeds than inland stations

---

## Analysis Context

### HKO Signal No. 8 Issuance Criteria

The Hong Kong Observatory issues Signal No. 8 when:
1. **Wind Speed**: Half or more (≥4 out of 8) reference stations record sustained winds of 63-117 km/h
2. **Persistence**: Wind conditions are expected to persist

### Geographic Considerations

**High-wind stations** (coastal/exposed):
- Cheung Chau - Southwestern islands, fully exposed
- Chek Lap Kok - Airport, western waters exposure
- Sai Kung - Eastern coastal location

**Low-wind stations** (inland/sheltered):
- Ta Kwu Ling - Northern New Territories, shielded by hills
- Sha Tin - Central New Territories valley, sheltered
- Tsing Yi - Western harbor, partially sheltered

### Key Question Addressed

**Was Signal No. 8 issuance justified by actual wind measurements?**

The analysis shows:
- ✓ Some stations (Cheung Chau) clearly experienced Signal 8 conditions
- ⚠ HKO criterion (4+ stations ≥63 km/h) met only briefly (~1% of time)
- → Suggests signal may have been issued based on:
  - Expected conditions rather than current measurements
  - Precautionary approach for public safety
  - Forecast models predicting stronger winds
  - Local severe conditions even if not widespread

### Interpretation Notes

1. **Spatial Heterogeneity**: Typhoon winds vary significantly across Hong Kong's varied terrain
2. **Temporal Variability**: Wind speeds fluctuate; brief periods may miss snapshot measurements
3. **Forecast vs. Observed**: Signals issued on forecasts may differ from subsequent observations
4. **Safety Margins**: Conservative approach prioritizes public safety

---

## Using These Visualizations

### For Reports
- Use time series for showing temporal evolution
- Use heatmap for visual impact and spatial patterns
- Use box plot for statistical comparison
- Use threshold analysis for criterion compliance
- Use statistics table for precise numbers

### For Presentations
- Time series: "How did winds change during the typhoon?"
- Heatmap: "Which areas were most affected?"
- Box plot: "How did stations compare overall?"
- Threshold analysis: "Did conditions justify Signal 8?"

### For Further Analysis
- Identify peak wind periods from time series
- Compare geographic patterns using heatmap
- Assess station vulnerability using box plot statistics
- Evaluate decision timing using threshold analysis

---

**Created**: November 4, 2025
**Purpose**: Help users understand and interpret typhoon wind analysis visualizations
