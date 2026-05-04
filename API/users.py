from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from MODELS.users import User
from DB.conn import get_db
from SCHEMAS.users import create_user, update_user, response_user
from SCHEMAS.general import success_response

router = APIRouter()


def record_exists(db: Session, model, **kwargs) -> bool:
    return db.query(model).filter_by(**kwargs).first() is not None


@router.post("/create_user/", response_model=success_response)
async def create_user(user:create_user, db: Session=Depends(get_db)):
    db_user=User
    new_user = db_user(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return success_response(data=response_user.model_validate(new_user), message="User created successfully", status="success")

@router.get("/get_user/{user_id}", response_model=success_response)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return success_response(data=response_user.model_validate(db_user), message="User retrieved successfully", status="success")


@router.get("/get_all_users/", response_model=success_response)
def get_all_users_endpoint(db: Session = Depends(get_db)):
    db_users = db.query(User).filter(User.is_active == True).all()
    return success_response(data=[response_user.model_validate(u) for u in db_users], message="Users retrieved successfully", status="success")


@router.put("/update_user/{user_id}", response_model=success_response)
def update_user_endpoint(user_id: int, user: update_user, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return success_response(data=response_user.model_validate(db_user), message="User updated successfully", status="success")


@router.patch("/update_user/{user_id}", response_model=success_response)
def patch_user_endpoint(user_id: int, user: update_user, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return success_response(data=response_user.model_validate(db_user), message="User updated successfully", status="success")


@router.delete("/delete_user/{user_id}", response_model=success_response)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.is_active = False
    db.commit()
    return success_response(data=None, message="User deleted successfully", status="success")
