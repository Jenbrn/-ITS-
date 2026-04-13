"""Autore: Janice Brun
Data: 13/04/2026
Titolo: Scrivere un programma che date due liste stampi "OK" se hanno almeno un membro
comune altrimenti stampi "KO".
- lista1=[1,5,8] lista2=[3,1,10] -> output: "OK"
- lista1=[1,5,8] lista2=[3,11,10] -> output: "KO"
"""

# Dati di input

lista1 = [1,5,8]
lista2 = [3,1,10]
lista3 = [3,11,10]

# Funzione di elaborazione

def verifica(l1: list,l2: list): 
    """ Funzione : Scorre uno a uno i valori in una lista e controlla se sono presenti in una seconda lista.
        Se trova una valore comune aumenta di 1 il calore della variabile contatore. Se il valore della var contatore
        è maggiore di 0 c'è almeno un membro in comune e stampa ok, diversamente ko

        Parametri : list

        Return : Str : ok se trova almeno un membro comune, ko se non ne trova  
    """
    contatore = 0
    for val in l1:
        if val in l2:
            contatore += 1
    if contatore > 0:
        return print('OK')
    else:
        return print('KO')

# Funzione main

def main():
    """Funzione : verifica la presenza o assenza di valori comuni tra due liste richiamando la funzione verifica

       Return : Restituisce il risultato del confronto 
    """
    a = verifica(lista1,lista2)
    b = verifica(lista1, lista3)
    c = verifica(lista2, lista3)
    return a, b, c

if __name__ == '__main__':
    main()