from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import Base
from pydantic import EmailStr


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(200), index=True)
    email: Mapped[EmailStr] = mapped_column(String(200), index=True, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
