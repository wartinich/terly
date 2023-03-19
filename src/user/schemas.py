from pydantic import BaseModel


class User(BaseModel):
    email: str
    username: str
    steam: str
    discord: str


class UserUpdate(BaseModel):
    steam: str
    discord: str
