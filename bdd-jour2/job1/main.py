import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mouf",
  database="LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM etudiants")

result = cursor.fetchall()

print(result)

mydb.close()