"""Recap"""
"""
titolo = 'Quo vadis'
anno = 1995
frutta = ['mele', 'pere', 'banane']

fruttini = ['mirtilli', 'fragole', 'ribes']
#frutta.extend(fruttini)
# append inserisce lista nella lista

#print(frutta)

#print(help(frutta))
#print(type(frutta))

tutti_frutti = frutta + fruttini
print(tutti_frutti)

tupla_frutti = tuple(tutti_frutti)
lista_frutti = list(tupla_frutti)
"""

"""UNPACKING"""

"""
frutti = ['mele' , 'pere', 'banane']
verdure = ['spinaci', 'costine', 'broccoli']
dolci = ['cassatina', 'cannolo', 'meringata']

for frutto in frutti:
    print(frutto)

zippini = zip(frutti, verdure, dolci)

for zip in zippini:
    print(zip)

for a, b, c in zippini:#printa il primo per ogni tupla
    print(a,)

for frutto, verdura, dolce in zippini:
    print(frutto, verdura, dolce)

"""

"""LIST COMPREANSION""" 

frutti = ['mele' , 'pere', 'banane']
verdure = ['spinaci', 'costine', 'broccoli']
dolci = ['cassatina', 'cannolo', 'meringata']

alimenti = frutti + verdure + dolci

print(alimenti)

#scatola = []

# for prod in alimenti:
#     if prod.startswith('c'):
#         scatola.append(prod)

scatole = [alimento for alimento in alimenti if alimento.startswith('c') ] 

print(scatole)






