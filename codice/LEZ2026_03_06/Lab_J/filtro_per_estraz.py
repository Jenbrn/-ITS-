""" Lab - Strutture Dati  """

# lista no eterogena con elementi ripetibili e un indicizzatav e 0 based
#citta = ['torino', 'Roma', 'Milano', 'Livorno'] 

#tupla immutabile, indicizzata e 0 based
#
#citta = ('torino', 'Roma', 'Milano', 'Livorno')

# set non ammette duplicati
citta = {'torino', 'Roma', 'Milano', 'Livorno'}

#citta.add('genova')
#print(citta)

#ctrl D selezionare tutte ad esempio virgole( simboli =)
#alt ctrl multiselez
#ctrl maiusc selez blocchi solo shift uno alla volta
#DIZIONARIO
#verticalmente le chiavi sono viste come un set(non ammettono duplicati)
#i valori possono ammettere lista
#citta.append('cumiana')

# print(type(citta))

# #visualizza elementi con dunderscore / cosa posso fare
#print(dir(citta))

# print(dir(citta))
# pop elimina ultimo elemento della lista
#append aggiunge un elemento fondo lista

regioni_1 = {
    "piemonte" : "Torino",
    "Liguria" : "Genova",
    "Lombardia" : "Milano",
    "Lazio" : "Roma"
}

regioni = {
    "piemonte" : ["Torino", " Alessandria", "Asti"],
    "Liguria" : ["Genova", "Savona", "Ventimiglia"],
    "Lombardia" : ["Milano", "Como", "Pavese"],
    "sicilia" : ["Palermo", "Siracusa", "Trapani"]
}

# print(regioni_1)
# print(type(regioni_1))
# print(dir(regioni_1))

# #for city in citta:
# #    print(city)

#for regione in regioni:
#    print(regione)

#for regione in regioni.keys():
#    print(regione)
#restituisce chiavi

#for regione in regioni.values():
#    print(regione)
#restituisce valore

#for regione in regioni.items():
#    print(regione)
#restituisce blocco chiave valore

#for regione, comuni in regioni.items():
#    print(f"La ragione {regione} ha i seguenti comuni: {comuni}")

for regione in regioni.keys():
    #print(f"La regione {regione} ha i suoi comuni: {regioni.get(regione, "regione sconosciuta")}")
    #get permette di inserire un valore di default
    #print(f"La regione {regione} ha i suoi comuni: {regioni[regione]}")


    print(f"La regione {regione} ha i seguenti comuni")
    for comune in regioni.get(regione):
        print(comune)