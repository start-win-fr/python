# ============================================================
# Exercice : majeur ou mineur ?
# ============================================================
# Objectifs :
# - convertir une saisie en entier avec int()
# - utiliser une condition if / else
# ============================================================

# input() renvoie une str → int() la convertit en nombre entier
age = int(input("Quel âge avez-vous ? "))

# Test conditionnel : si la condition est vraie → if, sinon → else
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
