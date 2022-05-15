"""Module d'encodage/décodage par rotation"""


def rot(decalage, lettre):
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractère de taille 1 ;
       - lettre est un soit une lettre majuscule
         soit une lettre minuscule.
    """
    if len(lettre) != 1:
        return None
    est_majuscule = ord('A') <= ord(lettre) <= ord('Z')
    est_minuscule = ord('a') <= ord(lettre) <= ord('z')
    if not(est_minuscule or est_majuscule):
        return None
    elif est_minuscule:
        return chr(ord('a') + (ord(lettre) - ord('a') + decalage) % 26)
    elif est_majuscule:
        return chr(ord('A') + (ord(lettre) - ord('A') + decalage) % 26)


def rot13(lettre):
    """Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    return rot(13, lettre)
