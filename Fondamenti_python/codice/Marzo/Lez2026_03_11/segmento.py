"""Segmento"""
from math import sqrt, pow

from Fondamenti_python.codice.Marzo.Lez2026_03_11.punto import Punto

class Segmento:

    def __init__(self, A: Punto, B: Punto):
        self.A = A
        self.B = B

    def lunghezza(self):
        """Questo metodo calcola la lungh del segm"""

        return sqrt(pow(self.B.x - self.A.x, 2) + pow(self.B.y - self.A.y, 2))
