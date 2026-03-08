""" Musica jenson"""

import json

estrazione = []

with open('musica.json', 'r', encoding= "utf8") as f:
    music = json.load(f)
    for musica in music:
        
        titolo = str(musica.get('titolo', 'titolo').replace("'", "\\'"))
        artista = musica.get('artista', 'artista').replace("'", "\\'")
        album = musica.get('album', 'album').replace("'", "\\'")
        genere = musica.get('genere', 'genere').replace("'", "\\'")
        certificazione = musica.get('certificazione').replace("'", "\\'")
        anno = musica.get('anno', 0)
        anno = int(anno)
        durata_secondi = musica.get('durata_secondi')
        durata_secondi = int(durata_secondi)

        estrazione.append(f"INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('{titolo}', '{artista}', '{album}', '{genere}', '{certificazione}', '{anno}', '{durata_secondi});")

        