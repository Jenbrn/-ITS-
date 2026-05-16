"""
    Autore: Janice Brun
    Data: 15/05/2026
    Titolo: Scrivete un programma Python per ottenere il valore massimo e minimo in un dizionario
    
"""

# Creazione del dizionario con valori numerici

dizionario = {'a': 1, 'b': 25, 'c': 12, 'd': 18}

# Funzione per ottenere il valore massimo e minimo dal dizionario

def logica(diz: dict) -> tuple:
    """Funzione: funzione che accetta un dizionario e restituisce il valore massimo e minimo
    
    Parametri:
        diz (dict): Il dizionario da cui ottenere il valore massimo e minimo
    
    Restituisce:
        tuple: Una tupla contenente il valore massimo e minimo del dizionario"""
    top = max(diz.values())
    minimo = min(diz.values())
    return top, minimo

# Funzione principale per eseguire il programma

def main():
    max, min = logica(dizionario)
    print(F"Il valore massimo è {max} e il valore minimo è {min}")

if __name__ == '__main__':
    main()