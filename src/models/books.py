import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.models.main_db import BaseModel


class Book(BaseModel):
    __tablename__ = "books"

    id = sa.Column(sa.Integer, primary_key=True, comment="ID книги")
    title = sa.Column(sa.String, nullable=False, comment="Название книги")

    authors = relationship("Author", secondary="book_authors", back_populates="books")


class BookAuthors(BaseModel):
    __tablename__ = "book_authors"
    __table_args__ = (
        sa.PrimaryKeyConstraint(
            "book_id", "author_id",
            name="book_authors_pkey"
        ),
        sa.ForeignKeyConstraint(
            ["book_id"], ["books.id"],
            name="books_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["author_id"], ["authors.id"],
            name="authors_fkey"
        ),
    )

    book_id = sa.Column(sa.Integer, comment="ID книги")
    author_id = sa.Column(sa.Integer, comment="ID автора")
