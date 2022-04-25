from fastapi import FastAPI
import aioredis

app = FastAPI()


async def input_words(redis):
    first = input('Input first: ')
    second = input('Input second: ')
    is_anagramm = False
    if first == second[::-1]:
        await redis.incr("counter")
        is_anagramm = True
    count = await redis.get("counter")
    if count is None:
        count = 0
    answer = {
        "is_anagramm": is_anagramm,
        "counter": count
    }
    return answer


@app.on_event('startup')
async def startup_event():
    redis = aioredis.from_url("redis://localhost", db=0, decode_responses=True)
    result = await input_words(redis)
    print(result)
