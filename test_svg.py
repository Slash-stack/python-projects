#!/usr/bin/env python3
"""Programme de test de notre module svg"""
from module_svg import genere_rectangle, genere_cercle, genere_balise_fin_image,\
    genere_balise_fin_groupe, genere_balise_debut_groupe, genere_balise_debut_image, Point


def test():
    """fonction de test"""
    print(genere_balise_debut_image(200, 200))
    print(genere_balise_debut_groupe('black', 'red', 1))
    print(genere_cercle(Point(50, 50), 20))
    print(genere_rectangle(100, 100, Point(70, 70)))
    print(genere_balise_fin_groupe())
    print(genere_balise_fin_image())


if __name__ == "__main__":
    test()
