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
        self.dbcursor = self.dbconn.cursor(pymysql.cursors.DictCursor)
    def insertDB(self, tableName, values):
        print("******insert DB")
        self.dbcursor.execute("INSERT INTO " + tableName + " VALUES " +  str(values))
        self.dbconn.commit()
        pass
    def deleteDB(self):
        pass
    def selectDB(self, tableName, fieldName, condString):
        print("SELECT " + fieldName + " FROM " + tableName + " WHERE " + condString)
        self.dbcursor.execute("SELECT " + fieldName + " FROM " + tableName + " WHERE " + condString)
        result = self.dbcursor.fetchone() #fetchall, fetchone
        return result
        #return self.dbcursor.fetchall()
        pass
    def updateDB(self):
        pass


#dbC = dbController(**translationFile_Dict)
#dbC.insertDB("user", ("a", "b", "c"))
#dbC.selectDB("user", "*", "user_id = 'test123'")
