"""Autore: Janice Brun
Data: 12/04/2026
Scrivere un programma che dica se una stringa è palindroma.
Esempio:
str="ABBA" PALINDROMA
str="PIPPO" NON PALINDROMA
"""
#Funzione controllo dell'input

def controllo_val(a):
    """
    Funzione: Valida che l'input non sia vuoto.Chiede ripetutamente un nuovo 
    input finché la stringa fornita contiene almeno due caratteri.

    patametri : a : str : la stringa da validare

    return : str : una stringa con almeno due caratteri
    """
    while len(a) < 1:
        a = input("L'input deve avere almeno 2 caratteri: ")
    else:
        print(f"hai inserito {a}")
    return a.lower()

#Funzione per l'inserimento input

def inserimento():
    """
    funzione : Richiede una stringa in input che verrà passata a main
    dopo aver validato con controllo_val che abbia almeno 2 caratteri

    parametri: input : str 

    return : una stringa tutta minuscolo con almeno due caratteri da passare a main
    """
    parola_da_validare = input('Inserisci una stringa per verificare se è palindroma(esc per uscire): ').lower()
    parola = controllo_val(parola_da_validare)
    return parola
    
#funzione principale

def main():
    """
    funzione : riceve una str in input e dopo aver controllato che contenga almeno 2 caratteri, aver fatto un 
    cast a minuscolo, inverte la str per controllare se è palindroma.

    parametri : parola : str 

    return: una fstring che scrive la parola inserita quando palindroma
    
    """
    parola = inserimento()
    while parola != parola[::-1]:
        if parola == 'esc':
            break
        print('LA parola da te scelta non è palindroma: ')
        parola = inserimento()
        
    else:
        print(f"{parola} è palindorma!")


if __name__ == '__main__':
    main()