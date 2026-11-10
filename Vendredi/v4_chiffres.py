# ============================================================
# Exercice V4 : La somme des chiffres
# ============================================================
# Objectifs :
# - découper un nombre avec % 10 et // 10
# - récursivité : un problème plus petit à chaque appel
# ============================================================


def somme_chiffres(n):
    """somme_chiffres(1234) vaut 1 + 2 + 3 + 4 = 10."""
    if n < 10:
        return n   # cas de base : un seul chiffre
    # n % 10 : le dernier chiffre (4), n // 10 : le reste du nombre (123)
    return n % 10 + somme_chiffres(n // 10)


print(somme_chiffres(1234))    # 10
print(somme_chiffres(7))       # 7
print(somme_chiffres(99999))   # 45
