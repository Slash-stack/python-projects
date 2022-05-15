#!/usr/bin/env python3

"""Illustration simple des f-strings."""


def teste_fstrings():
    """Utilisation de f-strings pour afficher un message."""
    prenom = "Alexia"
    age = 7
    message_a_afficher = f"{prenom} a {age} ans"
    print(message_a_afficher)


def convertit_point_en_chaine(x, y):
    """convertit un point définit par son abscisse et son ordonnée en chaîne de caractère"""
    return f"({x}, {y})"


if __name__ == "__main__":
    teste_fstrings()
    print(convertit_point_en_chaine(12.2, 3.3))
