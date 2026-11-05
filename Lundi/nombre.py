# ============================================================
# Exercice : positif / négatif / pair / impair
# ============================================================
# Objectifs :
# - combiner plusieurs conditions avec and
# - utiliser le modulo (%) pour savoir si un nombre est pair
# - structurer des cas avec if / elif / else
# ============================================================

nombre = int(input("Entrez un nombre : "))

if nombre == 0:
    print("C'est zéro.")
elif nombre > 0 and nombre % 2 == 0:
    # Positif ET divisible par 2 (reste = 0) → pair
    print("Positif et pair.")
elif nombre > 0:
    # Positif mais pas pair → impair
    print("Positif et impair")
else:
    # nombre < 0
    print("Négatif.")
