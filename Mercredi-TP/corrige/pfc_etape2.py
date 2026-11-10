# ============================================================
# TP Jeu 3 : Pierre, feuille, ciseaux, étape 2 (qui gagne ?)
# ============================================================
# Objectifs :
# - écrire une longue condition avec and et or
# - couper une ligne trop longue avec \
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
print(f"L'ordinateur a joué {ordi}.")

# Trois cas : égalité, le joueur gagne, sinon l'ordinateur gagne.
if joueur == ordi:
    print("Égalité !")
# Le joueur gagne dans 3 situations. Les parenthèses regroupent chaque
# situation (deux conditions liées par and), et or les relie entre elles.
# Le \ en fin de ligne dit à Python que l'instruction continue en dessous.
elif (joueur == "pierre" and ordi == "ciseaux") or \
     (joueur == "feuille" and ordi == "pierre") or \
     (joueur == "ciseaux" and ordi == "feuille"):
    print("Vous gagnez la manche !")
else:
    print("L'ordinateur gagne la manche.")
