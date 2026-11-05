import random

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
else:
    print("L'ordinateur a gagné la manche")