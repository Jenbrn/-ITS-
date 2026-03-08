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

costo_biglietto = 68.50

categoria = input('Inserire: S per studente / P per pensionato / D per disoccupato / I per intero / Q per uscire: ').lower()


# Inizializzazioni variabili

while categoria not in ('s', 'p', 'd', 'i', 'q'):
    categoria = input('Inserire: S per studente / P per pensionato / D per disoccupato / I per intero / Q per uscire: ').lower()

if categoria == 'q':
    print('Chiusura in corso')
if categoria == 's':
    print('Categoria studente, sconto 15%')
elif categoria == 'p':
    print('Categoria pensionato, sconto 10%')
elif categoria == 'd' :
    print('Categoria disoccupato, sconto 25%')
elif categoria == 'i':
    print('Nessuno sconto applicabile')

# Elaborazione

def sconto(a):
    if a == 'p':
        return(costo_biglietto - ((costo_biglietto / 100)*10))
    elif a == 's':
         return(costo_biglietto - ((costo_biglietto / 100)*15))
    elif a == 'd':
         return(costo_biglietto - ((costo_biglietto / 100)*25))
    else: 
        return costo_biglietto

prezzo_finale = sconto(categoria)

# Eventuali sotto processi di Elaborazione


# Sezione di output
while categoria in ('s', 'p', 'd', 'i'):
    print(f'Il prezzo del biglietto intero è: {costo_biglietto}, il prezzo finale è : {prezzo_finale}')
    break