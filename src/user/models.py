from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    steam = Column(String, nullable=True)
    discord = Column(String, nullable=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    data_joined = Column(DateTime, default=datetime.now())
