import mysql.connector as p
try:
    conn=p.connect(
        user ="root",
        password ="Mysql@123",
        host ="localhost",
        port =3306,
        database="tp"
    )
    if(conn.is_connected()):
        print("Connection successful")
except Exception as obj:
        print("Can't Connect")
else:
    pbc=conn.cursor()
    sql="SHOW TABLES"
    pbc.execute(sql)
    for li in pbc:
         print(li[0])
    pbc.execute("SELECT *FROM stp")
    for li in pbc:
        print(li)
    pbc.close()
    conn.close()