from supabase import create_client
from app.core.config import settings


if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
    raise RuntimeError("Supabase env variables not loaded")

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)
