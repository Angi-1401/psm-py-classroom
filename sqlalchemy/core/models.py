from datetime import date
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

Base = declarative_base()

author_books_association = Table(
    "author_books",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.id")),
    Column("book_id", Integer, ForeignKey("books.id")),
)

publisher_books_association = Table(
    "publisher_books",
    Base.metadata,
    Column("publisher_id", Integer, ForeignKey("publishers.id")),
    Column("book_id", Integer, ForeignKey("books.id")),
)


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    birthday: Mapped[date] = mapped_column(nullable=True)
    deceased: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"<Author(id={self.id}, name={self.first_name} {self.last_name})>"


class Publisher(Base):
    __tablename__ = "publishers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __repr__(self):
        return f"<Publisher(id={self.id}, name={self.name})>"


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    authors: Mapped[list["Author"]] = relationship(
        "Author", secondary=author_books_association, backref="books"
    )
    publishers: Mapped[list["Publisher"]] = relationship(
        "Publisher", secondary=publisher_books_association, backref="books"
    )

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title})>"

