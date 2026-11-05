# ============================================================
# Cours / démo : boucles for et listes
# ============================================================
# Objectifs :
# - parcourir une séquence avec for ... in range()
# - créer une liste et accéder à ses éléments par index
# - comprendre les index négatifs (depuis la fin)
# ============================================================

# range(1, 11) génère les entiers de 1 inclus à 11 exclu → 1..10
for i in range(1, 11):
    print(f"{i}")

# Une liste stocke plusieurs valeurs dans l'ordre
liste = [20, 50, 190, 2]

# Index positifs : 0 = premier élément
print(f"{liste[0]}")   # Vaut 20
print(f"{liste[1]}")   # Vaut 50
print(f"{liste[2]}")   # Vaut 190
print(f"{liste[3]}")   # Vaut 2

# Index négatifs : -1 = dernier élément, -2 = avant-dernier, etc.
print(f"{liste[-1]}")  # Vaut 2
print(f"{liste[-2]}")  # Vaut 190
