# ============================================================
# Exercice M1 : La table de multiplication
# ============================================================
# Objectifs :
# - répéter une instruction avec for ... in range()
# - comprendre que la borne de fin de range() est exclue
# - imbriquer deux boucles (deuxième partie)
# ============================================================

# Partie 1 : la table d'un seul nombre
n = int(input("Table de : "))

# range(1, 11) donne 1, 2, ..., 10 (le 11 est exclu)
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print()

# Partie 2 : toutes les tables de 1 à 10, avec deux boucles imbriquées.
# La boucle extérieure choisit la table, la boucle intérieure la parcourt.
for table in range(1, 11):
    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")
    # Ce print() est dans la boucle extérieure, après la boucle intérieure :
    # il s'exécute une fois par table, pour sauter une ligne entre deux tables.
    print()
