# ============================================================
# TP Jeu 3 : Pierre, feuille, ciseaux, étape 1 (le coup de l'ordinateur)
# ============================================================
# Objectifs :
# - transformer un nombre tiré au hasard en texte avec if / elif / else
# ============================================================

import random

tirage = random.randint(1, 3)
if tirage == 1:
    ordi = "pierre"
elif tirage == 2:
    ordi = "feuille"
else:
    ordi = "ciseaux"

joueur = input("pierre, feuille ou ciseaux ? ")
print(f"Vous avez joué {joueur}, l'ordinateur a joué {ordi}.")
