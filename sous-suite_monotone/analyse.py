#!/usr/bin/env python3
"""Module qui identifie la plus grande sous-suite monotone"""

import sys


def compte_dernier_elem(suite):
    compteur = 1
    nombre = suite[-1]
    while compteur + 1 <= len(suite):
        if suite[-(compteur+1)] == nombre:
            compteur += 1
        else:
            break
    return compteur


def traite_nombre(suite, type_suite, nombre):
    """Traite le nombre donné vis à vis de la suite donnée.

    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite a changé de sens
    """
    if len(suite) == 0:
        return True, 0
    if type_suite >= 0 and suite[-1] <= nombre:
        # suite croissante
        return True, 1
    if type_suite <= 0 and suite[-1] >= nombre:
        # suite décroissante
        return True, -1
    return False, -type_suite


def main():
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "fichier.txt")
        sys.exit(1)

    with open(sys.argv[1], 'r') as fichier:
        suite_max = []
        suite = []
        type_suite = 0
        for ligne in fichier:
            for chiffre in ligne.split():
                if chiffre.isdigit():
                    statement, type_suite = traite_nombre(suite, type_suite, int(chiffre))
                    if statement:
                        suite.append(int(chiffre))
                    else:
                        if len(suite) > len(suite_max):
                            suite_max = suite
                        suite = suite[-compte_dernier_elem(suite):]
                        suite.append(int(chiffre))
    print(suite_max)


if __name__ == '__main__':
    main()
