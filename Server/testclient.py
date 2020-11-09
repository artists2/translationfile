import socket
import bson

HOST = 'localhost'
PORT = 7677



c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.connect((HOST, PORT))

examDic = {
    "commandCode" : 1,
    "name" : "r00t0k",
    "age" : "24",
    "major" : "ComputerEngineering"
}


examDicBson = bson.dumps(examDic)
print(examDic)
print(examDicBson)

examDicBsonLoads = bson.loads(examDicBson)

print(examDicBsonLoads)

c.sendall("1,2,3,4,5".encode())

c.close()


