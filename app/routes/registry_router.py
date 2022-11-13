from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import registry
from app.repository import registry_repo as repo
from app.database.conn import get_db
from app.helpers.registry_helpers import (
    is_existing_course,
    is_existing_user,
    is_registration_user,
)


registry_router = APIRouter(prefix="/registry")


@registry_router.post(
    "/create", response_model=registry.Registry, status_code=status.HTTP_201_CREATED
)
def register(payload: registry.RegistryBase, db: Session = Depends(get_db)):
    if not is_existing_course(db, payload.course_id) or not is_existing_user(
        db, payload.user_id
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Non-existent course or user",
        )
    if is_registration_user(db, payload.user_id, payload.course_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already registered",
        )
    created_registry = repo.create_registry(db, payload)
    return created_registry
