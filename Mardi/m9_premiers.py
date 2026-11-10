# ============================================================
# Exercice M9 : Les nombres premiers
# ============================================================
# Objectifs :
# - écrire une fonction de test avec while
# - construire une liste avec append()
# - optimiser une recherche de diviseurs
# ============================================================


def est_premier(n):
    """Renvoie True si n est premier (divisible seulement par 1 et lui-même)."""
    if n < 2:
        return False   # 0 et 1 ne sont pas premiers
    d = 2
    # Inutile de chercher des diviseurs au-delà de la racine carrée de n :
    # si n = a x b avec a <= b, alors a x a <= n. Un diviseur, s'il existe,
    # est donc trouvé avant. « d * d <= n » évite de calculer la racine.
    while d * d <= n:
        if n % d == 0:
            return False   # d divise n : n n'est pas premier
        d += 1
    return True


premiers = []              # on part d'une liste vide...
for n in range(100):
    if est_premier(n):
        premiers.append(n)  # ... et on ajoute chaque nombre premier trouvé

print(premiers)
print(len(premiers), "nombres premiers")   # 25
