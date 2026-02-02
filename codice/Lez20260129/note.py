studenti = []

f = open('./studenti.txt')

for riga in f:
    # riga_trasformata = riga.replace('\n', '')
    # riga_trasformata = riga_trasformata.replace('\t', '-')
    # studenti.append(riga_trasformata)
    #meglio

    riga = riga.replace('\n', '')#sosttuisci senza rinominare
    riga = riga.replace('\t', ',')#csd comma separated
    studenti.append(riga)

    # riga_trasformata = riga[0:10]
    # studenti.append(riga_trasformata)
   
    # studenti.append(riga)


# print(type(f))
#    print(riga)


f.close()#senza f

f = open('studenti.sql', 'w')#?

query_tabella = """
DROP TABLE IF EXIST studenti;\n

CREATE TABLE studenti(\n
    id int primary key auto_increment, \n
    nome varcher(30) not null,\n
    cognome varchar(50) not null

    );

"""

f.write(query_tabella)
for s in studenti:
    s = str(s)
    pezzi = s.split(',')
    nome = pezzi[0]
    cognome = pezzi[1]
    f.write(f"insert into studenti (nome, cognome) value('{nome}', '{cognome}');\n")

f.close()


# for studente in studenti:
#     print(studente)