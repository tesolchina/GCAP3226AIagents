# Hong Kong Government Open Data API Access Guide

## Overview

This guide demonstrates how to access Hong Kong's government open data using the MTR (Mass Transit Railway) Next Train API as an example. The data is provided through DATA.GOV.HK, Hong Kong's open data portal.

## Data Source

- **Portal**: [DATA.GOV.HK](https://data.gov.hk/en-datasets)
- **Dataset**: [Real-time MTR train information](https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data)
- **API Endpoint**: `https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php`

## API Documentation

The MTR provides two key documentation files:
- **API Specification**: [Next_Train_API_Spec_v1.7.pdf](https://opendata.mtr.com.hk/doc/Next_Train_API_Spec_v1.7.pdf)
- **Data Dictionary**: [Next_Train_DataDictionary_v1.7.pdf](https://opendata.mtr.com.hk/doc/Next_Train_DataDictionary_v1.7.pdf)

## Available Data

The MTR Next Train API provides:
- **Real-time train arrival information** for all MTR stations
- **Train schedule data** including:
  - Current system time and data timestamp
  - Train sequence number
  - Destination station
  - Platform number
  - Estimated arrival time
  - Time to next train (in minutes)
  - Data validity status
  - Service delay indicators

## API Parameters

### Required Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `line` | MTR line code | `TML` (Tuen Ma Line) |
| `sta` | Station code | `TUM` (Tuen Mun) |

### Optional Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `lang` | Response language (EN/TC/SC) | EN |

## MTR Line Codes

| Line Code | Line Name |
|-----------|-----------|
| `AEL` | Airport Express |
| `TCL` | Tung Chung Line |
| `TML` | Tuen Ma Line |
| `TKL` | Tseung Kwan O Line |
| `EAL` | East Rail Line |
| `SIL` | South Island Line |
| `TWL` | Tsuen Wan Line |
| `ISL` | Island Line |
| `KTL` | Kwun Tong Line |
| `DRL` | Disneyland Resort Line |

## Example Station Codes

### Tuen Ma Line (TML)
- `TUM` - Tuen Mun
- `SIH` - Siu Hong
- `TIS` - Tin Shui Wai
- `LOP` - Long Ping
- `YUL` - Yuen Long
- `KSR` - Kam Sheung Road
- `TWW` - Tsuen Wan West
- `MEF` - Mei Foo
- `NAC` - Nam Cheong
- `AUS` - Austin
- `ETS` - East Tsim Sha Tsui
- `HUH` - Hung Hom
- `HOM` - Ho Man Tin
- `TKW` - To Kwa Wan
- `SUW` - Sung Wong Toi
- `KAT` - Kai Tak
- `DIH` - Diamond Hill
- `HIK` - Hin Keng
- `TAW` - Tai Wai
- `CHE` - Che Kung Temple
- `STW` - Sha Tin Wai
- `CIO` - City One
- `SHM` - Shek Mun
- `TSH` - Tai Shui Hang
- `HEO` - Heng On
- `MOS` - Ma On Shan
- `WKS` - Wu Kai Sha

## API Response Format

### Successful Response

```json
{
    "sys_time": "2025-10-13 23:39:28",
    "curr_time": "2025-10-13 23:39:22",
    "data": {
        "TML-TUM": {
            "curr_time": "2025-10-13 23:39:22",
            "sys_time": "2025-10-13 23:39:28",
            "DOWN": [
                {
                    "seq": "1",
                    "dest": "WKS",
                    "plat": "2",
                    "time": "2025-10-13 23:39:22",
                    "ttnt": "0",
                    "valid": "Y",
                    "source": "-"
                }
            ],
            "UP": []
        }
    },
    "isdelay": "N",
    "status": 1,
    "message": "successful"
}
```

### Response Fields

| Field | Description |
|-------|-------------|
| `sys_time` | System timestamp |
| `curr_time` | Current data timestamp |
| `data` | Train schedule data object |
| `DOWN`/`UP` | Train direction arrays |
| `seq` | Sequence number of the train |
| `dest` | Destination station code |
| `plat` | Platform number |
| `time` | Estimated arrival time |
| `ttnt` | Time to next train (minutes) |
| `valid` | Data validity (Y/N) |
| `isdelay` | Service delay indicator (Y/N) |
| `status` | Response status (1=success, 0=error) |
| `message` | Status message |

### Error Response

```json
{
    "resultCode": 0,
    "timestamp": "2025-10-13 23:39:39",
    "error": {
        "errorCode": "NT-301",
        "errorMsg": "Please type the line-station."
    },
    "status": 0,
    "message": "Please type the line-station."
}
```

## How to Retrieve Data

### Using cURL

```bash
# Get next train information for Tuen Mun station on Tuen Ma Line
curl "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=TML&sta=TUM"

# Get data in Traditional Chinese
curl "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=TML&sta=TUM&lang=TC"
```

### Using Python

```python
import requests

# API endpoint
url = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php"

# Parameters
params = {
    "line": "TML",
    "sta": "TUM"
}

# Make request
response = requests.get(url, params=params)
data = response.json()

print(f"Status: {data['message']}")
print(f"Current Time: {data['curr_time']}")
```

### Using JavaScript

```javascript
const url = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=TML&sta=TUM";

fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log("Status:", data.message);
    console.log("Current Time:", data.curr_time);
  });
```

## Rate Limits and Terms of Use

- The API is provided for **free public use**
- Please check [DATA.GOV.HK Terms and Conditions](https://data.gov.hk/en/terms-and-conditions)
- Be respectful of rate limits (not explicitly documented, but avoid excessive requests)
- Data is updated in real-time

## Testing the API

Run the included Python test script:

```bash
python mtr_api_test.py
```

This will:
1. Test basic API connectivity
2. Retrieve next train information for multiple stations
3. Save the output to `mtr_api_output.json`
4. Generate a summary report

## Use Cases

This API can be used for:
- **Transit apps** showing real-time train arrivals
- **Data analysis** of MTR service patterns
- **Research** on public transportation usage
- **Educational projects** demonstrating API integration
- **Dashboards** displaying live transit information

## Additional Resources

- [DATA.GOV.HK Datasets](https://data.gov.hk/en-datasets)
- [MTR Open Data Portal](https://opendata.mtr.com.hk/)
- [Transport Category Datasets](https://data.gov.hk/en-datasets/category/transport)

## Notes

- The API returns data in JSON format
- All times are in Hong Kong Time (HKT, UTC+8)
- Train directions: `UP` typically means towards the northern/eastern terminus, `DOWN` towards the southern/western terminus
- Station and line codes are case-sensitive
- Some stations may show empty arrays for `UP` or `DOWN` during late night hours when service is limited
