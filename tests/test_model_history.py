from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_model_history():
    response = client.get("/model-airport/model/history/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
