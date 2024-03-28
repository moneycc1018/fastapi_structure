from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from app.rss.models import RssInfo
from app.database import Session


def query_rss_info():
    with Session() as session:
        stmt = select(RssInfo).where(RssInfo.deprecated == False)
        result = session.scalars(stmt).all()

    return result
