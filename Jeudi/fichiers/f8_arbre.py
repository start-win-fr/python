# ============================================================
# Exercice F8 : Descendre dans les sous-dossiers
# ============================================================
# Objectifs :
# - parcourir tout un arbre de dossiers avec os.walk()
# - cumuler des totaux sur tout l'arbre
# ============================================================

import os

total = 0
nb_fichiers = 0
nb_dossiers = 0
# À chaque tour, os.walk donne : le dossier visité, la liste de ses
# sous-dossiers, la liste de ses fichiers.
for dossier, sous_dossiers, fichiers in os.walk("bac-a-sable"):
    # Trier la liste SUR PLACE change l'ordre dans lequel os.walk visitera
    # les sous-dossiers : l'affichage est le même sur toutes les machines.
    sous_dossiers.sort()
    nb_dossiers += 1
    print(f"{dossier}/")
    for nom in sorted(fichiers):
        taille = os.path.getsize(os.path.join(dossier, nom))
        total += taille
        nb_fichiers += 1
        print(f"    {nom:22} {taille:>9}")

# Le compte de dossiers inclut bac-a-sable lui-même
print(f"{nb_fichiers} fichiers dans {nb_dossiers} dossiers, {total / 1024 ** 2:.2f} Mo au total")
