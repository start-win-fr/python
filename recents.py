# ============================================================
# Exercice : Fichiers modifiés récemment
# ============================================================
# Objectifs :
# - lire la date de modification d'un fichier (getmtime)
# - comparer des dates avec datetime
# - filtrer et afficher les fichiers "récents"
# ============================================================

import os
from datetime import datetime

# Seuil : on affiche les fichiers modifiés à partir du 1er octobre 2026
limite = datetime(2026, 10, 1)

for dossier, sous_dossiers, fichiers in os.walk("bac-a-sable"):
    sous_dossiers.sort()  # parcours des sous-dossiers dans l'ordre alphabétique

    for nom in sorted(fichiers):
        chemin = os.path.join(dossier, nom)

        # getmtime renvoie un timestamp (secondes) → on le convertit en datetime
        date = datetime.fromtimestamp(os.path.getmtime(chemin))

        if date >= limite:
            # strftime formate la date : jour/mois/année heure:minute
            print(f"{date.strftime('%d/%m/%Y %H:%M')} {chemin}")
