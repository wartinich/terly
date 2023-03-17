import os

from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()


class Setting(BaseConfig):
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    JWT_SECRET: str = os.environ.get("JWT_SECRET")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM")


settings = Setting()
