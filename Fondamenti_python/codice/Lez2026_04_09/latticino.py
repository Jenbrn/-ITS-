
class Prodotto:
    def __init__(self):
        print("nuovo prodotto")


class Latticino(Prodotto):
    def __init__(self, nome, peso):
        super().__init__()
        self.nome = nome
        self.peso = peso

    def __str__(self):
            return f"{self.nome} ({self.peso} kg)"
    
#costruendo prima classe genitore in modo da non dover ripetere
#class Mozzarella:
class Mozzarella(Latticino):
    def __init__(self, nome, peso, tipo):
        super().__init__(nome, peso)
        #self.nome = nome
        #self.peso = peso
        self.tipo = tipo


cacio = Latticino("cacio", 1)
print(cacio)

m1 = Mozzarella("ciliegino", 0.2, "Bufalino")
print(m1)
