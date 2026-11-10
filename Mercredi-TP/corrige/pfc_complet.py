# ============================================================
# TP Jeu 3 : Pierre, feuille, ciseaux, version complète avec les bonus
# ============================================================
# Objectifs :
# - accepter les majuscules (.lower()) et les raccourcis p / f / c
# - redemander tant que la saisie n'est pas valable
# - compter les manches et les égalités
# ============================================================

import random

score_joueur = 0
score_ordi = 0
manches = 0
egalites = 0

while score_joueur < 3 and score_ordi < 3:
    tirage = random.randint(1, 3)
    if tirage == 1:
        ordi = "pierre"
    elif tirage == 2:
        ordi = "feuille"
    else:
        ordi = "ciseaux"

    # .lower() : « Pierre » ou « PIERRE » deviennent « pierre »
    joueur = input("pierre, feuille ou ciseaux (p/f/c) ? ").lower()
    if joueur == "p":
        joueur = "pierre"
    elif joueur == "f":
        joueur = "feuille"
    elif joueur == "c":
        joueur = "ciseaux"

    # Tant que la saisie n'est aucun des trois coups, on redemande
    while joueur != "pierre" and joueur != "feuille" and joueur != "ciseaux":
        print("Je n'ai pas compris.")
        joueur = input("pierre, feuille ou ciseaux (p/f/c) ? ").lower()
        # Les mêmes lignes qu'au-dessus : une fonction éviterait cette répétition
        if joueur == "p":
            joueur = "pierre"
        elif joueur == "f":
            joueur = "feuille"
        elif joueur == "c":
            joueur = "ciseaux"

    manches = manches + 1
    print(f"Vous : {joueur}, ordinateur : {ordi}")
    if joueur == ordi:
        print("Égalité !")
        egalites = egalites + 1
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

if score_joueur == 3:
    print("Vous gagnez la partie !")
else:
    print("L'ordinateur gagne la partie.")
print(f"{manches} manches, dont {egalites} égalité(s).")
