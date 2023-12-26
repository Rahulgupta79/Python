import mysql.connector
try:
    conn=mysql.connector.connect(
        user="root",
        password="Mysql@123",
        host="localhost",
        port=3306
    )
except Exception as obj:
    print(obj)
else:
    print("Connected SQL")
    cur=conn.cursor()
    cur.execute("SHOW DATABASES")
    Lst=list(cur)
    for data in Lst:
        print(data)
    print(Lst)
    # cur.execute("USE tp")
    # cur.execute("show tables")
    cur.close()
    conn.close()