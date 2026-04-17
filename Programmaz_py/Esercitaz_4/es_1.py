"""
Autore: Janice Brun
Data: gg/mm/aaaa
Titolo: Scrivere un programma per rimuovere l'n- esimo elemento da una tupla non vuota
"""
def creazioneTup():
    tupla = ()
    elemento = input("Inserisci un elemento da inserire nella tupla, miao per uscire ").lower
    while 'miao' not in elemento :
        tupla += (elemento, )
        elemento = input("Inserisci un elemento da inserire nella tupla, miao per uscire ").lower
    else:
        return tupla

def controllo_posiz(num):
    numy = controllo_val(num)
    prova = numy.replace('-','')
    while not prova.isdigit():
        numy = input("Inserisci il numero corrispondente alla posizione da del carattere da rimuovere, non una lettera: ")
        prova = numy.replace('-','')
        
        return int(controllo_val(numy))

def controllo_val(a):

    while len(a) <= 0:
        a = input("L'input deve avere almeno 1 carattere: ")
    else:
        return a

def main():
    tupla = creazioneTup()
    num_da_validare = input("Inserisci la posizione dell'elemento da rimuovere: ")
    numero = controllo_posiz(num_da_validare)
    print(type(tupla))

    # p1 = tupla[:(numero -1)]
    # p2 = tupla[numero:]
    # ris = p1 + p2
    # print(f"La tupla risultante è {ris}")

if __name__ == "__main__":
    main()

