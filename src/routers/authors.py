# ./src/routers/authors.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models.main_db import get_db
from src.schemas.authors import AuthorSchema
import src.services.authors as author_services

router = APIRouter()


@router.get(
    "/authors/{author_id}",
    response_model=AuthorSchema,
    description="Информация об авторе",
)
def get_author(author_id: int, db_session: Session = Depends(get_db)):
    return author_services.get_author(author_id, db_session)


@router.get(
    "/authors/",
    response_model=list[AuthorSchema],
    description="Список авторов"
)
def author_list(db_session: Session = Depends(get_db)):
    return author_services.get_authors(db_session)
