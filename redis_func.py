async def input_words(redis_db):
    first = input('Input first: ')
    second = input('Input second: ')
    is_anagramm = False
    if first == second[::-1]:
        await redis_db.incr("counter")
        is_anagramm = True
    count = await redis_db.get("counter")
    if count is None:
        count = 0
    answer = {
        "is_anagramm": is_anagramm,
        "counter": count
    }
    return answer
