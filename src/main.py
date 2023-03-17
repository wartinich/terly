from fastapi import FastAPI

from src.auth.routers import router as auth_router
from src.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
