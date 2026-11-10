# ============================================================
# Exercice F11 : Votre propre ls -l
# ============================================================
# Objectifs :
# - recevoir le dossier en argument avec sys.argv
# - réutiliser la conversion de F4 dans une fonction
# - refuser proprement un mauvais argument
# ============================================================
# Usage : python3 f11_mon_ls.py bac-a-sable/documents

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


# Sans argument : on explique comment s'en servir, et on quitte avec le code 1
if len(sys.argv) != 2:
    print("Usage : python3 f11_mon_ls.py dossier")
    sys.exit(1)

dossier = sys.argv[1]
if not os.path.isdir(dossier):
    print(f"{dossier} n'est pas un dossier.")
    sys.exit(1)

for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)
    date = datetime.fromtimestamp(os.path.getmtime(chemin)).strftime("%d/%m/%Y %H:%M")
    if os.path.isdir(chemin):
        print(f"d  {'-':>9}  {date}  {nom}/")
    else:
        print(f"-  {lisible(os.path.getsize(chemin)):>9}  {date}  {nom}")
# La date d'un dossier change quand on y ajoute ou retire un fichier,
# pas quand on modifie un fichier qui est dedans.
