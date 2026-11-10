# ============================================================
# Exercice V7 : La chasse au bug (version corrigée)
# ============================================================
# Objectifs :
# - trouver un bug avec le débogueur (point d'arrêt, F10)
# - comprendre l'effet d'un return mal placé
# ============================================================
# Le bug : il y avait un « return meilleur » DANS le if, sous
# « meilleur = mot ». La fonction s'arrêtait donc au premier mot plus
# long que le précédent (« chat », plus long que « le »), sans regarder
# la suite de la phrase. Il suffit de supprimer ce return :
# celui qui est après la boucle fait le travail.


def plus_long_mot(phrase):
    mots = phrase.split()
    meilleur = mots[0]
    for mot in mots:
        if len(mot) > len(meilleur):
            meilleur = mot
    return meilleur   # après la boucle : tous les mots ont été vus


print(plus_long_mot("le chat regarde attentivement la souris"))   # attentivement
