# ./src/schemas/books.py

from pydantic import BaseModel


class BookBase(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


from src.schemas.authors import AuthorBase


class BookSchema(BookBase):
    authors: list[AuthorBase]
