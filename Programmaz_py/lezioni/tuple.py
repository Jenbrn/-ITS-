tup = (2,) # necessita , per avere tupla con 1  sl elemento
tupla = ( 8, 'ciao', True)
a, b, c = tupla
# print(a, type(a), '-', b, type(b), '-',c , type(c))

x = 1
y = 2
# print(x, " ",y)
z = x #vaiabile passaggio
x = y
y = z
# print(x, " ", y)
x,y = y,x
# print(x, " ", y)

"""accedere e modificare """

tuplissima = (2, 'q', [10,20,30])
lista = tuplissima[2]
# print(lista)
# print(lista[1])
# print(tupla[2][1])
tuplissima[2][1] = -10
# print(tupla)
listaa = [10,3,4,5,6,3,8]
tuppy = (10,3,4,5,6,3,8)
stinga = 'abcdefkanbd'
#print(listaa.index(3,4))#il secondo num è la pos da cui iniziare a cercare
#print(listaa.index(3,4,10))#il secondo num è la pos da cui iniziare a cercare e il terzo delimita il range (fino a 10 escluso)
#numero da cercare - a partire da - dal secondo al terzo escluso
#print(listaa.index(-2)) #err non cerca a ritroso 

"""Numero di occorrenze"""
listaa.count(3)#conta quante volte c'è il 3
#count non da errore se non trova l'elemento

"""estazione e ricerca sottoseq"""
#start - stop - step -> lo stop non è mai incluso
(stinga.index("cde"))
(stinga.find("cde"))#solo sulle str
([3,4,5] in lista)# non trova nulla perchè cerca una lista non l'elemento singolo 
stinga.find('cdez')
stinga.index('cdez')
#ha start stop step
