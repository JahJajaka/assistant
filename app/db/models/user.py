import bcrypt
from sqlalchemy.orm import Mapped
from .base import Base, BaseMixin
from sqlalchemy import Column, String, Integer


class User(Base, BaseMixin):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = Column(String, unique=True, index=True)
    password: Mapped[str] = Column(String)

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

    def set_password(self, password: str):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
