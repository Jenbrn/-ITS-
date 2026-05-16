"""
    Autore: Janice Brun
    Data: 15/05/2026
    Titolo: Scrivete uno script Python per generare e stampare un dizionario che contenga un numero
    (compreso tra 1 e n) nella forma (x, x*x).
    Esempio:
    n = 5
    Dizionario: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""
# Creazione della funzione che genera un dizionario con i numeri da 1 a n nella forma (x, x*x)

def logica():
    """Funzione: funzione che genera e restituisce un dizionario che contenga un numero (compreso tra 1 e n) nella forma (x, x*x)
    
    Parametri: nessuno
    
    Restituisce:
        dict: Un dizionario che contiene i numeri da 1 a n nella forma (x, x*x)"""
    dizionario = {}

    for key in range(1,6):
        dizionario[key] = key ** 2
    return dizionario

# Funzione principale per eseguire il programma

def main():
    """Funzione: funzione principale per eseguire il programma
    
    Parametri: nessuno
    
    Restituisce: stampa il dizionario generato dalla funzione logica"""
    dizionario = logica()
    print(dizionario)

if __name__ == '__main__':
    main()