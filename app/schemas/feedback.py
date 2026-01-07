from pydantic import BaseModel

class FeedbackSchema(BaseModel):
    prediction_id: str
    is_accurate: bool
