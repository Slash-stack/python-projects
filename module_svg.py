"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

from collections import namedtuple

# Definition de la structure Point composée de deux attributs x et y
Point = namedtuple('Point', 'x y')


def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaine de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l’origine est en haut à gauche et l’axe des Y est orienté vers le
    bas.
    """
    return f"<svg width='{largeur}' height='{hauteur}'>"


def genere_balise_fin_image():
    """
    Retourne la chaine de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l’image, juste avant la fin du fichier.
    """
    return "</svg>"


def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    Retourne la chaine de caractères correspondant à une balise ouvrante
    définissant un groupe d’éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l’image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d’épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    return f"<g stroke='{couleur_ligne}' stroke-width='{epaisseur_ligne}' " \
           f"fill='{couleur_remplissage}'>"


def genere_balise_fin_groupe():
    """
    Retourne la chaine de caractères correspondant à la balise fermante pour un
    groupe d’éléments.
    """
    return "</g>"


def genere_cercle(centre, rayon):
    """
    Retourne la chaine de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
    """
    return f"<circle cx='{centre.x}' cy='{centre.y}' r='{rayon}'/>"


def genere_rectangle(largeur, hauteur, depart):
    """
    Retourne la chaine de caractères correspondant à un élément SVG représentant
    un rectangle.

    départ est une structure de données de type Point, et largeur et hauteur le nombre de
    pixels indiquant les dimensions du rectangle.
    """
    return f"<rect width='{largeur}' height='{hauteur}' x='{depart.x}' y='{depart.y}'/>"


def genere_segment(dep, arr):
    """
    Retourne la chaine de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr.
    """
    return f"<line x1='{dep.x}' y1='{dep.y}' x2='{arr.x}' y2='{arr.y}'/>"


def genere_polygone(points):
    """
    Retourne la chaine de caractères correspondant à un élément SVG représentant un polygone.
    points est un tableaux de points.
    """
    string = "<polygon points = '"
    for pt in points:
        string += f"{pt.x}, {pt.y} "
    string += "' />"
    return string


def genere_balise_debut_groupe_transp(niveau_opacite):
    """
    Retourne la chaine de caractères correspondant à une balise ouvrant un
    groupe d’éléments qui, dans son ensemble, sera partiellement transparent.
    Les éléments qui composent le groupe se masquent les uns les autres dans
    l’ordre d’apparition (ils ne sont pas transparents entre eux).
    niveau_opacite doit être un nombre entre 0 et 1. Ce groupe doit être refermé
    de la même manière que les groupes définissant un style.
    """
    return f"<g opacity='{niveau_opacite}'>"


def genere_balise_debut_text(point, font_size):
    return f"<text x='{point.x}' y='{point.y}' font-family='Verdana' font-size='{font_size}'>"


def genere_balise_fin_text():
    return "</text>"
