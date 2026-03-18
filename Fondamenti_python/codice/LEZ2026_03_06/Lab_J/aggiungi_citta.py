""" aggiungi città """
import sqlite3

while True:
    regione = input("Inserisci il nome della regione (q per uscire): ")
    if regione.lower() == 'q':
        break

    capoluogo = input("Inserisci il nome del capoluogo: ")
    query = "INSERT INTO regioni (nome, capoluogo) VALUES (?,?)"#prepared statement
    values = (regione, capoluogo)

    db = sqlite3.connect("regioni.db")

    cursor = db.cursor()

    cursor.execute(query, values)

    db.commit()

    print('record inserito con successo')
