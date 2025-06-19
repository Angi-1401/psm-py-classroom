from sqlalchemy.orm import Session
from datetime import date

from core.models import Author, Publisher, Book


def create_author(
    session: Session,
    first_name: str,
    last_name: str,
    birthday: date = date(1900, 1, 1),
    deceased: bool = False,
) -> Author:
    """Create a new Author object and add it to the database."""

    existing = (
        session.query(Author)
        .filter_by(first_name=first_name, last_name=last_name, birthday=birthday)
        .first()
    )
    if existing:
        raise ValueError("Author already exists.")

    new_author = Author(
        first_name=first_name,
        last_name=last_name,
        birthday=birthday,
        deceased=deceased,
    )

    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author


def create_publisher(session: Session, name: str) -> Publisher:
    """Create a new Publisher object and add it to the database."""

    existing = session.query(Publisher).filter_by(name=name).first()
    if existing:
        raise ValueError("Publisher already exists.")

    new_publisher = Publisher(name=name)

    session.add(new_publisher)
    session.commit()
    session.refresh(new_publisher)
    return new_publisher


def create_book(
    session: Session, title: str, authors: list[Author], publishers: list[Publisher]
) -> Book:
    """Create a new Book object and add it to the database."""

    existing = session.query(Book).filter_by(title=title).first()
    if existing:
        raise ValueError("Book already exists.")

    new_book = Book(title=title, authors=authors, publishers=publishers)

    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book


def read_all_authors(session: Session) -> list[Author]:
    """Get a list of all Author objects in the database."""

    return session.query(Author).all()


def read_all_publishers(session: Session) -> list[Publisher]:
    """Get a list of all Publisher objects in the database."""

    return session.query(Publisher).all()


def read_all_books(session: Session) -> list[Book]:
    """Get a list of all Book objects in the database."""

    return session.query(Book).all()


def read_author_by_id(session: Session, author_id: int) -> Author:
    """Get an Author object by ID from the ones in the database."""

    return session.get(Author, author_id)


def read_publisher_by_id(session: Session, publisher_id: int) -> Publisher:
    """Get a Publisher object by ID from the ones in the database."""

    return session.get(Publisher, publisher_id)


def read_book_by_id(session: Session, book_id: int) -> Book:
    """Get a Book object by ID from the ones in the database."""

    return session.get(Book, book_id)


def delete_author(session: Session, author_id: int) -> None:
    """Delete an Author object from the database."""

    if not read_author_by_id(session, author_id):
        raise ValueError("The given ID doesn't match any author.")

    session.query(Author).filter_by(id=author_id).delete()
    session.commit()


def delete_publisher(session: Session, publisher_id: int) -> None:
    """Delete a Publisher object form the database"""

    if not read_publisher_by_id(session, publisher_id):
        raise ValueError("The given ID doesn't match any publisher.")

    session.query(Publisher).filter_by(id=publisher_id).delete()
    session.commit()


def delete_book(session: Session, book_id: int) -> None:
    """Delete a Book object from the database."""

    if not read_book_by_id(session, book_id):
        raise ValueError("The given ID doesn't match any book.")

    session.query(Book).filter_by(id=book_id).delete()
    session.commit()


def update_author(
    session: Session,
    author_id: int,
    first_name: str,
    last_name: str,
    birthday: date = date(1900, 1, 1),
    deceased: bool = False,
) -> Author:
    author = read_author_by_id(session, author_id)
    if not author:
        raise ValueError("The given ID doesn't match any author.")

    author.first_name = first_name
    author.last_name = last_name
    author.birthday = birthday
    author.deceased = deceased

    session.commit()
    session.refresh(author)
    return author


def update_publisher(session: Session, publisher_id: int, name: str) -> Publisher:
    """Update a Publisher object in the database."""

    publisher = read_publisher_by_id(session, publisher_id)
    if not publisher:
        raise ValueError("The given ID doesn't match any publisher.")

    publisher.name = name

    session.commit()
    session.refresh(publisher)
    return publisher


def update_book(
    session: Session,
    book_id: int,
    title: str,
    authors: list[Author],
    publishers: list[Publisher],
) -> Book:
    """Update a Book object in the database."""

    book = read_book_by_id(session, book_id)
    if not book:
        raise ValueError("The given ID doesn't match any book.")

    book.title = title
    book.authors = authors
    book.publishers = publishers

    session.commit()
    session.refresh(book)
    return book
