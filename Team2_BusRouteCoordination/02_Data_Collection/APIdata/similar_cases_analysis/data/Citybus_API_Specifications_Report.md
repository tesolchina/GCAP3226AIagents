# Citybus Real-Time Data Access Report: API Specifications and Usage Guide

## 📊 **Executive Summary**
This report provides a comprehensive guide on accessing real-time "Next Bus" arrival time and related data from Citybus Limited using the API specifications outlined in the document Real-time "Next Bus" arrival time and related data of Citybus - API Specifications (Version 2.01, July 2023). The APIs are hosted on the Hong Kong Government's data platform and enable retrieval of company information, routes, stops, route-stop mappings, and estimated time of arrival (ETA) data.

### **Key Highlights:**
- **Base URL:** `https://rt.data.gov.hk/v2/transport/citybus`
- **Company ID:** Primarily "CTB" for Citybus Limited, which now integrates all former New World First Bus routes
- **HTTP Method:** All endpoints use GET requests
- **Response Format:** JSON, with common fields like type, version, generated_timestamp, and data
- **Error Handling:** Common errors include 422 (Invalid/Missing parameters), 429 (Too many requests), and 500 (Internal Server Error)
- **Transition Recommendation:** Migrate to V2 APIs, as V1.0 and V1.1 will be discontinued after December 31, 2023

## 🎯 **Introduction**
Citybus Limited, operating under the company ID "CTB", provides real-time bus data through open APIs hosted by the Hong Kong Government. The APIs support applications for public transport information, such as mobile apps or websites displaying bus routes, stops, and ETAs. The specifications emphasize the integration of New World First Bus routes into Citybus effective June 2023, ensuring all data is accessible under "CTB".

### **Key Considerations:**
- **Data Timestamps:** Responses include generated_timestamp (API response time) and data_timestamp (data update time), e.g., "2025-10-19T05:00:02+08:00"
- **No Authentication Required:** Publicly accessible, but rate limits may apply (leading to 429 errors)
- **Parameter Validation:** Invalid or missing parameters result in 422 errors with messages like "Invalid company code" or "Invalid/Missing parameter(s)."

## 🔧 **API Overview**
The APIs share a common base URL and return JSON responses. Below is a summary table of the endpoints:

| API Name | Endpoint Path | Required Parameters | Description |
|----------|---------------|-------------------|-------------|
| Company | `/company/{company_id}` | company_id (e.g., "CTB") | Retrieves company details like name, URL |
| Route | `/route/{company_id}/{route}` | company_id; route (optional) | Gets route info; omit route for full list |
| Stop | `/stop/{stop_id}` | stop_id (6-digit, e.g., "002737") | Retrieves stop details like name, coordinates |
| Route-Stop | `/route-stop/{company_id}/{route}/{direction}` | company_id, route, direction ("inbound" or "outbound") | Lists stops for a route and direction |
| ETA | `/eta/{company_id}/{stop_id}/{route}` | company_id, stop_id, route | Provides 1-3 ETAs for a stop and route |

### **Response Codes:**
- **200:** Success
- **422:** Invalid/missing parameters (see error response section)
- **429:** Rate limit exceeded
- **500:** Server error

## 📋 **Detailed API Usage**

### **1. Company API**
**Description:** Returns company information for the specified ID. Valid ID: "CTB" (Citybus Limited).

**Sample Request:**
```
GET https://rt.data.gov.hk/v2/transport/citybus/company/CTB
```

**Sample Response (JSON):**
```json
{
  "type": "Company",
  "version": "2.0",
  "generated_timestamp": "2023-07-01T11:40:48+08:00",
  "data": {
    "co": "CTB",
    "name_tc": "城巴有限公司",
    "name_en": "Citybus Limited",
    "name_sc": "城巴有限公司",
    "url": "https://www.citybus.com.hk",
    "data_timestamp": "2023-07-01T11:40:00+08:00"
  }
}
```

**Usage Tips:** Use this to verify company details or fetch the URL for further reference. Always use "CTB" as the ID.

### **2. Route API**
**Description:** Retrieves route details. If route is omitted, returns the full list of routes under "CTB".

**Sample Request (Specific Route):**
```
GET https://rt.data.gov.hk/v2/transport/citybus/route/CTB/107
```

**Sample Response (JSON):**
```json
{
  "type": "Route",
  "version": "2.0",
  "generated_timestamp": "2023-07-01T11:40:48+08:00",
  "data": {
    "co": "CTB",
    "route": "107",
    "orig_en": "Wah Kwai Estate",
    "orig_tc": "華貴邨",
    "orig_sc": "华贵邨",
    "dest_en": "Kowloon Bay",
    "dest_tc": "九龍灣",
    "dest_sc": "九龙湾",
    "data_timestamp": "2023-07-01T11:40:00+08:00"
  }
}
```

**Sample Request (Full List):**
```
GET https://rt.data.gov.hk/v2/transport/citybus/route/CTB
```

**Usage Tips:** The full list can be large (hundreds of routes). Parse the data array for origins/destinations. Routes include alphanumeric codes like "A25S" or "E11".

### **3. Stop API**
**Description:** Returns details for a 6-digit stop ID. Obtain stop IDs from Route-Stop API.

**Sample Request:**
```
GET https://rt.data.gov.hk/v2/transport/citybus/stop/002737
```

**Sample Response (JSON):**
```json
{
  "type": "Stop",
  "version": "2.0",
  "generated_timestamp": "2023-07-01T11:40:48+08:00",
  "data": {
    "stop": "002737",
    "name_tc": "砵典乍街, 德輔道中",
    "name_en": "Pottinger Street, Des Voeux Road Central",
    "name_sc": "砵典乍街, 德辅道中",
    "lat": 22.283948,
    "long": 114.156309,
    "data_timestamp": "2023-07-01T11:40:00+08:00"
  }
}
```

**Usage Tips:** Use latitude/longitude for mapping integration. Ensure stop ID is exactly 6 digits (padded with zeros if needed).

### **4. Route-Stop API**
**Description:** Lists stops for a route and direction ("inbound" towards origin, "outbound" towards destination).

**Sample Request:**
```
GET https://rt.data.gov.hk/v2/transport/citybus/route-stop/CTB/1/inbound
```

**Sample Response (Partial JSON; full response is an array):**
```json
{
  "type": "Route",
  "version": "2.0",
  "generated_timestamp": "2023-07-01T11:40:48+08:00",
  "data": [
    {
      "co": "CTB",
      "route": "1",
      "dir": "I",
      "seq": 1,
      "stop": "002403",
      "data_timestamp": "2023-07-01T11:40:00+08:00"
    }
  ]
}
```

**Usage Tips:** Direction "I" in response means inbound. Use this to map routes to stops for ETA queries.

### **5. ETA API**
**Description:** Returns 1-3 ETAs for a stop and route. May be empty if no data.

**Sample Request:**
```
GET https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/001145/11
```

**Sample Response (Partial JSON; full response is an array):**
```json
{
  "type": "ETA",
  "version": "2.0",
  "generated_timestamp": "2023-07-01T15:45:00+08:00",
  "data": [
    {
      "co": "CTB",
      "route": "11",
      "dir": "O",
      "seq": 1,
      "stop": "001145",
      "dest_tc": "渣甸山",
      "dest_sc": "渣甸山",
      "dest_en": "Jardine's Lookout",
      "eta_seq": 1,
      "eta": "2023-07-01T15:48:00+08:00",
      "rmk_tc": "",
      "rmk_sc": "",
      "rmk_en": "",
      "data_timestamp": "2023-07-01T15:44:33+08:00"
    }
  ]
}
```

**Usage Tips:** ETAs are in ISO format. Remarks (rmk_*) may include notes. Poll periodically for updates.

## 💻 **Implementation Examples**

### **Using cURL (Command Line)**
For the Company API:
```bash
curl -X GET "https://rt.data.gov.hk/v2/transport/citybus/company/CTB" | jq .
```

For ETA:
```bash
curl -X GET "https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/001145/11" | jq .
```

### **Using Python (requests library)**
```python
import requests

base_url = "https://rt.data.gov.hk/v2/transport/citybus"

def get_company(company_id):
    response = requests.get(f"{base_url}/company/{company_id}")
    return response.json() if response.status_code == 200 else None

# Example: print(get_company("CTB"))
```

Handle errors by checking response.status_code.

## 📊 **Best Practices and Limitations**

### **Best Practices:**
- **Parameter Sourcing:** Use Route API to get valid routes; Route-Stop for stop IDs
- **Rate Limiting:** Avoid excessive requests to prevent 429 errors
- **Data Freshness:** Check data_timestamp for recency
- **Localization:** Responses include English (_en), Traditional Chinese (_tc), and Simplified Chinese (_sc)

### **Limitations:**
- **ETAs Limited:** 1-3 per request; no bulk ETA endpoint
- **No Authentication:** Public use only
- **Rate Limits:** May encounter 429 errors with excessive requests
- **Data Availability:** Some endpoints may return 422 errors

## 🎯 **Project Application**

### **For Our Bus Route Coordination Research:**
1. **Route Data Collection:** Use Route API to get all Citybus routes
2. **Stop Analysis:** Use Route-Stop API to map routes to stops
3. **Overlap Detection:** Compare Citybus stops with KMB stops
4. **Real-time Analysis:** Use ETA API for coordination analysis

### **Data Collection Strategy:**
1. **Collect All Routes:** Use `/route/CTB` to get complete route list
2. **Map Route Stops:** Use `/route-stop/CTB/{route}/{direction}` for each route
3. **Analyze Overlaps:** Compare stop sequences between routes
4. **Coordination Analysis:** Identify overlapping routes for coordination

## 📈 **Conclusion**
The Citybus APIs provide a robust, free resource for accessing real-time bus data. By following the specifications, developers can integrate features like route planning and ETA displays. For the latest updates, visit the Citybus website or the PDF source. As of October 19, 2025, the APIs appear stable, but monitor for changes via the base URL or government data portal.

### **Next Steps for Our Project:**
1. **Implement API Collection:** Use the detailed specifications to collect comprehensive Citybus data
2. **Route-Stop Mapping:** Map all Citybus routes to their stops
3. **Overlap Analysis:** Compare with KMB routes to identify coordination opportunities
4. **Real-time Integration:** Use ETA data for dynamic coordination analysis

---

*This comprehensive API specification guide provides the foundation for accessing Citybus real-time data for our bus route coordination research project.*
