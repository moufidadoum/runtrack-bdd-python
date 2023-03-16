import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mouf",
    database="entreprise"
)

cursor = conn.cursor()

cursor.execute("SELECT employes.*, services.nom AS nom_service FROM employes JOIN services ON employes.id_service = services.id")

resultats = cursor.fetchall()

for resultat in resultats:
    print(f"ID: {resultat[0]}, Nom: {resultat[1]}, Prénom: {resultat[2]}, Salaire: {resultat[3]}, ID Service: {resultat[4]}, Service: {resultat[5]}")

cursor.close()
conn.close()
