"""Autore: Janice Brun
Data: 13/04/2026
Titolo: Primo Esercizio liste
Scrivere un programma python che rimuova gli elementi duplicati da una lista.
Esempio:
listaIN = [2, -4 ,5,6,5,5,2]
listaOUT=[2,-4,5,6]
"""
# Dati in input

listaIN = [2, -4 ,5,6,5,5,2,25,8,-5]
listaout = []

# Elaborazione

def smistamento(lista, output):
    """
    Funzione : prende una lista, la scorre e aggiunge ad una lista vuota solo i valori che non si ripetono

    Parametri : list 

    Return : list restituisce una lista con i valori filtrati
    """
    for val in lista:
        if val not in output:
            output += [val]
    return output

# Output

def main():
    """
    Funzione : Richiama la funzione smistamnto e stampa una lista senza duplicati
    """

    smistamento(listaIN, listaout)
    print(listaout)

if __name__ == '__main__':
    main()
