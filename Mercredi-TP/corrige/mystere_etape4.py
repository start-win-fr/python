# ============================================================
# TP Jeu 1 : Le nombre mystère, étape 4 (un vrai nombre mystère)
# ============================================================
# Objectifs :
# - tirer un nombre au hasard avec le module random
# ============================================================

import random   # une seule fois, tout en haut du fichier

# randint(1, 100) : un entier au hasard entre 1 et 100, les deux inclus
secret = random.randint(1, 100)
# print(secret)   # pratique pour tester... à retirer avant de jouer !
proposition = 0
coups = 0

while proposition != secret:
    proposition = int(input("Votre proposition : "))
    coups = coups + 1
    if proposition < secret:
        print("C'est plus")
    elif proposition > secret:
        print("C'est moins")

print(f"Bravo, trouvé en {coups} coups !")
