"""NUMBER GUESSING GAME"""

#INDOVINA NUM DA 1 A 100 
# numero_estratto = input(int('Inserisci un numero da 1 a 100'))

# numero_macchina = 

import random as rdm


numero_num = rdm.randint(1, 100)

giri = 0

indovinat = False

while not indovinat:
    guessin = int(input('inserisci num tra 1 e 100: '))
    if guessin < 1 and guessin > 100:
        print('Non in range, inserisci un numero tra 1 e 100')
    giri += 1

    if guessin > numero_num:
        print('Il numero da trovare è più basso')
    elif guessin < numero_num:
        print('Il numero da trovare è più elevato')
    else:
        indovinat = True
        print(f'Hai indovinato in {giri} tetativi') 