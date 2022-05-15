"""Module du joueur ordi pas très malin"""
import random


def joue_coup(cases, symbole):
    """Joue un coup.

    Cette fonction effectue les opérations suivantes tout en affichant
    ce qu'il se passe sur la sortie standard :
      - affiche le plateau représenté par cases
      - utilise le module joueur pour savoir quel coup doit être joué
      - met à jour le plateau de jeu avec ce coup
      - affiche le plateau et le numéro du joueur gagnant si c'est gagné
        puis quitte le programme
      - renvoie le nouveau plateau

    précondition : joueur est un module avec une fonction
                   joue_coup(cases, symbole) qui renvoie le
                   numéro d'une case précédemment inoccupée.
    précondition : joueur_num est soit l'entier 1 soit l'entier 2
    précondition : cases est un tuple de 9 éléments
    précondition : symbole est soit "x" soit "o"

    """
    position = random.randint(0, 8)
    while cases[position] != position:
        position = random.randint(0, 8)
    cases[position] = symbole
    return cases
