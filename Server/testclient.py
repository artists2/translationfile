import socket


HOST = 'localhost'
PORT = 7676



c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))


c.sendall('testfilename'.encode())

c.close()


