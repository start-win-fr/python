annee = int(input("Année à tester : "))

if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(f"{annee} est bissextile")
else:
    print(f"{annee} n'est pas bissextile")
