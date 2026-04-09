"""liste"""

#unpacking

class Studente:
    def __init__(self, nome, cognome, valutazione):
        self.nome  = nome
        self.cognome = cognome
        self.valutazione = valutazione

# lista

studenti = []

nome, cognome, valutazione = ['Pietro', 'Rossi', 28]

studenti.append(Studente(nome, cognome, valutazione))

#record1 = ['Pietro', 'Rossi', 28]
# nome = record1[0]
# cognome = record1[1]
# valutazione = record1[2]

# stud1 = Studente(nome, cognome, valutazione)

# studenti.append(stud1)







