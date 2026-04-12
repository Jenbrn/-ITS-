"""Primo Esercizio
Scrivere un programma python che rimuova gli elementi duplicati da una lista.
Esempio:
listaIN = [2, -4 ,5,6,5,5,2]
listaOUT=[2,-4,5,6]
"""

listaIN = [2, -4 ,5,6,5,5,2]
listaout = []

def smistamento():
    for val in listaIN:
        if val not in listaout:
            listaout += [val]

print(listaout)