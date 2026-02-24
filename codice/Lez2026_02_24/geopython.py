""" Geografia by python """

regioni = {
    'Piemonte' : ['Torino', 'Cuneo', 'Asti', 'Alessandria'],
    'Liguria'  : ['Genova', 'Savona', 'Imperia', 'La spezia']
}

#le chiavi non si possono ripetere, i valori in vece si

#print(help(regioni))

chiavi = regioni.keys()
valori = regioni.values()

#print(chiavi)
#print(valori)

# for chiave in chiavi:
#     print(chiave)
#     print(regioni.get(chiave))

for chiave, valore in regioni.items():
    print(f'La regione {chiave} ha i seguenti comuni capoluogo: {valore}')


for regione, comuni in regioni.items():
    print(f'La regione {regione} ha i seguenti comuni capoluogo: {comuni}')