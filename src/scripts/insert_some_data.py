# ./src/scripts/insert_some_data.py

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.settings import get_settings
from src.models.books import Book, BookAuthors
from src.models.authors import Author

settings = get_settings()

engine = create_engine(settings.DATABASE_URL, echo=True)

with Session(bind=engine) as session:
    book1 = Book(title="Летос")
    book2 = Book(title="Крадущийся в тени")
    book3 = Book(title="No game no life")

    author1 = Author(name="Алексей Пехов")
    author2 = Author(name="Ю Камия")

    session.add_all([book1, book2, book3, author1, author2])
    session.commit()

    book_author1 = BookAuthors(
        book_id=book1.id,
        author_id=author1.id,
        description="Основной автор книги",
    )
    book_author2 = BookAuthors(
        book_id=book2.id,
        author_id=author1.id,
        description="Основной автор еще одной книги",
    )
    book_author3 = BookAuthors(
        book_id=book3.id,
        author_id=author1.id,
        description="Главный автор книги",
    )
    book_author4 = BookAuthors(
        book_id=book3.id,
        author_id=author2.id,
        description="Главный редактор книги",
    )
    session.add_all([book_author1, book_author2, book_author3, book_author4])
    session.commit()
