# ============================================================
# Exercice F9 : Les fichiers récents
# ============================================================
# Objectifs :
# - lire la date de modification avec os.path.getmtime()
# - la transformer en vraie date avec datetime.fromtimestamp()
# - comparer et formater des dates
# ============================================================

import os
from datetime import datetime

limite = datetime(2026, 10, 1)   # le 1er octobre 2026, à minuit
for dossier, sous_dossiers, fichiers in os.walk("bac-a-sable"):
    sous_dossiers.sort()
    for nom in sorted(fichiers):
        chemin = os.path.join(dossier, nom)
        # getmtime renvoie un nombre de secondes depuis le 1er janvier 1970
        date = datetime.fromtimestamp(os.path.getmtime(chemin))
        if date >= limite:   # les dates se comparent comme des nombres
            # Le format de strftime est entre apostrophes, puisque la
            # f-string est déjà entre guillemets doubles.
            print(f"{date.strftime('%d/%m/%Y %H:%M')}  {chemin}")
