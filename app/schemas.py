# Pydantic models
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str

class ReviewCreate(BaseModel):
    content: str
    rating: int
