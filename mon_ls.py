# ============================================================
# Exercice : Mini commande "ls -lh" en Python
# ============================================================
# Objectifs :
# - lire un argument en ligne de commande (sys.argv)
# - écrire une fonction qui convertit une taille en o/Ko/Mo/Go
# - afficher date de modification + taille pour chaque entrée
# Usage : python mon_ls.py bac-a-sable
# ============================================================

import os
import sys
from datetime import datetime


def lisible(taille):
    """Renvoie la taille en o, Ko, Mo ou Go, comme ls -lh."""
    if taille < 1024:
        return f"{taille} o"
    elif taille < 1024 ** 2:
        return f"{taille / 1024:.1f} Ko"
    elif taille < 1024 ** 3:
        return f"{taille / 1024 ** 2:.1f} Mo"
    return f"{taille / 1024 ** 3:.1f} Go"


# sys.argv[0] = nom du script, sys.argv[1] = 1er argument (le dossier)
if len(sys.argv) != 2:
    print("Usage : python3 mon_ls.py dossier")
    sys.exit(1)  # quitte le programme avec un code d'erreur

dossier = sys.argv[1]
if not os.path.isdir(dossier):
    print(f"{dossier} n'est pas un dossier.")
    sys.exit(1)

for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)

    # getmtime = date de dernière modification (timestamp) → datetime → texte
    date = datetime.fromtimestamp(os.path.getmtime(chemin)).strftime("%d/%m/%Y %H:%M")

    if os.path.isdir(chemin):
        # "d" = dossier ; pas de taille affichée (tiret)
        print(f"d {'-':>9} {date} {nom}/")
    else:
        # "-" = fichier ; taille formatée alignée à droite sur 9 caractères
        print(f"- {lisible(os.path.getsize(chemin)):>9} {date} {nom}")
