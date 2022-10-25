from .Serial import *

class NClink:
    _loop=None
    _serial=None
    def __init__(self, baudrate=115200) -> None:
        self._loop = asyncio.get_event_loop()
        self._serial = serial_asyncio.create_serial_connection(loop, UAVSerial, 'COM1', baudrate=115200)
