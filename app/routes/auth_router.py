from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import CreateUserSchema, UserResponse
from app.database.conn import get_db
from app.repository import user_repo
from app.helpers.auth_helpers import is_password_equal_confirm_password

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def signup(payload: CreateUserSchema, db: Session = Depends(get_db)):
    if not is_password_equal_confirm_password(
            payload.password, payload.password_confirm
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password and confirm password must be the same!",
        )
    user = user_repo.get_user_by_login(db, payload.login)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account already exist!",
        )
    del payload.password_confirm
    return user_repo.create_user(db, payload)
