
from sqlalchemy import create_engine

from src.models.main_db import BaseModel
from src.settings import get_settings

settings = get_settings()
engine = create_engine(settings.DATABASE_URL, echo=True)
BaseModel.metadata.create_all(engine)
