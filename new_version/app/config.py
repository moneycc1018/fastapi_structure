import os

APP_TITLE = "FastAPI Structure"
APP_DESCRIPION = "FastAPI 架構"
ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "http://0.0.0.0:3000")
DATABASE_URL = "postgresql://admin:admin@localhost:1357/rss_db"
