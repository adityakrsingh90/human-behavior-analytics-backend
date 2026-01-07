import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from ml.feature_engineering import create_features

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "ml" / "models"
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "ml" / "data" / "behavior_data.csv")
df = create_features(df)

X = df[[
    "sleep_hours",
    "screen_time",
    "focus_sessions",
    "sleep_debt",
    "focus_ratio"
]]

y_prod = df["productivity"]
y_burn = df["burnout"]

rf_prod = RandomForestRegressor(n_estimators=100, random_state=42)
rf_burn = RandomForestRegressor(n_estimators=100, random_state=42)

rf_prod.fit(X, y_prod)
rf_burn.fit(X, y_burn)

joblib.dump(rf_prod, MODEL_DIR / "rf_productivity.pkl")
joblib.dump(rf_burn, MODEL_DIR / "rf_burnout.pkl")

print("✅ RF models saved successfully")
