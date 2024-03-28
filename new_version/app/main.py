from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.rss.router import router as rss_router
from app.user.router import router as user_router
from app import config

app = FastAPI(title=config.APP_TITLE, description=config.APP_DESCRIPION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rss_router, prefix="/rss", tags=["Rss"])
app.include_router(user_router, prefix="/user", tags=["User"])
