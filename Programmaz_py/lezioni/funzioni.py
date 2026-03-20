"""FUNZIONI / GLOBAL"""

# def fun(a,b):
#     somma = a + b 
#     print("Somma =", somma)
#     return(somma)#somma visibilità locale, esiste solo all'interno della funzione

#print(fun(2,3))
"""
var = 10
def fun():
    global var
    print("2 vaar=", var)
    var = var +1
    print("3 vaar=", var)


print("1 var=", var)
fun()
print("3 var=", var)

La variabile locale maschera la variabile globale. In questo caso var fuori funzione che è una variabile globale"""

#FUNCTION ANNOTATION    
"""Si può suggerire anche il valore di ritorno"""


def areaRettangolo(base: float, altezza: float) -> float:
    """

    base : float
    altezza : float
    
    """
    return base * altezza

print("Area 1 = ", areaRettangolo(3.2, 4.5))
print("Area 2 = ", areaRettangolo(4, 5))
print("Area 3 = ", areaRettangolo("A", 3))
print("Area 4 = ", areaRettangolo("B", "A"))
