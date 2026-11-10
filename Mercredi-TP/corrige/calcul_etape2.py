# ============================================================
# TP Jeu 2 : Le calcul mental, étape 2 (dix questions)
# ============================================================
# Objectifs :
# - répéter avec for ... in range(10)
# - placer le tirage au hasard DANS la boucle
# ============================================================

import random

for i in range(10):            # i va de 0 à 9
    # Le tirage est dans la boucle : une nouvelle multiplication à chaque tour.
    # Placé avant la boucle, il poserait dix fois la même question.
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    reponse = int(input(f"Question {i + 1} : {a} x {b} = "))   # i + 1 : de 1 à 10
    if reponse == a * b:
        print("Juste !")
    else:
        print(f"Faux, c'était {a * b}.")
