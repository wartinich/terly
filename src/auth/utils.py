import bcrypt
from sqlalchemy.orm import Session

from src.auth.schemas import Login
from src.user.models import User


def encode_pass(password: str) -> bytes:
    return bytes(password, encoding="utf-8")


def hashed_password(password: str) -> str:
    encode_password = encode_pass(password)
    hashed_pass = bcrypt.hashpw(encode_password, bcrypt.gensalt())
    return hashed_pass.decode()


def check_user_data(data: Login, db: Session) -> dict:
    if data.email_or_username.__contains__("@"):
        user = db.query(User).filter(User.email == data.email_or_username).first()
    else:
        user = db.query(User).filter(User.username == data.email_or_username).first()

    if user:
        password = encode_pass(data.password)
        return user if bcrypt.checkpw(password, encode_pass(user.password)) else {}
    else:
        return {}


def token_response(access_token: str, refresh_token: str) -> dict:
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
