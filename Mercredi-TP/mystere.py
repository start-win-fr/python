# ============================================================
# TP : Jeu du nombre mystère
# ============================================================
# Objectifs :
# - boucle while avec double condition (trouvé OU plus de coups)
# - gérer les erreurs de saisie avec try / except
# - donner des indices (+ / -) à chaque proposition
# ============================================================

import random

secret = random.randint(1, 100)  # nombre à trouver entre 1 et 100
proposition = 0
coups = 0

# On continue tant que ce n'est pas trouvé ET qu'il reste des essais
while proposition != secret and coups < 7:
    try:
        # Si la conversion échoue (ex: "abc"), on va dans except
        proposition = int(input("Votre proposition : "))
        coups += 1

        if proposition < secret:
            print("C'est +")
        elif proposition > secret:
            print("C'est -")
        # Si égalité, la boucle s'arrêtera au prochain test while
    except:
        # Saisie invalide : on n'incrémente pas les coups
        print("Merci d'entrer un nombre entier valide.")

if proposition == secret:
    print(f"Bravo, trouvé en {coups} coup(s) !")
else:
    print(f"Bouuuuuh, la bonne réponse était {secret}")
