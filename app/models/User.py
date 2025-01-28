from app.database import Base, str_uniq
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class User(Base):
    __tablename__ = 'users'

    username: Mapped[str_uniq]
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
