# ============================================================
# TP Jeu 1 : Le nombre mystère, étape 3 (compter les coups)
# ============================================================
# Objectifs :
# - utiliser un compteur : 0 avant la boucle, +1 à chaque tour
# ============================================================

secret = 42
proposition = 0
coups = 0   # le compteur

while proposition != secret:
    proposition = int(input("Votre proposition : "))
    coups = coups + 1   # une proposition de plus
    if proposition < secret:
        print("C'est plus")
    elif proposition > secret:
        print("C'est moins")

print(f"Bravo, trouvé en {coups} coups !")
