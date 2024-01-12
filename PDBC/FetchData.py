import mysql.connector
    
class FetchData:
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
            rl=int(input("Enter roll="))
            sql="SELECT *FROM ROLLBACK_TB WHERE Roll={}".format(rl)
            cur=dbc.cursor()
            try:
                cur.execute(sql)
                for i in cur:
                    print(i)
                dbc.commit()
            except:
                print("Database Connected but not fetch table")
        finally:
            cur.close()
            dbc.close()
            print("Database connection close Thankyou")


obj=FetchData()