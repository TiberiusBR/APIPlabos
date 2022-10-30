from sqlalchemy.orm import Session
from app.models import models
from app.models.models import User
from app.schemas.user import CreateUserSchema
from app.helpers.auth_helpers import hash_password


def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login.lower()).first()


def create_user(db: Session, user_payload: CreateUserSchema):
    user_payload.login = user_payload.login.lower()
    user_payload.password = hash_password(user_payload.password)
    new_user = User(**user_payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
