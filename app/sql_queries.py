# список всех устройств, которые не привязаны к endpoint
endpoindless = '''SELECT count(*), dev_type 
FROM devices LEFT JOIN endpoints ON devices.id = endpoints.device_id 
WHERE device_id IS NULL GROUP BY dev_type'''

# подсчет количества девайсов
count_devs = 'SELECT count(*) FROM devices'

# добавление новых девайсов
new_devices = 'INSERT INTO devices(dev_id, dev_type) VALUES (%s, %s)'

# привязка endpoints
new_endpoints = 'INSERT INTO endpoints(device_id, comment) VALUES (%s, %s)'
