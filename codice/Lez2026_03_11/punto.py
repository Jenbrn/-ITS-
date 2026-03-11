""" Punto"""

# class Punto:

#     def __init__(punt, x: int, y: int):
#         punt.x = y
#         punt.y = x
#         print(F"Ho creato un nuovo punto di coordinate{punt.x}, {punt.y}")
#puntatore autorfernziale


class Punto:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

#print(F"Ho creato un nuovo punto di coordinate{self.x}, {self.y}")