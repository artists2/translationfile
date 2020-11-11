import socket
import bson

HOST = 'localhost'
PORT = 7677



c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

sessionProtocol = {
    "method" : 1,
    "session" : "testSession", #None
    "params" : {
        "user" : "abc123", #None
        "pass" : "root123" #None
    }
}


sessionProtocolBson = bson.dumps(sessionProtocol)
#sessionProtocolLoads = bson.loads(examDicBson)

c.sendall(sessionProtocolBson)

c.close()


