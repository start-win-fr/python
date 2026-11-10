# ============================================================
# Exercice M7 : FizzBuzz
# ============================================================
# Objectifs :
# - combiner une boucle et des conditions if / elif / else
# - comprendre que l'ordre des conditions compte
# ============================================================

for i in range(1, 31):
    # Le cas « multiple de 3 ET de 5 » (donc de 15) doit être testé EN PREMIER.
    # Sinon 15 serait attrapé par le test du 3 et afficherait seulement « Fizz ».
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()   # retour à la ligne final
