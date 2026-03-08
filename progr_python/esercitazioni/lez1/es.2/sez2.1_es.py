"""
    Autore: Janice Brun
    Data: 08/03/2026
    Titolo:  Si hanno in input due numeri reali A e B e una successione di numeri reali positivi che
    termina con il valore 0. Si vuole in output la media dei soli numeri compresi tra A e B.
    Esempio:
    INPUT: A=2 B= 3.5 Successione: -3.4 4 2.5 3 10 0
    OUTPUT: 2.75 [ perchè media=(2.5+3)/2=2.75]"""



# Sezione di input Dati

a,b = map(float, input('Inserire due numeri separadoli con virgola: ').split(','))

elenco = []

print('Inserire dei valori e per terminare come ultimo valore inserire 0:')

massimo = max(a,b)
minimo = min(a,b)


# Inizializzazioni variabili

while True:
    numero = float(input('Numero: '))
    if numero == 0:
        break
    if minimo < numero < massimo:
        elenco.append(numero)

# Elaborazione
def c_media(a,b):
   return(a / b)

if len(elenco) > 0:
    media = c_media(sum(elenco),len(elenco))

print(f'L\'elenco dei valori di cui fare la media è {elenco}, a ha valore {a} e b ha valore {b}')
print(f'La media di {elenco} è {media}')








# Eventuali sotto processi di Elaborazione
# Sezione di output
