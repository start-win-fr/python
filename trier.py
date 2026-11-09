# ============================================================
# Exercice : Trier les fichiers par taille
# ============================================================
# Objectifs :
# - construire une liste de tuples (nom, taille)
# - trier cette liste avec sorted(..., reverse=True)
# - afficher les fichiers du plus gros au plus petit
# ============================================================

import os

dossier = 'bac-a-sable'

fichiers = []  # liste de tuples : (nom, taille)

for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)
    if os.path.isfile(chemin):
        # On stocke le nom ET la taille ensemble dans un tuple
        fichiers.append((nom, os.path.getsize(chemin)))

# sorted sur des tuples trie d'abord par le 1er élément (ici le nom).
# Pour trier par taille, on pourrait utiliser : key=lambda x: x[1]
for taille, nom in sorted(fichiers, reverse=True):
    print(f"{taille} {nom}")
