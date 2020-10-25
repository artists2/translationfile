import pymysql #host='localhost', port=3306, user='root', passwd='maria', db='estdb',charset='utf8',autocommit=True)

class dbController:
    def __init__(self, host, id, pw, db_name):
        self.dbconn = pymysql.connect(host = host, user = id, password = pw, db = db_name, charset = 'utf8')
        self.dbcursor = self.dbconn.cursor()
    def insertDB(self):
        pass
    def deleteDB(self):
        pass