import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="anisha"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (Name, Address) VALUES (%s,%s)"
val = ("Anisha", "Biratnagar")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Record Inserted!")