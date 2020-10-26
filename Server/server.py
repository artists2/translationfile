# -*- coding: utf8 -*-
import socket
import threading
import os
'''
import sys
sys.path.append('/Users/r00t0k/project/translationfile/DB/')
import dbCtrl
'''

HOST = 'localhost'
PORT = 7677


def FileView(dir):
    files = os.listdir(dir)
    print(len(files))
    for i in files:
        print(i)
    pass


def C2CPacket(src, dst): # Clinet To Clinet Packet

    
    pass

def serverStart():
    print('File translation server start .. !!')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Complete')
    #print('DB connection start .. !!')
    #dbcmd = dbCtrl.dbController(HOST, 'root', '1234', 'clientid')
    #print('Complete')
    FileView()
    print ('Wait...')
    while True:
        conn, addr = s.accept()
        #print(s.accept())
        print(addr + "Connect !!")
        filename = conn.recv(1024)
        filename.decode()
        print(filename)
        #파일을 확정지어서 휴대폰 -> 폰으로 보내는 거기 때문에 x
        
        #conn
    print ('wait.....')

if __name__ == "__main__":
    serverStart()    
    pass    

