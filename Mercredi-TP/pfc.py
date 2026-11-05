# ============================================================
# TP : Pierre – Feuille – Ciseaux (meilleur en 3 manches)
# ============================================================
# Objectifs :
# - importer le module random
# - utiliser une boucle while avec une condition composée
# - comparer des chaînes et gérer plusieurs cas de victoire
# - incrémenter un score
# ============================================================

import random  # pour tirer un choix aléatoire pour l'ordinateur

score_ordi = 0
score_joueur = 0

# La partie continue tant qu'aucun des deux n'a atteint 3 points
while score_joueur < 3 and score_ordi < 3:
    # Tirage du choix de l'ordinateur : 1=pierre, 2=feuille, 3=ciseaux
    tirage = random.randint(1, 3)
    if tirage == 1:
        ordi = "pierre"
    elif tirage == 2:
        ordi = "feuille"
    else:
        ordi = 'ciseaux'

    # .lower() et .strip() normalisent la saisie (majuscules / espaces)
    joueur = input("Pierre, Feuille ou ciseaux ? ").lower().strip()

    print(f"L'ordinateur à joué {ordi}")

    if joueur == ordi:
        print("égalité !")
    # Le \ permet de continuer la condition sur plusieurs lignes
    elif (joueur == "pierre" and ordi == "ciseaux") or \
        (joueur == "feuille" and ordi == 'pierre') or \
        (joueur == 'ciseaux' and ordi == 'feuille'):
        print("Vous avez gagné !")
        score_joueur += 1  # score_joueur = score_joueur + 1
    else:
        print("L'ordinateur a gagné la manche")
        score_ordi += 1

# Affichage du vainqueur de la partie
if score_joueur == 3:
    print("Vous avez gagné la partie")
else:
    print("L'ordinateur gagne la partie")
