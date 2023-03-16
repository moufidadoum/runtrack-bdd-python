import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mouf",
  database="LaPlateforme"
)

cursor = db.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

superficie_totale = cursor.fetchone()[0]

print("La superficie de La Plateforme est de", superficie_totale, "m2")

cursor.close()
db.close()
