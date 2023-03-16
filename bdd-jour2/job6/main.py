import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mouf",
  database="LaPlateforme"
)

cursor = db.cursor()

cursor.execute("SELECT SUM(capacite) FROM salles")

somme_capacites = cursor.fetchone()[0]

print("La capacité de toutes les salles est de :", somme_capacites)

cursor.close()
db.close()
