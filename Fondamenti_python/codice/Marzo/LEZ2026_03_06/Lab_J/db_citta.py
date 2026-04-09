""" DATABASE CITTA """

#import json
# regionipy = json.dumps(regioni)

# regionijson = json.loads(regionipy)

# print(regionipy)
# print(regionijson)

import sqlite3
#permette di lavorare con db semplificato

regioni = {
    "Piemonte" : ["Torino", " Alessandria", "Asti"],
    "Lombardia" : ["Milano", "Como", "Pavese"],
    "Liguria" : ["Genova", "Savona", "Ventimiglia"],
    "Veneto" : ["Venezia", "Verona", "Treviso"],
    "Toscana" : ["Livorno", "Firenze", "Pisa"],
    "Sicilia" : ["Palermo", "Siracusa", "Trapani"]
}

db = sqlite3.connect("regioni.db")

cursor = db.cursor()
#meccanismo intrno db che permette di scorrere a fare operazioni iterne ad db

query = """
    CREATE TABLE IF NOT EXISTs regioni(
        regione_id integer primary key autoincrement,
        nome text not null,
        capoluogo text not null     
        );

"""
#cursor.execute(query)


cursor.execute(query)


for regione in regioni:
    query = f"INSERT INTO regioni (nome, capoluogo) VALUES ('{regione}', '{regioni.get(regione)[0]}');"
    cursor.execute(query)


db.commit()
















