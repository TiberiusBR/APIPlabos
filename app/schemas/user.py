from pydantic import BaseModel


class UserBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
    login: str


class User(UserBase):
    id: int
    # courses: list[Course] = []
