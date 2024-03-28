from sqlalchemy.dialects.postgresql import (
    INTEGER,
    VARCHAR,
    BOOLEAN,
    TIMESTAMP,
)
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass


class RssInfo(Base):
    __tablename__ = "rss_info"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    source_id: Mapped[str] = mapped_column(VARCHAR(10))
    source_name: Mapped[str] = mapped_column(VARCHAR(50))
    price: Mapped[int] = mapped_column(INTEGER, default=0)
    rss_url: Mapped[str] = mapped_column(VARCHAR(150))
    source_url: Mapped[str] = mapped_column(VARCHAR(150))
    logo_url: Mapped[str] = mapped_column(VARCHAR(150), nullable=True)
    deprecated: Mapped[bool] = mapped_column(BOOLEAN)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now())
    update_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now())
    category: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
