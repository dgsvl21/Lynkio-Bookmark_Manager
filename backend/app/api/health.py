from fastapi import APIRouter, status
from sqlalchemy import text
from app.db.database import engine

router = APIRouter()

@router.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "database": result.scalar()
        }