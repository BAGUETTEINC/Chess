import random
import tkinter as tk
from tkinter import *
from fenetre import *
from f_annexe import *



class Partie:
    def __init__(self, taille):
        self.taille = taille
        self.tab = []

    def initialisation(self):
        taille   = self.taille
        self.tab = [[0 for x in range(taille)] for i in range(taille)]

    def changement(self, mouvement):
        taille=self.taille
        liste = [0 for x in range(taille)]
        liste2 = [0 for x in range(taille)]
        tab2 = self.tab
        if mouvement == "gauche":
            for ligne in range(taille):
                for colonne in range(taille):
                    liste[colonne] = self.tab[ligne][taille - colonne - 1]
                [liste,score] = decalage(liste)
                self.score_total += score
                for colonne in range(taille):
                    self.tab[ligne][colonne] = liste[taille - colonne - 1]

        elif mouvement == "bas":
            for colonne in range(taille):
                for ligne in range(taille):
                    liste[ligne] = tab2[ligne][colonne]
                [liste,score] = decalage(liste)
                self.score_total += score
                for ligne in range(taille):
                    self.tab[ligne][colonne] = liste[ligne]


        elif mouvement == "droite":
            for ligne in range(taille):
                [self.tab[ligne],score] = decalage(tab2[ligne])
                self.score_total += score

        elif mouvement == "haut":
            for colonne in range(taille):
                for ligne in range(taille):
                    liste[ligne] = tab2[taille - ligne - 1][colonne]
                [liste,score] = decalage(liste)
                self.score_total += score
                for ligne in range(taille):
                    self.tab[ligne][colonne] = liste[taille - ligne - 1]
        print("Le score total est : ",self.score_total)



    def apparition(self):
        compteur0 = 0
        compteur0b = 0
        proba4 = random.uniform(0, 10) > 9
        taille=self.taille
        for ligne in range(taille):
            for colonne in range(taille):
                compteur0 += (self.tab[ligne][colonne] == 0)
        n = random.randint(1, compteur0)
        for ligne in range(taille):
            for colonne in range(taille):
                compteur0b += (self.tab[ligne][colonne] == 0)
                if compteur0b == n:
                    self.tab[ligne][colonne] = 2 * (1 + proba4)
                    compteur0b=taille*taille+1

    def afficher(self):
        taille=self.taille
        for ligne in range(taille):
                print(self.tab[ligne][0],self.tab[ligne][1],self.tab[ligne][2],self.tab[ligne][3])
        print("\n")

