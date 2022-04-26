import random as rd
import aiopg
import sql_queries as s
import asyncio


# обработка запросов в БД
async def handle_queries(querie, data=None):
    conn = await aiopg.connect(database='devicess', user='postgres', password='11qa', host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute(querie, data)
    ret = await cur.fetchall()
    await conn.close()
    return ret


def random_devs():
    name = ''.join([hex(rd.randint(0, 255))[2:] for _ in range(6)])
    type = rd.choice(('emeter', 'zigbee', 'lora', 'gsm'))
    return name, type


def making_devices():
    data = [random_devs() for _ in range(10)]
    return data


def add_endpoints():
    'select count(*) from devices'
    devs = rd.sample(range(1, 10), 5)
    data = list(map(lambda x: (x, f'/dev{x}'), devs))
    return data


async def main():
    ret = await handle_queries(s.count_devs)
    print(ret)

asyncio.run(main())