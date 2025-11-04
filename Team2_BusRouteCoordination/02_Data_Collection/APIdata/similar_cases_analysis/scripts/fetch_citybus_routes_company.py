import requests
import json

# Base URL for the APIs
RT_DATA_BASE_URL = "https://rt.data.gov.hk/v2/transport/citybus"

def fetch_data(url, params=None):
    """Helper function to fetch data from API with error handling"""
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def get_company_info():
    """Fetch company information"""
    url = f"{RT_DATA_BASE_URL}/company/ctb"
    data = fetch_data(url)
    if data and 'data' in data:
        return data['data']
    return None

def get_routes():
    """Fetch all routes"""
    url = f"{RT_DATA_BASE_URL}/route/ctb"
    data = fetch_data(url)
    if data and 'data' in data:
        return data['data']
    return None

def main():
    # Fetch and display company information
    company_info = get_company_info()
    if company_info:
        print("Company Information:")
        print(json.dumps(company_info, indent=2))
        print("\n")
    else:
        print("Failed to retrieve company information.")

    # Fetch and display routes
    routes = get_routes()
    if routes:
        print("Available Routes:")
        for route in routes[:5]:  # Limit to first 5 routes for brevity
            print(f"Route: {route['route']} | Direction: {route['bound']} | "
                  f"Origin: {route['orig_en']} -> Destination: {route['dest_en']}")
        print(f"Total routes retrieved: {len(routes)}")
    else:
        print("No routes found.")

if __name__ == "__main__":
    main()