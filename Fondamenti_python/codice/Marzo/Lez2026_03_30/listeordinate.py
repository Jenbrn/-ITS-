"""liste ordinate"""

from dataclasses import dataclass

@dataclass
class Libro:
    titolo: str
    pagine: int

libri = [
    Libro('A nord di ushaia', 500),
    Libro('E oggi è ancora bello', 300),
    Libro('Bisogna saper perdere', 240),

]

def ordinatore_titoli(libro):
    return libro.titolo

def ordinatore_pagine(libro):
    return libro.pagine

#lambda libro:libro.pagine
#funzione sfunzionata e condensata

#libri.sort(key=lambda libro:libro.pagine)

libri.sort(key=ordinatore_titoli)
print(libri)

libri.sort(key=ordinatore_pagine)
print(libri)












# voti = [25,28,24,27,29,30,18,25]

# parole = ['pisolo', 'elolo', 'brontolo', 'mammolo', 'gongolo', 'cucciolo', 'dotto']

# # disordinare = [25,28,24,27,29]

# # ordinati = []

# # for i in disordinare:
# #     if i > i+1:

# voti.sort(), parole.sort()
# print(voti, parole) 