
"""INTO ALLE FUNZIONI"""

import random as rnd

# print(help(rnd))


def mia_funzione():
    """ Ho definito (def) la funzione"""

    saluti = ['buongiorno', 'ciao', 'buonasera', 'hello']

    print(rnd.choice(saluti))#? choice

#mia_funzione()

#parametri in inserimento, argomenti in utilizzo. Argoneti entrano al posto dei parametri
#per svolgere la funzione. Locali a questa funzione
#ciò permette di riusarli in più funz
# def addizione(a, b):
#     return a + b
#se richiedi due argomenti in una funzione devono essere inseriti due parametri a meno che
#def addizione(a, b = 0):
#se non passi in secondo valore da di default 0

def addizione(a: int, b: int = 0):
    return a + b
    """
    Docstring for addizione
    :param a: Description
    :type a: int
    :param b : Description
    :type b: int
    """
def sottrazione(a, b):
    return a + b

# print(addizione(a = numero2, b = numero1))

numero1 = 86
numero2 = 16
#volendo si possono anche passare varisbili in funzione
print(addizione(numero1, numero2))

print(addizione(4, 5))

print(sottrazione(4, 5))
print(sottrazione(3, 2))
print(sottrazione(8, 1))

print(sottrazione(addizione(7, 5), sottrazione(9, 6)))








# mia_funzione()
# mia_funzione()
# mia_funzione()
# mia_funzione()
