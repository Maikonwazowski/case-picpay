from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_model_predict():
    payload = {
        "month": "5",
        "distance": "1200",
        "air_time": "180",
        "origin": "JFK",
        "dest": "MIA",
        "carrier_code_AA": "1",
        "carrier_code_DL": "0",
        "carrier_code_SW": "0",
        "carrier_code_UA": "0",
        "route_ATL_ORD": "1",
        "route_JFK_LAX": "0",
        "route_SFO_DEN": "0"
    }

    response = client.post("/model-airport/model/predict/", data=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
