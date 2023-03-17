from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    username: str
    password: str


class Login(BaseModel):
    email_or_username: str
    password: str
