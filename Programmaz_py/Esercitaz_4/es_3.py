"""
Autore: Janice Brun
Data: 29/04/2026
Titolo: Scrivere un programma per sostituire l'ultimo valore delle liste in una tupla con un valore
richiesto in input.
Esempio:
valore : 100
TuplaIN: ([10, 20, 40], [40, 50, 60], [70, 80, 90])
TuplaOUT: ([10, 20, 100], [40, 50, 100], [70, 80, 100])
"""

# Inserimento input
def inserimento1() -> tuple:
    """
    Funzione : Crea 3 liste mediante input dell'utente che vangono aggiunti ad una tupla.
        L'utente inserisce elementi in ogni lista finché non digita 'miao'.
        Si una un counter per rendere più semplice l'inserimento per l'utenete

    Return : Tuple
        Tupla contenente 3 liste di elementi inseriti dall'utente.
    """
    tupla =()

    counter = 0
    for ins in range(3):
        counter += 1
        lista = []
        lista_da_inserire = validazione(input("Crea 3 liste da inserire in una tupla( miao per passare alla lista dopo): ").lower())
        while lista_da_inserire != 'miao':
            lista.append(lista_da_inserire)
            lista_da_inserire = validazione(input("Crea 3 liste da inserire in una tupla( miao per passare alla lista dopo): ").lower())

        print(F"Lista {counter} inserita: {lista}")
        tupla += (lista, )

    return tupla
    
    
def inserimento2() -> list:
    """
    Funzione: Richiede l'inserimento di 3 elementi da sostituire all'ultimo elemento delle
        liste interne alla tupla

    Return : list
        Lista coi 3 elementi di sostituzione
    """
    sostituti = []

    for e in range(3):
        elemento = validazione(input('Iserisci un elemento da sostituire all\'ultimo valore di ogni lista creata : '))
        sostituti.append(elemento)
    return sostituti

# Validazione input
def validazione(a) -> str:
    """
    Funzione: Valida che l'input abbia almeno un carattere

    Argomenti: input utente (str)
        stringa da validare

    Return : str
        una stringa validata
    """
    while len(a) <= 0:
        a = input("non puoi lasciare l'input vuoto: ")
    else:
        return a

#Funzione principale con output
def main() -> tuple:
    """
    Sostituisce gli ultimi elementi di ogni lista nella tupla.
    """
    tupla = inserimento1()
    sost1, sost2, sost3 = inserimento2()

    tupla[0][-1] = sost1
    tupla[1][-1] = sost2
    tupla[2][-1] = sost3
    print(tupla)
    return tupla
    

if __name__ == '__main__':
    main()