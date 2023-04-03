from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    email: str
    username: str
    steam: Optional[str]
    discord: Optional[str]

    class Config:
        orm_mode = True


class UserUpdateDTO(BaseModel):
    steam: str = Optional[str]
    discord: str = Optional[str]

    class Config:
        orm_mode = True


class TokenPayload(BaseModel):
    user_id: str = None
    expires: int = None
