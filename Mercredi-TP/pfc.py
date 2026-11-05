import random

score_ordi = 0
score_joueur = 0

while score_joueur < 3 and score_ordi < 3:
    tirage = random.randint(1, 3)
    if tirage == 1:
        ordi = "pierre"
    elif tirage == 2:
        ordi = "feuille"
    else:
        ordi = 'ciseaux'

    joueur = input("Pierre, Feuille ou ciseaux ? ").lower().strip()

    print(f"L'ordinateur à joué {ordi}")

    if joueur == ordi:
        print("égalité !")
    elif (joueur == "pierre" and ordi == "ciseaux") or \
        (joueur == "feuille" and ordi == 'pierre') or \
        (joueur == 'ciseaux' and ordi == 'feuille'):
        print("Vous avez gagné !")
        score_joueur += 1
    else:
        print("L'ordinateur a gagné la manche")
        score_ordi += 1

if score_joueur == 3:
    print("Vous avez gagné la partie")
else:
    print("L'ordinateur gagne la partie") 