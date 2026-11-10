# ============================================================
# Exercice V2 : Le tri à bulles
# ============================================================
# Objectifs :
# - échanger deux voisins mal rangés avec a, b = b, a
# - recommencer tant qu'il y a eu au moins un échange
# - compter le travail fait par l'algorithme
# ============================================================


def tri_bulles(liste):
    """Trie la liste sur place et renvoie le nombre d'échanges."""
    echanges = 0
    a_echange = True
    while a_echange:            # tant que le passage précédent a échangé quelque chose
        a_echange = False
        for i in range(len(liste) - 1):   # - 1 : on compare i et i + 1
            if liste[i] > liste[i + 1]:
                # Échange en une ligne, sans variable temporaire
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                echanges += 1
                a_echange = True
    return echanges


for essai in [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [12, 8, 15, 10, 17, 6]]:
    n = tri_bulles(essai)
    print(essai, n, "échange(s)")
# Liste à l'envers de 5 éléments : 10 échanges, le maximum (n x (n - 1) / 2).
# Liste déjà triée : aucun échange, un seul passage suffit pour le voir.
