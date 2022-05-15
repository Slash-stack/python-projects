#!/usr/bin/env python3
"""Une version python de l'outil standard cat qui permet d'afficher sur la sortie standard le contenu d'un fichier"""

import sys

def affiche_fichier(chemin_fichier):
    """Affiche le contenu du fichier donné en paramètre"""

    # On ouvre le fichier en lecture
    fichier = open(chemin_fichier, 'r')

    # On parcours un fichier ligne par ligne.
    # Gardons à l'esprit que beaucoup de choses se cachent
    # derrière ces boucles. Autrement dit, ça va piquer un
    # peu au début quand on devra faire la même chose en C
    # au second semestre. Merci pyhton :)
    for ligne in fichier:
        print(ligne, end="")

    # N'oublions pas de fermer le fichier
    fichier.close()

# Le chemin du fichier à affiché est donné en argument sur la ligne de commande.
# On le récupère avec sys.argv en se rappelant que sys.arv[0] ne contient pas
# le premier argument mais le nom du programme lui même.
affiche_fichier(sys.argv[1])
