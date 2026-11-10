# ============================================================
# TP Jeu 2 : Le calcul mental, étape 4 (le commentaire final)
# ============================================================
# Objectifs :
# - choisir un message selon le score avec if / elif / else
# - ordonner les conditions de la plus exigeante à la moins exigeante
# ============================================================

import random

score = 0
for i in range(10):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    reponse = int(input(f"Question {i + 1} : {a} x {b} = "))
    if reponse == a * b:
        print("Juste !")
        score = score + 1
    else:
        print(f"Faux, c'était {a * b}.")

print(f"Score : {score}/10")
# Python s'arrête à la PREMIÈRE condition vraie. Si on testait
# score >= 5 avant score >= 7, un 9/10 recevrait « Pas mal ».
if score == 10:
    print("Parfait, rien à redire.")
elif score >= 7:
    print("Très bien !")
elif score >= 5:
    print("Pas mal, encore un effort.")
else:
    print("Révisez vos tables et rejouez !")
