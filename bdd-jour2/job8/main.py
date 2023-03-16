# CREATE DATABASES Zoo #
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mouf",
  database="Zoo"
)

cursor = mydb.cursor()
cursor.execute("USE Zoo;")

cursor.execute('''CREATE TABLE animal (
                        id INT PRIMARY KEY,
                        name VARCHAR(50),
                        breed VARCHAR(50),
                        cage_id INT,
                        birthdate DATE,
                        origin_country VARCHAR(50)
                    )''')

cursor = mydb.cursor()
add_animals = [("1", "Tigrou", "Tigre", "1", "2018-01-01", "Inde"),
               ("2", "Baloo", "Ours", "2", "2019-05-12", "Canada"),
               ("3", "Nemo", "Poisson clown", "3", "2020-03-25", "Australie"),
               ("4", "Flipper", "Dauphin", "3", "2017-11-03", "États-Unis"),
               ("5", "Kaa", "Serpent", "4", "2016-07-22", "Inde"),
               ("6", "Rafiki", "Babouin", "5", "2015-12-10", "Kenya"),
               ("7", "Zazou", "Toucan", "6", "2014-06-18", "Brésil")]

for animal in add_animals:
    add_animal = ("INSERT INTO animal "
                  "(id, name, breed, cage_id, birthdate, origin_country) "
                  "VALUES (%s, %s, %s, %s, %s, %s)")
    cursor.execute(add_animal, animal)

mydb.commit()

cursor.execute('''CREATE TABLE cage (
                        id INT PRIMARY KEY,
                        area DECIMAL(10,2),
                        capacity INT
                    )''')

cursor.execute('''INSERT INTO cage (id, area, capacity)
                  VALUES 
                  (1, 20.5, 10),
                  (2, 25.2, 12),
                  (3, 18.7, 8),
                  (4, 22.1, 9),
                  (5, 30.0, 15)''')

cursor.close()
mydb.close()