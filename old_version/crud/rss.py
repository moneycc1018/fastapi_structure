from sqlalchemy.orm import Session
from models.rss_info import RssInfo


def query_rss_info(db: Session):
    return db.query(RssInfo).where(RssInfo.deprecated == False).all()
