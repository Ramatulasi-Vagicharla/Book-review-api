# 📚 Book Review Service – FastAPI + SQLite + Redis + Alembic

A small backend service to manage books and user reviews, built using **FastAPI**, **SQLAlchemy**, **Alembic**, **SQLite**, and **Redis**. Includes Swagger documentation, cache layer, and automated testing.

---

## 🚀 Features

- ✅ Add and view books
- ✅ Add and fetch reviews per book
- ✅ RESTful API with Swagger docs
- ✅ Data persisted using SQLAlchemy ORM and SQLite
- ✅ Redis cache on `GET /books`
- ✅ Alembic migrations for DB versioning
- ✅ Error handling with fallback from Redis
- ✅ Unit & integration tests (cache-miss path included)

---

## 🧱 Tech Stack

| Layer          | Tech                          |
|----------------|-------------------------------|
| Language       | Python 3.10+                  |
| Web Framework  | FastAPI                       |
| Database       | SQLite (or switch to PostgreSQL) |
| ORM            | SQLAlchemy                    |
| Caching        | Redis                         |
| Migrations     | Alembic                       |
| Testing        | Pytest                        |
| Docs           | OpenAPI/Swagger               |

---

## 📁 Folder Structure
book_review_service/
├── app/
│ ├── main.py # FastAPI app entry
│ ├── db.py # DB setup (engine, session, Base)
│ ├── models.py # SQLAlchemy models (Book, Review)
│ ├── routes.py # API endpoints
│ ├── cache.py # Redis setup
├── tests/ # Unit and integration tests
├── migrations/ # Alembic migrations
├── alembic.ini # Alembic config
├── requirements.txt # Python dependencies
└── README.md # This file

---

## 🛠️ Setup & Run Locally

### 1. 📦 Install Dependencies

pip install -r requirements.txt
### 2. 🔧 Run Alembic Migrations
alembic upgrade head

### 3. 🚀 Start FastAPI App
uvicorn app.main:app --reload
### 4. 🌐 Open in Browser
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

### 🧪 Run Tests
pytest
### 💾 Redis Integration
App uses Redis to cache book list on GET /books

If Redis is down, falls back to DB

Set Redis URL in .env or modify cache.py accordingly

### 🔄 Extend with GraphQL
To support real-time review updates:

Use GraphQL Subscriptions (e.g., via WebSockets)

Update schema to define newReviewAdded

Implement pub/sub logic using Redis or Kafka

Secure with authentication (JWT/session)

Scale via load balancing + event queue

### ✍️ Author
Rama Tulasi Vagicharla
Linkedin: https://www.linkedin.com/in/ramavagicharla/

Email: vagicharlaramatulasi@gmail.com

📘 License
MIT License
