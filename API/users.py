from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from MODELS.users import User
from DB.conn import get_db
from SCHEMAS.users import create_user, response_user
from SCHEMAS.general import success_response, error_response

router = APIRouter()


def record_exists(db: Session, model, **kwargs) -> bool:
    return db.query(model).filter_by(**kwargs).first() is not None


@router.post("/create_user/", response_model=success_response)
def create_user_endpoint(user: create_user, db: Session = Depends(get_db)):
    if record_exists(db, User, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if record_exists(db, User, username=user.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return success_response(data=response_user.model_validate(db_user), message="User created successfully", status="success")