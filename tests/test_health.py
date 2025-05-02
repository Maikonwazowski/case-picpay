from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_health():
    response = client.get("/model-airport/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "model_loaded" in data