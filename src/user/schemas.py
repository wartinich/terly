from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    email: str
    username: str
    steam: Optional[str]
    discord: Optional[str]

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    steam: str
    discord: str


class TokenPayload(BaseModel):
    user_id: str = None
    expires: int = None
