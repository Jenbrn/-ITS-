""" SLOTH MACHINE    """
import random

def spin():
    symbols = ['❤️', '🐛', '🍆', '🍔', '🌶️']
    riga = []
    for _ in range(3):
        riga.append(random.choice(symbols))
    return riga

def print_row(riga):
    print("*" * 20)
    print(" | ".join(riga))

    print("*" * 20)

def check(riga, puntata):
    if riga[0] == riga [1] == riga [2]:
        if riga [0] == "❤️":
            return puntata * 2
        if riga [1] == "🐛":
            return puntata * 4
        if riga [2] == "🍆":
            return puntata * 5
        if riga [3] == "🍔":
            return puntata * 6
        if riga [4] == "🌶️":
            return puntata * 7
    return 0

def main():
    credits = 100

    print("--------------")
    print("Gioco pitonich")
    print("--------------")

    while credits > 0:
        
        puntata = input("Quanto vuoi puntare: ")

        if not puntata.isdigit(): 
            print("Amico non puoi puntare lettere -> valore numerico tra 1 e 100")
            continue
    
        puntata = int(puntata)

        if puntata <= 0:
            print(f"Hai puntato {puntata}, devi puntare almeno 1!")
            continue

        if puntata > credits:
            print(F"Sei un poveraccio, hai scommesso {puntata} crediti ma ne hai solo {credits}. Punta meno")
            continue

        credits -= puntata

        riga = spin()
        print_row(riga)
        punteggio = check(riga, puntata)

        credits += punteggio

        if punteggio > 0:
            print(f"E bravo! Hai vinto {punteggio} crediti. Vatti a comprare due babbucce")
        else:
            print(F" ah - ha sfigato. Hai perso, non hai vinto nulla!")

        print(F"Il tue credito è di {credits} cipolle")

        if credits == 0:
            print("Game over")
            break


        play_again = input("Vuoi uscire? ").lower()

        if play_again == 'y':
            break


if __name__ == "__main__":
    main()



