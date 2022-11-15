from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.conn import get_db
from app.schemas.auth_schemas import TokenPayload
from pydantic import ValidationError
from app.repository import user_repo
from app.utils.settings import settings
from datetime import datetime

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin", scheme_name="JWT")

async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = user_repo.get_user_by_id(db, token_data.id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    return user
