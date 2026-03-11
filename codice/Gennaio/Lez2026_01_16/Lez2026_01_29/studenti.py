<<<<<<< HEAD

studenti = []

f = open('./studenti.txt')

for riga in f:
    riga = riga.replace('\n', '')
    riga = riga.replace('\t', ',')
    studenti.append(riga)

f.close()#senza f
=======
studenti = []

f = open('studenti.txt')

for riga in f:
    # print(riga)
    # per ogni riga del file aggiungo la riga alla lista studenti
    riga = riga.replace("\n", "")
    riga = riga.replace("\t", ",")
    studenti.append(riga)

f.close()
>>>>>>> 5a4e5586cb06949fe8f08349b909c4c7b9c027c8

f = open('studenti.sql', 'w')

query_tabella = """
<<<<<<< HEAD
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

=======
DROP TABLE IF EXISTS studenti;\n\n

CREATE TABLE studenti(\n
    id int primary key auto_increment,\n
    nome varchar(30) not null,\n
    cognome varchar(50) not null\n
);\n\n

"""
f.write(query_tabella)

for s in studenti:
    s = str(s)
    pezzi = s.split(",")
    nome = pezzi[0]
    cognome = pezzi[1]
    f.write(f"insert into studenti (nome, cognome) value ('{nome}', '{cognome}');\n")
    # print(f"Il nome dello studente è {nome} e il cognome è {cognome}")
>>>>>>> 5a4e5586cb06949fe8f08349b909c4c7b9c027c8
f.close()

