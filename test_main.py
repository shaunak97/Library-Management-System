from fastapi.testclient import TestClient
from main import app, books, Book
import pytest

client = TestClient(app)

# Clear the books list before each test
@pytest.fixture(autouse=True)
def clear_books():
    books.clear()

def test_book_model():
    # Test if the Book model can be instantiated
    book = Book(id=1, title="1984", author="George Orwell", year=1949)
    assert book.id == 1
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.year == 1949

def test_create_book():
    response = client.post("/books/", json={
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    })
    assert response.status_code == 200
    data = response.json()
    assert data == {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }

def test_create_book_duplicate_id():
    client.post("/books/", json={
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    })  # First book
    response = client.post("/books/", json={
        "id": 1,
        "title": "Animal Farm",
        "author": "George Orwell",
        "year": 1945
    })  # Duplicate ID
    assert response.status_code == 400
    assert response.json() == {"detail": "Book with this ID already exists"}

def test_get_all_books():
    client.post("/books/", json={
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    })
    client.post("/books/", json={
        "id": 2,
        "title": "Animal Farm",
        "author": "George Orwell",
        "year": 1945
    })
    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0] == {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }
    assert data[1] == {
        "id": 2,
        "title": "Animal Farm",
        "author": "George Orwell",
        "year": 1945
    }

def test_get_book_by_id():
    client.post("/books/", json={
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    })
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data == {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }

def test_get_book_by_id_not_found():
    response = client.get("/books/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_update_book():
    # Add a book first
    client.post("/books/", json={
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    })
    # Update the book's details
    response = client.put("/books/1", json={
        "id": 1,
        "title": "Nineteen Eighty-Four",
        "author": "George Orwell",
        "year": 1949
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Nineteen Eighty-Four"  # Updated title
    assert data["author"] == "George Orwell"
    assert data["year"] == 1949

def test_update_book_not_found():
    # Try to update a book that doesn’t exist
    response = client.put("/books/99", json={
        "id": 99,
        "title": "Nonexistent Book",
        "author": "Unknown",
        "year": 2025
    })
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_delete_book():
    # Add a book first
    client.post("/books/", json={
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    })
    
    # Delete the book
    response = client.delete("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data == {"detail": "Book deleted successfully"}

    # Verify the book is deleted
    response = client.get("/books/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_delete_book_not_found():
    # Try to delete a book that doesn’t exist
    response = client.delete("/books/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}
