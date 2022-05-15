#!/usr/bin/env python3

"""Illustration de pylint"""

def affiche_moyenne(note_projet, note_exam):
    """Affiche la moyenne comptabilisé avez la note de projet + note d'exam"""
    moyenne = (1 * note_projet + 3 * note_exam) / 4
    print(moyenne)

if __name__ == "__main__":
    affiche_moyenne(12, 12)
