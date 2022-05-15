#!/usr/bin/env python3

"""Module qui manipule des fichiers"""


def main():
    """crée un fichier toto.txt et écrit 2 lignes à l'aide des fonctions write et print"""
    with open("toto.txt", 'w', encoding="utf-8") as fichier:
        fichier.write("Bonjour,\n")
        print("Ceci est une deuxième ligne\n", file=fichier)
        fichier.close()


if __name__ == "__main__":
    main()
