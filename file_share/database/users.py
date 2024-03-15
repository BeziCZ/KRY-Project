from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BLOB
from .base import Base


class Users(Base):
    __tablename__ = "users"
    # Storage of users and their cert files
    name: Mapped[str] = mapped_column(primary_key=True)
    cert_file: Mapped[bytes] = mapped_column(BLOB)