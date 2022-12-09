from pydantic import BaseModel

from schemas.category import Category
from schemas.user import UserBaseSchema


class CourseBase(BaseModel):
    title: str
    course_load: int
    author_id: int
    description: str
    image_url: str = None

    class Config:
        orm_mode = True


class Course(CourseBase):
    id: int


class CourseCategory(Course):
    categories: list[Category] = None


class CreateCourseCategory(CourseBase):
    categories: list[int] = None

class CourseAuthorCategory(CourseCategory):
    user: UserBaseSchema = None
