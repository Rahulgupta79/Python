import mysql.connector
try:
    conn=mysql.connector.connect(
    user='root',
    password='Mysql@123',
    host='localhost',
    port=3306
)
except Exception as obj:
    print("Can not connect")
else:
    print("Connected")
