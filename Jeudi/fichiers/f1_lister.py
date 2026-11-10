# ============================================================
# Exercice F1 : Lister un dossier
# ============================================================
# Objectifs :
# - lister le contenu d'un dossier avec os.listdir()
# - trier les noms avec sorted() pour un affichage stable
# ============================================================
# À lancer dans le dossier qui contient bac-a-sable
# (fabriqué par : python3 creer_bac_a_sable.py)

import os

# os.listdir renvoie les NOMS (pas les chemins), dans un ordre quelconque :
# sorted() les remet par ordre alphabétique.
contenu = sorted(os.listdir("bac-a-sable"))
for nom in contenu:
    print(nom)
print(f"{len(contenu)} éléments")
