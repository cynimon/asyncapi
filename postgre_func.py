from fastapi import FastAPI
import asyncpg


global database


async def connection():
    database = await asyncpg.connect(DATABASE_URL)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await connection()
    print('success')

@app.on_event("shutdown")
async def shutdown():
    database.close()
