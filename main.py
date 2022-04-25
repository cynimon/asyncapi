from fastapi import FastAPI
import aioredis

app = FastAPI()


@app.on_event('startup')
async def startup_event():
    redis = aioredis.from_url("redis://localhost")
    await redis.set("my-key", "value")
    value = await redis.get("my-key")
    print(value)
    print('okay')
