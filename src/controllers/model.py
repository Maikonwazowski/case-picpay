from src.storage.storage import InMemoryStore
from src.schemas.schema import FlightInput, PredictInput
import pickle
import joblib
from io import BytesIO
from datetime import datetime, timezone
from src.services.airport_service import get_airport_coords
from src.services.weather_service import get_wind_speed

class Model:

    @staticmethod
    def health_status():
        model = InMemoryStore.get_model()
        model_loaded = model is not None

        status = "ok" if model_loaded else "degraded"

        try:
            _ = get_airport_coords("JFK")
            _ = get_wind_speed(40.7128, -74.0060)
            external_ok = True
        except Exception:
            external_ok = False
            status = "degraded"

        return {
            "status": status,
            "model_loaded": model_loaded,
            "external_apis_reachable": external_ok,
            "model_version": "1.0.0",
            "model_type": "LinearRegression",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    @staticmethod
    def load_model_from_file(file_bytes: bytes):
        model = pickle.load(BytesIO(file_bytes))
        InMemoryStore.set_model(model)

    @staticmethod
    def predict_from_input(input_data: PredictInput) -> float:
        model = InMemoryStore.get_model()
        if model is None:
            raise ValueError("Modelo não carregado")

        enriched_input = Model._enrich_input(input_data)
        print('enriched_input:', enriched_input)

        feature_names = [
            "month", "distance", "air_time",
            "wind_spd_origin", "wind_spd_dest",
            "carrier_code_AA", "carrier_code_DL", "carrier_code_SW", "carrier_code_UA",
            "route_ATL_ORD", "route_JFK_LAX", "route_SFO_DEN"
        ]

        X = [[enriched_input.model_dump()[key] for key in feature_names]]

        prediction = float(model.predict(X)[0])
        Model._add_history(enriched_input, prediction)
        return prediction

    @staticmethod
    def _add_history(payload: FlightInput, prediction: float):

        history_entry = {
            "model_version": "1.0.0",
            "model_type": "LinearRegression",
            "input": payload.model_dump(),
            "prediction": prediction,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        InMemoryStore.add_history(history_entry)

    @staticmethod
    def _enrich_input(input_data: PredictInput) -> FlightInput:
        date = datetime.now(timezone.utc).date().isoformat()

        origin_coords = get_airport_coords(input_data.origin)
        dest_coords = get_airport_coords(input_data.dest)

        wind_origin = get_wind_speed(origin_coords["latitude"], origin_coords["longitude"])
        wind_dest = get_wind_speed(dest_coords["latitude"], dest_coords["longitude"])

        enriched_dict = {
            **input_data.model_dump(),
            "wind_spd_origin": wind_origin,
            "wind_spd_dest": wind_dest
        }

        enriched_dict.pop("origin", None)
        enriched_dict.pop("dest", None)

        return FlightInput(**enriched_dict)

    @staticmethod
    def get_prediction_history():
        return InMemoryStore.get_history()
