""" App per estrarre dati json """

#f = open('game.json', 'r', encoding='utf-8') #* encode / reference type
#f.close()
# priu pulito e evita di dimenticare il close

import json

#movies = json.load(open('game.json', 'r', encoding='utf-8'))

# with open('game.json', 'r', encoding='utf-8') as f:
#     for riga in f:
#         print(riga)

istruzioni_insert = []

#trasformazione e inserimento dati in collezione
with open('game.json', 'r', encoding='utf-8') as f:
    games = json.load(f)
    for game in games:
        nome  = str(game.get('Game', 'Nome gioco')).replace("'", "\\'")
        genere = game.get('Genere', 'Genere').replace("'", "\\'")
        publisher = game.get('Publisher').replace("'", "\\'")
        platform = game.get('Original platform(s)[a]').replace("'", "\\'")
        year = game.get('year', 0)
        year = int(year)

        istruzioni_insert.append(f"INSERT INTO games (nome, genere, publisher, platform, year) VALUES ('{nome}', '{genere}', '{publisher}', '{platform}', {year});")
        #print(f'Il nome del gioco è {nome}')

#preparo file sql x inserimento in db

query_tabella = """
USE its2026;

#DROP TABLE IF EXISTS games;
CREATE TABLE GAMES (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    genere  VARCHAR(100),
    publisher VARCHAR(100),
    platform  VARCHAR(100),
    year INT CHECK (year > 1960)
);

"""
with open('games.sql', 'w', encoding='utf-8') as f:
    f.write(query_tabella)

    for istruzione in istruzioni_insert:
        f.write(istruzione)
        f.write('\n')

print('elavorazione conclusa')
print('TOP')