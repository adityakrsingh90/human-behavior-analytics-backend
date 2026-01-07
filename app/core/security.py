from fastapi import Header, HTTPException
from app.db.supabase import supabase

def verify_token(authorization: str = Header(...)):
    try:
        if not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid token format")

        token = authorization.split(" ")[1]

        # ✅ Supabase verifies its own JWT
        user = supabase.auth.get_user(token)

        if user.user is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {
            "sub": user.user.id,
            "email": user.user.email
        }

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
