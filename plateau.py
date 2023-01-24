"""
Code correspondant au plateau
"""
import numpy as np

class Plateau:
    SIZE = 8
    
    # Attributs de la pièce
    def __init__(self):
        self.grille = np.zeros((self.SIZE, self.SIZE))
        
    def initialisation(self):
        for X in range(0,self.SIZE-1):
            pass
            # self.grille[X][0] = 1
            # self.grille[X][1] = 1
            # self.grille[X][self.SIZE-2] = 2
            # self.grille[X][self.SIZE-1] = 2
       
            
    """
    Fonction is_case_empty()
    Teste si la case de la grille est vide
    Input:
        -case : 2D Vector
    Output:
        - booleen
    """
    def is_case_empty(self, case):
        return not self.grille[case[0]][case[1]]
    
    
    """
    Fonction try_way()
    Teste si le chemin est valide
    Input:
        -case : 2D Vector
    Output:
        - booleen
    """
    def try_way_plateau(self, ide, initial_case, final_case):
        Xi = initial_case[0]
        Yi = initial_case[1]
        Xf = final_case[0]
        Yf = final_case[1]
        if Xf - Xi == 0:
            direction = int((Yf-Yi)/abs(Yf-Yi))
            for Y in range(Yi+direction, Yf, direction):
                if self.grille[Xf][Y] != 0:
                    return 0
            return 1
        elif Yf - Yi == 0:
            direction = int((Xf-Xi)/abs(Xf-Xi))
            for X in range(Xi+direction, Xf, direction):
                if int(self.grille[X][Yf]) != 0:
                    return 0
            return 1
        else:
            directionX = int((Xf-Xi)/abs(Xf-Xi))
            directionY = int((Yf-Yi)/abs(Yf-Yi))
            X = Xi + directionX
            Y = Yi + directionY
            while X != Xf and self.grille[X][Y] == 0:
                X += directionX
                Y += directionY
            if X == Xf:
                return 1
            else:
                return 0
        
    
