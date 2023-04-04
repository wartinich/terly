from fastapi import FastAPI

from src.database import Base, engine

from src.auth.routers import router as auth_router
from src.user.routers import router as user_router
from src.assistance.routers import router as assistance_router
from src.category.routers import router as category_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(assistance_router)
app.include_router(category_router)
