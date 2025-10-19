# Quick Start Guide: MTR API Access

## Prerequisites

- Python 3.x installed
- `requests` library

## Installation

```bash
# Navigate to the project directory
cd Part2APIaccessGovOpenData

# Install dependencies
pip install -r requirements.txt
```

## Running the Test

```bash
python3 mtr_api_test.py
```

## Output Files

After running the script, you'll find:

- `mtr_api_output.json` - Full JSON data from all API calls
- `mtr_api_report.txt` - Human-readable summary report

## Quick API Test

### Using cURL

```bash
# Get next train for Central station on Island Line
curl "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=ISL&sta=CEN"

# Get data in Traditional Chinese
curl "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=ISL&sta=CEN&lang=TC"
```

### Using Python (Quick Test)

```python
import requests

response = requests.get(
    "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php",
    params={"line": "TML", "sta": "TUM"}
)

data = response.json()
print(f"Status: {data['message']}")
print(f"Time: {data['curr_time']}")
```

## Common Line-Station Combinations

| Line | Station | Code Example |
|------|---------|--------------|
| Tuen Ma Line | Tuen Mun | `line=TML&sta=TUM` |
| Island Line | Central | `line=ISL&sta=CEN` |
| Kwun Tong Line | Mong Kok | `line=KTL&sta=MOK` |
| East Rail Line | Sha Tin | `line=EAL&sta=SHT` |
| Tsuen Wan Line | Tsim Sha Tsui | `line=TWL&sta=TSW` |

## Understanding the Response

```json
{
  "status": 1,              // 1 = success, 0 = error
  "message": "successful",  // Status message
  "curr_time": "...",       // Current data timestamp
  "isdelay": "N",          // Service delay (Y/N)
  "data": {
    "LINE-STATION": {
      "UP": [...],         // Trains going UP
      "DOWN": [...]        // Trains going DOWN
    }
  }
}
```

Each train object contains:
- `dest` - Destination station code
- `plat` - Platform number
- `ttnt` - Time to next train (minutes)
- `time` - Estimated arrival time
- `valid` - Data validity (Y/N)

## Troubleshooting

### Error: "Please type the line-station"
- Make sure you include both `line` and `sta` parameters
- Check that codes are correct (case-sensitive)

### No trains showing
- May be outside service hours (typically ~6:00 AM - 1:00 AM)
- Check if `valid` field is "Y"

### Connection timeout
- Check internet connection
- MTR API server may be temporarily unavailable

## Next Steps

1. ✅ Read the full `README.md` for detailed documentation
2. ✅ Run `mtr_api_test.py` to see it in action
3. ✅ Modify the script to test your favorite stations
4. ✅ Build your own application using the API
5. ✅ Explore other datasets on DATA.GOV.HK

## Resources

- [DATA.GOV.HK](https://data.gov.hk/en-datasets)
- [MTR Dataset Page](https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data)
- [API Specification PDF](https://opendata.mtr.com.hk/doc/Next_Train_API_Spec_v1.7.pdf)

## Support

For questions about:
- **The API**: Check `README.md` or MTR's official documentation
- **The Python script**: Review code comments in `mtr_api_test.py`
- **Course project**: Consult your instructor or course materials

---

*Generated for GCAP3226 - Empowering Citizens through Data*
