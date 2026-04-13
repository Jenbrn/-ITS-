from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Chinook"
)

# @app.get("/studenti")
# def studenti():
#     studente = {"nome": "pippo", "eta": 25, "data_nascita": "2000-04-13"}
#     return studente

@app.get("/artists")
def artisti():
    cursore = db.cursor(dictionary=True)

    cursore.execute("SELECT * from artist")

    artisti = cursore.fetchall()

    return artisti


@app.get("/albums")
def album():
    # cursore = db.cursor(dictionary=True)
    cursore = db.cursor()

    query = """
    select 
	ar.Name, a.Title
    from album a
    join artist ar using (ArtistId)
    ;
    """

    cursore.execute(query)
    album = cursore.fetchall()

    return jsonify(album)#miao









app.run(debug=True, port=5000)