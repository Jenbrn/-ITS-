"""STRUTTURE DATI: liste , tuple, set, dict"""

def analizza(collezione):
    print("#elementi", len(voti))
    print("Tipo del dato", type(voti))
    # print('metodi disponibili', help(voti))

#list -> mutabile 
voti = [25, 29,26]


#tuple -> immutabile 
voti = (25, 29, 26)

#set -> unordere collection - ma unique
voti = {25, 29, 26}

#dict -> collezione chiave : valore
voti = {
    'python' : 25,
    'java' : 29,
    'c#' : 26,  
}
analizza(voti)
print(voti.keys)