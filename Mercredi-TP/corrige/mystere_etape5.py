# ============================================================
# TP Jeu 1 : Le nombre mystère, étape 5 (sept coups maximum)
# ============================================================
# Objectifs :
# - combiner deux conditions dans un while avec and
# - savoir APRÈS la boucle pourquoi elle s'est arrêtée
# ============================================================

import random

secret = random.randint(1, 100)
proposition = 0
coups = 0

# La boucle continue tant que ce n'est pas trouvé ET qu'il reste des coups.
# Elle s'arrête dès qu'une des deux conditions devient fausse.
while proposition != secret and coups < 7:
    print(f"Coup n°{coups + 1} sur 7")
    proposition = int(input("Votre proposition : "))
    coups = coups + 1
    if proposition < secret:
        print("C'est plus")
    elif proposition > secret:
        print("C'est moins")

# Laquelle des deux conditions a arrêté la boucle ?
if proposition == secret:
    print(f"Bravo, trouvé en {coups} coups !")
else:
    print(f"Perdu ! Le nombre était {secret}.")

# 7 coups suffisent toujours si on propose le milieu de ce qui reste
# possible (50, puis 25 ou 75...) : 2 puissance 7 = 128, plus que 100.
