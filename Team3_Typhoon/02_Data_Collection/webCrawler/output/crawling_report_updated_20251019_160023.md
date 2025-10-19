# HKO Typhoon Signal 8 Crawling Report (Updated)

**Generated:** 2025-10-19T16:00:23.133080
**Crawler:** HKO Typhoon Signal 8 Web Crawler (Updated)
**Course:** GCAP3226 - Empowering Citizens Through Data

## Summary

- **Total Signal 8 Announcements:** 0
- **Total Weather Data Points:** 0
- **Total Crawl Activities:** 15
- **Data Directory:** /Users/simonwang/Documents/Usage/GCAP3226/Team3_Typhoon/02_Data_Collection/webCrawler/data
- **Output Directory:** /Users/simonwang/Documents/Usage/GCAP3226/Team3_Typhoon/02_Data_Collection/webCrawler/output

## Signal 8 Announcements Found

## Weather Data Collected

## Crawl Activities Log

- **2025-10-19T16:00:22.825404:** CRAWL_START - Starting HKO typhoon data crawling (Updated)
- **2025-10-19T16:00:22.825462:** CRAWL_API - Fetching data from HKO API
- **2025-10-19T16:00:22.825485:** API_REQUEST - Fetching API data from: https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=warnsum&lang=en
- **2025-10-19T16:00:22.825510:** HTTP_REQUEST - Fetching: https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=warnsum&lang=en
- **2025-10-19T16:00:22.884994:** HTTP_SUCCESS - Status: 200, URL: https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=warnsum&lang=en
- **2025-10-19T16:00:22.885112:** API_SUCCESS - Retrieved API data: 2 items
- **2025-10-19T16:00:22.885162:** API_PARSE - Found 0 Signal 8 references in API
- **2025-10-19T16:00:22.885197:** CRAWL_WARNING - Crawling typhoon warning page
- **2025-10-19T16:00:22.885227:** HTTP_REQUEST - Fetching: https://www.hko.gov.hk/en/wservice/warning/ts.htm
- **2025-10-19T16:00:23.057401:** HTTP_ERROR - Error fetching https://www.hko.gov.hk/en/wservice/warning/ts.htm: 404 Client Error: Not Found for url: https://www.hko.gov.hk/en/wservice/warning/ts.htm
- **2025-10-19T16:00:23.057637:** CRAWL_WEATHER - Crawling weather page
- **2025-10-19T16:00:23.057675:** HTTP_REQUEST - Fetching: https://www.hko.gov.hk/en/wxinfo/currwx/weather.htm
- **2025-10-19T16:00:23.131446:** HTTP_ERROR - Error fetching https://www.hko.gov.hk/en/wxinfo/currwx/weather.htm: 404 Client Error: Not Found for url: https://www.hko.gov.hk/en/wxinfo/currwx/weather.htm
- **2025-10-19T16:00:23.131623:** SAVE_DATA - Saving collected data
- **2025-10-19T16:00:23.132800:** SAVE_JSON - Saved 14 records to /Users/simonwang/Documents/Usage/GCAP3226/Team3_Typhoon/02_Data_Collection/webCrawler/data/crawl_log_updated.json
