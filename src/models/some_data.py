
from sqlalchemy.orm import Session
from .main_db import Book, Author, book_authors


def insert_data_to_db(engine):
    with Session(bind=engine) as session:
        book1 = Book(title="Убийство в восточном экспрессе")

        author1 = Author(name="Агата Кристи")
        book1.authors = [author1]

        session.add_all([book1, author1])


    
