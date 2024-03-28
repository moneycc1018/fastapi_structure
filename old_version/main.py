from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_router
import config

app = FastAPI(title=config.APP_TITLE, description=config.APP_DESCRIPION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
