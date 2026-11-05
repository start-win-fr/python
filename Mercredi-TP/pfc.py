import random

tirage = random.randint(1, 3)
if tirage == 1:
    ordi = "pierre"
elif tirage == 2:
    ordi = "feuille"
else:
    ordi = 'ciseaux'

joueur = input("Pierre, Feuille ou ciseaux ? ")
print(f"L'ordinateur à joué {ordi}")