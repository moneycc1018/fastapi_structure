from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api import api_router

app = FastAPI(title="FastAPI Structure", description="FastAPI公版架構")

origins = ["http://0.0.0.0:3333"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(api_router, prefix="/api")