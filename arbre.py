# ============================================================
# Exercice : Parcourir un arbre de dossiers (os.walk)
# ============================================================
# Objectifs :
# - découvrir os.walk() pour explorer récursivement
# - compter fichiers / dossiers et sommer les tailles
# - formater un affichage (alignement :30 et :>9)
# ============================================================
# Variante avec pathlib (commentée) :
# from pathlib import Path
# dossier = Path('./bac-a-sable')
# files = [f for f in dossier.rglob('*') if f.is_file()]
# for f in files:
#     print(f)
# ============================================================

import os

total = 0        # taille totale en octets
nb_fichiers = 0
nb_dossiers = 0

# os.walk parcourt TOUS les sous-dossiers récursivement
# À chaque tour : dossier courant, liste des sous-dossiers, liste des fichiers
for dossier, sous_dossiers, fichiers in os.walk('bac-a-sable'):
    nb_dossiers += 1
    print(f"{dossier}/")

    for nom in sorted(fichiers):
        # Chemin complet du fichier (dossier + nom)
        taille = os.path.getsize(os.path.join(dossier, nom))
        total += taille
        nb_fichiers += 1
        # {nom:30} → nom aligné sur 30 caractères
        # {taille:>9} → taille alignée à droite sur 9 caractères
        print(f"    {nom:30} {taille:>9}")

print(f"{nb_fichiers} fichiers dans {nb_dossiers} dossiers, {total / 1024 ** 2:.2f} Mo au total")
