"""
Classe de la dame
"""

from piece import Piece
from jeu import *
import numpy as np
from plateau import *

class Dame(Piece):
    # Attributs de la pièce
    def __init__(self, position, color):
        super().__init__("Dame", position, color)
        self.image = PhotoImage(file = "C:/Users/ed190/Desktop/Chess/Sprite/bqueen.png")

    """
    Procédure move()
    Fait bouger la pièce
    Input:
        -new_position : 2D Vector
    Output: N/A
    """
    def move(self, new_position, tableau):
        if self.valid(new_position):
            pass
       
    """
    Fonction valid()
    Teste si l'action est valide
    Input:
        -new_position : 2D Vector
    Output:
        -boolean: booleen
    """
    def valid(self, new_position, plateau):
        boolean = False
        movement_vector = new_position - self.position
        if self.valid_movement(movement_vector):
            if self.try_way(new_position, plateau):
                boolean = True
        return boolean
      
    """
    Fonction try_way()
    Teste si le chemin est possible
    Input:
        -grille: attribut de la classe plateau
    Output:
        -boolean: booleen
    """    
    def try_way(self, case, plateau):
        ide = self.convert()
        return plateau.try_way_plateau(ide, self.position, case)
    
    """
    Fonction valid_movement()
    Teste si le mouvement est valide
    Input:
        -new_position : 2D Vector
    Output:
        -boolean: booleen
    """    
    # movement_vector : 2D Vector
    def valid_movement(self, movement_vector):
        boolean = False
        if movement_vector[0] == 0 or movement_vector[1] == 0:
            boolean = True
        elif abs(movement_vector[0]) == abs(movement_vector[1]):
            boolean = True
        else:
            pass
        return boolean   
        
    
    