# Similar Cases Analysis - Bus Route Coordination

## Overview
This directory contains scripts and tools for analyzing similar cases of overlapping bus routes across Hong Kong. The analysis identifies routes with significant overlaps between different operators and analyzes their coordination patterns.

## Directory Structure
```
similar_cases_analysis/
├── scripts/                          # Python analysis scripts
│   ├── route_overlap_analyzer.py    # Main overlap detection script
│   ├── coordination_analyzer.py      # Coordination pattern analysis
│   ├── visualization_generator.py   # Data visualization tools
│   └── run_analysis.py              # Main execution script
├── data/                            # Data storage directory
│   ├── raw_routes/                  # Raw route data from APIs
│   ├── route_stops/                 # Route-stop mappings
│   ├── overlap_analysis/            # Overlap analysis results
│   └── coordination_data/          # Coordination analysis data
└── results/                         # Analysis results and outputs
    ├── high_overlap/                # High overlap route pairs (10+ stops)
    ├── medium_overlap/              # Medium overlap route pairs (5-9 stops)
    ├── low_overlap/                 # Low overlap route pairs (3-4 stops)
    ├── coordination_analysis/       # Coordination pattern analysis
    ├── visualizations/              # Generated charts and visualizations
    └── reports/                     # Final analysis reports
```

## Scripts Documentation

### 1. route_overlap_analyzer.py
**Purpose:** Find bus routes with overlapping stops across different operators

**Key Features:**
- Collects all routes from KMB and Citybus APIs
- Identifies routes with overlapping stops
- Categorizes overlaps by severity (high/medium/low)
- Analyzes operator combinations and geographic distribution

**Usage:**
```python
from route_overlap_analyzer import RouteOverlapAnalyzer

analyzer = RouteOverlapAnalyzer()
results = analyzer.run_complete_analysis(min_overlap=5)
```

**Output:**
- JSON files with overlap analysis results
- Categorized route pairs by overlap severity
- Coordination pattern analysis

### 2. coordination_analyzer.py
**Purpose:** Analyze coordination patterns between overlapping routes

**Key Features:**
- Collects real-time ETA data for route pairs
- Analyzes headway patterns and consistency
- Calculates coordination effectiveness scores
- Compares coordination approaches across route pairs

**Usage:**
```python
from coordination_analyzer import CoordinationAnalyzer

analyzer = CoordinationAnalyzer()
result = analyzer.analyze_route_pair_coordination(route1_info, route2_info)
```

**Output:**
- Coordination effectiveness scores
- Headway analysis results
- Comparative coordination analysis

### 3. visualization_generator.py
**Purpose:** Generate visualizations for analysis results

**Key Features:**
- Overlap distribution charts
- Operator combination analysis
- Top overlapping routes visualization
- Interactive maps and dashboards
- Coordination effectiveness charts

**Usage:**
```python
from visualization_generator import VisualizationGenerator

generator = VisualizationGenerator()
visualizations = generator.generate_all_visualizations(overlap_data_path)
```

**Output:**
- PNG charts and graphs
- Interactive HTML visualizations
- Comprehensive dashboards

### 4. run_analysis.py
**Purpose:** Main script to run complete analysis pipeline

**Key Features:**
- Orchestrates all analysis components
- Generates comprehensive reports
- Provides progress tracking and logging
- Creates final summary reports

**Usage:**
```bash
python run_analysis.py
```

## Data Sources

### Hong Kong Government Open Data APIs
- **KMB/LWB API:** https://data.etabus.gov.hk/v1/transport/kmb
- **Citybus API:** https://data.etabus.gov.hk/v1/transport/citybus

### Data Collection Strategy
1. **Route Information:** Collect all routes from both operators
2. **Stop Data:** Map routes to their stops and sequences
3. **Real-time Data:** Collect ETA data for coordination analysis
4. **Overlap Detection:** Identify routes with common stops

## Analysis Methodology

### 1. Route Overlap Identification
- **Minimum Overlap:** 5+ overlapping stops between different operators
- **Operator Combinations:** KMB vs Citybus route pairs
- **Geographic Coverage:** Routes serving similar areas or corridors

### 2. Overlap Categorization
- **High Overlap (10+ stops):** Routes with extensive overlaps
- **Medium Overlap (5-9 stops):** Routes with moderate overlaps  
- **Low Overlap (3-4 stops):** Routes with limited overlaps

### 3. Coordination Analysis
- **Headway Analysis:** Service frequency and consistency
- **Effectiveness Scoring:** Coordination quality assessment
- **Pattern Recognition:** Successful coordination strategies

## Expected Outcomes

### 1. Similar Cases Identification
- **High-Overlap Routes:** 10-15 routes with significant overlaps
- **Coordination Patterns:** Different approaches to route coordination
- **Best Practices:** Successful coordination examples
- **Improvement Opportunities:** Areas for better coordination

### 2. Analysis Results
- **Coordination Effectiveness:** Assessment of current coordination approaches
- **Passenger Impact:** Impact of coordination decisions on passengers
- **Operational Impact:** Impact of coordination decisions on operators
- **Policy Implications:** Recommendations for improved coordination

## Usage Instructions

### 1. Setup
```bash
# Install required packages
pip install requests pandas matplotlib seaborn plotly numpy

# Navigate to scripts directory
cd scripts/
```

### 2. Run Complete Analysis
```bash
# Run full analysis pipeline
python run_analysis.py
```

### 3. Run Individual Components
```bash
# Run only overlap analysis
python route_overlap_analyzer.py

# Run only coordination analysis
python coordination_analyzer.py

# Generate visualizations
python visualization_generator.py
```

## Configuration Options

### Route Overlap Analyzer
- `min_overlap`: Minimum overlapping stops to consider (default: 5)
- `data_dir`: Directory for data storage
- `results_dir`: Directory for results storage

### Coordination Analyzer
- `duration_hours`: Hours to collect coordination data (default: 1)
- `analysis_interval`: Minutes between data collection (default: 2)

### Visualization Generator
- `chart_format`: Output format (PNG, HTML, etc.)
- `interactive`: Generate interactive visualizations
- `dashboard`: Create comprehensive dashboards

## Output Files

### Data Files
- `all_routes_YYYYMMDD_HHMMSS.json`: Complete route database
- `all_route_stops_YYYYMMDD_HHMMSS.json`: Route-stop mappings
- `route_overlaps_YYYYMMDD_HHMMSS.json`: Overlap analysis results

### Results Files
- `high_overlap_routes_YYYYMMDD_HHMMSS.json`: High overlap route pairs
- `medium_overlap_routes_YYYYMMDD_HHMMSS.json`: Medium overlap route pairs
- `low_overlap_routes_YYYYMMDD_HHMMSS.json`: Low overlap route pairs
- `coordination_patterns_YYYYMMDD_HHMMSS.json`: Coordination analysis

### Visualization Files
- `overlap_distribution_YYYYMMDD_HHMMSS.png`: Overlap distribution chart
- `operator_combinations_YYYYMMDD_HHMMSS.png`: Operator combination chart
- `top_overlapping_routes_YYYYMMDD_HHMMSS.png`: Top overlapping routes
- `interactive_overlap_map_YYYYMMDD_HHMMSS.html`: Interactive map
- `comprehensive_dashboard_YYYYMMDD_HHMMSS.png`: Complete dashboard

### Report Files
- `final_report_YYYYMMDD_HHMMSS.json`: Comprehensive analysis report
- `complete_analysis_YYYYMMDD_HHMMSS.json`: Complete analysis results
- `visualization_summary_YYYYMMDD_HHMMSS.json`: Visualization summary

## Troubleshooting

### Common Issues
1. **API Rate Limiting:** Scripts include rate limiting, but may need adjustment
2. **Data Quality:** Some routes may have incomplete stop data
3. **Network Issues:** API calls may fail due to network connectivity
4. **Memory Usage:** Large datasets may require significant memory

### Solutions
1. **Rate Limiting:** Increase sleep intervals between API calls
2. **Data Validation:** Implement data quality checks
3. **Error Handling:** Scripts include comprehensive error handling
4. **Memory Management:** Process data in smaller batches

## Dependencies

### Required Packages
- `requests`: API data collection
- `pandas`: Data manipulation and analysis
- `matplotlib`: Static visualizations
- `seaborn`: Enhanced visualizations
- `plotly`: Interactive visualizations
- `numpy`: Numerical computations
- `json`: Data serialization
- `datetime`: Time handling
- `logging`: Progress tracking

### Installation
```bash
pip install requests pandas matplotlib seaborn plotly numpy
```

## Support and Maintenance

### Logging
All scripts include comprehensive logging for debugging and monitoring:
- Progress tracking
- Error reporting
- Performance metrics
- Data quality indicators

### Data Backup
- All data files are timestamped
- Results are saved in multiple formats
- Backup copies are created for important analyses

### Updates
- Scripts are designed for modular updates
- API changes can be handled through configuration
- New analysis methods can be added easily

---

*This documentation provides comprehensive guidance for using the similar cases analysis tools for bus route coordination research.*
