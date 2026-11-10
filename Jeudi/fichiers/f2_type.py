# ============================================================
# Exercice F2 : Fichier ou dossier ?
# ============================================================
# Objectifs :
# - fabriquer un chemin complet avec os.path.join()
# - distinguer dossiers et fichiers avec os.path.isdir()
# ============================================================

import os

dossier = "bac-a-sable"
nb_fichiers = 0
nb_dossiers = 0
for nom in sorted(os.listdir(dossier)):
    # « photos » seul ne suffit pas : Python le chercherait dans le dossier
    # courant, ne le trouverait pas, et isdir répondrait False sans erreur.
    # Il faut le chemin complet « bac-a-sable/photos ».
    chemin = os.path.join(dossier, nom)
    if os.path.isdir(chemin):
        print(f"[D] {nom}")
        nb_dossiers += 1
    else:
        print(f"[F] {nom}")
        nb_fichiers += 1
print(f"{nb_fichiers} fichiers, {nb_dossiers} dossiers")
