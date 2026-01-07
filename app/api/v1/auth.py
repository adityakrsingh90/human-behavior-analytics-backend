from fastapi import APIRouter, HTTPException
from app.db.supabase import supabase
from app.schemas.auth import SignupSchema, LoginSchema

router = APIRouter(tags=["Auth"])


@router.post("/signup")
def signup(payload: SignupSchema):
    res = supabase.auth.sign_up({
        "email": payload.email,
        "password": payload.password
    })

    if res.user is None:
        raise HTTPException(status_code=400, detail="Signup failed")

    return {
        "message": "Signup successful"
    }


@router.post("/login")
def login(payload: LoginSchema):
    res = supabase.auth.sign_in_with_password({
        "email": payload.email,
        "password": payload.password
    })

    if res.session is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": res.session.access_token,
        "user_id": res.user.id
    }
