from fastapi import APIRouter, Depends
from app.core.security import verify_token
from app.schemas.feedback import FeedbackSchema
from app.db.supabase import supabase

router = APIRouter(tags=["Feedback"])

@router.post("/feedback")
def submit_feedback(feedback: FeedbackSchema, user=Depends(verify_token)):

    supabase.table("user_feedback").insert({
        "user_id": user["sub"],
        "prediction_id": feedback.prediction_id,
        "is_accurate": feedback.is_accurate
    }).execute()

    return {"message": "Feedback recorded"}
