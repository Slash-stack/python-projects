#!/usr/bin/env python3

"""Module qui implémente le jeu Lights Out"""

from os import system
import sys

ON = "\u2588"
OFF = ' '
SEP_0 = '+'
SEP_1 = '-'
SEP_2 = '|'
ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z')


def eval(state):
    for element in state:
        if not element:
            return False
    return True


def jouer(state, largeur, hauteur):
    jeu = input("Choisissez la case à jouer:")
    ligne = ALPHABET.index(jeu[0])
    colonne = int(jeu[1]) - 1

    state[ligne * largeur + colonne] = not state[ligne * largeur + colonne]

    if ligne != 0:
        state[(ligne-1) * largeur + colonne] = not state[(ligne-1) * largeur + colonne]
    if ligne != hauteur - 1:
        state[(ligne + 1) * largeur + colonne] = not state[(ligne + 1) * largeur + colonne]
    if colonne != 0:
        state[ligne * largeur + colonne - 1] = not state[ligne * largeur + colonne - 1]
    if colonne != largeur - 1:
        state[ligne * largeur + colonne + 1] = not state[ligne * largeur + colonne + 1]


def afficher_table(state, largeur, hauteur):
    ligne = '  '
    for i in range(largeur):
        ligne += ' ' + str(i + 1) + ' '
    print(ligne)
    print(' ' + SEP_0 + SEP_1 * largeur * 3 + SEP_0)
    for i in range(hauteur):
        for w in range(3):
            if w == 1:
                ligne = ALPHABET[i] + SEP_2
            else :
                ligne = ' ' + SEP_2
            for j in range(largeur * 3):
                if state[i * largeur + (j // 3)]:
                    ligne += ON
                else:
                    ligne += OFF
            ligne += SEP_2
            print(ligne)
    print(' ' + SEP_0 + SEP_1 * largeur * 3 + SEP_0)


def jeu_par_defaut():
    hauteur = 8
    largeur = 8
    nb_cases = largeur * hauteur
    state = [False for _ in range(nb_cases)]
    afficher_table(state, largeur, hauteur)
    while not eval(state):
        jouer(state, largeur, hauteur)
        system('clear')
        afficher_table(state, largeur, hauteur)
    print("C'est gagné !!")
    exit(0)


def jeu_config(nom_fichier):
    """
    Exemple de fichier de configuration :
    +----+
    |..o.|
    |....|
    |o...|
    |..oo|
    +----+
    """
    with open(nom_fichier, 'r') as f:
        etat = f.readlines()
        hauteur = len(etat) - 2
        largeur = len(etat[-1]) - 2
        nb_cases = largeur * hauteur
        state = [False for _ in range(nb_cases)]
        i = 0
        for ligne in etat:
            j = 0
            for caracter in ligne:
                if caracter == '.':
                    state[hauteur * i + j] = False
                    j += 1
                if caracter == 'o':
                    state[hauteur * i + j] = True
                    j += 1
            if ligne[0] == '|':
                i += 1
    afficher_table(state, largeur, hauteur)
    while not eval(state):
        jouer(state, largeur, hauteur)
        system('clear')
        afficher_table(state, largeur, hauteur)
    print("C'est gagné !!")
    exit(0)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        jeu_par_defaut()
    elif len(sys.argv) != 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print('Utilisation ', sys.argv[0])
        print('Utilisation ', sys.argv[0], 'fichier_de_configuration.txt')
    else:
        jeu_config(sys.argv[1])
