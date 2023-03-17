from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.schemas import Token, UserCreate, Login
from src.auth.services import create_user, sign_jwt, login_user
from src.database import get_db

router = APIRouter(tags=["auth"])


@router.post("/register", response_model=Token)
async def register(body: UserCreate, db: Session = Depends(get_db)):
    result = create_user(body, db)
    return sign_jwt(result.id)


@router.post("/login", response_model=Token)
async def login(body: Login, db: Session = Depends(get_db)):
    result = login_user(body, db)
    return result
