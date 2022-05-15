""" module de dessin pour générer un kaléidoscope"""

from random import choice
import module_svg


def couleur_aleatoire():
    return choice(["red", "green", "blue", "orange", "yellow"])


def affiche_triangle(triangle, couleur):
    print(module_svg.genere_polygone(triangle))
