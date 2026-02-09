
"""" Questo è: LANCIADAI! """

import random
import time

# for i in range (19):
#     print(random.random())
    # print(f'Il valore di dado 1 è: {dado1} e {dado2}')

num_lanci = 1000_000
vittorie = 0


start = time.time()
for i in range(num_lanci):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    if dado1 == dado2:
       # print(f'Hai vinto con una coppia di {dado1}')
        vittorie += 1
    # print(f'Il valore di dado 1 è: {dado1}')
    # print(f'Il valore di dado 2 è: {dado2}')
    # print('-------------------------------')
stop = time.time()

#print(f'Hai lanciato {num_lanci} volte e hai vinto {vittorie} volte')
print(f'Hai lanciato {num_lanci} volte')
print(f'Hai vinto {vittorie} volte')
print(f'La percentuale di vittorie è {vittorie/ float(num_lanci)*100: .2f}% volte')
print(f'L\'elaborazione è durata {stop - start: .2f} secondi')