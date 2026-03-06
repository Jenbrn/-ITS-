import mysql.connector
import json

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'its2026'
)

cursor = db.cursor()

#cursor.execute("SHOW DATABASES;")
cursor.execute("SHOW TABLES;")

for database in cursor.fetchall():
    print(database)

cursor.execute("SELECT * FORM games")

games = cursor.fetchall()

with open('game.json', 'w') as f:
    json.dump(games, f, indent=4)


for game in games:
    print(game[1])