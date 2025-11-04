# HKO Typhoon Signal 8 Web Crawler

A specialized web crawler for collecting typhoon signal data from hko.gov.hk, with particular focus on Signal 8 announcements and weather data during typhoon events.

## Features

- **Signal 8 Detection**: Automatically detects and extracts Signal 8 announcements
- **Weather Data Collection**: Collects wind speed, pressure, and other meteorological data
- **Tropical Cyclone Tracking**: Monitors tropical cyclone position and intensity data
- **Comprehensive Logging**: Detailed logging of all crawling activities
- **Data Export**: Exports data in both CSV and JSON formats
- **Report Generation**: Generates comprehensive crawling reports

## Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation**:
   ```bash
   python hko_typhoon_crawler.py
   ```

## Usage

### Basic Usage

```bash
cd /Users/simonwang/Documents/Usage/GCAP3226/Team3_Typhoon/02_Data_Collection/webCrawler
python hko_typhoon_crawler.py
```

### Output Structure

The crawler creates the following directory structure:

```
webCrawler/
├── data/                    # Collected data files
│   ├── signal_8_announcements.csv
│   ├── signal_8_announcements.json
│   ├── weather_data.csv
│   ├── weather_data.json
│   └── crawl_log.json
├── output/                  # Generated reports
│   └── crawling_report_YYYYMMDD_HHMMSS.md
├── logs/                    # Crawling logs
│   └── hko_crawler_YYYYMMDD_HHMMSS.log
├── hko_typhoon_crawler.py   # Main crawler script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Data Collection

### Signal 8 Announcements

The crawler specifically looks for:
- "Signal No. 8" or "TC8" references
- "Tropical Cyclone Warning Signal No. 8"
- "Gale or Storm" mentions
- Context around Signal 8 announcements

### Weather Data

Collects:
- Wind speed measurements (km/h and knots)
- Wind gust data
- Atmospheric pressure readings
- Tropical cyclone position and intensity

### Tropical Cyclone Tracking

Monitors:
- Tropical cyclone names and positions
- Intensity measurements
- Movement patterns
- Forecast data

## Logging

All crawling activities are logged with:
- **Timestamp**: When each activity occurred
- **Activity Type**: What was being done
- **Details**: Specific information about the activity
- **Results**: What was found or collected

## Output Files

### CSV Files
- **signal_8_announcements.csv**: Signal 8 announcements with context
- **weather_data.csv**: Weather measurements and meteorological data

### JSON Files
- **signal_8_announcements.json**: Structured Signal 8 data
- **weather_data.json**: Structured weather data
- **crawl_log.json**: Complete crawling activity log

### Reports
- **crawling_report_YYYYMMDD_HHMMSS.md**: Comprehensive crawling report

## Configuration

The crawler can be configured by modifying the `HKOTyphoonCrawler` class:

- **Base Directory**: Change `base_dir` parameter
- **URLs**: Modify HKO URLs in the `__init__` method
- **Patterns**: Update regex patterns for data extraction
- **Timeouts**: Adjust request timeouts

## Error Handling

The crawler includes comprehensive error handling:
- **Network Errors**: Retry logic for failed requests
- **Parsing Errors**: Graceful handling of parsing failures
- **File I/O Errors**: Safe data saving with error recovery
- **Logging**: All errors are logged for debugging

## Course Context

This crawler is part of GCAP3226: Empowering Citizens Through Data - Participatory Policy Analysis for Hong Kong at Hong Kong Baptist University.

**Course**: GCAP3226 - Empowering Citizens Through Data  
**Instructor**: Dr. Simon Wang  
**Institution**: Hong Kong Baptist University  
**Project**: Typhoon Signal 8 Analysis

## Research Applications

The collected data can be used for:
- **Mathematical Modeling**: Regression analysis of signal timing
- **Statistical Analysis**: Cross-incident comparative analysis
- **Policy Research**: Evidence-based recommendations
- **Emergency Management**: Optimization of response coordination

## Troubleshooting

### Common Issues

1. **Network Timeout**: Increase timeout values in the crawler
2. **Parsing Errors**: Check if HKO website structure has changed
3. **Permission Errors**: Ensure write permissions for output directories
4. **Missing Dependencies**: Run `pip install -r requirements.txt`

### Debug Mode

Enable detailed logging by modifying the logging level in the `setup_logging` method.

## License

This project is part of academic research at Hong Kong Baptist University.

## Contact

For questions about this crawler:
- **Course**: GCAP3226 - Empowering Citizens Through Data
- **Instructor**: Dr. Simon Wang
- **Institution**: Hong Kong Baptist University
