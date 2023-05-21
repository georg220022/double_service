from typing import Any

from sqlalchemy import UUID, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import UUID as uid

Base: Any = declarative_base()


class User(Base):
    __tablename__ = "user"

    id: Mapped[uid] = mapped_column(UUID, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    token: Mapped[str] = mapped_column(String)


user_ = User.__table__


class UserFiles(Base):
    __tablename__ = "user_files"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[uid] = mapped_column(ForeignKey("user.id"))
    file_path: Mapped[str] = mapped_column(String)


user_file_ = UserFiles.__table__
