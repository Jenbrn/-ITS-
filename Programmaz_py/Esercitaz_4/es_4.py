"""
Autore: Janice Brun
Data: 29/04/2026
Titolo: Scrivere un programma per contare gli elementi in una lista finché non si incontra un
elemento di tipo tupla. [Suggerimento: si usi la funzione isinstance( ) ]

"""
#Sezione input

lista = [ 'cane',(1,1,1), 42, 'gatto', (1,2,3), 'rosso', 99 ]

#Funzioni controllo ed elaborazione

def analisi(lista: list) -> str:
    """
    Funzione: Trova la posizione della prima tupla in una lista.
    Ritorna un messaggio con la posizione o un avviso se non trovata.
    
    Argomenti: lista: list
        Lista da analizzare.
    
    Returns: str
        Messaggio con posizione della tupla / avviso di lista vuota/nessuna tupla.
    """
    while controllo(lista) != False:
        for numero, elemento in enumerate(lista):
            if isinstance(elemento, tuple):
                return f"L'elemento numero {numero + 1} è una tupla"
    
        return "Nessuna tupla trovata"
    else:
        return "Hai inserito una lista vuota"
         
def controllo(lis: list) -> bool:
    """
    Funzione: controlla se la lista non è vuota.
    
    Args: lis: list
      Lista da controllare.
    
    Returns: bool
       False se vuota True se non lo è
    """
    if len(lis) == 0:
        return False
        
#Funzione output

def main():
    print(F"{analisi(lista)}")
   

if __name__ == '__main__':
    main()