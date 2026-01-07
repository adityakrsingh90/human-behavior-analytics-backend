from fastapi import APIRouter, Depends
from app.core.security import verify_token

router = APIRouter(tags=["Explainability"])

@router.post("/explain")
def explain_prediction(features: dict, user=Depends(verify_token)):
    """
    Placeholder for SHAP/XAI
    """

    explanation = {
        "sleep_hours": "Low sleep increased burnout risk",
        "screen_time": "High screen time reduced focus"
    }

    return {
        "user_id": user["sub"],
        "explanation": explanation
    }
