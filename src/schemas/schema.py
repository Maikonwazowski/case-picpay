from pydantic import BaseModel

class PredictInput(BaseModel):
    month: int
    distance: float
    air_time: float
    origin: str
    dest: str
    carrier_code_AA: int
    carrier_code_DL: int
    carrier_code_SW: int
    carrier_code_UA: int
    route_ATL_ORD: int
    route_JFK_LAX: int
    route_SFO_DEN: int

class FlightInput(BaseModel):
    month: int
    distance: float
    air_time: float
    wind_spd_origin: float
    wind_spd_dest: float
    carrier_code_AA: int
    carrier_code_DL: int
    carrier_code_SW: int
    carrier_code_UA: int
    route_ATL_ORD: int
    route_JFK_LAX: int
    route_SFO_DEN: int