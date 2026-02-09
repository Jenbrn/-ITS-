
piemonte = ['asti', 'cuneo', 'torino', 'alessandria']
piemonte2 = ['vco', 'novara', 'vercelli', 'biella']

liguria = ['savona', 'genova', 'laspezia', 'imperia']

piemonteAll = piemonte + piemonte2
#piemonte.extend(piemonte2)
#usare append per aggiungere una lista ad una lista genere una lista annidata non una lista unica

# print(piemonteAll)
# print(liguria)

#piemonte(dir(piemonte))elenco possibilità
#piemonte(help(piemonte)) - big help for janice

# citta = input('Dimmi la citta dove vuoi andare: ')
# if 'tornino' in piemonte:
#     print(f'Il bus per {citta} è disponibile')
# else:
#     print(f'Il bus per {citta} non è disponibile')

#dammi la sedia miao

piemonte.sort()
print(piemonte)
piemonteAll.sort()
print(piemonteAll)