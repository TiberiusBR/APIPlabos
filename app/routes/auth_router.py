from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.user import CreateUserSchema, UserResponse, LoginUserSchema
from app.database.conn import get_db
from app.repository import user_repo
from app.helpers.auth_helpers import (
    authenticate_user,
    create_access_token,
    is_password_equal_confirm_password,
)
from app.middlewares.auth_middleware import get_current_user

auth_router = APIRouter(prefix="/auth")


@auth_router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
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


@auth_router.post("/signin", status_code=status.HTTP_200_OK)
async def signin(payload: LoginUserSchema, db: Session = Depends(get_db)):
    user = user_repo.get_user_by_login(db, payload.login)
    auth = authenticate_user(user, payload)
    if auth is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token({"id": user.id})
    return {"id": user.id, "name": user.name, "access_token": access_token}


@auth_router.post("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def me(user: User = Depends(get_current_user)):
    return user
