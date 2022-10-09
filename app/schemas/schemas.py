import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer
from app.config.conn import metadata

category = sqlalchemy.Table(
    "category_name",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)