import mysql.connector

def connetti():
    DB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "Chinook"
    )

    return DB

def interroga(DB, query):
    #query = f"SELECT * FROM {tabella}"
    cursore = DB.cursor()
    cursore.execute(query)
    result = cursore.fetchall()
    return result

def disconnetti(DB):
    if DB:
        DB.close()
        print('connessione chiusa con successo')


def main():
    DB = connetti()
    if DB:
        print('connesso con successo')
        risultati_query = interroga(DB, "select * from Employee")
        print(risultati_query)
        disconnetti(DB)
    else:
        print('errore di connessione')


if __name__ == "__main__":
    main()