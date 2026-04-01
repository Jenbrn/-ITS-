"""
Autore: Janice Brun
Data: 29/03/2026
Titolo: Esercizio quattro:
    4.a Scrivere una funzione che restituisca un valore approssimato di e all'ennesimo termine,
    dove N è inserito come parametro formale alla funzione. La funzione calcola_e deve richiamare la funzione di calcolo del fattoriale.
    Scrivere il codice della funzione e il programma principale che la chiama chiedendo in input
    il numero N.

    """

def calcola_e(ter):
    """Funzione: Calcola l'approssimazione del numero di Nepero

       Parametri : ter -> (int) Numero di termini da unare nella somma 
    
       Return : (float) -> il valore approssimato di e 
    """
    e = 0
    for x in range(0, ter+1):
        e += 1 / fattoriale(x)
    return e

def fattoriale(n):
    """Funzione : calcola il fattoriale di un numero intero non negatio.

       Parametri : n : (int) > 0

       Return :  (int) -> Il fattoriale ni n (n!)
    
    """
    fatt = 1
    for x in range(1, n +1):
        fatt *= x
    return fatt

def main():
    """Funzione : corpo  principale del programma. Richiede in input
       un numero int positivo, esegue controllo su intero e valori inseriti per
       poter fare un cast da str a int. 
       
       Return: Calcola e stampa il valoe approssimato del numero di Nepero
       usando n tentativi
    
    """
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