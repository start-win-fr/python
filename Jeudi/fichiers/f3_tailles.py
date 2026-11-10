# ============================================================
# Exercice F3 : La taille de chaque fichier
# ============================================================
# Objectifs :
# - lire la taille d'un fichier avec os.path.getsize()
# - aligner un affichage en colonnes dans une f-string
# ============================================================

import os

dossier = "bac-a-sable"
for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)
    # On ne garde que les fichiers : la « taille » d'un dossier donnée par
    # getsize n'est pas celle de son contenu.
    if os.path.isfile(chemin):
        taille = os.path.getsize(chemin)   # en octets
        # {nom:15} : 15 caractères réservés au nom
        # {taille:>10} : la taille alignée à droite sur 10 caractères
        print(f"{nom:15} {taille:>10} octets")
