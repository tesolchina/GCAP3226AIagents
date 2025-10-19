# Team 2: API Data Collection Plan - Bus Route Coordination

## Project Overview
**Team:** Bus Route Coordination Optimization
**Focus Routes:** KMB 272A and Citybus 582 (8 overlapping stops)
**Data Sources:** Hong Kong Government Open Data Portal (data.gov.hk)
**Current Status:** Week 5 - Data Collection Planning

## Available Data Sources

### 1. Citybus Real-time Data
**Source:** [Citybus ETA Transport Real-time Data](https://data.gov.hk/en-data/dataset/ctb-eta-transport-realtime-eta)
**Provider:** Citybus Limited
**Update Frequency:** ETA data updated every 1 minute
**Data Format:** JSON
**API Version:** V2 (recommended for future access)

**Available Data Resources:**
- Company data
- Route data
- Bus Stop data
- Bus Stop List of specific Route data
- Estimated Time of Arrival (ETA) data

### 2. KMB/LWB Real-time Data
**Source:** [KMB/LWB Real-time Arrival Data](https://data.gov.hk/en-data/dataset/hk-td-tis_21-etakmb)
**Provider:** Transport Department (disseminates KMB/LWB data)
**Update Frequency:** ETA data updated every 1 minute, other data updated daily
**Data Format:** JSON

**Available Data Resources:**
- Route List Data
- Route Data
- Stop List Data
- Stop Data
- Route-Stop List Data
- Route-Stop Data
- ETA Data
- Stop ETA Data
- Route ETA Data

## Data Collection Strategy

### Phase 1: Route-Specific Data Collection (Weeks 5-7)

#### Target Routes
- **KMB Route 272A:** [Route details to be collected]
- **Citybus Route 582:** [Route details to be collected]
- **Overlapping Stops:** 8 identified stops with overlapping service

#### Data Collection Tasks

##### 1. Route Information Collection
- [ ] **KMB 272A Route Data:**
  - Route details and stops
  - Timetable information
  - Service frequency and headways
  - Route performance metrics

- [ ] **Citybus 582 Route Data:**
  - Route details and stops
  - Timetable information
  - Service frequency and headways
  - Route performance metrics

##### 2. Real-time ETA Data Collection
- [ ] **KMB 272A Real-time Data:**
  - ETA data for all stops
  - Service reliability metrics
  - Headway consistency analysis
  - Passenger load factors

- [ ] **Citybus 582 Real-time Data:**
  - ETA data for all stops
  - Service reliability metrics
  - Headway consistency analysis
  - Passenger load factors

##### 3. Overlapping Stops Analysis
- [ ] **Identified Overlapping Stops (8 stops):**
  - Stop-specific ETA data
  - Coordination analysis
  - Passenger waiting time analysis
  - Service frequency comparison

### Phase 2: City-wide Similar Cases Analysis (Weeks 6-8)

#### Similar Route Identification
- [ ] **Route Overlap Analysis:**
  - Identify other routes with significant overlaps
  - Analyze coordination patterns across the city
  - Compare different operator coordination approaches

#### Data Collection for Similar Cases
- [ ] **High-Overlap Routes:**
  - Routes with 5+ overlapping stops
  - Different operator combinations
  - Various coordination strategies

- [ ] **Coordination Patterns:**
  - Successful coordination examples
  - Failed coordination attempts
  - Different approaches to overlap management

### Phase 3: Data Analysis and Modeling (Weeks 8-10)

#### Data Processing Tasks
- [ ] **Data Cleaning and Validation:**
  - ETA data accuracy verification
  - Route data consistency checks
  - Stop data validation

- [ ] **Performance Metrics Calculation:**
  - Average waiting times
  - Service reliability metrics
  - Headway consistency analysis
  - Passenger load factor analysis

#### Mathematical Modeling
- [ ] **Coordination Analysis:**
  - Current coordination effectiveness
  - Potential coordination improvements
  - Impact assessment of coordination decisions

- [ ] **Optimization Modeling:**
  - Optimal headway coordination
  - Passenger waiting time optimization
  - Service efficiency improvements

## Technical Implementation

### API Access and Data Collection

#### 1. Citybus API Implementation
```python
# Example API endpoints for Citybus data
base_url = "https://data.etabus.gov.hk/v1/transport/citybus"
endpoints = {
    "company": "/company",
    "routes": "/route",
    "stops": "/stop",
    "route_stops": "/route-stop",
    "eta": "/eta"
}
```

#### 2. KMB/LWB API Implementation
```python
# Example API endpoints for KMB/LWB data
base_url = "https://data.etabus.gov.hk/v1/transport/kmb"
endpoints = {
    "route_list": "/route",
    "route_data": "/route/{route_id}",
    "stop_list": "/stop",
    "stop_data": "/stop/{stop_id}",
    "route_stop": "/route-stop",
    "eta": "/eta",
    "stop_eta": "/stop-eta",
    "route_eta": "/route-eta"
}
```

### Data Collection Schedule

#### Daily Data Collection (Weeks 5-10)
- [ ] **Morning Peak (7:00-9:00 AM):**
  - ETA data collection every 5 minutes
  - Passenger load analysis
  - Headway consistency monitoring

- [ ] **Evening Peak (5:00-7:00 PM):**
  - ETA data collection every 5 minutes
  - Passenger load analysis
  - Headway consistency monitoring

- [ ] **Off-Peak Hours (10:00 AM-4:00 PM):**
  - ETA data collection every 15 minutes
  - Service reliability analysis
  - Coordination effectiveness assessment

#### Weekly Data Analysis
- [ ] **Route Performance Analysis:**
  - Weekly service reliability reports
  - Headway consistency analysis
  - Passenger load factor trends

- [ ] **Coordination Assessment:**
  - Weekly coordination effectiveness
  - Passenger waiting time analysis
  - Service efficiency metrics

## Data Storage and Management

### Data Organization
```
Team2_BusRouteCoordination/
├── data/
│   ├── raw_data/
│   │   ├── kmb_272a/
│   │   │   ├── route_data/
│   │   │   ├── stop_data/
│   │   │   ├── eta_data/
│   │   │   └── performance_data/
│   │   ├── citybus_582/
│   │   │   ├── route_data/
│   │   │   ├── stop_data/
│   │   │   ├── eta_data/
│   │   │   └── performance_data/
│   │   └── overlapping_stops/
│   │       ├── coordination_analysis/
│   │       └── passenger_flow/
│   ├── processed_data/
│   │   ├── performance_metrics/
│   │   ├── coordination_analysis/
│   │   └── optimization_models/
│   └── analysis_results/
│       ├── coordination_effectiveness/
│       ├── passenger_impact/
│       └── policy_recommendations/
```

### Data Quality Assurance
- [ ] **Data Validation:**
  - ETA data accuracy verification
  - Route data consistency checks
  - Stop data validation
  - Performance metrics verification

- [ ] **Data Cleaning:**
  - Missing data handling
  - Outlier detection and treatment
  - Data consistency checks
  - Performance metrics validation

## Expected Outcomes

### Data Collection Results
- [ ] **Route Performance Data:**
  - Comprehensive performance metrics for KMB 272A and Citybus 582
  - Real-time ETA data for analysis
  - Service reliability and consistency metrics

- [ ] **Coordination Analysis:**
  - Current coordination effectiveness
  - Passenger waiting time analysis
  - Service efficiency assessment

- [ ] **City-wide Similar Cases:**
  - Identification of similar route overlaps
  - Analysis of different coordination approaches
  - Best practice identification

### Research Impact
- **Data-Driven Analysis:** Evidence-based assessment of current coordination decisions
- **Policy Recommendations:** Data-supported recommendations for improved coordination
- **Framework Development:** Methodology for analyzing route coordination effectiveness

## Timeline and Milestones

### Week 5-6: Initial Data Collection
- [ ] API access setup and testing
- [ ] Initial route data collection
- [ ] Data validation and quality checks
- [ ] Baseline performance metrics establishment

### Week 7-8: Comprehensive Data Collection
- [ ] Full route data collection
- [ ] Overlapping stops analysis
- [ ] City-wide similar cases identification
- [ ] Data processing and analysis

### Week 9-10: Analysis and Modeling
- [ ] Performance metrics analysis
- [ ] Coordination effectiveness assessment
- [ ] Mathematical modeling implementation
- [ ] Policy recommendations development

## Resources and Support

### Technical Resources
- **API Documentation:** [Citybus API](https://data.gov.hk/en-data/dataset/ctb-eta-transport-realtime-eta), [KMB/LWB API](https://data.gov.hk/en-data/dataset/hk-td-tis_21-etakmb)
- **Data Dictionaries:** Available for both APIs
- **Developer Support:** API specifications and guides

### Team Support
- **Technical Lead:** API implementation and data collection
- **Data Analyst:** Data processing and analysis
- **Mathematical Modeler:** Performance analysis and optimization
- **Project Manager:** Timeline coordination and quality assurance

---

*This data collection plan provides a comprehensive framework for collecting and analyzing real-time bus data to support the bus route coordination research project.*
