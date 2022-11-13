from pydantic import BaseModel
from app.schemas.course import Course


class CategoryCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Category(CategoryCreate):
    id: int


class CategoryCourse(Category):
    courses: list[Course] = None
