#!/usr/bin/env python3
"""Convertisseur : fichier txt -> image svg"""
from module_svg import *


def main():
    """
    Lit dans l'entree standard les coordonnées des 1000 points et écrit
    dans la sortie standard le fichier svg.
    """
    print(genere_balise_debut_image(640, 480))
    print(genere_balise_debut_groupe('black', 'white', 2))
    for _ in range(1000):
        abscisse = int(input())
        ordonnee = int(input())
        print(genere_cercle(Point(abscisse, ordonnee), 2))
    print(genere_balise_fin_groupe())
    print(genere_balise_fin_image())


if __name__ == "__main__":
    main()