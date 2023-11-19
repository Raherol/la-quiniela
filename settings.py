from pathlib import Path

BASE_DIR = Path(__file__).parent

DATABASE_PATH = BASE_DIR / "laliga.sqlite"

MODELS_PATH = BASE_DIR / "models"

LOGS_PATH = BASE_DIR / "logs"

DATA_PATH = BASE_DIR / "data" / "modeldata.xlsx"

PREDICTION_PATH = BASE_DIR / "data" / "predictions.xlsx"
