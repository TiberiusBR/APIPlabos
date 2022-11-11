from pydantic import BaseModel


class CategoryCourseCreate(BaseModel):
    course_id: int
    category_id: int

    class Config:
        orm_mode = True


class CategoryCoursePayload(BaseModel):
    course_id: int
    category_ids: list[int]
