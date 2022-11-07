from pydantic import BaseModel, constr


class UserBaseSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    login: str
    password: constr(min_length=8)
    password_confirm: str


class LoginUserSchema(BaseModel):
    login: str
    password: constr(min_length=8)


class UserResponse(UserBaseSchema):
    id: int
    name: str