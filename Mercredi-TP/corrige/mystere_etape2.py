# ============================================================
# TP Jeu 1 : Le nombre mystère, étape 2 (jusqu'à trouver)
# ============================================================
# Objectifs :
# - répéter avec while tant qu'une condition est vraie
# - initialiser une variable AVANT la boucle
# ============================================================

secret = 42
# Python vérifie la condition du while AVANT le premier tour :
# la variable doit déjà exister. 0 n'est jamais le secret,
# donc on entre forcément dans la boucle.
proposition = 0

while proposition != secret:
    proposition = int(input("Votre proposition : "))
    if proposition < secret:
        print("C'est plus")
    elif proposition > secret:
        print("C'est moins")

# On sort de la boucle uniquement quand proposition == secret
print("Bravo, c'est gagné !")
