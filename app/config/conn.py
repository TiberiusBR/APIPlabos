import databases
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

load_dotenv()

DATABASE_URL = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    os.environ.get("POSTGRES_USER"),
    os.environ.get("POSTGRES_PASSWORD"),
    os.environ.get("HOST"),
    os.environ.get("PORT"),
    os.environ.get("POSTGRES_DB"),
)

# database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
