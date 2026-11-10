# ============================================================
# Exercice M3 : La somme de 1 à n
# ============================================================
# Objectifs :
# - utiliser un accumulateur dans une boucle
# - faire attention à la borne de fin de range()
# - vérifier un résultat avec une formule
# ============================================================

n = int(input("n = "))

somme = 0                     # l'accumulateur part de 0
for i in range(1, n + 1):     # n + 1, sinon on s'arrête à n - 1 !
    somme += i                # équivalent : somme = somme + i

# Formule de Gauss : 1 + 2 + ... + n = n x (n + 1) / 2
# On utilise // pour obtenir un entier (n x (n + 1) est toujours pair).
gauss = n * (n + 1) // 2

print(f"Boucle : {somme}, Gauss : {gauss}, égaux : {somme == gauss}")
# Avec 10 : 55. Avec 100 : 5050.
