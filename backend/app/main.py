from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="Lynkio API",
    description="AI-Powered Bookmark Manager",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Lynkio API"}

app.include_router(health_router)