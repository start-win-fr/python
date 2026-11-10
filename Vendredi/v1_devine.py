# ============================================================
# Exercice V1 : Le juste prix, côté ordinateur
# ============================================================
# Objectifs :
# - appliquer la recherche dichotomique
# - faire évoluer deux bornes (debut, fin)
# - détecter un tricheur quand l'intervalle devient vide
# ============================================================

print("Pensez à un nombre entre 1 et 100.")
debut, fin = 1, 100   # l'intervalle des nombres encore possibles
coups = 0
trouve = False

while debut <= fin and not trouve:
    milieu = (debut + fin) // 2   # on propose toujours le milieu
    coups += 1
    reponse = input(f"Je propose {milieu}. Plus (+), moins (-) ou trouvé (=) ? ")
    if reponse == "=":
        trouve = True
    elif reponse == "+":
        debut = milieu + 1    # le nombre est au-dessus : on garde la moitié haute
    elif reponse == "-":
        fin = milieu - 1      # le nombre est en dessous : on garde la moitié basse

if trouve:
    print(f"Trouvé en {coups} coups !")
else:
    # Si les réponses se contredisent, debut finit par dépasser fin :
    # plus aucun nombre ne correspond.
    print("Vous avez triché : aucun nombre ne correspond à vos réponses.")
