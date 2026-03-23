"""GESTIONE RQE HTTP"""

import requests
from film import Film


URL = "https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/film/imdb_top_2000_movies.json"

resp = requests.get(URL)

if resp.status_code == 200:
    elenco = resp.json()
    for movie in elenco:
        title = movie['Movie Name']
        director = movie['Director']
        year = movie['Release Year']
        rating = movie['IMDB Rating']
        f = Film(title, director, year, rating)
        print(f)





