# ============================================================
# Exercice M8 : La recherche
# ============================================================
# Objectifs :
# - parcourir une liste par ses indices avec range(len(...))
# - sortir d'une fonction dès qu'on a trouvé (return)
# - renvoyer une valeur spéciale (-1) quand on ne trouve pas
# ============================================================


def indice(liste, valeur):
    """Renvoie la position de la première occurrence de valeur, ou -1."""
    for i in range(len(liste)):
        if liste[i] == valeur:
            return i   # trouvé : on renvoie la position et la fonction s'arrête
    # Le return -1 est APRÈS la boucle : on n'y arrive que si on a tout
    # parcouru sans trouver. Dans un else à l'intérieur de la boucle,
    # il ne regarderait que le premier élément.
    return -1


print(indice([4, 8, 15, 16, 23, 42], 16))   # 3
print(indice([4, 8, 15], 7))                # -1
print(indice([], 7))                        # -1 : la liste vide marche aussi
