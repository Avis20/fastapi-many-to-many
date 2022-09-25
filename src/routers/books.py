
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

import src.services.books as book_service
from src.models.main_db import get_db
from src.schemas.books import BookSchema

router = APIRouter()

@router.get(
    "/books/{book_id}",
    response_model=BookSchema,
    description="Информация о книги"
)
def get_book(book_id: int, db_session: Session = Depends(get_db)) -> BookSchema:
    return book_service.get_book(book_id, db_session)

@router.get(
    "/books/",
    response_model=list[BookSchema],
    description="Список книг"
)
def book_list(db_session: Session = Depends(get_db)):
    return book_service.get_books(db_session)
