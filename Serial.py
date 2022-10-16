# 异步串口
# import serial
import asyncio
import serial_asyncio


class UAVSerial(asyncio.Protocol):
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

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    serial = serial_asyncio.create_serial_connection(loop, UAVSerial, 'COM1', baudrate=115200)
    # writer = serial_asyncio.create_serial_connection(loop, Writer, 'COM2', baudrate=115200)
    # asyncio.ensure_future(serial)
    
    transport, protocol = loop.run_until_complete(serial)
    # loop.call_later(10, loop.stop)
    loop.run_forever()
    loop.close()
    print('Done')