
class Figura():
    def area(self):
        pass
    def perimetro(self):
        pass

class Rettangolo(Figura):
    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza
    
    def perimetro(self):
        return 2 * (self.base + self.altezza)
    

class Quadrato(Rettangolo):
    def __init__(self, lato):
        super().__init__(lato, lato)

#riconosce il tipo dell'istanza
q1 = Quadrato(5)
print(isinstance(q1, Quadrato))
print(isinstance(q1, int))

print(q1.area())
print(q1.perimetro())

r1 = Rettangolo(4,6)
print(isinstance(r1, Quadrato))
print(isinstance(r1, int))

print(r1.area())
print(r1.perimetro())