"""
Autore: Nome Cognome
Data: gg/mm/aaaa
Titolo: Esercizio quattro:
    """

def calcola_e(ter):
    e = 0
    for x in range(0, ter+1):
        e += 1 / fattoriale(x)
    return e

def fattoriale(n):
    fatt = 1
    for x in range(1, n +1):
        fatt *= x
    return fatt

def main():
    termine = input('Inserire il numero di termini N per il calcolo di e: ')

    prova = termine.replace('.','')
    while not prova.isdigit():
        termine = input('Valore errato. Inserire un numero intero maggiore di 0: ')
        prova = termine.replace('.','')
        
    while '.' in termine:
        termine = input('Valore errato. Il numero deve essere intero e maggiore di 0: ')
    
    termine = int(termine)

    while not termine > 0:
        termine = input('Valore errato. Inserire un numero intero maggiore di 0: ')
        prova = termine.replace('.','')
        while not prova.isdigit():
            termine = input('Valore errato. Inserire un numero intero maggiore di 0: ')
            prova = termine.replace('.','')
        while '.' in termine:
                termine = input('Valore errato. Il numero deve essere intero e maggiore di 0: ')
    termine = int(termine)

    print(f"Usando {termine} termini il valore approssimato del numero di Nepero è {calcola_e(termine)}")

if __name__ == '__main__':
    main()