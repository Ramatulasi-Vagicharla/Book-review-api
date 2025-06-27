from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Book, Review
from app.schemas import BookCreate, ReviewCreate
from app.cache import get_books_from_cache, set_books_to_cache

router = APIRouter()

@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    # redis logic
    books = get_books_from_cache()
    if books:
        return books
    books = db.query(Book).all()
    set_books_to_cache(books)
    return books

@router.post("/books")
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/books/{book_id}/reviews")
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return db.query(Review).filter(Review.book_id == book_id).all()

@router.post("/books/{book_id}/reviews")
def add_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    db_review = Review(book_id=book_id, rating=review.rating, comment=review.comment)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
