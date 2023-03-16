import mysql.connector

# Connexion à la base de données
cnx = mysql.connector.connect(
    user='root',
    password='mouf',
    host='localhost',
    database='zoo')
cursor = cnx.cursor()

# Fonction pour ajouter un animal
def ajouter_animal():
    print("Ajouter un nouvel animal :")
    nom = input("Nom : ")
    race = input("Race : ")
    cage_id = input("Identifiant de la cage : ")
    birthdate = input("Date de naissance (format YYYY-MM-DD) : ")
    origin_country = input("Pays d'origine : ")
    query = "INSERT INTO animal (id, name, breed, cage_id, birthdate, origin_country) VALUES (DEFAULT, %s, %s, %s, %s, %s)"
    values = (nom, race, cage_id, birthdate, origin_country)
    cursor.execute(query, values)
    cnx.commit()
    print("L'animal a été ajouté avec succès !\n")

def supprimer_animal():
    animal_id = input("Entrez l'ID de l'animal à supprimer : ")
    query = "DELETE FROM animal WHERE id = %s"
    values = (animal_id,)
    cursor.execute(query, values)
    cnx.commit()
    print(cursor.rowcount, "animal supprimé de la base de données")

def modify_animal_or_cage(id, table, column, value):
    query = f"UPDATE {table} SET {column} = %s WHERE id = %s"
    cursor.execute(query, (value, id))
    cnx.commit()


def demander_action():
    action = input("Que souhaitez-vous faire ? (ajouter (1) / supprimer (2) / modifier un animal/cage (3) ) : ")
    if action == "1":
        ajouter_animal()
    elif action == "2":
        supprimer_animal()
    elif action == "3":
        modify_animal_or_cage()
    else:
        print("Action invalide")

demander_action()


def afficher_animaux():
    print("Animaux présents dans le zoo :")
    cursor.execute("SELECT * FROM animal")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print("\nAnimaux présents dans les cages :")
    cursor.execute("SELECT cage.id, cage.area, animal.name, animal.breed, animal.birthdate, animal.origin_country FROM cage LEFT JOIN animal ON cage.id = animal.cage_id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def calculer_superficie_totale():
    query = "SELECT SUM(area) FROM cage"
    cursor.execute(query)
    superficie_totale = cursor.fetchone()[0]
    print(f"La superficie totale de toutes les cages est de {superficie_totale} m².")
