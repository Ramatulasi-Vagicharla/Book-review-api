from fastapi import FastAPI
from app.routes import router
from app.db import Base, engine
app = FastAPI(
    title="Book Review API",
    description="A simple FastAPI service with Redis caching and SQLite DB",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)
app.include_router(router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Review API!"}

