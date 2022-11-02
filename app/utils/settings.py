from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    JWT_SECRET_KEY: str = str(os.environ.get("JWT_SECRET_KEY"))
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3  # 12 hours
    ALGORITHM: str = "HS256"


settings = Settings()
