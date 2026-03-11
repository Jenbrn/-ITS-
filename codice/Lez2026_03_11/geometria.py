"""chiamata funz"""

#import punto 

#a = punto.Punto

from punto import Punto
from segmento import Segmento
from modello_triangolo import Triangolo

A = Punto (2, 2)
B = Punto (6, 2)
C = Punto (2, 5)

print(A)
print(B)
print(C)

AB = Segmento(A, B)
AC = Segmento(A, C)
BC = Segmento(B , C)

print(f"La lunghezza {AB.lunghezza()}")
print(f"La lunghezza {AC.lunghezza()}")
print(f"La lunghezza {BC.lunghezza()}")

t1 = Triangolo(A, B, C)

print(t1.perimetro)
print(t1.area)
print(t1)