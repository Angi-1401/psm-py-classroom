# SQLAlchemy Library CRUD Project

This project is a command-line CRUD (Create, Read, Update, Delete) application for managing a library database using Python, SQLite, and SQLAlchemy ORM.

## Features

- Manage Authors, Publishers, and Books
- Many-to-many relationships between Books and Authors/Publishers
- Interactive menu for all CRUD operations
- Data persistence with SQLite
- Sample data provided in [db/sample-data.csv](db/sample-data.csv)

## Project Structure

```
sqlalchemy/
│
├── main.py                # Entry point for the CLI application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── core/
│   ├── controller.py      # CRUD logic for models
│   ├── models.py          # SQLAlchemy ORM models
│   └── views.py           # User interface functions
│
└── db/
    ├── connection.py      # Database connection and session management
    └── sample-data.csv    # Example data for import
```

## Getting Started

1. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Run the application:**

   ```sh
   python main.py
   ```

3. **Follow the on-screen menu to manage authors, publishers, and books.**

## Notes

- The database file (`db.sqlite`) will be created automatically in the project directory.
- You can modify or extend the models and views as needed for your use case.

## License

This project is for educational purposes.