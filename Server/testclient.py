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
        "user" : None,
        "pass" : None
    }
}


sessionProtocolBson = bson.dumps(sessionProtocol)
#sessionProtocolLoads = bson.loads(examDicBson)

c.sendall(sessionProtocolBson)

c.close()


