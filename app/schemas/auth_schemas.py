from pydantic import BaseModel


class TokenPayload(BaseModel):
    id: int
    exp: float
