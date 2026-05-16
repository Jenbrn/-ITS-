"""
    Autore: Janice Brun
    Data: 15/05/2026
    Titolo: Scrivete un programma Python per rimuovere i duplicati dal dizionario.

"""
# Creazione del dizionario con duplicati

dizionario_duplicati = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 7, 'f': 'gatto', 'g': 'gatto'}

# Rimozione dei duplicati creando un nuovo dizionario

def logica(diz: dict) -> dict:
    """Funzione: funzione che accetta un dizionario e restituisce un nuovo dizionario senza duplicati
    
    Parametri:
        diz (dict): Il dizionario da cui rimuovere i duplicati
    
    Restituisce:
        dict: Un nuovo dizionario senza duplicati"""
    
    dizionario_singoli = {}
    while len(diz) > 0 and isinstance(diz, dict):
        for key, values in diz.items():
            if values not in dizionario_singoli.values():
                dizionario_singoli[key] = values

        return dizionario_singoli
    
# Creazione del dizionario senza duplicati

def main():
    """Funzione: funzione principale per eseguire il programma
    
    Parametri: nessuno
    
    Restituisce: stampa il dizionario senza duplicati creato dalla funzione logica
    """
    
    diz_pulito = logica(dizionario_duplicati)

    print("Dizionario senza duplicati:", diz_pulito)

if __name__ == "__main__":
    main()
        

