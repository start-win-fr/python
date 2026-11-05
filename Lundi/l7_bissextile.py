# ============================================================
# Exercice L7 : Année bissextile
# ============================================================
# Objectifs :
# - combiner des conditions avec and / or
# - appliquer une règle métier (calendrier grégorien)
# ============================================================
# Une année est bissextile si :
# - elle est divisible par 4 ET non divisible par 100
#   OU
# - elle est divisible par 400
# Exemples : 2024 oui, 1900 non, 2000 oui
# ============================================================

annee = int(input("Année à tester : "))

if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(f"{annee} est bissextile")
else:
    print(f"{annee} n'est pas bissextile")
