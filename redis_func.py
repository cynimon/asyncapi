async def main_red(redis_db):
    first = input("Input first: ")
    second = input("Input second: ")
    is_anagramm = "No"
    if first == second[::-1]:
        await redis_db.incr("counter")
        is_anagramm = "Yes"
    count = await redis_db.get("counter")
    return is_anagramm, count


async def output_answer(answer):
    anagramm, counter = answer
    if counter is None:
        counter = 0
    return {"is_anagramm": anagramm, "counter": counter}
