"""citta"""

import sqlite3

query = "select * from regioni;"
db = sqlite3.connect("regioni.db")

cursor = db.cursor()

cursor.execute(query)

result = cursor.fetchall()
#print(result)

for riga in result:
    print(f"il capoluogo della regione {riga[1]} è: {riga[2]}")