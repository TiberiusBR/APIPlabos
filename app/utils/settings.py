from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

p_host = os.environ.get("POSTGRES_HOST")
p_port = os.environ.get("POSTGRES_PORT")
u_host = os.environ.get("UVICORN_HOST")


class Settings(BaseSettings):
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = 'localhost' if p_host is None else p_host
    POSTGRES_PORT: str = '5432' if p_port is None else p_port
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    API_PORT: int = os.environ.get("API_PORT") or 8000
    JWT_SECRET_KEY: str = str(os.environ.get("JWT_SECRET_KEY"))
    UVICORN_HOST: str = '127.0.0.1' if u_host is None else u_host
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 720  # 12 hours
    ALGORITHM: str = "HS256"


settings = Settings()
