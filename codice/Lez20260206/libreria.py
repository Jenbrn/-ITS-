
libri = [
    ['l\'uomo ragno', 120, 15, 2],
    ['la donna ragno', 150, 25, 2],
    ['ll bambino ragno', 220, 35, 2],
    ['l\'insetto ragno', 80, 10, 1],
    ['l\'opossum grigio', 320, 45, 1]  
]

f = open("insert_liri.sql", "w")

for libro in libri:
    titolo = str(libro[0]).replace("'", "\\'")
    pagine = libro[1]
    prezzo = libro[2]
    editore_id = libro[3]
    f.write(f"insert into libri set titolo = '{titolo}', pagine = '{pagine}', prezzo = {prezzo}, editore_id = {editore_id};\n")

f.close()

