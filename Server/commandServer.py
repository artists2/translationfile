# -*- coding: utf8 -*-
import socket
import threading
import os
import getpass
import bson
import asyncio
import uuid
import time
import sys
sys.path.append('/Users/r00t0k/project/translationfile/DB')
import dbCtrl

HOST = 'localhost'
PORT = 7677

user = getpass.getuser()
location = "C:/Users/" + user + "/Desktop"

#DB 객체 생성
dbC = dbCtrl.dbController(**(dbCtrl.translationFile_Dict))

def translation_file():
    pass

def dir_client():
    pass


def login_user(method, session, params):
    _login = int(dbC.selectDB("select COUNT(*) from user where user_id = '" + params["userInfo"]["userId"] + "' and user_pw = '" + params["userInfo"]["userPw"] + "' ")["COUNT(*)"])
    if _login == 1:
        print("로그인 성공")
    else:
        print("로그인 실패")
    pass

def join_user(method, session, params):
    #print(method, session ,params["userInfo"]["userId"], params["userInfo"]["userPw"], params["userInfo"]["userEmail"])
    _user_info_list = (params["userInfo"]["userId"], params["userInfo"]["userPw"], params["userInfo"]["userEmail"])
    try:
        dbC.insertDB("user", _user_info_list)
        print("회원가입 완료")
    except:
        print("중복 된 아이디가 존재합니다.")
    pass

def find_user(method, session, params):
    try:
        dbC.selectDB("select user_id from user where user_email = '" + params["userInfo"]["user_email"] + "' ")["user_id"]
    except:
        print("이메일에 매칭되는 아이디가 없습니다.")
    pass

def check_expired_session(method, session, params):
    # 세션 만료시간 체크
    exprie_time = int(dbC.selectDB("select session_expired from session where user_id = '" + params["userInfo"]["user_id"] + "' ")["session_expired"])
    if (time.time() > exprie_time):
        #만료
        print("만료 되었습니다.")
        return delete_session(exprie_time)
    else:
        #만료x
        print("만료되지 않았습니다.")
    pass

def delete_session(expiretime):
    query_delete_session = "DELETE FROM session WHERE session_expired = '" + expiretime + "' "
    dbC.deleteDB(query_delete_session)
    # 만료된 세션 삭제
    pass



def create_session(method, session, params):
    #print(session, params["userInfo"]["userId"], params["userInfo"]["userPw"])
    #print(dbC.selectDB("select * from session where user_pw = '" + params["userInfo"]["userId"] + "' "))
    
    print(dbC.selectDB("SELECT COUNT(*) FROM session WHERE user_id= '" + params["userInfo"]["userId"] + "' ")["COUNT(*)"]) # 0이면 세션 없는거, 1이면 세션 있는거
    isSession = int(dbC.selectDB("SELECT COUNT(*) FROM session WHERE user_id= '" + params["userInfo"]["userId"] + "' ")["COUNT(*)"])

    if isSession == 1:
        print("세션이 존재합니다.")
    else:
        print("세션이 존재하지 않아 세션을 생성합니다.")
        realSession = str(uuid.uuid4())
        sessionTime = (time.time() + 600)
        querySession = (realSession, sessionTime, params["userInfo"]["userId"])
        dbC.insertDB("session", querySession)

        # 앱으로 다시 보내주기
    pass

def start_server():
    print('File translation server start .. !!')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(str(addr) + " Connection Complete !!")


        data = conn.recv(1024)
        loadsData = bson.loads(data)
        
        print(loadsData)
        del loadsData["method"]
        print(loadsData)
        if (loadsData["method"] == 1):
            print("sessionProtocol")
            create_session(**loadsData)
            pass
        elif (loadsData["method"] == 2):
            join_user(**loadsData)
            pass
        elif (loadsData["method"] == 3):
            pass

if __name__ == "__main__":
    print(location)
    start_server()
    pass

