import random


def initialisation(taille):
    return [[0 for x in range(taille)] for i in range(taille)]


def identique(liste, valeur):
    if not (liste):
        return [0, -2]
    else:
        compteur2 = len(liste) - 1
        while (liste[compteur2] == 0) & (compteur2 >= 0):
            compteur2 -= 1
        if compteur2 < 0:
            return [0, -1]
        else:
            if liste[compteur2] == valeur:
                return [1, compteur2]
            else:
                return [0, -1]


def decalage(liste):
    taille=len(liste)
    current_pos = taille - 1
    compteur = taille - 1
    liste2 = [0 for x in range(taille)]
    score= 0

    while (current_pos >= 0) & (compteur >= 0):
        while (liste[compteur] == 0) & (compteur >= 0):
            compteur -= 1
        if compteur < 0:
            return [liste2,score]
        else:
            [isidentique, pos] = identique(liste[0:compteur], liste[compteur])
            if isidentique:
                liste2[current_pos] = liste[compteur] * 2
                score += liste[compteur] * 2
                compteur = pos - 1
            else:
                liste2[current_pos] = liste[compteur]
                compteur -= 1
            current_pos -= 1
    return [liste2,score]