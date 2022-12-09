from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import user_repo as repo
from schemas import user as user_schema
from database.conn import get_db

user_router = APIRouter(prefix="/user")

@user_router.get("/id/{user_id}", response_model=user_schema.UserBaseSchema)
def get_user_name_by_id(user_id: int, db: Session = Depends(get_db)):
    user = repo.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No user found."
        )
    return user