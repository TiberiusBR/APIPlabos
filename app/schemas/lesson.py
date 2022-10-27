from pydantic import BaseModel


class LessonBase(BaseModel):
    name: str
    video_uuid: str
    course_id: int

    class Config:
        orm_mode = True


class Lesson(LessonBase):
    id: int
