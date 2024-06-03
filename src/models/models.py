from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Text, Boolean, TIMESTAMP, func

from src.models.base_class import Base


class Users(Base):
    """
        Users Table Model
    """
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())


class Credentials(Base):
    """
        Credentials Table Model
    """
    credential_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())


class Projects(Base):
    """
        Projects Table Model
    """
    project_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())
