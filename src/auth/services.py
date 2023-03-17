import time

import jwt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.auth.schemas import UserCreate, Login
from src.user.models import User
from src.auth.utils import hashed_password, token_response, check_user_data
from src.settings import settings


def create_user(data: UserCreate, db: Session) -> User | HTTPException:
    check_user = db.query(User).filter(User.email == data.email, User.username == data.username).first()
    if check_user:
        raise HTTPException(status_code=401, detail="A user with this email or username already exists")

    hashed_pass = hashed_password(data.password)
    user = User(email=data.email, username=data.username,  password=hashed_pass)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def sign_jwt(user_id: str) -> dict:
    access_payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    refresh_payload = {
        "user_id": user_id,
        "expires": time.time() + 3600
    }

    access_token = jwt.encode(access_payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    refresh_token = jwt.encode(refresh_payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

    return token_response(access_token, refresh_token)


def login_user(data: Login, db: Session) -> dict:
    if data := check_user_data(data, db):
        return sign_jwt(data.id)
    raise HTTPException(detail="Incorrect login or password.", status_code=401)
