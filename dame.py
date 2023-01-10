"""
Classe de la dame
"""

from piece import Piece
from jeu import *
import numpy as np
import plateau

class Dame(Piece):
    # Attributs de la pièce
    def _init_(self, position, color):
        super()._init_("Dame", position, color) 

    """
    Procédure move()
    Fait bouger la pièce
    Input:
        -new_position : 2D Vector
    Output: N/A
    """
    def move(self, new_position):
        if self.valid(self, new_position):
            pass
       
    """
    Fonction valid()
    Teste si l'action est valide
    Input:
        -new_position : 2D Vector
    Output:
        -boolean: booleen
    """
    def valid(self, new_position):
        boolean = False
        if self.case_empty():
            movement_vector = new_position - self.position
            if self.valid_movement(movement_vector):
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
    def try_way(self, case):
        ide = self.convert()
        return plateau.is_case_empty(ide, self.position, case)
    
    """
    Fonction valid_movement()
    Teste si le mouvement est valide
    Input:
        -new_position : 2D Vector
    Output:
        -boolean: booleen
    """    
    # movement_vector : 2D Vector
    def valid_movement(movement_vector):
        boolean = False
        if movement_vector[0] == 0 or movement_vector[1] == 0:
            boolean = True
        elif abs(movement_vector[0]) == abs(movement_vector[1]):
            boolean = True
        else:
            pass
        return boolean   
        
    
    