import socket

HOST = 'localhost'
PORT = 7677



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def CreateID():
    print(socket.gethostname()) # 

    return

def SendID_Server(): # Mac Addr 서버로 보내주기
    pass


CreateID()
