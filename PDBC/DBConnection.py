import mysql.connector
class DBConnection:
    def __init__(self):
        try:
            dbc=mysql.connector.connect(
            user="root",
            password="Mysql@123",
            host="localhost",
            port=3306
        )
        except:
            print("Database note connected")
        else:
            sql="CREATE DATABASE IF NOT EXISTS ROLLBACK"
            cur=dbc.cursor()
            try:
                cur.execute(sql)
                print("Database Created Successfully")
            except:
                print("Database Connected but not create Database")
        finally:
            cur.close()
            dbc.close()
            print("Connection close")

obj=DBConnection()