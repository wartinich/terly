from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.user.schemas import UserDTO, UserUpdateDTO
from src.user.dependencies import get_current_user
from src.user.services import update_user

router = APIRouter(tags=["users"])


@router.get("/users/me", response_model=UserDTO)
async def user_profile(user: UserDTO = Depends(get_current_user)):
    return user


@router.patch("/users/me", response_model=UserUpdateDTO)
async def update_user_profile(
        body: UserUpdateDTO,
        current_user: UserDTO = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    result = update_user(body, current_user, db)
    return result
