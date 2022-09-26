# ./src/schemas/authors.py

from pydantic import BaseModel


class AuthorBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


from src.schemas.books import BookBase


class AuthorSchema(AuthorBase):
    books: list[BookBase]
