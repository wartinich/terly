from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str


class UserCreate(BaseModel):
    email: str
    username: str
    password: str


class Login(BaseModel):
    email_or_username: str
    password: str
