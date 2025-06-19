import os
import time

from db.connection import engine
from core.models import Base
from core.views import *

OPT = {
    "1": create_author_view,
    "2": create_publisher_view,
    "3": create_book_view,
    "4": read_all_authors_view,
    "5": read_all_publishers_view,
    "6": read_all_books_view,
    "7": read_author_by_id_view,
    "8": read_publisher_by_id_view,
    "9": read_book_by_id_view,
    "10": update_author_view,
    "11": update_publisher_view,
    "12": update_book_view,
    "13": delete_author_view,
    "14": delete_publisher_view,
    "15": delete_book_view,
}


def wait_and_clear(s: int) -> None:
    time.sleep(s)
    os.system("cls")


def main():
    """Main function."""

    while True:
        print("=== CRUD Library with Python, SQLite3 & SQLAlchemy ===\n")
        print("1. Create a new Author")
        print("2. Create a new Publisher")
        print("3. Create a new Book")
        print("4. Read all Authors")
        print("5. Read all Publishers")
        print("6. Read all Books")
        print("7. Read Author by ID")
        print("8. Read Publisher by ID")
        print("9. Read Book by ID")
        print("10. Update an existing Author")
        print("11. Update an existing Publisher")
        print("12. Update an existing Book")
        print("13. Delete an existing Author")
        print("14. Delete an existing Publisher")
        print("15. Delete an existing Book")
        print("0. Exit")
        opt = input("\nSelect an option: ").strip()

        if opt == "0":
            break
        elif opt in OPT:
            wait_and_clear(0)
            OPT[opt]()
            if int(opt) >= 4:
                input("\nPress any key to continue...")
                wait_and_clear(0)
            else:
                wait_and_clear(1)
        else:
            print("❌ Invalid option.")
            wait_and_clear(1)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    main()
