from fastapi import APIRouter, Depends
from app.core.security import verify_token

router = APIRouter(tags=["Prediction"])

@router.post("/predict")
def predict(data: dict, user=Depends(verify_token)):
    return {
        "user_id": user["sub"],
        "prediction": "Low Burnout"
    }
