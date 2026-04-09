"""chiamata funz"""

#import punto 

#a = punto.Punto

from Fondamenti_python.codice.Marzo.Lez2026_03_11.punto import Punto
from Fondamenti_python.codice.Marzo.Lez2026_03_11.segmento import Segmento
from Fondamenti_python.codice.Marzo.Lez2026_03_11.modello_triangolo import Triangolo

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

t2 = Triangolo(Punto(5,5), Punto(9,9), Punto(15,6))

print(t2.perimetro)
print(t2.area)
print(t2)