from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR, TIMESTAMP, TEXT
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(50))
    age: Mapped[int] = mapped_column(INTEGER, nullable=True)
    subscription: Mapped[str] = mapped_column(TEXT, nullable=True)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now())
    update_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now())
