import mysql.connector
    
class TableCreated:
    def __init__(self):
        try:
            dbc=mysql.connector.connect(
            user="root",
            password="Mysql@123",
            host="localhost",
            port=3306,
            database="ROLLBACK"
        )
        except:
            print("Database not connected")
        else:
            # sql2="USE ROLLBACK"      #It is use for connect database
            sql1="""CREATE TABLE IF NOT EXISTS ROLLBACK_TB(
                    Name VARCHAR(45) NOT NULL,
                    Roll INTEGER,
                    Age  INTEGER)"""            
            sql3="SHOW TABLES"
            cur=dbc.cursor()
            try:
                cur.execute(sql1)
                cur.execute(sql3)
                print("Table Created Successfully")
                for i in cur:
                    print(i[0])
            except:
                print("Database Connected but not created table")
        finally:
            cur.close()
            dbc.close()
            print("Database connection close Thankyou")


obj=TableCreated()