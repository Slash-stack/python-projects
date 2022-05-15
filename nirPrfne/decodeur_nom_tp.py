#!/usr/bin/env python3
"""Decodeur pour le nomdu tp"""
import rotx


def main():
    """Decoder nirPrfne"""
    nom_fichier = input('Donnez le nom du fichier qui contiendra'
                        ' le résultat puis taper "entrée":\n')
    with open(nom_fichier, 'w') as fichier:
        fichier.write(rotx.rot13("n"))
        fichier.write(rotx.rot13("i"))
        fichier.write(rotx.rot13("r"))
        fichier.write(rotx.rot13("P"))
        fichier.write(rotx.rot13("r"))
        fichier.write(rotx.rot13("f"))
        fichier.write(rotx.rot13("n"))
        fichier.write(rotx.rot13("e"))
        fichier.close()
    print(rotx.rot(4, 'B'),
          rotx.rot(4, 'e'),
          rotx.rot(4, 'n'),
          rotx.rot(4, 'n'),
          rotx.rot(4, 'a'),
          rotx.rot(4, 'c'),
          rotx.rot(4, 'e'),
          rotx.rot(4, 'u'),
          rotx.rot(4, 'r'),
          sep='')


if __name__ == "__main__":
    main()
