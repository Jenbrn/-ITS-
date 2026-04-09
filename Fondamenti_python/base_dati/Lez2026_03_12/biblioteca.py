"""classe biblioteca"""

from Fondamenti_python.base_dati.Lez2026_03_12.libro import Libro
from Fondamenti_python.base_dati.Lez2026_03_12.libro_dao import tabella_libri

class Biblioteca:

    libreria = []
    
    def __init__(self):
        self.libreria = tabella_libri

    def addlibro(self, libro : Libro):
        self.libreria.append(libro)
    
    def getLibri(self):
        
        return self.libreria