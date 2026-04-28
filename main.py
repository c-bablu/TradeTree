from fastapi import FastAPI
from sqlalchemy.orm import Session
from API.users import router as users_router
from DB.conn import get_db
import uvicorn

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)