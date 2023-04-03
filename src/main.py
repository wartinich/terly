from fastapi import FastAPI

from src.database import Base, engine

from src.auth.routers import router as auth_router
from src.user.routers import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(user_router)
