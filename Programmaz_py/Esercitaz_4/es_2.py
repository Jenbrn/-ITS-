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
    while len(a) < 1:
        a = input("L'input deve avere almeno 1 carattere: ")
    else:
        print(f"hai inserito {a}")
    return a

#Funzione inserimento input

def inserimento() -> tuple:
    tpl = ()
    parola_da_validare = controllo_val(input('Inserisci una stringa per verificare (esc per uscire): ').lower())
    # parola = controllo_val(parola_da_validare)
    while parola_da_validare != 'esc':
        tpl += (parola_da_validare, )
        parola_da_validare = controllo_val(input('Inserisci una stringa per verificare (esc per uscire): ').lower())
    return tpl

# Funzione principale
def main():
    tpleIN = inserimento()
    tplOUT = tpleIN[::-1]
    print(tpleIN, tplOUT)

if __name__ == '__main__':
    main()