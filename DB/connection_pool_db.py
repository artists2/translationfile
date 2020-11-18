from pymysqlpool.pool import Pool
    
_db_info = {
    "user" : "root",
    "password" : "mysql1234",
    "host" : "127.0.0.1",
    "db" : "translationfile",
    "autocommit" : True
}

class DBController:
    pool = Pool(**_db_info)
    pool.init()

    @classmethod
    def select_db(cls,querystring):
        connection = cls.pool.get_conn()
        cursor = connection.cursor()
        
        cursor.execute(querystring)
        result = cursor.fetchone() #fetchall()

        cls.pool.release(connection)
        return result

    @classmethod
    def insert_db(cls,querystring):
        connection = cls.pool.get_conn()
        cursor = connection.cursor()
        
        result = cursor.execute(querystring)

        cls.pool.release(connection)
        return result
        
    @classmethod
    def delete_db(cls,querystring):
        connection = cls.pool.get_conn()
        cursor = connection.cursor()

        result = cursor.execute(querystring)

        cls.pool.release(connection)
        return result

    @classmethod
    def update_db(cls,querystring):
        pass



"""pool = Pool(**_db_info)
pool.init()

connection = pool.get_conn()
cur = connection.cursor()
#print(pool.get_pool_size())
cur.execute("select * from user;")
print(cur.fetchone())
pool.release(connection)
"""
