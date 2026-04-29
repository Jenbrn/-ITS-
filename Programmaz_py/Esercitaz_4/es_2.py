"""
Autore: Janice Brun
Data: 29/04/2026
Titolo: Scrivere un programma per invertire una tupla
Esempio:
tpleIN=('a', 'c', 'f')
tpleOUT=('f', 'c', 'a')
"""
#Controllo input

def controllo_val(a: str) -> str:
    """
    Funzione: Valida che l'input non sia vuoto.

    Argomenti: a : str
        Stringa da validare.

    Return: a : str
        Stringa validata.
    """
    while len(a) < 1:
        a = input("L'input deve avere almeno 1 carattere: ")
    else:
        print(f"hai inserito {a}")
    return a

#Funzione inserimento input

def inserimento() -> tuple:
    """
    Funzione:  Raccoglie stringhe da input finché l'utente digita 'esc'

    Returns: tuple
        Tupla con le stringhe inserite.    
    """
    tpl = ()
    parola_da_validare = controllo_val(input('Inserisci una stringa per verificare (esc per uscire): ').lower())

    while parola_da_validare != 'esc':
        tpl += (parola_da_validare, )
        parola_da_validare = controllo_val(input('Inserisci una stringa per verificare (esc per uscire): ').lower())
    return tpl

# Funzione principale
def main():
    """
    Crea una tupla e ne stampa il rovescio.
    """
    tpleIN = inserimento()
    tplOUT = tpleIN[::-1]
    print(tpleIN, tplOUT)

if __name__ == '__main__':
    main()