#!/usr/bin/env python3

"""Module qui génere un plateau du jeu de l'oie"""

import module_svg
import sys
from collections import namedtuple

TAILLE = 40
Case = namedtuple('Case', 'a b c d')
# c-------d
# |       |
# |       |
# b-------a


def dessiner_case(largeur, hauteur, i, j, compteur):
    # case dans la ligne i et la colonne j
    global case_a_dessiner
    font_size = 10
    if compteur == 42:
        font_size = 20
    if i % 4 == 0:
        case_a_dessiner = Case(
            module_svg.Point((j+1) * TAILLE, hauteur - i * TAILLE),
            module_svg.Point(j * TAILLE, hauteur - i * TAILLE),
            module_svg.Point(j * TAILLE, hauteur - (i+1) * TAILLE),
            module_svg.Point((j+1) * TAILLE, hauteur - (i+1) * TAILLE),
        )
    elif i % 4 == 1:
        case_a_dessiner = Case(
            module_svg.Point(largeur, hauteur - i * TAILLE),
            module_svg.Point(largeur - TAILLE, hauteur - i * TAILLE),
            module_svg.Point(largeur - TAILLE, hauteur - (i + 1) * TAILLE),
            module_svg.Point(largeur, hauteur - (i + 1) * TAILLE),
        )
    elif i % 4 == 2:
        case_a_dessiner = Case(
            module_svg.Point(largeur - j * TAILLE, hauteur - i * TAILLE),
            module_svg.Point(largeur - (j+1) * TAILLE, hauteur - i * TAILLE),
            module_svg.Point(largeur - (j+1) * TAILLE, hauteur - (i + 1) * TAILLE),
            module_svg.Point(largeur - j * TAILLE, hauteur - (i + 1) * TAILLE),
        )
    elif i % 4 == 3:
        case_a_dessiner = Case(
            module_svg.Point(TAILLE, hauteur - i * TAILLE),
            module_svg.Point(0, hauteur - i * TAILLE),
            module_svg.Point(0, hauteur - (i+1) * TAILLE),
            module_svg.Point(TAILLE, hauteur - (i+1) * TAILLE),
        )
    print(module_svg.genere_polygone(case_a_dessiner))
    print(module_svg.genere_balise_debut_groupe("none", "red", 0))
    print(module_svg.genere_balise_debut_text(module_svg.Point(case_a_dessiner.b.x + 4, case_a_dessiner.b.y - 4), font_size))
    print(compteur)
    print(module_svg.genere_balise_fin_text())
    print(module_svg.genere_balise_fin_groupe())


def main():
    if len(sys.argv) != 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], " largeur hauteur > fichier.svg")
        sys.exit(1)
    largeur = int(sys.argv[1])
    hauteur = int(sys.argv[2])

    nb_cases_horizontale = largeur // TAILLE
    nb_cases_verticale = hauteur // TAILLE

    print(module_svg.genere_balise_debut_image(largeur, hauteur))
    print(module_svg.genere_balise_debut_groupe("black", 'white', 1))

    compteur = 0
    for i in range(nb_cases_verticale):
        for j in range(nb_cases_horizontale):
            if i % 4 == 1 and j > 1:
                continue
            if i % 4 == 3 and j > 1:
                continue
            compteur += 1
            dessiner_case(largeur, hauteur, i, j, compteur)

    print(module_svg.genere_balise_fin_groupe())
    print(module_svg.genere_balise_fin_image())


if __name__ == "__main__":
    main()
