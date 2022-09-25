from sqlalchemy import create_engine
from sqlalchemy.orm import Session, joinedload

from src.settings import get_settings
from src.models import Book, Author

settings = get_settings()
engine = create_engine(settings.DATABASE_URL, echo=True)

def get_book():
    with Session(bind=engine) as session:
        # Выберем книгу с id == 1
        book1 = session.query(Book).\
            options(joinedload(Book.authors)).\
            where(Book.id == 3).one()
        print(book1.title)
        """
            SELECT
                books.id AS books_id,
                books.title AS books_title,
                authors_1.id AS authors_1_id,
                authors_1.name AS authors_1_name
            FROM books
            LEFT OUTER JOIN (
                book_authors AS book_authors_1
                JOIN authors AS authors_1
                    ON authors_1.id = book_authors_1.author_id)
                    ON books.id = book_authors_1.book_id
            WHERE books.id = %(id_1)s
        """
        for author in book1.authors:
            print("author =", author.name)

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
