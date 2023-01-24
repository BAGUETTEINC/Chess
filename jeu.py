# """
# Code correspondant à la partie
# """

import tkinter as tk
from tkinter import *
from fenetre import *


taille: int=8

if __name__ == '__main__':
    jeu = tk.Tk()
    jeu.title("2048")
    jeu.geometry("1080x720")
    jeu.minsize(720, 480)
    jeu.config(background='white')
    app = Fenetre_JOUER(jeu)
    jeu.mainloop()