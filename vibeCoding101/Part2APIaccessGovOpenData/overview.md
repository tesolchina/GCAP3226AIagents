# Part 2: API Access to Government Open Data

## Project Overview

This folder demonstrates how to work with AI agents to access Hong Kong government open data through APIs. The AI agent was given a URL and instructions to analyze it, extract API information, and create a complete working example.

## What Was Created

Based on the instructions to analyze https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data, the AI agent generated:

### Documentation Files
- **README.md** - Comprehensive API documentation with examples
- **QUICKSTART.md** - Quick start guide for immediate use
- **overview.md** - This file explaining the project

### Code Files
- **mtr_api_test.py** - Full-featured test script with multiple station queries
- **simple_example.py** - Simple, beginner-friendly example code
- **requirements.txt** - Python dependencies

### Output Files (Generated when scripts run)
- **mtr_api_output.json** - Full JSON data from API calls
- **mtr_api_report.txt** - Human-readable summary report
- **Next_Train_API_Spec.pdf** - Official API specification (downloaded)

### Notebook Update
- Added comprehensive section to **vibe_coding_tutorial.ipynb** explaining the project

## How This Was Built

1. **AI agent received**: URL to the MTR dataset page
2. **AI agent analyzed**: 
   - Fetched the webpage content
   - Identified API endpoint links
   - Found documentation PDF links
   - Tested the API to understand response format
3. **AI agent created**:
   - Complete README with API documentation
   - Working Python test scripts
   - Quick start guide
   - Updated the tutorial notebook
4. **AI agent validated**:
   - Ran test scripts to ensure they work
   - Generated sample output files
   - Created summary reports

## Key Learnings

This project demonstrates:
- ✅ How AI agents can explore web pages and extract information
- ✅ How to document APIs comprehensively
- ✅ Creating both simple and advanced code examples
- ✅ Generating proper project structure with documentation
- ✅ Testing and validating API access programmatically

## Using This Project

### Quick Test
```bash
python3 simple_example.py
```

### Full Test Suite
```bash
python3 mtr_api_test.py
```

### Read Documentation
- Start with QUICKSTART.md for immediate usage
- Read README.md for comprehensive information
- Check the notebook section for educational context

## Data Available Through This API

- **Real-time train arrivals** for all MTR stations
- **Platform information**
- **Service delay indicators**
- **Train destinations**
- **Estimated arrival times**

## Extension Ideas

You could extend this to:
- Build a web dashboard showing live train times
- Analyze peak hour service patterns
- Create mobile notifications for train arrivals
- Compare service frequency across different lines
- Visualize train movement patterns

## About DATA.GOV.HK

Hong Kong's open data portal provides hundreds of datasets including:
- Transportation data
- Weather and air quality
- Public facility locations
- Government statistics
- And much more!

Explore: https://data.gov.hk/en-datasets

---

*This project was created for GCAP3226 - Empowering Citizens through Data: Participatory Policy Analysis for Hong Kong*