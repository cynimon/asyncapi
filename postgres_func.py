import aiopg
import sql_queries as s
import random as rd
from prettytable import PrettyTable


# обработка запросов в БД
async def handle_queries(querie):
    conn = await aiopg.connect(database='devicess', user='postgres', password='11qa', host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute(querie)
    ret = await cur.fetchall()
    await conn.close()
    return ret


# добавление данных в бд
async def insert_queries(querie, data=None):
    conn = await aiopg.connect(database='devicess', user='postgres', password='11qa', host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute(querie, data)
    await conn.close()


# привязка endpoint-ов
async def add_endpoints():
    ret = await handle_queries(s.count_devs)
    devs = rd.sample(range(1, ret[0][0]), 5)
    data = list(map(lambda x: (x, f'/dev{x}'), devs))
    for dt in data:
        await insert_queries(s.new_endpoints, dt)


# генерация имен девайсов
def random_devs():
    name = ''.join([hex(rd.randint(0, 255))[2:] for _ in range(6)])
    d_type = rd.choice(('emeter', 'zigbee', 'lora', 'gsm'))
    return name, d_type


# создание новых девайсов
def making_devices():
    data = [random_devs() for _ in range(10)]
    return data


# добавление новых девайсов
async def devices_foo():
    data = making_devices()
    for dt in data:
        await insert_queries(s.new_devices, dt)
    await add_endpoints()


# создание таблицы вывода данных
def making_table(data):
    x = PrettyTable()
    x.field_names = ["dev_type", "amount"]
    for dt in data:
        x.add_row([dt[1], dt[0]])
    x.align = "l"
    return x


# вывод девайсов без endoints
async def endpointless():
    table_data = await handle_queries(s.endpoindless)
    result = making_table(table_data)
    return result
