"""
Code correspondant au plateau
"""
import numpy as np

class Plateau:
    SIZE = 8
    
    # Attributs de la pièce
    def _init_(self):
        self.grille = np.zeros(self.SIZE, self.SIZE)
        for X in range(0,self.SIZE-1):
            self.grille[X][0] = 1
            self.grille[X][1] = 1
            self.grille[X][self.SIZE-2] = 2
            self.grille[X][self.SIZE-1] = 2
            
            
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
    def try_way(self, ide, initial_case, final_case):
        boolean = True
        Xi = initial_case[0]
        Yi = initial_case[1]
        Xf = final_case[0]
        Yf = final_case[1]
        if Xf - Xi == 0:
            direction = (Yf-Yi)/abs(Yf-Yi)
            for Y in range(Yi, Yf, direction):
                if self.grille[Xf][Y] != 0:
                    return 0
        elif final_case[1] - initial_case[1] == 0:
            direction = (Xf-Xi)/abs(Xf-Xi)
            for X in range(Xi, Xf, direction):
                if self.grille[X][Yf] != 0:
                    return 0
        else:
            directionX = (Xf-Xi)/abs(Xf-Xi)
            directionY = (Yf-Yi)/abs(Yf-Yi)
            for X in range(Xi, Xf, direction):
                if self.grille[X][X*direction] != 0:
                    return 0
        
        return boolean
    
