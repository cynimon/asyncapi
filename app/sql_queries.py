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

# создание таблиц
tables_init = '''
create table if not exists devices
(
    id       bigserial    not null
        constraint devices_pk
            primary key,
    dev_id   varchar(200) not null,
    dev_type varchar(120) not null
);

alter table devices
    owner to postgres;

create index if not exists devices_dev_id_dev_type_index
    on devices (dev_id, dev_type);

create table if not exists endpoints
(
    id        bigserial not null
        constraint endpoints_pk
            primary key,
    device_id integer
        constraint endpoints_devices_id_fk
            references devices
            on update cascade on delete cascade,
    comment   text
);

alter table endpoints
    owner to postgres;
    '''

# удаление таблиц на shutdown
tables_drop = '''
DROP TABLE IF EXISTS endpoints;
DROP TABLE IF EXISTS devices;'''
