import joblib
import pandas as pd
from pathlib import Path
from ml.feature_engineering import create_features

# 🔹 Base directory = backend/
BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_DIR = BASE_DIR / "ml" / "models"

rf_prod = joblib.load(MODEL_DIR / "rf_productivity.pkl")
rf_burn = joblib.load(MODEL_DIR / "rf_burnout.pkl")
kmeans  = joblib.load(MODEL_DIR / "kmeans.pkl")


def run_prediction(features: dict):
    df = pd.DataFrame([features])
    df = create_features(df)

    X = df[[
        "sleep_hours",
        "screen_time",
        "focus_sessions",
        "sleep_debt",
        "focus_ratio"
    ]]

    productivity = float(rf_prod.predict(X)[0])
    burnout = float(rf_burn.predict(X)[0])

    cluster = kmeans.predict([[productivity, burnout]])[0]
    archetype_map = {0: "Focused", 1: "Balanced", 2: "Distracted"}

    return {
        "productivity_score": round(productivity, 2),
        "burnout_score": round(burnout, 2),
        "archetype": archetype_map.get(cluster, "Balanced")
    }
