from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import models
from schemas.registry import RegistryBase


def create_registry(db: Session, registration_data: RegistryBase):
    new_registry = models.Registry(**registration_data.dict())
    db.add(new_registry)
    db.commit()
    db.refresh(new_registry)
    return new_registry


def get_registration_by_user_and_course(db: Session, user_id: int, course_id: int):
    return (
        db.query(models.Registry)
        .filter(
            and_(
                models.Registry.user_id == user_id,
                models.Registry.course_id == course_id,
            )
        )
        .first()
    )
