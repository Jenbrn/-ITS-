"""Autore: Janice Brun
Data: 13/04/2026
Titolo: Scrivi un programma per trovare il secondo numero più piccolo in una lista
"""
# Input

listadis = [2, 6, 18, -2 , 25, 1]

# Elaborazione

def riordino(lista: list):
    """
    Funzione : riordina una lista di numeri e restituisce il secondo più piccolo
    
    Parametri : list : richiede una lista in input
    
    Return : Restituisce il secondo numero più piccolo
    """
    lista_asc = sorted(lista)
    return lista_asc[1] 

# Output

def main():
    """
    Funzione : richiama la funzione riordino su una lista per stampare il secondo numero più piccolo
    """
    print(F"Data la lista contenente i numeri {listadis} il secondo più piccolo è {riordino(listadis)}")

if __name__ == '__main__':
    main()
    
"""
def miao(a):
    miao = 0
    prova = []
    listinoz = sorted(a)
    while miao < 2:
        for n in listinoz:
            if n < n+1:
                prova += [n]
                miao += 1
        return print(prova)

"""