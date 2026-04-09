from Fondamenti_python.codice.Marzo.Lez2026_03_26.prod_repo import ProdottoRepo

class MagazzinoService:

    def __init__(self):
        self.repo_prodotti = ProdottoRepo()

    
    def getAllProducts(self):
        return self.repo_prodotti.getProdotti()