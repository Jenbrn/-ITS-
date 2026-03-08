"""
    Autore: Janice Brun
    Data: 08/03/2026
    Titolo: Sesto esercizio
    Su una linea ferroviaria, rispetto alla tariffa piena, gli utenti pensionati usufruiscono di uno
    sconto del 10%, gli studenti del 15% e i disoccupati del 25%. Codificando i pensionati con
    un 1, gli studenti con un 2 e i disoccupati con un 3, scrivere un programma che, richiesto il
    costo di un biglietto e l'eventuale condizione particolare dell'utente, visualizzi l'importo da
    pagare.
  
"""

# Sezione di input Dati
import random as rdm
prezzo = [1, 300]
costo_biglietto = rdm.choice(prezzo)

categoria = input('ioisdidskdsds: S per studente / P per pensionato / D per disoccupato / I per intero / Q per uscire: ').lower()


# Inizializzazioni variabili
while categoria != 'q':
    if categoria == 's':
        studente = categoria
    elif categoria == 'p':
        pensionato = categoria
    elif categoria == 'd' :
        disoccupato = categoria
    elif categoria == 'i':
        intero = categoria
    elif categoria not in ('s', 'p', 'd', 'i'):
        categoria = input('ioisdidskdsds: S per studente / P per pensionato / D per disoccupato / I per intero / Q per uscire: ').lower()
    elif categoria == False:
        break



# Elaborazione

def sconto(a):
    if a == pensionato:
        return(costo_biglietto - ((costo_biglietto / 100)*10))
    elif a == studente:
         return(costo_biglietto - ((costo_biglietto / 100)*15))
    elif a == disoccupato:
         return(costo_biglietto - ((costo_biglietto / 100)*25))
    else: 
        return costo_biglietto

prezzo_finale = sconto(categoria)

# Eventuali sotto processi di Elaborazione


# Sezione di output
print(f'il prezzo finale è : {prezzo_finale}')