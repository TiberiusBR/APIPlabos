from pydantic import BaseModel
from schemas import user


class ReviewBase(BaseModel):
    grade: int
    course_id: int
    user_id: int

    class Config:
        orm_mode = True


class Review(ReviewBase):
    id: int
    user: user.UserBaseSchema
