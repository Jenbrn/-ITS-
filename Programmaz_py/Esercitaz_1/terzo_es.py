"""
    Autore: Janice Brun
    Data: 08/03/2026
    Titolo: Scrivere un programma che legga il raggio r di una circonferenza e ne calcoli l'area e la
    lunghezza.
    Perimetro = r * 3.14
    Area = 3.14 * r^2
"""

# Sezione di input Dati

raggio = float(input('Inserire il raggio: '))

# Inizializzazioni variabili
if raggio < 0:
    raggio = float(input('Impossibile avere un valore < 0. Inserire il nuovo raggio: '))
# Elaborazione

def calcola_perimetro(a):
    return(a * 3.14)

def calcola_area(a):
    return((a**2)  * 3.14)

# Eventuali sotto processi di Elaborazione

perimetro = calcola_perimetro(raggio)

area = calcola_area(raggio)

# Sezione di output

print(f'Dato il raggio {raggio} il perimetro del cerchio corrispone a p= {perimetro} e la sua area a a= {area}')
 
