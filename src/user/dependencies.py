import jwt

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.user.token import JWTBearer
from src.database import get_db
from src.user.schemas import UserDTO, TokenPayload
from src.settings import settings
from src.user.models import User


async def get_current_user(token: str = Depends(JWTBearer()), db: Session = Depends(get_db)) -> UserDTO:
    payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    token_data = TokenPayload(**payload)

    user = db.query(User).get(token_data.user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return UserDTO.from_orm(user)
