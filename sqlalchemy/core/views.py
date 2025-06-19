import datetime

from db.connection import db_session
from core.controller import *
from core.models import Author, Publisher, Book


def create_author_view() -> None:
    """Create a new Author."""

    print("=== Create a New Author ===")

    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()

    birthday_str = input("Birthday (YYYY-MM-DD) [optional]: ").strip()
    if birthday_str:
        birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()
    else:
        birthday = datetime.date(1900, 1, 1)

    deceased_input = input("Is the author deceased? (y/n): ").strip().lower()
    deceased = deceased_input == "y"

    with db_session() as session:
        try:
            author = create_author(
                session,
                first_name=first_name,
                last_name=last_name,
                birthday=birthday,
                deceased=deceased,
            )
            print(f"✅ Author created: {author.first_name} {author.last_name}")
        except ValueError as e:
            print(f"❌ Error: {e}")


def create_publisher_view() -> None:
    """Create a new Publisher."""

    print("=== Create a New Publisher ===")

    name = input("Publisher name: ").strip()

    with db_session() as session:
        try:
            publisher = create_publisher(session, name)
            print(f"✅ Publisher created: {publisher.name}")
        except ValueError as e:
            print(f"❌ Error: {e}")


def create_book_view() -> None:
    """Create a new Book."""

    print("=== Create a New Book ===")

    title = input("Title: ").strip()

    author_ids_str = input("Associated author IDs (comma separated): ").strip()
    author_ids = [int(aid) for aid in author_ids_str.split(",") if aid]

    publisher_ids_str = input("Associated publisher IDs (comma separated): ").strip()
    publisher_ids = [int(pid) for pid in publisher_ids_str.split(",") if pid]

    with db_session() as session:
        authors = session.query(Author).filter(Author.id.in_(author_ids)).all()
        publishers = (
            session.query(Publisher).filter(Publisher.id.in_(publisher_ids)).all()
        )
        try:
            book = create_book(session, title, authors, publishers)
            print(f"✅ Book created: {book.title}")
        except ValueError as e:
            print(f"❌ Error: {e}")


def read_all_authors_view() -> None:
    """Display all authors."""

    with db_session() as session:
        authors = read_all_authors(session)
        print("=== All Authors ===")
        for author in authors:
            print(
                f"{author.id}: {author.first_name} {author.last_name} (Born: {author.birthday}, Deceased: {author.deceased})"
            )


def read_all_publishers_view() -> None:
    """Display all publishers."""

    print("=== All Publishers ===")

    with db_session() as session:
        publishers = read_all_publishers(session)
        for publisher in publishers:
            print(f"{publisher.id}: {publisher.name}")


def read_all_books_view() -> None:
    """Display all books."""

    print("=== All Books ===")

    with db_session() as session:
        books = read_all_books(session)
        for book in books:
            author_names = ", ".join(
                [f"{a.first_name} {a.last_name}" for a in book.authors]
            )
            publisher_names = ", ".join([p.name for p in book.publishers])
            print(
                f"{book.id}: {book.title} | Authors: {author_names} | Publishers: {publisher_names}"
            )


def read_author_by_id_view() -> None:
    """Display an author by ID."""

    print("=== Display Author by ID ===")

    author_id = int(input("Author ID: ").strip())
    with db_session() as session:
        author = read_author_by_id(session, author_id)
        if author:
            print(
                f"{author.id}: {author.first_name} {author.last_name} (Born: {author.birthday}, Deceased: {author.deceased})"
            )
        else:
            print("❌ Author not found.")


def read_publisher_by_id_view() -> None:
    """Display a publisher by ID."""

    print("=== Display Publisher by ID ===")

    publisher_id = int(input("Publisher ID: ").strip())
    with db_session() as session:
        publisher = read_publisher_by_id(session, publisher_id)
        if publisher:
            print(f"{publisher.id}: {publisher.name}")
        else:
            print("❌ Publisher not found.")


def read_book_by_id_view() -> None:
    """Display a book by ID."""

    print("=== Display Book by ID ===")

    book_id = int(input("Book ID: ").strip())
    with db_session() as session:
        book = read_book_by_id(session, book_id)
        if book:
            author_names = ", ".join(
                [f"{a.first_name} {a.last_name}" for a in book.authors]
            )
            publisher_names = ", ".join([p.name for p in book.publishers])
            print(
                f"{book.id}: {book.title} | Authors: {author_names} | Publishers: {publisher_names}"
            )
        else:
            print("❌ Book not found.")


def update_author_view() -> None:
    """Update an existing Author."""

    print("=== Update an existing Author ===")

    author_id = int(input("Author ID to update: ").strip())
    with db_session() as session:
        try:
            if not read_author_by_id(session, author_id):
                print("❌ Error: The given ID doesn't match any Author.")
                return

            first_name = input("New first name: ").strip()
            last_name = input("New last name: ").strip()
            birthday_str = input("New birthday (YYYY-MM-DD): ").strip()
            birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()
            deceased_input = input("Is the author deceased? (y/n): ").strip().lower()
            deceased = deceased_input == "y"

            author = update_author(
                session, author_id, first_name, last_name, birthday, deceased
            )
            print(f"✅ Author updated: {author.first_name} {author.last_name}")
        except ValueError as e:
            print(f"❌ Error: {e}")


def update_publisher_view() -> None:
    """Update an existing Publisher."""

    print("=== Update an existing Publisher ===")

    publisher_id = int(input("Publisher ID to update: ").strip())
    with db_session() as session:
        try:
            if not read_publisher_by_id(session, publisher_id):
                print("❌ Error: The given ID doesn't match any Publisher.")
                return

            name = input("New publisher name: ").strip()

            publisher = update_publisher(session, publisher_id, name)
            print(f"✅ Publisher updated: {publisher.name}")
        except ValueError as e:
            print(f"❌ Error: {e}")


def update_book_view() -> None:
    """Update an existing Book."""

    print("=== Update an existing Book ===")

    book_id = int(input("Book ID to update: ").strip())
    with db_session() as session:
        try:
            if not read_publisher_by_id(session, book_id):
                print("❌ Error: The given ID doesn't match any Book.")
                return

            title = input("New title: ").strip()
            author_ids_str = input(
                "New associated author IDs (comma separated): "
            ).strip()
            author_ids = [int(aid) for aid in author_ids_str.split(",") if aid]
            publisher_ids_str = input(
                "New associated publisher IDs (comma separated): "
            ).strip()
            publisher_ids = [int(pid) for pid in publisher_ids_str.split(",") if pid]

            authors = session.query(Author).filter(Author.id.in_(author_ids)).all()
            publishers = (
                session.query(Publisher).filter(Publisher.id.in_(publisher_ids)).all()
            )

            book = update_book(session, book_id, title, authors, publishers)
            print(f"✅ Book updated: {book.title}")
        except ValueError as e:
            print(f"❌ Error: {e}")


def delete_author_view() -> None:
    """Delete an Author."""

    print("=== Delete an Author ===")

    author_id = int(input("Author ID to delete: ").strip())
    with db_session() as session:
        try:
            delete_author(session, author_id)
            print("✅ Author deleted.")
        except ValueError as e:
            print(f"❌ Error: {e}")


def delete_publisher_view() -> None:
    """Delete a Publisher."""

    print("=== Delete a Publisher ===")

    publisher_id = int(input("Publisher ID to delete: ").strip())
    with db_session() as session:
        try:
            delete_publisher(session, publisher_id)
            print("✅ Publisher deleted.")
        except ValueError as e:
            print(f"❌ Error: {e}")


def delete_book_view() -> None:
    """Delete a Book."""

    book_id = int(input("Book ID to delete: ").strip())
    with db_session() as session:
        try:
            delete_book(session, book_id)
            print("✅ Book deleted.")
        except ValueError as e:
            print(f"❌ Error: {e}")
