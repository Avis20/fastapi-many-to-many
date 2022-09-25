# ./src/models/authors.py

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.models.main_db import BaseModel


class Author(BaseModel):
    __tablename__ = "authors"

    id = sa.Column(sa.Integer, primary_key=True, comment="ID автора")
    name = sa.Column(sa.Text, nullable=False, comment="ФИО автора")

    # "Book" - Класс по которому происходит выборка
    # secondary="book_authors" - таблица (НЕ КЛАСС), в которой прописаны foreign связи
    # back_populates="authors" - название relation по которому можно обратно выбрать данные
    books = relationship("Book", secondary="book_authors", back_populates="authors")
