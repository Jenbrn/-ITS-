"""
    Autore : Janice Brun
    Data: 06/03/2026
    Titolo: Primo esercizio:
    Scrivere un programma che legga i coefficienti a e b di un'equazione di primo grado ax=b e
    ne scriva la soluzione (attenzione al dominio del coefficiente a)
"""
#x = b/a - a != 0
#Sezione input dati


a,b = map(float,input('Iserire due numeri separati da virgola: ').split(','))


# Inizializzazioni variabili

# Elaborazione

while True:
    if a == 0 and b == 0:
        print(f'il risultato dell\'equazione indeterminata ax = b è: {a} * 0 = {b} dove X = 0')
    elif a == 0 and b != 0:
        print('Calcolo impossibile, inserire altri due valori')
        a,b = map(float, input('Iserire due numeri separati da virgola: ').split(','))
    else:
        x = float(b / a)
        print('Elaborazione equazione determinata')
    break



# def equaz(a, b):
#     return(float(b / a))

# x = equaz(a, b)


# Eventuali sotto processi di Elaborazione


# Sezione di output

print(f'il risultato dell\'equazione determinata ax = b è: {a} * {x} = {b} dove X = {x}')