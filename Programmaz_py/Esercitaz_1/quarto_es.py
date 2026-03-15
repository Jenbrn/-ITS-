"""
Autore: Janice Brun
Data: 14/03/2026
Titolo: Testo esercizio
Scrivere un programma che legga le lunghezze dei tre lati di un triangolo a, b, c e ne calcoli
il perimetro e l'area S, quest'ultima tramite la formula di Erone
S = sqr(p (p-a) * (p - b) * (p - c))
dove p è il semiperimetro.

"""
#importo librerie necessarie

from math import sqrt

#Richiedo inserimento input per calcolo chiedendo all'utente 3 valori separati da , e un'opzione per uscire
#uso try/except per evitare errori se l'utenete inserisce valori numerici
#separo i 3 numeri inseriti in valori e li converto da str a float per effettuare i calcoli
#verifico che non siano negativi o 0 e che sia possibile generare un triangolo

while True:
    valori = input('Inserire tre valori numerici separati da virgola (premere q per uscire): ').lower()
    if (valori) == 'q':
        break
    try:
        a, b, c = valori.split(',') 
        a, b, c = map(float, (a, b, c))
        if a <= 0 or b <= 0 or c <= 0:
            print('Impossibile assegnare valore negativo o 0')
        elif (a + b) < c or ( b + c) < a or (c + a) < b:
            print('Impossibile avere un triangolo il cui terzo lato è minore della somma degli altri 2')
            continue

        break
    except ValueError:
        print('Valore inserito non valido, iserire valore numerico')
        
    print(a, b, c)

#credo funzione per calcolo perimetro e area passando 3 valori

def calcola_perimetro(v,y,z):
    return v + y + z

def erone(v,y,z):
    p = (calcola_perimetro(v, y, z) / 2)
    return sqrt(p * (p - v) * (p - y) * (p - z))

# chiamo le funzioni con dentro le variabili ottenute da input per effettuare i calcoli

perimetro = calcola_perimetro(a,b,c)
area = erone(a,b,c)

print(F"Lati tringolo = a: {a}cm, b: {b}cm, c: {c}cm ")
print(F"Dati i lati perimetro ha lunghezza: {perimetro}cm")
print(F"Avendo i lati è possibile calcolare l'area che corrispone a: {area}cm^2")
