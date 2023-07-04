from typing import Union

from sqlalchemy import Column, Integer, String
from fastapi_sqlalchemy import db
from .base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)

    @classmethod
    def get_by_email(cls, email: str) -> Union["User", None]:
        """
        Get user by email

        Args:
            email: user email

        Returns:
            User
        """
        row = db.session.query(cls).filter(User.email == email).first()
        return row
