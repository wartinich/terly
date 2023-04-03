from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.user.models import User
from src.user.schemas import UserUpdateDTO, UserDTO


def update_user(body: UserUpdateDTO, current_user: UserDTO, db: Session):
    user_id = current_user.id

    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")

    user.steam = body.steam
    user.discord = body.discord

    db.commit()
    db.refresh(user)

    return user
