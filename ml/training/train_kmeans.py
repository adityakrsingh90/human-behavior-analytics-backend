import pandas as pd
import joblib
from pathlib import Path
from sklearn.cluster import KMeans
from ml.feature_engineering import create_features

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "ml" / "models"

df = pd.read_csv(BASE_DIR / "ml" / "data" / "behavior_data.csv")
df = create_features(df)

X = df[["productivity", "burnout"]]

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

joblib.dump(kmeans, MODEL_DIR / "kmeans.pkl")

print("✅ KMeans model saved successfully")
