import asyncio
from asyncio import transports
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
import bson

POOL_SIZE = 1000
ASYNC = True


class Action:
    def 

    pass







class HandlerFactory(asyncio.Protocol):
    transport: transports.Transport
    peer_name = None
    server_name = None
    pool = ThreadPoolExecutor(POOL_SIZE)

    def connection_made(self, transport: transports.Transport):
        self.peer_name = transport.get_extra_info("peername")
        self.server_name = transport.get_extra_info("sockname")[1]
        print(f"Connection from {self.peer_name} -> App Server" 
                if self.server_name == 7077 else 
              f"Connection from {self.peer_name} -> Cmd Server")
        self.transport = transport

    def connection_lost(self, exc: Optional[Exception]):
        #print(f"Connection lost: {self.peer_name}")
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
        msg = bson.loads(data) #data.decode()
        print(f"Data received: {msg}")
        
        if ["method"] == 1:
            pass
        if ["method"] == 2:
            pass

        return data


class Server:
    #def __init__:
    server = None
    routes = {}

    def __init__(self, cmd_server_port: int, app_server_port: int):
        self.cmd_port = cmd_server_port
        self.app_port = app_server_port
        

    async def init(self):
        loop = asyncio.get_running_loop()

        self.cmd_server = await loop.create_server(
            lambda: HandlerFactory(),
            "localhost", self.cmd_port
        )
        self.app_server = await loop.create_server(
            lambda: HandlerFactory(),
            "localhost", self.app_port
        )

        async with self.cmd_server, self.app_server:
            await self.cmd_server.start_serving()
            await self.app_server.start_serving()
            print("Server start\n\n")

            await self.cmd_server.wait_closed()
            await self.app_server.wait_closed()


async def main():
    _app_server_port = 7077
    _command_server_port = 7078

    command_server = Server(_command_server_port, _app_server_port)
    await command_server.init()
    print(f"{_app_server_port} start")


if __name__ == "__main__":
    asyncio.run(main())