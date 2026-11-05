# ============================================================
# Exercice L5 : Trouver le plus grand de 3 nombres
# ============================================================
# Objectifs :
# - lire plusieurs valeurs
# - comparer des nombres avec des if successifs
# - mettre à jour une variable "champion" (plus_grand)
# ============================================================

a = int(input("Premier : "))
b = int(input("Deuxieme : "))
c = int(input("Troiseme : "))

# On part du principe que a est le plus grand, puis on compare
plus_grand = a

if b > plus_grand:
    plus_grand = b  # b devient le nouveau maximum
if c > plus_grand:
    plus_grand = c  # c devient le nouveau maximum

print(f"Le plus grand nombre est {plus_grand}")
