# -*- coding: utf8 -*-
import socket
import threading
import os
import getpass
import bson
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


# 프로토콜 정의
sessionProtocol = {
    "method" : 1,
    "session" : None,
    "params" : {
        "user" : None,
        "pass" : None
    }
}

fileTransferReq = {
    "method" : 2,
    "srcClientId" : None,
    "dstClientId" : None,
    "fileLocation" : None,
    "fileName" : None
}

fileViewReq = {
    "method" : 3,
    "reqLocation" : None
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

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(str(addr) + " Connection Complete !!")


        data = conn.recv(1024)

        #if data == 
        print(data)
        loadsData = bson.loads(data)
        
        if (loadsData["method"] == 1):
            pass
        elif (loadsData["method"] == 2):
            pass
        elif (loadsData["method"] == 3):
            pass

        
        print(loadsData["method"])




    print ('wait.....')

if __name__ == "__main__":
    print(location)
    serverStart()
    pass

