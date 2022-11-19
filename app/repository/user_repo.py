from sqlalchemy.orm import Session
from models import models
from models.models import User
from schemas.user import CreateUserSchema
from helpers.auth_helpers import hash_password


def get_user_by_login(db: Session, login: str) -> User:
    return db.query(models.User).filter(models.User.login == login.lower()).first()


def get_user_by_id(db: Session, id: str) -> User:
    return db.query(models.User).filter(models.User.id == id).first()


def create_user(db: Session, user_payload: CreateUserSchema):
    user_payload.login = user_payload.login.lower()
    user_payload.password = hash_password(user_payload.password)
    new_user = User(**user_payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
