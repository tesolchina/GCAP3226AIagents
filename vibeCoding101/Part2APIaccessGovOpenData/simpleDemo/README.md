# How to Retrieve "Population by Sex and Age Group" Dataset via API

## Dataset Overview
This dataset provides population statistics for Hong Kong, broken down by sex and age group. It is available in English, Traditional Chinese, and Simplified Chinese.

## API Endpoints
You can retrieve the data in JSON format using the following API endpoints:

- **English:**
  https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=en&full_series=1
- **Traditional Chinese:**
  https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=tc&full_series=1
- **Simplified Chinese:**
  https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=sc&full_series=1

## How to Use the API
You do not need an API key. Just copy and paste the link into your browser or use a tool like Excel, Python, or R to fetch the data.

### Example (for non-programmers)

#### Using a Web Browser
1. Copy the English API link above.
2. Paste it into your browser's address bar and press Enter.
3. The browser will show the data in JSON format.

#### Using Excel
1. Open Excel.
2. Go to the "Data" tab.
3. Click "From Web".
4. Paste the API link and click OK.
5. Excel will import the data.

#### Using Python (pseudocode)
```
# Pseudocode for fetching data
set url to "https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=en&full_series=1"
get data from url
show data
```

#### Using R (pseudocode)
```
# Pseudocode for fetching data
url <- "https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=en&full_series=1"
data <- fetch data from url
print data
```

## Data Structure
Each record contains:
- SEX: Male (M), Female (F), or Total
- AGE: Age group (e.g., "0-4", "5-9", ..., "85+", or "Total")
- figure: Percentage of total population
- period: Data period (e.g., "202506" for June 2025)

## More Information
- Maintainer: Demographic Statistics Section (1), Census and Statistics Department
- Email: population@censtatd.gov.hk
- Phone: (852) 3903 6943

For more details, visit the [dataset page](https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-01001).
