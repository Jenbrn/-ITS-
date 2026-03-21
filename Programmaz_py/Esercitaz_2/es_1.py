"""
    Autore: Janice Brun
    Data: 21/03/2026
    Titolo: Testo esercizio:
    Primo Esercizio
    Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la
    restituisca espressa solamente in secondi. Successivamente creare un programma
    principale che chieda in input due quantità di tempo e stampi in output quale quantità di
    tempo è maggiore. La funzione deve avere i parametri formali con valori predefiniti.
"""

def calcola_secondi(a: int = 0, b: int = 0, c: int = 0) -> int:
    """Funzione : converte tre valori che rappresntano ore minuti e secondi
       nella somma dei secondi che li compongono
    
    Parametri :
        a : int, optional, default 0 . Rappresenta ore
        b : int, optional, default 0 . Rappresenta Min
        c : int, optional, default 0 . Rappresenta sec
    
    Return :
        Int : Restituisce somma di secondi presenti in min + sec presenti in
              ore + secondi passati in iput    
    """
    sec_min = b * 60
    sec_ore = (a * 60) * 60
    return sec_ore + sec_min + c

def estrai_sec():
        """Funzione : Richiede in input 3 valori interi con : come sepratore
           Split separa la stringa e map(int) esegue un cast su ogni elemento
           che viene poi assegnato alle variabili ore - minuti - secondi.

           Utilizzo un promo ciclo while per filtrare input con separatore mancante o incompleti

           Utilizzo secondo ciclo While per verificare che i numeri inseriti siano 
           in un range tra 0 e 59 escludendo negativi e superiori di 59. Si esce
           dal ciclo solo quando i valori inseriti saranno tra 0 e 59

           Return :
                Chiama la funzione Calcola_secondi e li inserisce come parametri della funz.
                restituisce il totale dei secondi presenti nel tempo inserito in input              
        """     
        tempo = input("Inserire una quantità di tempo in formato ore, minuti e secondi usando : come separatore: ")

        while len(tempo.split(':')) != 3:            
            tempo = input("Inserimento errato, valore mancante. Necessario inserire 3 valori in formato ore, minuti e secondi usando : come separatore: ")
       
        ore, minuti, secondi = map(int, tempo.split(':'))
       
        while minuti > 59 or minuti < 0 or secondi > 59 or secondi < 0:
            if minuti > 59 or secondi > 59:
                tempo = input("Non è possibile avere più di 60 min o/e 60 sec. Reinserire l'input: ")
                ore, minuti, secondi = map(int, tempo.split(':'))
            elif minuti < 0 or secondi < 0:
                tempo = input("Non si possono avere valori negativi su min e/o sec: ")
                ore, minuti, secondi = map(int, tempo.split(':'))
            
        print(F"Hai inserito: {ore} h - {minuti} min - {secondi} sec")
        return calcola_secondi(ore, minuti, secondi)


def main():
    """Funzione programma principale :
       Serve a richiedere in input due tempi e restituire solo il maggiore
       Chiamo la funzione estrai_sec e assegno il valore di ritorno a due variabili( primo - secpndo)
       inizializzo una terza variabile dove ricavo il maggiore dei due inpu inserriti
       Ciclo if per stampare quale è il maggiore o se sono =

       Return: 
            Restituisce una fString che stampa le quantità di secondi inserite
    
    """
    primo = estrai_sec()
    secondo = estrai_sec()
    massimo = max(primo, secondo)
    if primo > secondo:
         print(F"Il primo tempo contiene una quantità di secondi superiore")       
    elif primo < secondo:
         print(F"Il secondo tempo contiene una quantità di secondi superiore")       
    elif primo == secondo:
         print(F"I due input si equivalgono")   

    print(F"La quantità di tempo maggiore contiene {massimo} secondi, la minore invece {min(primo,secondo)} secondi")

#Esegue main() solo quando il file viene lanciato direttamente
if __name__ == "__main__":
    main()





