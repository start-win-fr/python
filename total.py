# ============================================================
# Exercice : Taille totale et plus gros fichier
# ============================================================
# Objectifs :
# - parcourir les fichiers d'un dossier
# - mesurer la taille avec os.path.getsize()
# - accumuler un total et mémoriser le maximum
# ============================================================

import os

dossier = 'bac-a-sable'

total = 0              # somme des tailles (en octets)
plus_gros_nom = ""     # nom du plus gros fichier trouvé
plus_gros_taille = -1  # -1 pour démarrer : toute taille réelle sera plus grande

for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)

    # On ignore les sous-dossiers : on ne traite que les fichiers
    if os.path.isfile(chemin):
        taille = os.path.getsize(chemin)  # taille en octets
        total += taille

        # Mise à jour du "champion" si ce fichier est plus gros
        if taille > plus_gros_taille:
            plus_gros_taille = taille
            plus_gros_nom = nom

# 1024 ** 2 = 1 Mo (mégaoctet)
print(f"Total : {total} octets, soit {total / 1024 ** 2:.2f} Mo")
print(f"Le plus gros : {plus_gros_nom} ({plus_gros_taille} octets)")
