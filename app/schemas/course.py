from pydantic import BaseModel

from app.schemas.category import Category
from app.schemas.lesson import Lesson
from app.schemas.registry import Registry
from app.schemas.review import Review
from app.schemas.user import UserBaseSchema


class CourseBase(BaseModel):
    title: str
    course_load: int
    author_id: int

    class Config:
        orm_mode = True


class Course(CourseBase):
    id: int

    user: UserBaseSchema = None
    lessons: list[Lesson] = None
    registries: list[Registry] = None
    reviews: list[Review] = None


class CourseCategory(Course):
    categories: list[Category] = None
