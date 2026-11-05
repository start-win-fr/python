# ============================================================
# Exercice : mention selon la note
# ============================================================
# Objectifs :
# - convertir une saisie en float (nombre décimal)
# - enchaîner plusieurs conditions avec if / elif / else
# - comprendre l'ordre des tests (du plus strict au moins strict)
# ============================================================

note = float(input("Votre note sur 20 : "))

# On teste d'abord les notes les plus hautes.
# Dès qu'une condition est vraie, on entre dans ce bloc et on ignore la suite.
if note >= 16:
    print("Mention très bien")
elif note >= 14:
    print("Mention bien")
elif note >= 12:
    print("Mention assez bien")
elif note >= 10:
    print("Admis")
else:
    # Toutes les conditions précédentes sont fausses → note < 10
    print("Recalé")
