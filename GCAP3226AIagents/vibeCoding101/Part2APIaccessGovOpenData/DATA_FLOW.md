# MTR API Data Flow

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA.GOV.HK Portal                          │
│         https://data.gov.hk/en-datasets                        │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ 1. Browse datasets
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   MTR Dataset Page                              │
│   https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data │
└────────────┬──────────────────────────────┬─────────────────────┘
             │                              │
             │ 2. Links to                  │ 3. Documentation
             ▼                              ▼
┌──────────────────────┐        ┌──────────────────────────┐
│   API Endpoint       │        │   API Documentation      │
│   rt.data.gov.hk     │        │   (PDF files)            │
└──────────┬───────────┘        └──────────────────────────┘
           │
           │ 4. HTTP GET Request
           │    ?line=TML&sta=TUM
           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   MTR Real-time Server                          │
│              (Backend data processing)                          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ 5. JSON Response
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Your Application                             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Python Script (mtr_api_test.py or simple_example.py)   │  │
│  │  - Parse JSON                                             │  │
│  │  - Extract train data                                     │  │
│  │  - Format output                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ 6. Output
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Generated Files                              │
│  - mtr_api_output.json (Full data)                             │
│  - mtr_api_report.txt  (Summary)                               │
│  - Console output      (Real-time display)                      │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow Details

### Step 1: User Browses Portal
- User visits DATA.GOV.HK
- Searches for transportation datasets
- Finds MTR real-time train data

### Step 2: Access Dataset Page
- Page shows dataset description
- Lists available resources
- Provides API endpoint link

### Step 3: Review Documentation
- Download API specification PDF
- Understand parameters and response format
- Learn about line and station codes

### Step 4: Make API Request
```
HTTP GET https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php
Parameters:
  - line: TML (Tuen Ma Line)
  - sta: TUM (Tuen Mun Station)
  - lang: EN (optional)
```

### Step 5: Receive JSON Response
```json
{
  "status": 1,
  "message": "successful",
  "curr_time": "2025-10-13 23:43:12",
  "isdelay": "N",
  "data": {
    "TML-TUM": {
      "DOWN": [
        {
          "dest": "WKS",
          "plat": "2",
          "ttnt": "3",
          "time": "2025-10-13 23:46:12",
          "valid": "Y"
        }
      ]
    }
  }
}
```

### Step 6: Process and Display
Python script:
1. Parses JSON response
2. Extracts relevant fields
3. Formats for display
4. Saves to output files

## Request/Response Cycle

```
┌─────────────┐                           ┌─────────────┐
│             │  HTTP GET Request         │             │
│   Client    │ ─────────────────────────>│   Server    │
│  (Python)   │  ?line=TML&sta=TUM       │   (MTR)     │
│             │                           │             │
│             │  JSON Response            │             │
│             │ <─────────────────────────│             │
└─────────────┘  {status: 1, data: ...}  └─────────────┘
```

## Data Processing Pipeline

```
Raw API Data
     │
     │ (1) JSON Parsing
     ▼
Python Dictionary
     │
     │ (2) Data Extraction
     ▼
Train Objects
     │
     │ (3) Formatting
     ▼
Human-Readable Output
     │
     ├─> (4a) Console Display
     ├─> (4b) JSON File
     └─> (4c) Text Report
```

## Example Data Transformation

### Input (Raw JSON)
```json
{
  "seq": "1",
  "dest": "WKS",
  "plat": "2",
  "ttnt": "3",
  "time": "2025-10-13 23:46:12",
  "valid": "Y"
}
```

### Output (Formatted)
```
Train to WKS: 3 minutes (Platform 2)
```

## Integration Points

### Where You Can Integrate This

1. **Web Applications**
   - Display real-time train info on websites
   - Create transit dashboards
   - Build mobile-responsive displays

2. **Mobile Apps**
   - iOS/Android transit apps
   - Location-based notifications
   - Route planning features

3. **Data Analysis**
   - Service pattern analysis
   - Delay detection systems
   - Frequency monitoring

4. **IoT/Display Systems**
   - Digital signage
   - Station information displays
   - Smart home integrations

5. **Research Projects**
   - Transportation studies
   - Public policy analysis
   - Urban planning research

## API Characteristics

| Characteristic | Value |
|---------------|-------|
| Protocol | HTTP/HTTPS |
| Method | GET |
| Format | JSON |
| Authentication | None required |
| Rate Limit | Not specified (be respectful) |
| Update Frequency | Real-time (~seconds) |
| Availability | 24/7 |
| Cost | Free |

## Error Handling Flow

```
Make API Request
     │
     ▼
  Success? ──No──> Check Error Code
     │                    │
    Yes                   ├─> NT-301: Missing parameters
     │                    ├─> Connection timeout
     │                    └─> Invalid line/station
     ▼
Parse Data
     │
     ▼
Display Results
```

## Performance Considerations

- **Request Time**: Typically < 1 second
- **Response Size**: ~1-5 KB per station
- **Caching**: Consider caching for 30-60 seconds
- **Batch Requests**: Query multiple stations if needed

## Best Practices

1. ✅ Cache responses appropriately
2. ✅ Handle errors gracefully
3. ✅ Validate user input (line/station codes)
4. ✅ Respect rate limits
5. ✅ Log API calls for debugging
6. ✅ Display user-friendly error messages

---

*This diagram shows the complete data flow from government portal to your application*
