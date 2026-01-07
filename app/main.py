from fastapi import FastAPI
from app.api.v1 import auth, predict, explain, metrics, feedback

app = FastAPI(
    title="Human Behavior Analytics API",
    version="1.0"
)

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(predict.router, prefix="/api/v1")
app.include_router(explain.router, prefix="/api/v1")
app.include_router(metrics.router, prefix="/api/v1")
app.include_router(feedback.router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "Backend running"}
