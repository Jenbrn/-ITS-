

from Fondamenti_python.base_dati.Lez2026_03_12.biblioteca import Biblioteca
from Fondamenti_python.base_dati.Lez2026_03_12.libro import Libro

biblioteca_civica = Biblioteca()

for libro in biblioteca_civica.getLibri():
    print(f"Titolo: {libro}")