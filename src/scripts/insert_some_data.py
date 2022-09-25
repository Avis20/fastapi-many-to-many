# ./src/scripts/insert_some_data.py

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.settings import get_settings
from src.models.books import Book
from src.models.authors import Author

settings = get_settings()

engine = create_engine(settings.DATABASE_URL, echo=True)

with Session(bind=engine) as session:
    book1 = Book(title="Летос")
    book2 = Book(title="Крадущийся в тени")
    book3 = Book(title="No game no life")

    author1 = Author(name="Алексей Пехов")
    author2 = Author(name="Ю Камия")

    book1.authors = [author1]
    book2.authors = [author1]
    book3.authors = [author1, author2]
    session.add_all([book1, book2, book3, author1, author2])

    # session.add_all([book1])
    session.commit()
