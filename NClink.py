from .Serial import *

class NClink:
    __loop=None
    __serial=None
    def __init__(self, baudrate=115200) -> None:
        __loop = asyncio.get_event_loop()
        __serial = serial_asyncio.create_serial_connection(loop, UAVSerial, 'COM1', baudrate=115200)
