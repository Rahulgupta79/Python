import mysql.connector
    
class UpdateData:
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
            nme=input("Enter name;")
            age=int(input("Enter age="))
            sql="UPDATE ROLLBACK_TB SET Name='{}', Age='{}' WHERE Roll={}".format(nme,age,rl)
            cur=dbc.cursor()
            try:
                cur.execute(sql)
                dbc.commit()
            except:
                print("Database Connected but not Update table")
        finally:
            cur.close()
            dbc.close()
            print("Database connection close Thankyou")


obj=UpdateData()