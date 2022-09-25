# ./src/scripts/serializing_some_data.py

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, joinedload

from src.settings import get_settings
from src.models import Book, Author
from src.schemas.books import BookSchema

settings = get_settings()
engine = create_engine(settings.DATABASE_URL, echo=True)

def get_book():
    with Session(bind=engine) as session:
        # Выберем книгу с id == 1
        book1 = (
            session.query(Book)
            .options(joinedload(Book.authors))
            .where(Book.id == 3)
            .first()
        )
        print(book1.id)
        b1_schema = BookSchema.from_orm(book1)
        print(b1_schema.json(ensure_ascii=False))
        """
        {
          "id": 3,
          "title": "No game no life",
          "authors": [
            {
              "id": 2,
              "name": "Ю Камия"
            },
            {
              "id": 1,
              "name": "Алексей Пехов"
            }
          ]
        }
        """

def get_author():
    with Session(bind=engine) as session:
        # Выберем автора с книгами
        author1 = (
            session.query(Author).
            options(joinedload(Author.books)).
            where(Author.id == 1).one()
        )
        print(author1.name)
        for book in author1.books:
            print("book", book.title)

if __name__ == '__main__':
    get_author()
