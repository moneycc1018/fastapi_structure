from fastapi import APIRouter
from app.rss import service
from app.rss.schemas import RssInfoResponse

router = APIRouter()


@router.get("/", response_model=list[RssInfoResponse])
async def get_rss_info():
    rss_info = service.query_rss_info()

    return rss_info
