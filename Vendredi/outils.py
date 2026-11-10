# ============================================================
# Exercice V6 : Ma boîte à outils (le module)
# ============================================================
# Objectifs :
# - regrouper ses fonctions dans un module réutilisable
# - protéger les tests avec if __name__ == "__main__"
# ============================================================
# Lancé directement (python3 outils.py) : les tests s'exécutent.
# Importé par un autre fichier (import outils) : seulement les fonctions.


def est_pair(n):
    return n % 2 == 0


def est_premier(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def est_palindrome(mot):
    return mot == mot[::-1]


def moyenne(nombres):
    return sum(nombres) / len(nombres)


def demander_entier(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Il faut un nombre entier.")


if __name__ == "__main__":
    # Chaque ligne doit afficher True
    print(est_pair(4) and not est_pair(7))
    print(est_premier(97) and not est_premier(91))
    print(est_palindrome("kayak") and not est_palindrome("python"))
    print(moyenne([10, 12, 14]) == 12)
