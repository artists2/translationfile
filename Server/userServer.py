# -*- coding: utf8 -*-
import socket
import threading
import os
import zipfile
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

filelist = []

def ZipFile(filelist):
    with zipfile.ZipFile(location/ZipName(), w) as zip_file:
        for file in filelist:
            zip_file.write(file)
        zip_file.close()

def ZipName():
    zipName = input("Zip Name?: ")
    return zipName


def FileUpload(filename): # 목적지로 파일 업로드 할 때
    try:
        print("File : " + filelist + "Upload Start")

    except:
        pass
    pass

def FileDownload(filename): # 출발지에서 파일 다운로드 받을때
    try:
        print("File : " + filelist + "Download Start")
        pass
    except:
        pass
    pass


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
    print('Complete')
    #print('DB connection start .. !!')
    #dbcmd = dbCtrl.dbController(HOST, 'root', '1234', 'clientid')
    #print('Complete')
    #FileView()
    print ('Wait...')
    while True:
        # Test Code



        conn, addr = s.accept()
        #print(s.accept())
        print(str(addr) + " Connect Complete !!")
        filename = conn.recv(1024)
        filename.decode()
        print(filename)
        #파일을 확정지어서 휴대폰 -> 폰으로 보내는 거기 때문에 x

        #conn
    print ('wait.....')

if __name__ == "__main__":
    print(location)
    serverStart()
    pass

