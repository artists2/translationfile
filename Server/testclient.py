import socket
import bson

HOST = 'localhost'
PORT = 7677



c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

sessionProtocol = {
    "method" : 1,
    "session" : None,
    "params" : {
        "userInfo" : {
            "userId" : "abcd1233",
            "userPw" : "abcd1233"
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


