"""
    Autore: Nome Cognome
    Data: gg/mm/aaaa
    Titolo: Testo esercizio:
    Primo Esercizio
    Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la
    restituisca espressa solamente in secondi. Successivamente creare un programma
    principale che chieda in input due quantità di tempo e stampi in output quale quantità di
    tempo è maggiore. La funzione deve avere i parametri formali con valori predefiniti.
"""
def calcola_secondi(a: int, b: int, c: int) -> int:
    sec_min = b * 60
    sec_ore = (a * 60) * 60
    return sec_ore + sec_min + c


# tempo = input("Inserire una quantità di tempo in formato ore, minuti e secondi usando : come separatore: ")

# ore, minuti, secondi = tempo.split(':')
# ore, minuti, secondi = map(int, (ore, minuti, secondi))

# if minuti > 59 or secondi > 59:
#     tempo = input("Non è possibile avere più di 60 minu o/e 60 sec. Reinserire l'input: ")
# print(ore, minuti, secondi)

# Risultato = calcola_secondi(ore, minuti, secondi)
# print(Risultato)


verificatore = False

while verificatore != True:
    tempo = input("Inserire una quantità di tempo in formato ore, minuti e secondi usando : come separatore: ")

    ore, minuti, secondi = tempo.split(':')
    ore, minuti, secondi = map(int, (ore, minuti, secondi))

    if minuti > 59 or secondi > 59:
        tempo = input("Non è possibile avere più di 60 minu o/e 60 sec. Reinserire l'input: ")

    elif ore < 0 or minuti < 0 or secondi < 0:
        tempo = input("impossibile avere valori tempo negativi")     
    verificatore = True

print(ore, minuti, secondi)

Risultato = calcola_secondi(ore, minuti, secondi)
print(Risultato)











