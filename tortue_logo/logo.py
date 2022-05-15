"""Module tortue logo.

Ce module implémente les primitives graphiques basiques
d'une tortue logo.
"""

from module_svg import *
from math import sin, cos, pi


def avance(abscisse, ordonnee, direction, crayon_en_bas, distance):
    """Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un Point (défini dans notre module svg).
    """
    nouveau_abscisse = cos(direction * pi / 180) * distance + abscisse
    nouveau_ordonnee = ordonnee - sin(direction * pi / 180) * distance
    if crayon_en_bas:
        print(genere_segment(Point(abscisse, ordonnee), Point(nouveau_abscisse, nouveau_ordonnee)))
    return nouveau_abscisse, nouveau_ordonnee


def tourne_droite(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return (direction - angle) % 360


def tourne_gauche(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return (direction + angle) % 360
