import tkinter as tk
from tkinter import *
from partie import *
from piece import *
from dame import *
from plateau import *
from PIL import Image, ImageTk
import numpy as np

taille: int=8
global img

class Fenetre_JOUER:
    def __init__(self, root=None, app=None, tableau=None):
        self.root = root
        self.click_status = 0
        self.frame = tk.Frame(self.root,bg='white')
        self.frame.pack(expand=YES)
        self.plateau = Plateau()
        self.plateau.initialisation()
        self.piece =[]
        # Convas Lignes
        self.cnv = Canvas(self.root, width=720, height=720, bg="ivory")
        # Quadrillage
        
        for x in range(0,8,2):
            for y in range(0,8,2):
                    self.cnv.create_rectangle(x*91, y*91, (x+1)*91, (y+1)*91, 
                                              fill="ivory", 
                                              width = 0, 
                                              tags = "move_button"+str(x+8*y))
                    print(x+8*y, x, y)
                    
        for x in range(1,8,2):
            for y in range(0,8,2):
                    self.cnv.create_rectangle(x*91, y*91, (x+1)*91, (y+1)*91, 
                                              fill="#5DA743", 
                                              width = 0, 
                                              tags = "move_button"+str(x+8*y))
                    print(x+8*y, x, y)

        for x in range(0,8,2):
            for y in range(1,8,2):
                    self.cnv.create_rectangle(x*91, y*91, (x+1)*91, (y+1)*91, 
                                              fill="#5DA743", 
                                              width = 0, 
                                              tags = "move_button"+str(x+8*y))
                    print(x+8*y, x, y)



        for x in range(1,8,2):
            for y in range(1,8,2):
                    self.cnv.create_rectangle(x*91, y*91, (x+1)*91, (y+1)*91, 
                                              fill="ivory", 
                                              width = 0, 
                                              tags = "move_button"+str(x+8*y))
                    print("move_button"+str(x+8*y), x, y)
                    
        # Initialisation des pièces
        self.cnv.image = []
        
        position_initiale = np.array([0,7])
        bqueen = Dame(position_initiale, "black")
        self.piece.append(bqueen)
        self.plateau.grille[bqueen.position[0]][bqueen.position[1]] = 2 
        self.cnv.image.append(self.cnv.create_image(91 * (bqueen.position[0]+1) - 47, 
                                                    770 - 91 * (bqueen.position[1]+1), 
                                                    image = bqueen.image, 
                                                    tags="move_button"))
        self.cnv.tag_bind("move_button", "<Button-1>", lambda tag:self.button_clicked(1,1))
        for x in range(0,8):
            for y in range(0,8):
                print("move_button"+str(x+8*y),x,y)
                self.cnv.tag_bind("move_button"+str(x+8*y), 
                                  "<Button-1>", 
                                  lambda tag:self.button_clicked(x,y))
                    
        
        self.cnv.pack(expand=YES)
        # Changement avec touches
        # self.root.bind("<KeyPress>", self.fonction_changement)
        
    def button_clicked(self, x, y):
        if self.click_status:
            self.click_status = 0
            if self.piece[0].valid(np.array([x,y]), self.plateau):
                print(x, y)
                print(91*(x+1)-47-self.piece[0].position[0],770-91*(y+1)-self.piece[0].position[1])
                self.cnv.move(self.cnv.image[0],
                              91*(x+1)-47-self.piece[0].position[0],
                              770-91*(y+1)-self.piece[0].position[1])
        else:
            self.click_status = 1
        
    def supprimer(self):
        for ligne in range(taille):
            for colonne in range(taille):
                self.cnv.delete(self.nombre[ligne][colonne])

    def afficher(self):
        pass
        
        
        # def fonction_changement(self,event):
        #     touche=event.keysym
        #     # self.supprimer()
        #     if touche == "Left":
        #         if self.piece[0].valid(np.array([x,y]), self.plateau):
        #             self.cnv.move(self.cnv.image[0],
        #                           91*(x+1) - 47-self.piece[0].position[0],
        #                           770-91*(y+1)-self.piece[0].position[1])
        #     elif touche == "Right":
        #         self.tableau.changement("droite")
        #     elif touche == "Up":
        #         self.tableau.changement("haut")
        #     elif touche == "Down":
        #         self.tableau.changement("bas")
        #     elif touche == "Escape":
        #         self.click_status = unclicked
        #     # self.tableau.apparition()
        #     # self.afficher()         




