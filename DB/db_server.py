import pymysql #host='localhost', port=3306, user='root', passwd='mysql1234', db='estdb',charset='utf8',autocommit=True)
from pymysqlpool.pool import Pool

translationFile_Dict = {
    "user" : "root",
    "password" : "mysql1234",
    "host" : "127.0.0.1",
    "db" : "translationfile",
    "charset" : "utf8"
}






class DbController:
    pool = Pool(**translationFile_Dict)

    def __init__(self, host, user, password, db, charset):
        self.dbconn = pymysql.connect(host = host, user = user, password = password, db = db, charset = charset)
        self.dbcursor = self.dbconn.cursor(pymysql.cursors.DictCursor)
    def insert_db(self, tableName, values):
        print(queryString)
        self.dbcursor.execute("INSERT INTO " + tableName + " VALUES " +  str(values))
        self.dbconn.commit()
        pass
    def delete_db(self, queryString):
        self.dbcursor.execute(queryString)
        self.dbconn.commit()
        pass
    def select_db(self, queryString):
        print(queryString)
        self.dbcursor.execute(queryString)
        result = self.dbcursor.fetchone() #fetchall, fetchone
        return result
        pass
    def update_db(self):
        pass


#dbC = dbController(**translationFile_Dict)
#dbC.insert_db("user", ("a", "b", "c"))
#dbC.select_db("select * from user where user_id = 'test123'")
#print(dbC.select_db("select * from user where user_id = 'test123'")["user_pw"])
