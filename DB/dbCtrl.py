import pymysql #host='localhost', port=3306, user='root', passwd='mysql1234', db='estdb',charset='utf8',autocommit=True)

translationFile_Dict = {
    "user" : "root",
    "password" : "mysql1234",
    "host" : "127.0.0.1",
    "db" : "translationfile",
    "charset" : "utf8"
}

class dbController:
    def __init__(self, host, user, password, db, charset):
        self.dbconn = pymysql.connect(host = host, user = user, password = password, db = db, charset = charset)
        self.dbcursor = self.dbconn.cursor()
    def insertDB(self, table, ):
        pass
    def deleteDB(self):
        pass
    def selectDB(self):
        pass
    def updateDB(self):
        pass

dbC = dbController(**translationFile_Dict)

dbC.insertDB()
"""dbC = dbController()
print(type(dbC))"""