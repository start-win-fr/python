# ============================================================
# Exercice V6 : Ma boîte à outils (le programme qui l'utilise)
# ============================================================
# Objectifs :
# - importer son propre module (outils.py, dans le même dossier)
# - appeler ses fonctions avec outils.nom_de_la_fonction()
# ============================================================

import outils   # le fichier outils.py, sans le .py

n = outils.demander_entier("Un nombre : ")
# « A if condition else B » choisit une valeur en une ligne
print("pair" if outils.est_pair(n) else "impair")
print("premier" if outils.est_premier(n) else "pas premier")
# Les tests de outils.py ne s'affichent pas : ils sont protégés par
# if __name__ == "__main__", qui est faux quand le fichier est importé.
