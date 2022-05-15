#!/usr/bin/env python3

"""Utilisation d'Input"""

import datetime


def main():
    """Fonction qui lit dans l'entrée standard l'âge du capitaine et renvoie son âge en 2050"""
    age = int(input("Entrez l'âge du capitaine: "))
    current_time = datetime.date(2022, 4, 18)
    target_time = datetime.date(2050, 1, 1)
    age += (target_time - current_time).days / 356
    print("En 2050, le capitaine aura : ", int(age), " ans.")


if __name__ == "__main__":
    main()
