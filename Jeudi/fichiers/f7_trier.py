# ============================================================
# Exercice F7 : Du plus gros au plus petit
# ============================================================
# Objectifs :
# - construire une liste de tuples (taille, nom)
# - trier avec sorted(..., reverse=True)
# - garder les premiers éléments avec [:3]
# ============================================================

import os

dossier = "bac-a-sable"
fichiers = []
for nom in os.listdir(dossier):
    chemin = os.path.join(dossier, nom)
    if os.path.isfile(chemin):
        # La taille EN PREMIER dans le tuple : sorted compare les tuples
        # élément par élément, donc il triera par taille.
        fichiers.append((os.path.getsize(chemin), nom))

fichiers = sorted(fichiers, reverse=True)   # du plus gros au plus petit
for taille, nom in fichiers[:3]:            # on déballe chaque tuple
    print(f"{taille:>10}  {nom}")
