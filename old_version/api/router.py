from fastapi import APIRouter
from api.routers import rss, user

api_router = APIRouter()
api_router.include_router(rss.router, prefix="/rss", tags=["Rss"])
api_router.include_router(user.router, prefix="/user", tags=["User"])
