"""
Classe mère d'une pièce ou d'un pion
"""

class Piece:
    # Attributs de la pièce
    def __init__(self, name, position, color):
        self.name = name
        self.position = position
        self.color = color
        

    """
    Procédure move()
    Fait bouger la pièce
    Générique
    """
    def move(self):
        pass
    
    """
    Fonction get_position()
    Récupère la position de la pièce sur la grille
    Input: N/A
    Output: 
        -self.position : 2D vector
    """
    def get_position(self):
        return self.position
    
    """
    Procédure get_position()
    Modifie la position de la pièce sur la grille
    Input:
        -new_position: 
    Output: N/A
    """
    def set_position(self, new_position):
        self.position = new_position
    
    """
    Fonction valid()
    Teste si l'action est valide
    Générique
    """
    def valid(self, new_position):
        pass
            
    """
    Fonction case_empty()
    Teste si la case d'arrivée est vide
    Générique
    """
    def case_empty():
        pass
    
    """
    Fonction valid_movement()
    Teste si le mouvement est valide
    Générique
    """    
    # movement_vector : 2D Vector
    def valid_movement(movement_vector):
        pass
    
    """
    Fonction convert()
    Convertit la couleur en identifiant, 1 pour blanc, 2 pour noir
    Input: N/A
    Output:
        -id: int
    """  
    def convert(self):
        if self.color == 'white':
            return 1
        else:
            return 2
        