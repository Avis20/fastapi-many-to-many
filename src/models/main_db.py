
from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.orm import relationship
from src.models.db import BaseModel

class Book(BaseModel):
    __tablename__ = "books"
    __table_args__ = (
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True, comment="ID книги")
    title = Column(String, nullable=False, comment="Заголовок книги")

    authors = relationship("Author", secondary="book_authors", back_populates="books")


class Author(BaseModel):
    __tablename__ = "authors"
    __table_args__ = (
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True, comment="ID автора")
    name = Column(String, comment="Название книги")

    books = relationship("Book")


class book_authors(BaseModel):
    __tablename__ = "book_authors"
    __table_args__ = (
        {"extend_existing": True}
    )

    book_id = Column(Integer, primary_key=True, comment="ID книги"),
    author_id = Column(Integer, primary_key=True, comment="ID автора"),

"""
# Table() класс - imperative style «императивный стиль»
book_authors = Table(
    'book_authors', BaseModel.metadata,
    Column('book_id', Integer, primary_key=True, comment="ID книги"),
    Column('author_id', Integer, primary_key=True, comment="ID автора"),
    __table_args__ = (
        {"extend_existing": True}
    )
)
"""

"""
class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = (
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
        sa.Index("username_uniq", "username", unique=True),
        {"extend_existing": True},
    )

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    username = sa.Column(sa.String(255), nullable=False)
    name = sa.Column(sa.String(255), nullable=True)
    last_name = sa.Column(sa.String(255), nullable=True)

    phones = relationship("PhoneNumber", back_populates="user")


class PhoneNumber(BaseModel):
    __tablename__ = "phone_numbers"
    __table_args__ = (
        {"extend_existing": True}
    )

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    number = sa.Column(sa.String(255), nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey(User.id), nullable=False)

    user = relationship("User", back_populates="phones")
"""