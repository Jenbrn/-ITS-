"""Autore: Janice Brun
Data: 12/04/2026
Titolo: Primo Esercizio
Scrivere un programma per rimuovere l'n- esimo carattere da una stringa non vuota.
Progettare una funzione che accetti la stringa, la posizione del carattere e restituisca la
stringa modificata."""

#Funzioni per la validazione degli input

def contrtollo_posiz(num: int):
    """Funzione: controlla che l'input sia un numero, che non sia negativo 
    e lo convert da str a int

    parametri: num : int
        finchè non viene passato un interio continua a richiedere input

    return : int : numero int non negativo
    """
    numy = controllo_val(num)
    prova = numy.replace('-','')
    while not prova.isdigit():
        numy = input("Inserisci il numero corrispondente alla posizione da del carattere da rimuovere, non una lettera: ")
        prova = numy.replace('-','')
        
    while int(numy) < 0:
        numy = input("Il numero si riferisce ad una posizione, non può essere negativo. Inserire nuovamente:  ")
    else:
        return int(controllo_val(numy))

def controllo_val(a):
    """
    Funzione: Valida che l'input non sia vuoto.Chiede ripetutamente un nuovo 
    input finché la stringa fornita contiene almeno un carattere.

    patametri : a : str : la stringa da validare

    return : str : una stringa con almeno un carattere  
    """
    while len(a) <= 0:
        a = input("L'input deve avere almeno 1 carattere: ")
    else:
        print(f"hai inserito {a}")
    return a

#Funzione main cpn inserimento input- elaborazione - output

def main():
    """
    Funzione principale del programma

    Chiede all'utente una stringa e la posizione di un carattere
    da rimuovere, valida entrambi gli input, rimuove il carattere
    alla posizione indicata e stampa il risultato.    
    """
    str = input("Inserisci una stringa: ")
    stringa = controllo_val(str)
    num_da_validare = input("Inserisci la posizione del carattere da rimuovere: ")
    numero = contrtollo_posiz(num_da_validare)

    a = stringa[0:numero]
    b = stringa[(numero + 1):]
    risultato = a + b
    print(f"La stringa meno il carattere corrisponde a {risultato}")


if __name__ == "__main__":
    main()
