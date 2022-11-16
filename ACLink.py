import asyncio
import serial_asyncio

class AClink(asyncio.Protocol):
    _loop = None
    _serial = None
    
    def __init__(self, loop, UAVSerial, port = 'COM1', baudrate=115200, *args, **kwargs) -> None:
        self._loop = asyncio.get_event_loop()
        self._serial = serial_asyncio.create_serial_connection(loop, UAVSerial, port, baudrate)
    
    def move(x,y,yaw):
        a = 'M'
        a += x
        a += y
        a += yaw
        self.send(self, message=b"hello")
        
    
    def send_order(ser_input, the_order, number, number1, number2):
        ser_input.write(the_order.encode("gbk"))
        ser_input.write([int(number)])
        ser_input.write([int(number1)])
        ser_input.write([int(number2)])
        print(the_order, int(number), int(number1), int(number2))
    
    def connection_made(self, transport):
        """Called when a connection is made.

        The argument is the transport representing the pipe connection.
        To receive data, wait for data_received() calls.
        When the connection is closed, connection_lost() is called.
        
        Store the serial transport and prepare to receive data.
        """
        self.transport = transport
        self.buf = bytes()
        self.msgs_recvd = 0
        print('Reader connection created')

        asyncio.ensure_future(self.send())
        print('Writer connection created')

    def data_received(self, data):
        """Called when some data is received.

        The argument is a bytes object.
        
        Store characters until a newline is received.
        """
        self.buf += data

        if b'\n' in self.buf:
            lines = self.buf.split(b'\n')
            self.buf = lines[-1]  # whatever was left over
            for line in lines[:-1]:
                print(f'Reader received: {line.decode()}')
                self.msgs_recvd += 1
        # if self.msgs_recvd == 10:
        #     self.transport.close()

    def connection_lost(self, exc):
        """Called when the connection is lost or closed.

        The argument is an exception object or None (the latter
        meaning a regular EOF is received or the connection was
        aborted or closed).
        """
        print('Serial closed!')
        
    async def send(self, message=b"hello"):
        """Send four newline-terminated messages, one byte at a time.
        """
        # message = b'foo\nbar\nbaz\nqux\nfoo\nbar\nbaz\nqux\nfoo\nbar\nbaz\nqux\nfoo\nbar\nbaz\nqux\nfoo\nbar\nbaz\nqux\n'
        for b in message:
            await asyncio.sleep(0.5)
            self.transport.serial.write(bytes([b]))
            print(f'Writer sent: {bytes([b])}')
        # self.transport.close()