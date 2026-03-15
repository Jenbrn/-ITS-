"""buh"""

# def fun(a):
#     a = a +1
#     print(a)

# a = 4
# print(a)
# print(fun(a))
# print(a)

# a = 1
# b = 2
# c = b

# print(id(a), id(b), id(c), sep= "\n")

# print(c is b )

# a = 1
# print('id prima di modifica:', id(a))

# a += 1
# print(' id dopo mod:', id(a))

""" a è immutabile, dopo il calcolo il nuovo a non sosituisce
realmente perchè a rimane allocato nello stesso spazio di memoria
si ha una sostituzione logica dove nuovo a occupa uno spazio in un'altra allocazione di memoriq"""

# a = [1,2]
# print('id prima di modifica:', id(a))
# a += [3]#a.append[3]
# print('id prima di modifica:', id(a))

# def fun(a):
#     print('id prima di modifica:', id(a))
#     a += 1
#     print('id dopo modifica:', id(a))
#     print('id prima di modifica:', a)


# a = 1
# print('id prima chiamata:', id(a))
# fun(a)
# print('id dopo chiamata', id(a))
# print('valore a dopo:', a)

"""Parametri predefiniti"""

def rettangoloArea(base = 2, altezza = 4):
    return base*altezza

print('Area1 = ', rettangoloArea())
print('Area2 = ', rettangoloArea(5))
print('Area3 = ', rettangoloArea(5,5))


def rettangoloAreas(base, altezza, profondita):
    return base*altezza*profondita

print('Area1 = ', rettangoloAreas(3, profondita=4, altezza=5))
print('Area2 = ', rettangoloAreas(profondita=4, altezza=5, base=3))









