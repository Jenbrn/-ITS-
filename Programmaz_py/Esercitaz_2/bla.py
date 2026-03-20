"""
    Autore: Nome Cognome
    Data: gg/mm/aaaa
    Titolo: Testo esercizio:
    Primo Esercizio
    Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la
    restituisca espressa solamente in secondi. Successivamente creare un programma
    principale che chieda in input due quantità di tempo e stampi in output quale quantità di
    tempo è maggiore. La funzione deve avere i parametri formali con valori predefiniti.
"""

def calcola_secondi(a: int, b: int, c: int) -> int:
    sec_min = b * 60
    sec_ore = (a * 60) * 60
    return sec_ore + sec_min + c

def estrai_sec():      
        tempo = input("Inserire una quantità di tempo in formato ore, minuti e secondi usando : come separatore: ")

        ore, minuti, secondi = map(int, tempo.split(':'))
       
        while minuti > 59 or minuti < 0 or secondi > 59 or secondi < 0:
            if minuti > 59 or secondi > 59:
                tempo = input("Non è possibile avere più di 60 min o/e 60 sec. Reinserire l'input: ")
                ore, minuti, secondi = map(int, tempo.split(':'))
            elif minuti < 0 or secondi < 0:
                tempo = input("Non si possono avere valori negativi su min e/o sec: ")
                ore, minuti, secondi = map(int, tempo.split(':'))
            
        return calcola_secondi(ore, minuti, secondi)
                
        

def main():
    primo = estrai_sec()
    secondo = estrai_sec()
    return print(max(primo, secondo))


if __name__ == "__main__":
    main()





