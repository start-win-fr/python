# ============================================================
# Exercice V9 : La fusion de deux listes triées
# ============================================================
# Objectifs :
# - avancer dans deux listes en même temps avec deux indices
# - ne pas oublier la fin de la liste qui n'est pas épuisée
# ============================================================


def fusion(a, b):
    resultat = []
    i, j = 0, 0   # i avance dans a, j avance dans b
    while i < len(a) and j < len(b):
        # On prend le plus petit des deux éléments en tête
        if a[i] <= b[j]:
            resultat.append(a[i])
            i += 1
        else:
            resultat.append(b[j])
            j += 1
    # L'une des deux listes est épuisée : on ajoute toute la fin de l'autre.
    # Sans ces deux lignes, les derniers éléments disparaissent.
    resultat.extend(a[i:])
    resultat.extend(b[j:])
    return resultat


print(fusion([1, 4, 9], [2, 3, 10, 12]))   # [1, 2, 3, 4, 9, 10, 12]
print(fusion([], [5, 6]))
print(fusion([1, 1, 2], [1, 3]))
# C'est le cœur du tri fusion : couper la liste en deux, trier chaque
# moitié (récursivement), puis fusionner les deux moitiés.
