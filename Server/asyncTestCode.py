import asyncio
from asyncio import transports
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
import bson

POOL_SIZE = 1000
ASYNC = True


class 






class HandlerFactory(asyncio.Protocol):
    transport: transports.Transport
    peer_name = None
    pool = ThreadPoolExecutor(POOL_SIZE)

    def connection_made(self, transport: transports.Transport):
        self.peer_name = transport.get_extra_info("peername")
        print(f"Connection from {self.peer_name}")
        self.transport = transport

    def connection_lost(self, exc: Optional[Exception]):
        # print(f"Connection lost: {self.peer_name}")
        pass

    def data_received(self, data: bytes):
        asyncio.create_task(self.__recv(data))

    async def __recv(self, data: bytes):
        if ASYNC:
            result = await self.threading(target=self.__data_received, args=(data,))
            self.transport.write(result)
        else:
            self.transport.write(self.__data_received(data))

    async def threading(self, target=None, args=()):
        loop = asyncio.get_running_loop()
        result = loop.run_in_executor(
            self.pool, target, *args
        )
        return await result

    @staticmethod
    def __data_received(data: bytes):
        msg = bson.loads(data)#data.decode()
        print(f"Data received: {msg}")
        return data


class Server:
    #def __init__:
    server = None
    routes = {}

    async def init(self):
        loop = asyncio.get_running_loop()

        self.server = await loop.create_server(
            lambda: HandlerFactory(),
            "localhost", 8081
        )

        async with self.server:
            await self.server.serve_forever()


async def main():
    command_server = Server()
    await command.init()


if __name__ == "__main__":
    asyncio.run(main())