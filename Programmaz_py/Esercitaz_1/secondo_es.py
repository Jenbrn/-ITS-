"""
Autore: Janice Brun
Data: 15/03/2026
Titolo: Testo esercizio
Scrivere un programma che legga i coefficienti a, b e c di un'equazione di secondo grado
ax2+bx+c=0 e ne scriva le soluzioni.
"""

#importo potenza da libreria mat

from math import pow, sqrt

#importo dati, verifico non corrispondano a q e in quel caso blocco il ciclo, faccio assegnazione multipla
# usando la virgola come divisore e a quel punto converto str in float. Filtro l'input con a = 0
#perchè impossibile e eseguo con un try except per evitare errore nel caso l'utente inserisca lettere e non numeri

while True:
     numeri = input('Inserire tre valori numerici (a, b, c) separati da virgola, a non può corrisponedere a 0 (premere Q per uscire): ').lower()
     if (numeri) == 'q':
          break
     try:
        a, b, c = numeri.split(',') 
        a, b, c = map(float, (a, b, c))
        if a == 0:
          print('a non puoò avere valore 0')
          continue
        break
        
     except ValueError:
            print('Valore inserito non valido, iserire valore numerico')
            

# numeri = input('Inserire tre valori numerici (a, b, c) separati da virgola, a non può corrisponedere a 0 (premere Q per uscire): ').lower()

# while (numeri) != 'q':
          
#      try:
#         a, b, c = numeri.split(',') 
#         a, b, c = map(float, (a, b, c))
#         if a == 0:
#           print('a non puoò avere valore 0')
#           continue
#         break
        
#         numeri = input('Reinserire tre valori numerici (a, b, c) separati da virgola, a non può corrisponedere a 0 (premere Q per uscire): ').lower()
#      except ValueError:
#             print('Valore inserito non valido, iserire valore numerico')

#creo funzioni per calcolare Delta e risolvere l'equaz in base al delta

def delta(x,y,z):
     return ( pow(y, 2) - (4 * x * z))

def equaz(x,y,z):
     if delta(a, b, c) < 0:
          return(f'Delta = {delta(a,b,c)}. Nessuna soluzione reale')
     
     elif delta(a,b,c) == 0:
          x = - b / (2 * a)
          return x
    
     else:
          x1 = ((-b + sqrt(delta(a, b , c))) / (2*a))
          x2 = ((- b - sqrt(delta(a, b , c))) / (2*a))
          return x1, x2 , f"Delta > 0 quindi ci sono due soluzioni possibili: x1 = {x1} e x2 = {x2}"
     

# assegno e stampo i risultati di ax2+bx+c=0

print(f"data l'equazione {a}x2 + {b}x + {c} = 0 si trovi le possibili soluzioni: ")

risultato = equaz(a,b,c)

print(risultato)            
     
     
