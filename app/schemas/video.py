from pydantic import BaseModel


class VideoBaseSchema(BaseModel):
    name: str
    course_id: int

    class Config:
        orm_mode = True