import aiopg
import sql_queries as s
import random as rd


# обработка запросов в БД
async def handle_queries(querie, data=None):
    conn = await aiopg.connect(database='devicess', user='postgres', password='11qa', host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute(querie, data)
    ret = await cur.fetchall()
    await conn.close()
    return ret


# привязка endpoint-ов
async def add_endpoints():
    ret = await handle_queries(s.count_devs)
    devs = rd.sample(range(1, ret[0][0]), 5)
    data = list(map(lambda x: (x, f'/dev{x}'), devs))
    await handle_queries(s.new_endpoints, data)


# генерация имен девайсов
def random_devs():
    name = ''.join([hex(rd.randint(0, 255))[2:] for _ in range(6)])
    type = rd.choice(('emeter', 'zigbee', 'lora', 'gsm'))
    return name, type


# создание новых девайсов
def making_devices():
    data = [random_devs() for _ in range(10)]
    return data


# добавление новых девайсов
async def devices_foo():
    data = making_devices()
    await handle_queries(s.new_devices, data)
    await add_endpoints()


# вывод девайсов без endoints
async def endpointless():
    result = await handle_queries(s.endpoindless)
    return result
