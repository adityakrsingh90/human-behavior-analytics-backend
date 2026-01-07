from fastapi import APIRouter, HTTPException
from app.db.supabase import supabase
from app.schemas.feedback import FeedbackSchema

router = APIRouter(tags=["Feedback"])


@router.post("/feedback")
def submit_feedback(payload: FeedbackSchema):
    data = payload.dict()

    res = supabase.table("user_feedback").insert(data).execute()

    if not res.data:
        raise HTTPException(status_code=500, detail="Failed to submit feedback")

    return {
        "message": "Thank you for your feedback!"
    }
