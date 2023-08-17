from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router as api_router_v1
import config

app = FastAPI(title=config.APP_TITLE, description=config.APP_DESCRIPION)

app.add_middleware(CORSMiddleware,
                   allow_origins=config.ALLOW_ORIGINS,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# version1
v1 = APIRouter(prefix="/v1")
v1.include_router(api_router_v1)

app.include_router(v1, prefix="/api")
