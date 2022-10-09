import databases
from dotenv import load_dotenv
import sqlalchemy
import os

load_dotenv()

DATABASE_URL = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    os.environ.get("POSTGRES_USER"),
    os.environ.get("POSTGRES_PASSWORD"),
    os.environ.get("HOST"),
    os.environ.get("PORT"),
    os.environ.get("POSTGRES_DB"),
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
