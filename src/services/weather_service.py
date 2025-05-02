import requests
from config.settings import WEATHERBIT_API_KEY

def get_wind_speed(lat: float, lon: float):
    url = "https://api.weatherbit.io/v2.0/current"
    params = {
        "lat": lat,
        "lon": lon,
        "key": WEATHERBIT_API_KEY
    }
    r = requests.get(url, params=params)
    if r.status_code == 200:
        data = r.json().get("data", [{}])
        return data[0].get("wind_spd")
    raise RuntimeError(f"WEATHERBIT ERROR {r.status_code}: {r.text}")
