import requests
import json
import pandas as pd
from typing import Dict, Any, List

class CityBusAPI:
    def __init__(self):
        self.base_urls = {
            'gov_hk_v2': 'https://rt.data.gov.hk/v2/transport/citybus',
            'etabus': 'https://data.etabus.gov.hk/v1/transport/citybus'
        }
    
    def make_request(self, url: str) -> Dict[str, Any]:
        """Make API request and handle errors"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return {}
    
    def get_company_info(self) -> Dict[str, Any]:
        """Get company information"""
        url = f"{self.base_urls['etabus']}/company"
        return self.make_request(url)
    
    def get_all_routes(self) -> Dict[str, Any]:
        """Get all bus routes"""
        url = f"{self.base_urls['etabus']}/route"
        return self.make_request(url)
    
    def get_route_stops_etabus(self, route: str, direction: str = None) -> Dict[str, Any]:
        """Get stops for a specific route from etabus"""
        url = f"{self.base_urls['etabus']}/route-stop/{route}"
        if direction:
            url += f"/{direction}"
        return self.make_request(url)
    
    def get_route_stops_govhk(self, route: str) -> Dict[str, Any]:
        """Get stops for a specific route from gov.hk v2 API"""
        url = f"{self.base_urls['gov_hk_v2']}/route-stop/ctb/{route}"
        return self.make_request(url)
    
    def get_eta_etabus(self, stop_id: str, route: str = None) -> Dict[str, Any]:
        """Get estimated time of arrival from etabus"""
        url = f"{self.base_urls['etabus']}/eta/{stop_id}"
        if route:
            url += f"/{route}"
        return self.make_request(url)
    
    def get_eta_govhk(self, stop_id: str, route: str) -> Dict[str, Any]:
        """Get estimated time of arrival from gov.hk v2 API"""
        url = f"{self.base_urls['gov_hk_v2']}/eta/ctb/{stop_id}/{route}"
        return self.make_request(url)
    
    def display_routes(self, limit: int = 10):
        """Display sample routes"""
        routes_data = self.get_all_routes()
        if routes_data and 'data' in routes_data:
            df = pd.DataFrame(routes_data['data'][:limit])
            print("Sample Bus Routes:")
            print(df[['route', 'orig_en', 'dest_en', 'service_type']].to_string(index=False))
            return routes_data['data']
        return []
    
    def display_route_stops(self, route: str, direction: str = "outbound"):
        """Display stops for a specific route"""
        stops_data = self.get_route_stops_etabus(route, direction)
        if stops_data and 'data' in stops_data:
            df = pd.DataFrame(stops_data['data'])
            print(f"\nStops for Route {route} ({direction}):")
            print(df[['stop', 'name_en', 'name_tc']].to_string(index=False))
            return stops_data['data']
        return []

# Example usage
if __name__ == "__main__":
    bus_api = CityBusAPI()
    
    # Get company info
    print("Company Information:")
    company_info = bus_api.get_company_info()
    print(json.dumps(company_info, indent=2, ensure_ascii=False))
    
    # Get and display sample routes
    routes = bus_api.display_routes(5)
    
    if routes:
        # Get stops for first route
        sample_route = routes[0]['route']
        bus_api.display_route_stops(sample_route)
        
        # Get ETA for first stop (if available)
        stops = bus_api.get_route_stops_etabus(sample_route)
        if stops and 'data' in stops and stops['data']:
            first_stop = stops['data'][0]['stop']
            eta_data = bus_api.get_eta_etabus(first_stop, sample_route)
            print(f"\nETA for Stop {first_stop}, Route {sample_route}:")
            print(json.dumps(eta_data, indent=2, ensure_ascii=False))