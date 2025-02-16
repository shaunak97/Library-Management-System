# Library Management System

## Overview
This is a **Library Management System** built using **FastAPI**, **PostgreSQL**. The system allows users to perform CRUD operations on books stored in a PostgreSQL database

## Features
- **Book Management**
  - Add books
  - Retrieve all books
  - Retrieve a specific book by ID
  - Update book details
  - Delete a book
- **Database Integration**
  - Uses **PostgreSQL** for structured book data
  

## Tech Stack
- **FastAPI**: Web framework
- **PostgreSQL**: Relational database
- **SQLAlchemy**: ORM for PostgreSQL
- **Uvicorn**: ASGI server
- **Docker**: Containerization


## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/shaunak97/Library-Management-System.git
cd Library-Management-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL
#### Using Docker
```bash
# Start PostgreSQL
docker run --name postgres-db -e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=sompura -e POSTGRES_DB=library_db \
-p 5432:5432 -d postgres

```

### 4. Run the FastAPI Application
```bash
uvicorn main:app --reload
```

### 5. Access API Documentation
Once the server is running, open:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints
### Books API (`/books/`)
| Method | Endpoint         | Description                |
|--------|-----------------|----------------------------|
| GET    | /books/         | Get all books              |
| POST   | /books/         | Add a new book             |
| GET    | /books/{book_id} | Get a book by ID          |
| PUT    | /books/{book_id} | Update book details       |
| DELETE | /books/{book_id} | Delete a book             |

## Running Tests
Run unit tests using `pytest`:
```bash
pytest
```


## License
This project is licensed under the **MIT License**.

## Author
- **Your Name** - [GitHub](https://github.com/your-username)

