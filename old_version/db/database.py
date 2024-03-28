from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

engine = create_engine(config.DATABASE_URL, echo=True)
Session = sessionmaker(engine, expire_on_commit=False)
