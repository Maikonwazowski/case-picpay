import os
from dotenv import load_dotenv

load_dotenv()

AIRPORTDB_API_KEY = os.getenv("AIRPORTDB_API_KEY")
WEATHERBIT_API_KEY = os.getenv("WEATHERBIT_API_KEY")

if not AIRPORTDB_API_KEY or not WEATHERBIT_API_KEY:
    raise RuntimeError("Variáveis de ambiente não carregadas corretamente")