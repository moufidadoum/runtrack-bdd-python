import mysql.connector

class Crud:

    def __init__(self, user, password, database):
        self.plug = mysql.connector.connect(
            user = user,
            password = password,
            database = database,
        )

        self.cursor = self.plug.cursor()
        print("Connexion à la BDD réussie.")


    def crea(self, id, nom, prenom, salaire, id_service):
        sql = "insert into employes (id, nom, prenom, salaire, id_service) values (%s, %s, %s, %s, %s)"
        values = (id, nom, prenom, salaire, id_service)
        self.cursor.execute(sql, values)
        self.plug.commit()


    def lire(self, condition=None):
        sql = "select * from employes"
        if condition:
            sql += f" where {condition}"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


    def maj(self, colonne, valeur, condition):
        sql = f"update employes set {colonne} = %s where {condition}"
        values = (valeur,)
        self.cursor.execute(sql, values)
        self.plug.commit()



    def dele(self, condition):
        sql = f"delete from employes where {condition}"
        self.cursor.execute(sql)
        self.plug.commit()


crud = Crud(user="root", password="mouf", database='entreprise')


result = crud.lire()

print(result)
