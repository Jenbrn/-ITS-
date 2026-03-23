"""FORME"""
#INCAPSULAMENTO
#EREDITARIETA
#POLIMORFISMO- reference type
#

class Shape:
    def __init__(self, colour):
        self.colour = colour

    def __str__(self):
        return f"Sono una forma di colore {self.colour}"   

class Circle(Shape):
    def __init__(self, radius, colour):
        super().__init__(colour)
        self.radius = radius

    def __str__(self):
        descrizione = f"sono un'antilope di superficie { 3.14 * self.radius * self.radius}\n"
        descrizione += super().__str__()
        return descrizione


class Triangle(Shape):
    def __init__(self, width, height, colour):
        super().__init__(colour)
        self.width = width
        self.height = height
        

class Square(Shape):
    def __init__(self, width, colour):
        super().__init__(colour)
        self.width = width
    

cerchio = Circle(5, 'red')
cerchio_rosso = cerchio

triangolo = Triangle(4, 6, 'blue')

quadrato = Square(4, 'green')

#occupano lo stesso spazio di memoria
print(cerchio)
print(quadrato)
print(triangolo)
print(type(cerchio))