import json
import redis.asyncio as redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

async def get_books_from_cache():
    books = await r.get("books")
    if books:
        return json.loads(books)
    return None

async def set_books_to_cache(books):
    await r.set("books", json.dumps(books), ex=60)  # optional expiry
