# ============================================================
# TP Jeu 2 : Le calcul mental, étape 1 (une seule question)
# ============================================================
# Objectifs :
# - tirer deux nombres au hasard
# - poser la question directement dans input() avec une f-string
# ============================================================

import random

a = random.randint(2, 10)
b = random.randint(2, 10)

# input() affiche son texte avant d'attendre la réponse :
# on y met directement la question.
reponse = int(input(f"{a} x {b} = "))
if reponse == a * b:
    print("Juste !")
else:
    print(f"Faux, c'était {a * b}.")
