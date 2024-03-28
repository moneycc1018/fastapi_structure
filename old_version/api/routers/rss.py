from fastapi import APIRouter, Depends
from api.dependencies import get_db
from sqlalchemy.orm import Session
import crud.rss as crud
from schemas.rss import RssInfoResponse

router = APIRouter()


@router.get("/", response_model=list[RssInfoResponse])
async def get_rss_info(db: Session = Depends(get_db)):
    rss_info = crud.query_rss_info(db)

    return rss_info
