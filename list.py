# ============================================================
# Exercice : Lister le contenu d'un dossier
# ============================================================
# Objectifs :
# - utiliser os.listdir() pour lister un dossier
# - construire un chemin avec os.path.join()
# - distinguer fichiers et dossiers (isdir)
# ============================================================

import os

dossier = "bac-a-sable"

# sorted() trie les noms par ordre alphabétique
contenu = sorted(os.listdir(dossier))

for nom in contenu:
    # On reconstruit le chemin complet : "bac-a-sable" + "rapport.txt"
    chemin = os.path.join(dossier, nom)

    # isdir() → True si c'est un dossier, False si c'est un fichier
    if os.path.isdir(chemin):
        print(f"[D] {nom}")  # D = Dossier
    else:
        print(f"[F] {nom}")  # F = Fichier
