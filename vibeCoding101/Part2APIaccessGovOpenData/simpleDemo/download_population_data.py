import requests
import pandas as pd

# API endpoint for English data
url = "https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=en&full_series=1"

# Fetch data from API

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
try:
    data = response.json()
except Exception as e:
    print("Failed to decode JSON. Raw response:")
    print(response.text[:500])  # Print first 500 chars for debug
    raise

# Convert to DataFrame
# The data is expected to be in a list under a key, so we find the correct key

# The API response is a dict with a 'dataSet' key containing the data array
records = data.get('dataSet', []) if isinstance(data, dict) else []
if records:
    df = pd.DataFrame(records)
    df.to_csv("population_by_sex_and_age.csv", index=False)
    print("Data saved to population_by_sex_and_age.csv")
else:
    print("No data found in API response.")
