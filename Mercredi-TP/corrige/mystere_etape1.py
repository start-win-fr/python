# ============================================================
# TP Jeu 1 : Le nombre mystère, étape 1 (une seule proposition)
# ============================================================
# Objectifs :
# - lire un nombre avec int(input())
# - comparer avec if / elif / else
# ============================================================

secret = 42   # pour l'instant, le nombre est écrit en dur

proposition = int(input("Votre proposition : "))
if proposition < secret:
    print("C'est plus")
elif proposition > secret:
    print("C'est moins")
else:
    # ni plus petit, ni plus grand : c'est forcément égal
    print("Bravo, c'est gagné !")
