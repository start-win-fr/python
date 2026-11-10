# ============================================================
# TP Jeu 2 : Le calcul mental, version complète avec les bonus
# ============================================================
# Objectifs :
# - tirer aussi l'opération au hasard (+, -, x)
# - adapter les seuils au nombre de questions choisi
# - mesurer le temps avec le module time
# ============================================================

import random
import time

nb_questions = int(input("Combien de questions ? "))
score = 0
debut = time.time()   # l'heure de départ, en secondes

for i in range(nb_questions):
    operation = random.randint(1, 3)   # 1 : +, 2 : -, 3 : x
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    if operation == 1:
        signe = "+"
        resultat = a + b
    elif operation == 2:
        signe = "-"
        resultat = a - b      # peut être négatif : ça corse le jeu
    else:
        signe = "x"
        resultat = a * b

    reponse = int(input(f"Question {i + 1} : {a} {signe} {b} = "))
    if reponse == resultat:
        print("Juste !")
        score = score + 1
    else:
        print(f"Faux, c'était {resultat}.")

duree = time.time() - debut   # temps écoulé depuis le départ
print(f"Score : {score}/{nb_questions}, en {round(duree)} secondes")

# Avec un nombre de questions variable, les seuils deviennent des proportions :
# 70 % et 50 % des questions au lieu de 7 et 5.
if score == nb_questions:
    print("Parfait, rien à redire.")
elif score >= nb_questions * 0.7:
    print("Très bien !")
elif score >= nb_questions * 0.5:
    print("Pas mal, encore un effort.")
else:
    print("Révisez et rejouez !")
