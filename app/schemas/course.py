from pydantic import BaseModel

from app.schemas.category import Category


class CourseBase(BaseModel):
    title: str
    course_load: int
    author_id: int

    class Config:
        orm_mode = True


class Course(CourseBase):
    id: int


class CourseCategory(Course):
    categories: list[Category] = None


class CreateCourseCategory(CourseBase):
    categories: list[int] = None
