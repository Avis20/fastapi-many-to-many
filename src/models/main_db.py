
import sys
import logging
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from src.settings import get_settings

settings = get_settings()

if settings.ECHO_DB:
    logger = logging.StreamHandler(sys.stdout)
    logger_sa = logging.getLogger("sqlalchemy")
    logger_sa.setLevel(logging.INFO)
    logger_sa.addHandler(logger)

engine = sa.create_engine(settings.DATABASE_URL, echo=True)
metadata = sa.MetaData()
BaseModel = declarative_base(metadata=metadata)

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
