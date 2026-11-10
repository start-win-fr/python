# ============================================================
# Exercice F6 : Trier par extension
# ============================================================
# Objectifs :
# - filtrer des noms avec .endswith()
# - récupérer l'extension avec os.path.splitext()
# - compter avec un dictionnaire
# ============================================================

import os

dossier = "bac-a-sable"

# 1. Seulement les fichiers texte
print("Les fichiers texte :")
for nom in sorted(os.listdir(dossier)):
    if nom.endswith(".txt"):   # le nom se termine-t-il par .txt ?
        print(" ", nom)

# 2. Le nombre de fichiers par extension
compte = {}
for nom in sorted(os.listdir(dossier)):
    if os.path.isfile(os.path.join(dossier, nom)):
        # splitext("rapport.txt") renvoie ("rapport", ".txt") : [1] = l'extension
        extension = os.path.splitext(nom)[1]
        compte[extension] = compte.get(extension, 0) + 1   # le patron du compteur
print(compte)
