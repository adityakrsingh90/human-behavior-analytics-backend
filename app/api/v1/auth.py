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

        if hasattr(res, 'error') and res.error:
            error_msg = res.error.message
            raise HTTPException(status_code=400, detail=error_msg)

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
        error_msg = "Invalid credentials"

        if hasattr(res, "error") and res.error:
            error_msg = res.error.message

        raise HTTPException(status_code=401, detail=error_msg)

    return {
        "access_token": res.session.access_token,
        "user_id": res.user.id
    }

@router.post("/resend")
def resend_verification(payload: dict):
    email = payload.get("email")

    if not email:
        raise HTTPException(status_code=400, detail="Email required")

    supabase.auth.resend({
        "type": "signup",
        "email": email
    })

    return {"message": "Verification email resent"}

