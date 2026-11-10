# ============================================================
# Exercice F4 : Des tailles lisibles
# ============================================================
# Objectifs :
# - convertir des octets en Ko, Mo, Go avec if / elif
# - arrondir l'affichage avec :.1f
# ============================================================

import os

dossier = "bac-a-sable"
for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)
    if os.path.isfile(chemin):
        taille = os.path.getsize(chemin)
        # 1 Ko = 1024 octets, 1 Mo = 1024 Ko = 1024 ** 2 octets, etc.
        # On teste du plus petit au plus grand : l'ordre compte.
        if taille < 1024:
            lisible = f"{taille} o"
        elif taille < 1024 ** 2:
            lisible = f"{taille / 1024:.1f} Ko"
        elif taille < 1024 ** 3:
            lisible = f"{taille / 1024 ** 2:.1f} Mo"
        else:
            lisible = f"{taille / 1024 ** 3:.1f} Go"
        print(f"{nom:15} {lisible:>9}")
# Les fabricants de disques divisent par 1000 au lieu de 1024 :
# c'est pour ça qu'un disque « de 1 To » affiche 931 Go.
