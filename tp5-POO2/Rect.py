class Rectangle :
    def __init__(self, longueur:int = 5, largeur:int=3):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle" 

    def affichage(self):
        return f"{self.nom} de {self.longueur} par {self.largeur}"

    def surface(self):
        return f"surface de {self.longueur*self.largeur}"

class Carré(Rectangle):
    def __init__(self, cote:int=4):
        super().__init__(longueur=cote, largeur=cote)
        self.nom = "carré"