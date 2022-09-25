

from fastapi import Depends
from sqlalchemy.orm import Session, joinedload

from src.schemas.books import BookSchema
from src.models.books import Book

def get_book(book_id: int, db_session: Session) -> BookSchema:
    db_book = (
        db_session.query(Book)
        # .options(joinedload(Book.authors))
        .where(Book.id == book_id)
        .first()
    )
    return db_book

def get_books(db_session: Session) -> list[BookSchema]:
    db_books = (
        db_session.query(Book)
        .options(joinedload(Book.authors))
        .all()
    )
    return db_books
