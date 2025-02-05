from fastapi import FastAPI
from database import engine
from models.book import Base
from routers import books

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include the books router
app.include_router(books.router)
