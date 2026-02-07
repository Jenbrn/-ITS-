
libri = []

source = open("database\\librii.csv", 'r')

for riga in source:
    riga_splittata = riga.split(",")
    titolo = riga_splittata[0].replace('"', '')
    pagine = int(riga_splittata[2].replace('"', ''))
    prezzo = float(riga_splittata[4].replace('"', ''))
    print(f"Il liblro {titolo} ha {pagine} pagine e costa {prezzo} eu")
    libri.append([titolo, pagine, prezzo, 1])

source.close()

f = open("insert_liri.sql", "w")

for libro in libri:
    titolo = str(libro[0]).replace("'", "\\'")
    pagine = libro[1]
    prezzo = libro[2]
    editore_id = libro[3]
    f.write(f"insert into libri set titolo = '{titolo}', pagine = '{pagine}', prezzo = {prezzo}, editore_id = {editore_id};\n")

f.close()


#torvare una strategia per editore    














# f = open("insert_liri.sql", "w")

# for libro in libri:
#     titolo = str(libro[0]).replace("'", "\\'")
#     pagine = libro[1]
#     prezzo = libro[2]
#     editore_id = libro[3]
#     f.write(f"insert into libri set titolo = '{titolo}', pagine = '{pagine}', prezzo = {prezzo}, editore_id = {editore_id};\n")

# f.close()

