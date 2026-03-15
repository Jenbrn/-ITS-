"""
    Autore: Janice Brun
    Data: 08/02/2026
    Titolo:
   
    Testo esercizio
    Leggere una successione di numeri interi passati dall’utente, fermandosi al primo numero
    che rende la successione non crescente e restituendo quanti numeri formano la
    successione inserita.
    Esempio:
    INPUT: 2 5 28 10 OUTPUT: 3
    INPUT: 2 -2 OUTPUT: 1
"""
# Sezione di input Dati

elenco = []

real_elenco = []

# Inizializzazioni variabili

while True:
  numero = input('Inserisci un numero intero, premi Q per uscire: ').lower()
  if numero == 'q':
        break
  try:
      numero = int(numero)
      elenco.append(numero)
  except ValueError:
      print('Inserire solo numeri interi')

# Elaborazione

for valore in range(len(elenco) - 1 ):
    thiiss = elenco[valore]
    neeext = elenco[valore + 1]
    if thiiss < neeext:
        real_elenco.append(thiiss)
    else:
        print(f'Ciclo finito, {thiiss} è maggiore di {neeext}')
        break

    
# Eventuali sotto processi di Elaborazione


# Sezione di output

print(f'L\'elenco di numeri interi interi e crescenti in successione che hai inserito è: {real_elenco}')
