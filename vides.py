# ============================================================
# Exercice : Trouver les dossiers et fichiers vides
# ============================================================
# Objectifs :
# - parcourir récursivement avec os.walk()
# - détecter un dossier sans contenu
# - détecter un fichier de taille 0
# ============================================================

import os

for dossier, sous_dossiers, fichiers in os.walk("bac-a-sable"):
    # Tri alphabétique des sous-dossiers (modifie la liste en place)
    sous_dossiers.sort()

    # Aucun sous-dossier ET aucun fichier → dossier vide
    if len(sous_dossiers) == 0 and len(fichiers) == 0:
        print(f"Dossier vide : {dossier}")

    for nom in sorted(fichiers):
        chemin = os.path.join(dossier, nom)
        # Un fichier vide fait 0 octet
        if os.path.getsize(chemin) == 0:
            print(f"Fichier vide : {chemin}")
