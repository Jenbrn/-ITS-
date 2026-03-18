
import random

simboli = ['rock', 'paper', 'scissor']



macchina = random.choice(simboli)

umano = input(f'Umano schegli tra: {simboli} ')


print(f'La macchia ha scleto {macchina}')
print(f'L\' umano ha scleto {umano}')

if macchina == umano:
    print(f'Non potete avere entrambi {macchina}, riprovate')
elif umano == 'rock' and macchina == 'scissor':
    print(f'macchina ha scelto {umano} e ha vinto')
elif umano == 'paper' and macchina == 'rock':
    print(f'macchina ha scelto {umano} e ha vinto')
elif umano == 'scissor' and macchina == 'paper':
    print(f'macchina ha scelto {umano} e ha vinto')
else:
    print(f'l\'umano ha scelto {macchina} e ha vinto')















# match scelta:
#     case 1:
#         print("Inserisci")
#     case 2:
#         print("Modifica")
#     case 3:
#         print("Elimina")
#     case _:
#         print("SCELTA NON VALIDA")