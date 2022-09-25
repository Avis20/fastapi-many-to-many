# ./src/schemas/books.py

from pydantic import BaseModel
from src.schemas.authors import AuthorBase

class BookBase(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class BookSchema(BookBase):
    authors: list[AuthorBase]
