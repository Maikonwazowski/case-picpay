from fastapi import Form, APIRouter, UploadFile, File, HTTPException
from src.schemas.schema import PredictInput
from src.controllers.model import Model

router = APIRouter(prefix="/model-airport", tags=["Model"])

@router.get("/health/")
def health():
    return Model.health_status()

@router.post("/model/load/")
async def load_model(file: UploadFile = File(...)):
    if not file.filename.endswith(".pkl"):
        raise HTTPException(status_code=400, detail="Arquivo precisa ser .pkl")
    try:
        contents = await file.read()
        Model.load_model_from_file(contents)
        return {"message": "Modelo carregado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/model/predict/")
def predict(
    origin = Form(...),
    dest = Form(...),
    month: int = Form(...),
    distance: float = Form(...),
    air_time: float = Form(...),
    carrier_code_AA: int = Form(...),
    carrier_code_DL: int = Form(...),
    carrier_code_SW: int = Form(...),
    carrier_code_UA: int = Form(...),
    route_ATL_ORD: int = Form(...),
    route_JFK_LAX: int = Form(...),
    route_SFO_DEN: int = Form(...)
):
    try:
        flight_input = PredictInput(
            origin=origin,
            dest=dest,
            month=month,
            distance=distance,
            air_time=air_time,
            carrier_code_AA=carrier_code_AA,
            carrier_code_DL=carrier_code_DL,
            carrier_code_SW=carrier_code_SW,
            carrier_code_UA=carrier_code_UA,
            route_ATL_ORD=route_ATL_ORD,
            route_JFK_LAX=route_JFK_LAX,
            route_SFO_DEN=route_SFO_DEN
        )
        prediction = Model.predict_from_input(flight_input)
        return {"prediction": prediction}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    
@router.get("/model/history/")
def get_history():
    return Model.get_prediction_history()
