# ============================================================
# TP Jeu 2 : Le calcul mental, étape 3 (le score)
# ============================================================
# Objectifs :
# - compter les bonnes réponses avec un compteur
# ============================================================

import random

score = 0   # avant la boucle !
for i in range(10):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    reponse = int(input(f"Question {i + 1} : {a} x {b} = "))
    if reponse == a * b:
        print("Juste !")
        score = score + 1   # seulement pour une bonne réponse
    else:
        print(f"Faux, c'était {a * b}.")

print(f"Score : {score}/10")
