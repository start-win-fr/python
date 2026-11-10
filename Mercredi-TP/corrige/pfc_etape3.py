# ============================================================
# TP Jeu 3 : Pierre, feuille, ciseaux, étape 3 (le premier à trois)
# ============================================================
# Objectifs :
# - deux compteurs de score
# - une boucle qui continue tant que personne n'a gagné
# ============================================================

import random

score_joueur = 0
score_ordi = 0

# Tant que PERSONNE n'a 3 points
while score_joueur < 3 and score_ordi < 3:
    # Le tirage est DANS la boucle : un nouveau coup à chaque manche
    tirage = random.randint(1, 3)
    if tirage == 1:
        ordi = "pierre"
    elif tirage == 2:
        ordi = "feuille"
    else:
        ordi = "ciseaux"

    joueur = input("pierre, feuille ou ciseaux ? ")
    print(f"L'ordinateur a joué {ordi}.")

    if joueur == ordi:
        print("Égalité !")
    elif (joueur == "pierre" and ordi == "ciseaux") or \
         (joueur == "feuille" and ordi == "pierre") or \
         (joueur == "ciseaux" and ordi == "feuille"):
        print("Vous gagnez la manche !")
        score_joueur = score_joueur + 1
    else:
        print("L'ordinateur gagne la manche.")
        score_ordi = score_ordi + 1
    print(f"Score : vous {score_joueur}, ordinateur {score_ordi}")
    print()

# Après la boucle, l'un des deux a forcément 3 points
if score_joueur == 3:
    print("Vous gagnez la partie !")
else:
    print("L'ordinateur gagne la partie.")
