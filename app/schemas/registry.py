from pydantic import BaseModel


class RegistryBase(BaseModel):
    is_teacher: bool
    course_id: int
    user_id: int

    class Config:
        orm_mode = True


class Registry(RegistryBase):
    id: int
