from fastapi.testclient import TestClient
from src.app import app
import pickle
import io
from sklearn.linear_model import LinearRegression
import numpy as np

client = TestClient(app)

def test_model_load():
    X = np.random.rand(10, 12)
    y = np.random.rand(10)
    model = LinearRegression().fit(X, y)
    buffer = io.BytesIO()
    pickle.dump(model, buffer)
    buffer.seek(0)

    response = client.post(
        "/model-airport/model/load/",
        files={"file": ("model.pkl", buffer, "application/octet-stream")}
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Modelo carregado com sucesso"}
