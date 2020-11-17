import socket
import bson

HOST = 'localhost'
PORT = 7077
# 7077 = _app_server_port
# 7078 = _command_server_port



c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

sessionProtocol = {
    "method" : 1,
    "session" : None,
    "params" : {
        "userInfo" : {
            "userId" : "test123",
            "userPw" : "abcd1243"
        }
    }
}

joinProtocol = {
    "method" : 2,
    "session" : None,
    "params" : {
        "userInfo" : {
            "userId" : "test1234",
            "userPw" : "abcd1233",
            "userEmail" : "aaa@naver.com"
    }
    }
}


Bson = bson.dumps(sessionProtocol)
#sessionProtocolLoads = bson.loads(examDicBson)

c.sendall(Bson)

c.close()


