from fastapi import FastAPI
import asyncpg

DATABASE_URL = "postgresql://postgres:11qa@localhost:5432/devicess"
global database


async def connection():
    database = await asyncpg.connect(DATABASE_URL)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await connection()
    print('sucess')

@app.on_event("shutdown")
async def shutdown():
    database.close()
