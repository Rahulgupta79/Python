import mysql.connector as p
try:
    conn=p.connect(
        host="localhost",
        user ="root",
        password ="Mysql@123",
        port =3306,
        database ="demodb"# it tells that you choose the database 
    )
    if(conn.is_connected()):
        print("Connection successful")
except Exception as e:
    print("Not Connected")
else:
    cur=conn.cursor()
    # cur.execute("CREATE TABLE demo(Name varchar(30) NOT NULL,Roll INTEGER,Address varchar(30))")
    sql="SHOW TABLES"
    cur.execute(sql)
    for data in cur:
        print(data[0])

    cur.execute("DESC demo")
    for data in cur:
        print(data)


    cur.execute("INSERT INTO demo VALUES('Rahul',101,'Mainatand')")
    cur.execute("select *from demo")
    for data in cur:
        print(data)
    conn.commit()#it tells the data which you insert into table is commited means inserted without this command data show but not inserted

    cur.close()
    conn.close()