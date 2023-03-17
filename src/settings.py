from pydantic import BaseConfig

class Setting(BaseConfig):
    DATABASE_URL: str = "sqlite:///./portal.db"


settings = Setting()
