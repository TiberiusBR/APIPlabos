from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Category(CategoryCreate):
    id: int


from app.schemas.course import Course


class CategoryCourse(Category):
    courses: list[Course] = None
