import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.models.base import BaseModel


class Book(BaseModel):
    __tablename__ = "books"
    __table_args__ = (
        {'extend_existing': True}
    )

    id = sa.Column(sa.Integer, primary_key=True, comment="ID книги")
    title = sa.Column(sa.String, nullable=False, comment="Название книги")

    authors = relationship("Author", secondary="book_authors", back_populates="book")


class Author(BaseModel):
    __tablename__ = "authors"
    __table_args__ = {"extend_existing": True}

    id = sa.Column(sa.Integer, primary_key=True, comment="ID автора")

    books = relationship("Book", secondary="book_authors", back_populates="author")


class BookAuthors(BaseModel):
    __tablename__ = "book_authors"
    __table_args__ = {"extend_existing": True}

    book_id = sa.Column(sa.Integer, primary_key=True, comment="ID книги")
    author_id = sa.Column(sa.Integer, primary_key=True, comment="ID автора")
