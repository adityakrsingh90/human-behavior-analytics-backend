from fastapi import APIRouter, Depends
from app.core.security import verify_token
from app.services.ml_service import run_prediction
from app.services.nudge_service import generate_nudge
from app.db.supabase import supabase

router = APIRouter(tags=["Prediction"])

@router.post("/predict")
def predict(features: dict, user=Depends(verify_token)):

    prediction = run_prediction(features)
    nudge = generate_nudge(prediction)

    data = {
        "user_id": user["sub"],
        **prediction
    }

    supabase.table("user_predictions").insert(data).execute()

    return {
        "prediction": prediction,
        "nudge": nudge
    }
