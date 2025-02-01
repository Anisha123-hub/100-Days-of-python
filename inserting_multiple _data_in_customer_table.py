import mysql.connector

# Establish database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="anisha"
)

mycursor = mydb.cursor()

# Corrected SQL query (fixed INSERT INTO syntax and %s placeholders)
sql = "INSERT INTO customers (Name, Address) VALUES (%s, %s)"

# Corrected tuple values
val = [
    ("Anusha", "Bangladesh"),  # Fixed typo in country name
    ("Krishna", "Biratnagar"),
    ("Narayani", "Biratnagar"),
    ("Abiral", "Kathmandu")
]

# Print SQL query and values to verify correctness before execution
print("SQL Query:", sql)
print("Values:", val)

# Execute SQL query
mycursor.executemany(sql, val)

# Commit the changes to the database
mydb.commit()

# Print success message
print(mycursor.rowcount, "records were inserted successfully!")
 
