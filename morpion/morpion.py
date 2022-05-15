#!/usr/bin/env python3

"""Un jeu de morpion"""


# Les différents types de joueurs sont représentés par des modules.
# Les modules joueur_humain et joueur_ordi doivent être réaliser.
# Le module joueur_ordi_malin est fourni.
# Le module joueur_humain demande simplement à l'utilisateur de jouer.
# Le module joueur_ordi joue automatiquement. Sa stratégie n'est pas spécifiée.
import joueur_humain
import joueur_ordi
import joueur_ordi_malin


def recupere_chaine_a_afficher(symbole):
    """Renvoie la chaîne de caractère à afficher pour le symbole donné.

    Pour le symbole "x", le caractère unicode "MULTIPLICATION X", affiché
    en rouge doit être utilisé.
    Pour le symbole "o", le caractère unicode "WHITE CIRCLE", affiché
    en bleu doit être utilisé.

    précondition : symbole est soit "x" soit "o"
    """
    if symbole == 'x':
        return u"\033[91m✖\033[0m"
    elif symbole == 'o':
        return u"\033[0m●\033[0m"
    else:
        return ' '


def affiche_plateau(cases):
    """Affiche le plateau représenté par le tuples cases à 9 éléments.

    L'affichage se fait sur la sortie standard uniquement en utilisant
    des appels à la fonction print.

    précondition : chacune des cases contient soit
      - la chaîne de caractères "x" (case occupée par le joueur 1)
      - la chaîne de caractères "o" (case occupée par le joueur 2)
      - la chaîne de caractères "i" avec i entier correspondant au
        numéro de la case (case libre)
    précondition : cases est un tuple de 9 éléments
    """
    if len(cases) != 9:
        return None
    print("\n============================\n")
    print(' ' + recupere_chaine_a_afficher(cases[0]) + ' ',
          ' ' + recupere_chaine_a_afficher(cases[1]) + ' ',
          ' ' + recupere_chaine_a_afficher(cases[2]) + ' ', sep=' | ')
    print("____ ____ ____")
    print(' ' + recupere_chaine_a_afficher(cases[3]) + ' ',
          ' ' + recupere_chaine_a_afficher(cases[4]) + ' ',
          ' ' + recupere_chaine_a_afficher(cases[5]) + ' ', sep=' | ')
    print("____ ____ ____")
    print(' ' + recupere_chaine_a_afficher(cases[6]) + ' ',
          ' ' + recupere_chaine_a_afficher(cases[7]) + ' ',
          ' ' + recupere_chaine_a_afficher(cases[8]) + ' ', sep=' | ')


def joue_coup(joueur, joueur_num, cases, symbole):
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
    affiche_plateau(cases)
    cases = joueur.joue_coup(cases, symbole)
    if (cases[0] == symbole and cases[1] == symbole and cases[2] == symbole) or \
            (cases[3] == symbole and cases[4] == symbole and cases[5] == symbole) or \
            (cases[6] == symbole and cases[7] == symbole and cases[8] == symbole) or \
            (cases[0] == symbole and cases[3] == symbole and cases[6] == symbole) or \
            (cases[1] == symbole and cases[4] == symbole and cases[7] == symbole) or \
            (cases[2] == symbole and cases[5] == symbole and cases[8] == symbole) or \
            (cases[0] == symbole and cases[4] == symbole and cases[8] == symbole) or \
            (cases[2] == symbole and cases[4] == symbole and cases[6] == symbole):
        affiche_plateau(cases)
        print("Le joueur ", joueur_num, " a gagné la partie !!!\n Bien joué ^^")
        exit(0)
    return cases


def joue_partie():
    """Joue une partie complète de morpion"""

    # Initialisation des deux joueurs en demandant à l'utilisateur
    # Parenthèses nécessaires pour "spliter un string literal"
    message_choix_joueur = ("Veuillez choisir le type du joueur {} en tapant\n"
                            "  0 pour humain\n"
                            "  1 pour un ordinateur\n"
                            "  2 pour un ordinateur très malin\n"
                            "  entrez votre choix : ")

    print(message_choix_joueur.format(1), end="")
    type1 = int(input())
    print(message_choix_joueur.format(2), end="")
    type2 = int(input())
    joueur1 = joueur_humain if type1 == 0 else (joueur_ordi
                                                if type1 == 1
                                                else joueur_ordi_malin)
    joueur2 = joueur_humain if type2 == 0 else (joueur_ordi
                                                if type2 == 1
                                                else joueur_ordi_malin)
    print()

    # Initialisation et affichage du plateau vide
    # Une case vide est représentée par son numéro,
    # utilisé par le joueur humain pour indiquer
    # quelle case il joue.
    cases = [0, 1, 2,
             3, 4, 5,
             6, 7, 8]

    # Joue 9 coups au maximum
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")

    # Si on arrive là, il y a égalité
    print("Match nul !")


if __name__ == "__main__":
    joue_partie()
