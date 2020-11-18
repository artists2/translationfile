import asyncio
from asyncio import transports
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
import bson
import sys

sys.path.append("/Users/r00t0k/project/translationfile/DB")
from connection_pool_db import DBController

controller = DBController()


POOL_SIZE = 1000
ASYNC = True

# -> AUTH

def join_user(method, session, params):
    #print(method, session ,params["userInfo"]["userId"], params["userInfo"]["userPw"], params["userInfo"]["userEmail"])
    _user_info_list = (params["userInfo"]["userId"], params["userInfo"]["userPw"], params["userInfo"]["userEmail"])
    try:
        controller.insert_db("user", _user_info_list)
        print("회원가입 완료")
    except:
        print("중복 된 아이디가 존재합니다.")
    pass

def login_user(method, session, params):
    _login = int(controller.select_db("select COUNT(*) from user where user_id = '" +
                                    params["userInfo"]["userId"] +
                                    "' and user_pw = '" +
                                    params["userInfo"]["userPw"] +
                                    "' ")["COUNT(*)"])
    if _login == 1:
        print("로그인 성공")
    else:
        print("로그인 실패")
    pass

def find_user(method, session, params):
    try:
        controller.select_db("select user_id from user where user_email = '" +
                            params["userInfo"]["user_email"] +
                            "' ")["user_id"]
    except:
        print("이메일에 매칭되는 아이디가 없습니다.")
    pass

# <- AUTH 

# -> Session

def create_session(method, session, params):
    #print(session, params["userInfo"]["userId"], params["userInfo"]["userPw"])
    #print(controller.select_db("select * from session where user_pw = '" + params["userInfo"]["userId"] + "' "))

    print(controller.select_db("SELECT COUNT(*) FROM session WHERE user_id= '" +
                                params["userInfo"]["userId"] +
                                "' ")["COUNT(*)"]) # 0이면 세션 없는거, 1이면 세션 있는거

    isSession = int(controller.select_db("SELECT COUNT(*) FROM session WHERE user_id= '" +
                                        params["userInfo"]["userId"] +
                                        "' ")["COUNT(*)"])

    if isSession == 1:
        print("세션이 존재합니다.")

    else:
        print("세션이 존재하지 않아 세션을 생성합니다.")
        _realsession = str(uuid.uuid4())
        _sessiontime = (time.time() + 600)

        session_query = (_realsession, _sessiontime, params["userInfo"]["userId"])

        controller.insert_db("session", session_query)

        # 앱으로 다시 보내주기
    pass

def check_expired_session(method, session, params):
    # 세션 만료시간 체크
    exprie_time = int(controller.select_db("select session_expired from session where user_id = '" +
                                            params["userInfo"]["user_id"] +
                                            "' ")["session_expired"])

    if (time.time() > exprie_time):
        #만료
        print("SESSION_EXPIRED")
        return delete_session(exprie_time)
    elif (time.time() <= exprie_time):
        #만료x
        print("SESSION_VALID")
    else:
        print("SESSION_INVALID")
    pass

def delete_session(expiretime):
    query_delete_session = "DELETE FROM session WHERE session_expired = '" + expiretime + "' "
    controller.delete_db(query_delete_session)
    # 만료된 세션 삭제
    pass

# <- Session

# -> File View

def dir_client():
    pass

# <- File View


# -> File Transfer

def translation_file():
    pass

# <- File Transfer


# -> Factory
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
        
        """
        method = 1  -> create session
        method = 2  -> join user
        method = 3  -> 
        """
        if msg["method"] == 1:
            print("Protocol 1")
            
            pass
        elif msg["method"] == 2:
            print("Protocol 2")
            pass

        return data

# <- Factory

# -> Server

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

# <- Server

# -> Main
async def main():
    _app_server_port = 7077
    _command_server_port = 7078

    command_server = Server(_command_server_port, _app_server_port)
    await command_server.init()
    print(f"{_app_server_port} start")


if __name__ == "__main__":
    asyncio.run(main())

# <- Main
