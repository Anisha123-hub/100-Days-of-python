import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "anisha"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE CUSTOMERS (Name VARCHAR(255), Address VARCHAR(255))")