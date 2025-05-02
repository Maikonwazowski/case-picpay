import requests
from config.settings import AIRPORTDB_API_KEY

def get_airport_coords(airport_code: str):
    url = f"https://airportdb.io/api/v1/airport/K{airport_code}?apiToken={AIRPORTDB_API_KEY}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return {
            "latitude": data.get("latitude_deg"),
            "longitude": data.get("longitude_deg")
        }
    raise RuntimeError(f"AIRPORT API ERROR {r.status_code}: {r.text}")
