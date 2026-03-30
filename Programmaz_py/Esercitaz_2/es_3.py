"""
Autore: Janice Brun
Data: 28/03/2026
Titolo: Terzo esercizio 
    Conversione temperatura: implementare una funzione convertiCF che converta una
    temperatura espressa in gradi Fahrenheit in una temperatura espressa in gradi Celsius.
    Usare la seguente formula:
    C = (F - 32) * 5 / 9
    Creare un programma principale che richiami la funzione e ne stampi il risultato
    visualizzando solo 3 cifre decimali.
"""
#sezione input dati

def richiesta_fahrenheit():
    """Funzione : richiesta input per temperatura da convertire. Sostituisco eventuali virgole inserite erroneamente
       prima di effettuare il cast in float eseguo una verifica con ciclo while: duplico f e elimino il . che è presente
       se è stato inserito un num con la virgola, a questo punto uso isdigit per verificare che la str
       contenga solo valori numerici. Quando il valore in input è pronto eseguo cast in float.

       Return : variabile che corrisponde a un num float pronto x conversione    
    """
    f = input("Inserisci di seguito la temperatura in fahrenheit che vuoi convertire in Celsius: ").replace(',','.')

    prova = f.replace('.','')
    while not prova.isdigit():
        f = input("Inserisci di seguito la temperatura valida in fahrenheit che vuoi convertire in Celsius: ").replace(',','.')
        prova = f.replace('.','')
    f = float(f)    
        
    return f

#Elaborazione

def convertiCF():
    """Funzione : Esegue la conversione da fahrenheit a celsius richiamando la funzione richiesta_fahrenheit()
       per ottenere il valore. Global per poter richiamare le variabili in main 

       Return : Valore float della temeratura convertita in celsius
    """

    global fahr, cels
    fahr = richiesta_fahrenheit()
    cels = ((fahr - 32) * 5 / 9)
    return cels

#Sezione Output

def main():
    """Funzione : Richiama la funzionne convertiCF per effettuare il calcolo e ottenere valori

       Return : stampa la temperatura inserita e la temperatura a conversione effettuata 
    """
    
    convertiCF()
    print(f"La temperatura da te inserita è: {fahr:.3f} F")
    print(f"Il risultato della conversione è {fahr:.3f}F = {cels:.3f} C")

    pass

if __name__ == '__main__':
    main()




