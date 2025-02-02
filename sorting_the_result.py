import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "anisha"
)

mycursor = mydb.cursor()

sql = "SELECT *FROM customers ORDER BY Name"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)