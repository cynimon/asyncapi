from fastapi import FastAPI
import aioredis
import redis_func as rf
import asyncpg
import databases

DATABASE_URL = "postgresql://postgres:11qa@localhost:5432/devicess"
app = FastAPI()
database = databases.Database(DATABASE_URL)


@app.on_event("startup")
async def startup_event():
    redis_db = aioredis.from_url("redis://localhost", db=0, decode_responses=True)
    result = await rf.input_words(redis_db)
    await database.connect()
    print(result)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    await redis_db.ConnectionPool.disconnect()


@app.get("/")
async def ping_postgres():
    some = await database.fetch_all('SELECT * FROM devices')
    print(some)
