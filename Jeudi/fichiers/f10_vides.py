# ============================================================
# Exercice F10 : Le ménage, vides et inutiles
# ============================================================
# Objectifs :
# - repérer les fichiers vides (taille 0)
# - repérer les dossiers vides (ni sous-dossier, ni fichier)
# ============================================================

import os

for dossier, sous_dossiers, fichiers in os.walk("bac-a-sable"):
    sous_dossiers.sort()
    # Un dossier vide : aucun sous-dossier ET aucun fichier
    if len(sous_dossiers) == 0 and len(fichiers) == 0:
        print(f"Dossier vide  : {dossier}")
    for nom in sorted(fichiers):
        chemin = os.path.join(dossier, nom)
        if os.path.getsize(chemin) == 0:
            print(f"Fichier vide  : {chemin}")
# L'équivalent bash : find bac-a-sable -empty
