import mysql.connector
    
class InsertData:
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
            sql4="""INSERT INTO ROLLBACK_TB VALUES("Rahul ",1,23)"""
            cur=dbc.cursor()
            try:
                cur.execute(sql4)
                dbc.commit()
                print("Data Inserted Successfully")
            except:
                print("Database Connected but not created table")
        finally:
            cur.close()
            dbc.close()
            print("Database connection close Thankyou")


obj=InsertData()