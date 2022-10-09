from pydantic import BaseModel


class Category(BaseModel):
    name: str
    id: int


class CategoryIdentifer(BaseModel):
    id: int


class CategoryCreate(BaseModel):
    name: str
