"""
    Autore: Janice Brun
    Data: 15/05/2026
    Titolo: Scrivete un programma Python per creare un dizionario da una stringa. Le lettere della
    stringa rappresentano le chiavi, i valori rappresentano le occorrenze della chiave nella
    stringa
    Esempio
    stringa = “ciao mamma”'
    Dizionario: {'c': 1, 'i': 1, 'a': 3, 'o': 1, ' ':1,'m': 3}

    
"""
# Creazione della stringa da cui generare il dizionario

stringa = 'Tanto va la gatta al lardo che ci lascia lo zampino'

# Funzione per creare un dizionario da una stringa

def logica(stringa: str) -> dict:
    """Funzione: funzione che accetta una stringa e restituisce un dizionario con le lettere come chiavi e le occorrenze come valori
    
    Parametri:
        stringa (str): La stringa da cui creare il dizionario
    
    Restituisce:
        dict: Il dizionario con le lettere come chiavi e le occorrenze come valori
    """
    dizionario = {}

    while len(stringa) > 0 and isinstance(stringa, str):
        for key in stringa:
            if key not in dizionario:
                dizionario[key] = 1
            else:
                dizionario[key] += 1
        
        return dizionario
    else:
        print("La stringa è vuota o non è una stringa")

# Funzione principale per eseguire il programma

def main():
    """Funzione: funzione principale per eseguire il programma
    
    Parametri: nessuno

    Restituisce: stampa il dizionario creato dalla stringa
    """
    dizionario = logica(stringa)
    print(dizionario)

if __name__ == '__main__':
    main()