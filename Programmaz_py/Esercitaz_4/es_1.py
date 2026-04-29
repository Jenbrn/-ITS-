"""
Autore: Janice Brun
Data: 29/04/2026
Titolo: Scrivere un programma per rimuovere l'n- esimo elemento da una tupla non vuota
"""
#Funzione inserimento input

def creazioneTup()-> tuple:
    """
    Funzione :     Crea una tupla raccogliendo elementi da input dell'utente.
        Si ferma quando l'utente digita 'miao'.

    Return: Tuple
        Tupla con gli elementi inseriti
    """
    tupla = ()
    elemento = input("Inserisci un elemento da inserire nella tupla, miao per uscire: ").lower()
    while 'miao' not in elemento :
        tupla += (elemento, )
        elemento = input("Inserisci un elemento da inserire nella tupla, miao per uscire: ").lower()
    else:
        return tupla

# Funzioni di controllo

def controllo_posiz(num: int) ->int:
    """
    Funzione: Valida e converte l'input a numero intero, controllando che sia un numero valido.

    Argomenti: num : int
        Numero da validare.
    
    Return: numy : int
        Numero intero validato.
    """
    numy = controllo_val(num)
    prova = numy.replace('-','')
    while not prova.isdigit():
        numy = input("Inserisci il numero corrispondente alla posizione da del carattere da rimuovere, non una lettera: ")
        prova = numy.replace('-','')
        
    return int(controllo_val(numy))

def controllo_val(a: int) -> int:
    """
    Funzione: Controlla che l'input non sia vuoto, richiede reinserimento se necessario.

    Argomenti: a :int 
        Valore da controllare

    Return: a: int 
        Valore validato non vuoto.
    """
    while len(a) <= 0:
        a = input("Devi assegnare un valore numerico: ")
    else:
        return a

#Funzione principale 

def main() -> str:
    """
    Funzione principale che crea una tupla, rimuove un elemento 
    alla posizione specificata e stampa il risultato.
    """
    tupla = creazioneTup()
    num_da_validare = input("Inserisci la posizione dell'elemento da rimuovere: ")
    numero = controllo_posiz(num_da_validare)
    print(tupla)

    p1 = tupla[:(numero -1)]
    p2 = tupla[numero:]
    ris = p1 + p2
    print(f"La tupla risultante è {ris}")

if __name__ == "__main__":
    main()

