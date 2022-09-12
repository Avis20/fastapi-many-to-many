
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base

from src.settings import get_settings

settings = get_settings()
engine = create_engine(
    settings.DATABASE_URL,
    echo=True, future=True
)

metadata = MetaData()
BaseModel = declarative_base(metadata=metadata)
