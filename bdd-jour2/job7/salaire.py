import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mouf",
    database="entreprise"
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE employes("
                "id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"
                "nom VARCHAR NOT NULL,"
                "prenom VARCHAR NOT NULL,"
                "salaire DECIMAL NOT NULL,"
                "id_service INT NOT NULL)")


cursor.execute("""INSERT INTO employes (id, nom, prenom, salaire, id_service)
         VALUES
            (19, 'Dupont', 'Pierre', 2500.00, 1),
            (20, 'Martin', 'Sophie', 3800.00, 2),
            (21, 'Doe', 'John', 1700.00, 3),
            (22, 'Dupuis', 'Marie', 3250.00, 4),
            (23, 'Roy', 'Luc', 2050.00, 5),
            (24, 'Michel', 'Isabelle', 2450.00, 6)""")


cursor.execute("SELECT * FROM employes WHERE salaire > 3000")


resultats = cursor.fetchall()

for resultat in resultats:
    print(resultat)

cursor.close()
conn.close()
