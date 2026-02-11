
"""ROCK PAPAER SCISSOR"""

import random

simboli = ['rock', 'paper', 'scissor']

scelta_macchina = random.choice(simboli)

while True:
    scelta_umano = input(f'Umano schegli tra: {simboli} ').lower().strip()
    match scelta_umano:
        case 'rock' | 'paper' | 'scissor':
            print(f'L\' umano ha scleto {scelta_umano}')
            break
        case _:
            print(f'scelta non valida, scegli tra: {simboli}')

print(f'La macchia ha scleto {scelta_macchina}')

if scelta_macchina == scelta_umano:
    print(f'Entrambi avete scelto: {scelta_umano}! Pareggio')
elif scelta_macchina == 'rock' and scelta_umano != 'paper':
    print(f'La macchina ha scelto {scelta_macchina} e ha vinto!')
elif scelta_macchina == 'paper' and scelta_umano != 'scissor':
    print(f'La macchina ha scelto {scelta_macchina} e ha vinto!')
elif scelta_macchina == 'scissor' and scelta_umano != 'rock':
    print(f'La macchina ha scelto {scelta_macchina} e ha vinto!')
else:
    print(f'l\'umano ha scelto {scelta_umano} e ha vinto')