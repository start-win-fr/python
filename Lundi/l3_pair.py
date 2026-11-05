# ============================================================
# Exercice L3 : Pair ou impair
# ============================================================
# Objectifs :
# - utiliser le modulo (%) pour tester la parité
# - écrire une condition if / else
# ============================================================

n = int(input("Un nombre : "))

# Un nombre est pair si le reste de sa division par 2 vaut 0
if n % 2 == 0:
    print(f"{n} est pair")
else:
    print(f"{n} est impair")
