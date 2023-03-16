import mysql.connector

# Se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mouf",
  database="Laplateforme"
)

cursor = mydb.cursor()

cursor.execute("SELECT nom, capacite FROM salles")

result = cursor.fetchall()

print(result)

mydb.close()