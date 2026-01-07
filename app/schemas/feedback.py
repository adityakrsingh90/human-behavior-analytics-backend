from pydantic import BaseModel, EmailStr
from typing import Optional


class FeedbackSchema(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    is_accurate: Optional[bool] = None
    rating: Optional[int] = None
    feedback: Optional[str] = None
