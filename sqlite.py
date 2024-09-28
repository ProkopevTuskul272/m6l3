import sqlite3


conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('CREATE TABLE caloriesbotdb(food_name, calories)')
cur.execute("INSERT INTO caloriesbotdb VALUES ('Rice', 130), ('Maraconis', 371)")

conn.commit()
conn.close()