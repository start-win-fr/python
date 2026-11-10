# ============================================================
# Exercice F5 : Le total et le plus gros
# ============================================================
# Objectifs :
# - deux accumulateurs dans la même boucle : une somme et un maximum
# ============================================================

import os

dossier = "bac-a-sable"
total = 0
plus_gros_nom = ""
plus_gros_taille = -1   # -1 : même un fichier vide (0 octet) le remplacera
for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)
    if os.path.isfile(chemin):
        taille = os.path.getsize(chemin)
        total += taille
        if taille > plus_gros_taille:   # un nouveau « champion »
            plus_gros_taille = taille
            plus_gros_nom = nom

print(f"Total : {total} octets, soit {total / 1024 ** 2:.2f} Mo")
print(f"Le plus gros : {plus_gros_nom} ({plus_gros_taille} octets)")
# Ce total ne compte que les fichiers posés directement dans bac-a-sable.
# Pour descendre dans les sous-dossiers : os.walk (exercice F8).
