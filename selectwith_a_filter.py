import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "anisha"
)

mycursor = mydb.cursor()

sql = "SELECT *FROM customers WHERE Address = 'Biratnagar'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)