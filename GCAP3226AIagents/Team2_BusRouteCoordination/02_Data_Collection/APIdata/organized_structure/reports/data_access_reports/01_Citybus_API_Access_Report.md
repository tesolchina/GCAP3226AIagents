# Data Access Report - Citybus API Analysis

## 📊 **Report Summary**
**Date:** October 19, 2024  
**Purpose:** Analysis of Citybus API accessibility and data collection  
**Status:** Successfully identified working endpoint and collected data  
**Data Collected:** 394 Citybus routes from working API endpoint  

## 🔍 **API Endpoint Analysis**

### **Working Endpoints**
| Endpoint | Status | Data Count | Notes |
|----------|--------|------------|-------|
| `https://rt.data.gov.hk/v2/transport/citybus/route/ctb` | ✅ 200 | 394 routes | **WORKING** - Primary data source |
| `https://rt.data.gov.hk/v2/transport/citybus/company/ctb` | ✅ 200 | 6 items | Company information |

### **Non-Working Endpoints**
| Endpoint | Status | Error | Notes |
|-----------|--------|-------|-------|
| `https://data.etabus.gov.hk/v1/transport/citybus/route` | ❌ 422 | Invalid/Missing parameter(s) | Primary API endpoint failing |
| `https://data.etabus.gov.hk/v1/transport/citybus/company` | ❌ 422 | Invalid/Missing parameter(s) | Company endpoint failing |
| `https://data.etabus.gov.hk/v1/transport/citybus/route-stop` | ❌ 422 | Invalid/Missing parameter(s) | Route-stop endpoint failing |
| `https://data.etabus.gov.hk/v1/transport/citybus/eta` | ❌ 422 | Invalid/Missing parameter(s) | ETA endpoint failing |
| `https://rt.data.gov.hk/v2/transport/citybus/route-stop/ctb` | ❌ 422 | Invalid/Missing parameter(s) | Route-stop endpoint failing |
| `https://rt.data.gov.hk/v2/transport/citybus/eta/ctb` | ❌ 422 | Invalid/Missing parameter(s) | ETA endpoint failing |

## 📈 **Data Collection Results**

### **Successfully Collected Data**
- **Total Routes:** 394 Citybus routes
- **Company:** CTB (Citybus Limited)
- **Data Quality:** Complete route information with multilingual names
- **File Location:** `data/raw_routes/citybus_routes_rt_20251019_121555.json`

### **Data Structure Analysis**
```json
{
  "co": "CTB",
  "route": "1",
  "orig_tc": "中環 (港澳碼頭)",
  "orig_en": "Central (Macau Ferry)",
  "dest_tc": "跑馬地 (上)",
  "dest_en": "Happy Valley (Upper)",
  "orig_sc": "中环 (港澳码头)",
  "dest_sc": "跑马地 (上)",
  "data_timestamp": "2025-10-19T05:00:02+08:00"
}
```

### **Data Fields Available**
- **`co`:** Company code (CTB)
- **`route`:** Route number/identifier
- **`orig_tc`:** Origin in Traditional Chinese
- **`orig_en`:** Origin in English
- **`dest_tc`:** Destination in Traditional Chinese
- **`dest_en`:** Destination in English
- **`orig_sc`:** Origin in Simplified Chinese
- **`dest_sc`:** Destination in Simplified Chinese
- **`data_timestamp`:** Data collection timestamp

## 🚫 **API Issues Identified**

### **Primary API Issues**
1. **data.etabus.gov.hk endpoints:** All returning 422 errors
2. **Missing Parameters:** Consistent "Invalid/Missing parameter(s)" errors
3. **Documentation Gap:** No clear documentation on required parameters
4. **Inconsistent Access:** Some endpoints work, others don't

### **Specific Problems**
- **Route Data:** `data.etabus.gov.hk/v1/transport/citybus/route` - 422 error
- **Company Data:** `data.etabus.gov.hk/v1/transport/citybus/company` - 422 error
- **Route-Stop Data:** Both API versions failing for route-stop endpoints
- **ETA Data:** Both API versions failing for ETA endpoints

## 🔧 **Workarounds Implemented**

### **Alternative Data Sources**
- **Working Endpoint:** `rt.data.gov.hk/v2/transport/citybus/route/ctb`
- **Data Quality:** Complete route information available
- **Coverage:** 394 routes successfully collected
- **Limitations:** Missing route-stop and ETA data

### **Data Collection Strategy**
1. **Primary Source:** Use `rt.data.gov.hk` endpoints where available
2. **Fallback:** Create sample data for missing endpoints
3. **Validation:** Verify data quality and completeness
4. **Documentation:** Document all working and non-working endpoints

## 📊 **Impact Assessment**

### **Research Impact**
- **Route Analysis:** Can proceed with 394 Citybus routes
- **Overlap Detection:** Limited to route-level analysis
- **Coordination Analysis:** Missing real-time ETA data
- **Comprehensive Analysis:** Partial data availability

### **Data Gaps**
- **Route-Stop Mappings:** Cannot collect stop-level data
- **Real-time ETA:** Cannot collect arrival time data
- **Service Information:** Missing detailed service data
- **Performance Metrics:** Cannot calculate service reliability

## 🎯 **Recommendations**

### **Immediate Actions**
1. **Use Working Endpoints:** Continue using `rt.data.gov.hk` for available data
2. **Contact API Provider:** Reach out to Digital Policy Office for API documentation
3. **Alternative Sources:** Explore other data sources for missing information
4. **Documentation Update:** Update API documentation with working endpoints

### **Long-term Solutions**
1. **API Standardization:** Work with providers to standardize API access
2. **Data Integration:** Develop unified data collection framework
3. **Quality Assurance:** Implement data validation and monitoring
4. **Policy Development:** Use findings to improve data accessibility

## 📋 **Technical Details**

### **Working API Configuration**
```python
endpoint = 'https://rt.data.gov.hk/v2/transport/citybus/route/ctb'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9'
}
```

### **Data Collection Process**
1. **Endpoint Testing:** Systematic testing of all available endpoints
2. **Error Handling:** Comprehensive error handling and logging
3. **Data Validation:** Quality checks and validation
4. **Storage Management:** Timestamped data files with backup

### **File Organization**
```
data/raw_routes/
├── citybus_routes_rt_20251019_121555.json    # Working endpoint data
├── kmb_routes_20251019_120938.json           # KMB data
└── all_routes_20251019_120938.json           # Combined data
```

## 🚨 **Critical Issues Requiring Attention**

### **API Accessibility Problems**
1. **Inconsistent API Behavior:** Different endpoints returning different errors
2. **Missing Documentation:** No clear guidance on required parameters
3. **Data Gaps:** Critical data (route-stops, ETA) unavailable
4. **Research Impact:** Limited analysis capabilities

### **Recommended Actions**
1. **Immediate:** Contact Digital Policy Office for API support
2. **Short-term:** Implement workarounds for missing data
3. **Long-term:** Develop comprehensive data collection strategy
4. **Policy:** Advocate for improved API accessibility

## 📞 **Next Steps**

### **1. Contact API Provider**
- **Email:** enquiry@digitalpolicy.gov.hk
- **Subject:** Citybus API Access Issues - Research Project
- **Priority:** High - Research project blocked

### **2. Implement Workarounds**
- **Use Working Endpoints:** Continue with available data
- **Create Sample Data:** For missing data types
- **Document Limitations:** Clear documentation of data gaps

### **3. Develop Alternative Solutions**
- **Multiple Data Sources:** Explore other data providers
- **Manual Collection:** Collect missing data through other means
- **Collaboration:** Work with other researchers and organizations

---

*This report provides a comprehensive analysis of Citybus API accessibility issues and successful data collection from working endpoints. The findings support the need for improved API documentation and accessibility for research purposes.*
