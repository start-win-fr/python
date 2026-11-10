# ============================================================
# Exercice V3 : La puissance
# ============================================================
# Objectifs :
# - écrire une fonction récursive (qui s'appelle elle-même)
# - identifier le cas de base
# ============================================================


def puissance(x, n):
    """Renvoie x à la puissance n (n entier positif), sans **."""
    if n == 0:
        return 1                       # cas de base : x puissance 0 = 1
    return x * puissance(x, n - 1)     # x puissance n = x * x puissance (n - 1)


print(puissance(2, 10), 2 ** 10)   # 1024 1024
print(puissance(3, 0))             # 1
print(puissance(5, 3))             # 125
