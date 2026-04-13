"""Autore: Janice Brun
Data: 13/04/2026
Titolo: Scrivere un programma Python per dividere una data lista in due parti in cui viene data la
lunghezza della prima parte della lista.
Esempio:
Lista originale: [1, 1, 2, 3, 4, 4, 5, 1]
Lunghezza della prima parte della lista: 3
Output : Prima parte: [1, 1, 2] ,
Seconda parte: [3, 4, 4, 5, 1]
"""

# Dati di input

lista_originale = [1, 1, 2, 3, 4, 4, 5, 1]
divisore = 3

# Funzioni elaborazione

def divisione(lista: list , div: int) -> list:
    """
    Funzione : Divide una lista basandosi sul valore di div 

    Parametri : lista : list
                div : int

    Return : firsthalf : list
             secondhalf : list
             due liste con la list passata nel paramtro list frazionata in posizione corrispondente a div
    """
    firsthalf = lista[0:(div)]
    secondhalf = lista[(div):]
    return firsthalf, secondhalf 

# Funzione output

def main():
    """
    Funzione : Richiama la funzione divisione() per avere la lista originale divisa in due

    Return : Stampa due liste corrispondenti a due frazioni della lista originaria    
    """
    inizio, fine = divisione(lista_originale, divisore)
    print(f"""Dividendo la lista {lista_originale} dopo il valore in posizione {divisore} otteniamo:
    -{inizio} come prima metà 
    -{fine} come seconda metà""")

if __name__ == "__main__":
    main()