# -*- coding: utf8 -*-
import socket
import threading
import os
import getpass
'''
import sys
sys.path.append('/Users/r00t0k/project/translationfile/DB/')
import dbCtrl
'''

HOST = 'localhost'
PORT = 7677

user = getpass.getuser()
location = "C:/Users/" + user + "/Desktop"

#packet = (controlCode, srcClientId, dstClientId, fileLocation, fileName)
# controlCode|srcClient|dstClient|fileLocation|fileName


#dic


fileTransferReq = {
    "controlCode" : 1,
    "srcClientId" : None,
    "dstClientId" : None,
    "fileLocation" : None,
    "fileName" : None
}

fileViewReq = {
    "controlCode" : 2,
    "reqLocation" : None
}

sessionProtocol = {
    "method" : 1,
    "session" : None,
    "params" : {
        "user" : None,
        "pass" : None
    }
}





def TreeView(dir):
    files = os.listdir(dir)
    print(len(files))
    for i in files:
        print(i)
    pass


def C2CPacket(src, dst): # Clinet To Clinet Packet
    #files = FileDownload(filename)

    pass

def serverStart():
    print('File translation server start .. !!')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    #s.listen()
    while True:
        conn, addr = s.recvfrom(1024)
        print(str(addr) + " Connect Complete !!")

        xx = conn.recv(1024).decode().split(',')
        print(xx)
        #if xx == 1:
        #    print("command 1")
        #xx.decode()

        #conn
    print ('wait.....')

if __name__ == "__main__":
    print(location)
    serverStart()
    pass

