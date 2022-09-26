# ./src/services/authors.py

from sqlalchemy.orm import Session, joinedload

from src.models.authors import Author


def get_author(author_id: int, db_session: Session) -> Author:
    db_author = (
        db_session.query(Author)
        .options(joinedload(Author.books))
        .where(Author.id == author_id)
        .first()
    )
    return db_author


def get_authors(db_session: Session) -> list[Author]:
    db_authors = db_session.query(Author).options(joinedload(Author.books)).all()
    return db_authors
