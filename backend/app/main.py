from fastapi import FastAPI

app = FastAPI(
    title="Lynkio API",
    description="Bookmark Manager AI-Powered",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Lynkio API"}