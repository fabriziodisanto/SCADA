import random

from pyModbusTCP.server import ModbusServer
from pyModbusTCP.client import ModbusClient
from pyModbusTCP.utils import encode_ieee, decode_ieee, long_list_to_word, word_list_to_long

HOST = "localhost"
PORT = 12345


def get_plc_server():
    return ModbusServer(HOST, PORT, no_block=True)


def get_plc_client():
    return ModbusClient(host=HOST, port=PORT, auto_open=True, auto_close=True)


def read_floats(plc, address, len=1):
    """Read float(s) with read holding registers."""
    reg_l = plc.read_holding_registers(address, len * 2)
    if reg_l:
        return [decode_ieee(f) for f in word_list_to_long(reg_l)]
    else:
        return None


def write_floats(plc, address, floats_list):
    """Write float(s) with write multiple registers."""
    b32_l = [encode_ieee(f) for f in floats_list]

    b16_l = long_list_to_word(b32_l)
    return plc.write_multiple_registers(address, b16_l)


def generate_random_numbers(size):
    global random_values
    random_values = []
    for i in range(size):
        random_values.append(random.normalvariate(mu=0, sigma=1))
    return random_values
