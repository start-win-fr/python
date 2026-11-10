# ============================================================
# Exercice J4 : Le juste prix
# ============================================================
# Objectifs :
# - tirer un nombre au hasard avec random.randint()
# - rattraper une saisie invalide avec try / except ValueError
# - ranger la saisie robuste dans une fonction réutilisable
# ============================================================

import random


def demander_entier(question):
    """Redemande jusqu'à obtenir un nombre entier, et le renvoie."""
    while True:
        try:
            # Si int() échoue, Python saute directement au except
            return int(input(question))
        except ValueError:
            print("Il faut un nombre entier.")


secret = random.randint(1, 100)
coups = 0
proposition = 0
while proposition != secret:
    proposition = demander_entier("Votre proposition : ")
    coups += 1   # une saisie invalide n'arrive jamais ici : elle ne compte pas
    if proposition < secret:
        print("C'est plus")
    elif proposition > secret:
        print("C'est moins")
print(f"Trouvé en {coups} coups !")

# La stratégie gagnante : toujours proposer le milieu de ce qui reste possible.
# Chaque réponse divise l'intervalle par deux, et 2 puissance 7 = 128 > 100 :
# on trouve en 7 coups au maximum. C'est la recherche dichotomique.
