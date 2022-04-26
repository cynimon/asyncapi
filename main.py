from fastapi import FastAPI
import aioredis
import redis_func as rf
import aiopg
import postgres_func as pf

app = FastAPI()


@app.get("/")
async def get_redis():
    redis_db = aioredis.from_url("redis://localhost", db=0, decode_responses=True)
    result = await rf.main_red(redis_db)
    await rf.output_answer(result)


@app.post("/", status_code=201)
async def post_postgres():
    await pf.devices_foo()


@app.get("/devices")
async def get_devices():
    result = await pf.endpointless()
    print(*result)
