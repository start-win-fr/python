# ============================================================
# Exercice V5 : Le palindrome récursif
# ============================================================
# Objectifs :
# - écrire un test récursif sur une chaîne
# - couvrir les deux cas de base (longueur 0 et 1)
# ============================================================


def est_palindrome(mot):
    # Cas de base : un mot vide (longueur paire, comme « abba » à la fin)
    # ou d'une seule lettre (longueur impaire, comme « kayak ») est un palindrome.
    if len(mot) <= 1:
        return True
    if mot[0] != mot[-1]:      # la première et la dernière lettre diffèrent
        return False
    # Sinon, il reste à vérifier ce qu'il y a ENTRE les deux :
    # mot[1:-1] est le mot sans sa première ni sa dernière lettre.
    return est_palindrome(mot[1:-1])


for mot in ["kayak", "radar", "python", "abba", "a", ""]:
    print(mot, est_palindrome(mot))
