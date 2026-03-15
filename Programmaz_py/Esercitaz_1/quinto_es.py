"""
    Autore : Janice Brun
    Data : 06/03/2026
    Titolo : Quinto esercizio
    Un negoziante per ogni spesa di importo superiore a 100 € effettua uno sconto del 5%, se
    l’importo risulta superiore a 300€ lo sconto è del 10%. Scrivere un programma che richieda
    all'utente l'ammontare della spesa e visualizzi quindi l'importo effettivo da pagare.
    
"""

# Sezione di input Dati

spesa = float(input(f"Inserire il valore della spesa: "))

# Inizializzazioni variabili

# Elaborazione

if spesa > 100 and spesa < 300:
    nuovo_totale = spesa - ((spesa / 100)*5)
    print(f'Il totale è: {nuovo_totale}')
elif spesa >= 300:
    nuovo_totale = spesa - ((spesa / 100)*10)
    print(f'Il totale è: {nuovo_totale}')
else:
    print(f'Il totale è: {spesa}')

# Eventuali sotto processi di Elaborazione

# Sezione di output