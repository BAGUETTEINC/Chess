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
    
    cnv = Canvas(jeu, width=720, height=720, bg="ivory")
    imagee = PhotoImage(file = "C:/Users/ed190/Desktop/Chess/Sprite/bqueen.png")    
    item = cnv.create_image((0,0), image = imagee)
    cnv.image = imagee
    cnv.pack(expand=YES)
    cnv.move(item,400,400)
    jeu.mainloop()
