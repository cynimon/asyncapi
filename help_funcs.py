import random as rd
from string import ascii_letters as al

mac_addr = ''.join([hex(rd.randint(0, 255))[2:] for _ in range(6)])

dev_id = rd.choice(('emeter', 'zigbee', 'lora', 'gsm'))


