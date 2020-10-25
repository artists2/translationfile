import socket
import threading
import dbCtrl

HOST = 'localhost'
PORT = 7676





def threaded():
    t = threading.Thread(target=(), args=())
    t.start
    pass

def server():
    pass


def serverStart():
    print('File translation server start .. !!')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Complete')

        print('DB connection start .. !!')
        dbcmd = dbCtrl.dbController(HOST, 'root', 'dpswpf0819@', 'clientid')
        print('Complete')

        print ('Wait...')
        while True:
            conn, addr = s.accept()
            filename = conn.recv(1024)
            filename.decode()
            print(filename)
            #파일을 확정지어서 휴대폰 -> 폰으로 보내는 거기 때문에 x
            
            conn
    

    print ('wait.....')


serverStart()


