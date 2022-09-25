# ./src/schemas/authors.py

from pydantic import BaseModel

class AuthorBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# TODO: циклический импорт...
# from src.schemas import BookSchema
# class AuthorSchema(AuthorBase):
#     books: list[BookSchema]
