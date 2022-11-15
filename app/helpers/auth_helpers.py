from jose import jwt
from passlib.context import CryptContext
from app.models.models import User
from app.schemas.user import LoginUserSchema
from datetime import datetime, timedelta
from app.utils.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def is_password_equal_confirm_password(password: str, confirm_password: str):
    if password != confirm_password:
        return False
    return True


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def authenticate_user(user: User, payload: LoginUserSchema):
    if not user:
        return False
    if not verify_password(payload.password, user.password):
        return False
    return True


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(
        claims=to_encode, key=settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return token
