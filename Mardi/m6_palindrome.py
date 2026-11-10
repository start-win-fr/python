# ============================================================
# Exercice M6 : Le palindrome
# ============================================================
# Objectifs :
# - écrire des fonctions qui renvoient True ou False
# - inverser une chaîne avec [::-1]
# - comparer les caractères deux à deux avec une boucle
# ============================================================


def est_palindrome(mot):
    """Version courte : le mot est-il égal à son inverse ?"""
    return mot == mot[::-1]


def est_palindrome_boucle(mot):
    """Version avec une boucle : on compare le 1er et le dernier caractère,
    le 2e et l'avant-dernier, etc. Il suffit d'aller jusqu'à la moitié."""
    for i in range(len(mot) // 2):
        if mot[i] != mot[len(mot) - 1 - i]:
            return False   # une seule différence suffit : on s'arrête tout de suite
    # On n'arrive ici que si TOUTES les paires sont égales.
    # Piège classique : mettre ce return True dans un else à l'intérieur
    # de la boucle, ce qui ne vérifierait que la première paire.
    return True


def est_palindrome_phrase(phrase):
    """Niveau 3 : on ignore les majuscules et les espaces."""
    lettres = phrase.lower().replace(" ", "")
    return est_palindrome(lettres)


for mot in ["kayak", "radar", "python", "a", ""]:
    print(mot, est_palindrome(mot), est_palindrome_boucle(mot))

print(est_palindrome_phrase("Esope reste ici et se repose"))   # True
