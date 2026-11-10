# ============================================================
# Exercice M10 : La saisie des notes
# ============================================================
# Objectifs :
# - lire des saisies jusqu'à une valeur « sentinelle » (fin)
# - remplir une liste au fur et à mesure
# - gérer le cas de la liste vide
# ============================================================


def moyenne(notes):
    """Renvoie la moyenne d'une liste de nombres (non vide)."""
    return sum(notes) / len(notes)


notes = []

# Le schéma classique : une saisie AVANT la boucle, une à la FIN de la boucle.
saisie = input("Note (ou fin) : ")
while saisie != "fin":
    notes.append(float(saisie))   # float : on accepte les notes à virgule
    saisie = input("Note (ou fin) : ")

# Si l'utilisateur tape « fin » tout de suite, la liste est vide :
# sans ce test, la moyenne ferait une division par zéro.
if len(notes) == 0:
    print("Aucune note")
else:
    print(f"{len(notes)} notes, moyenne {moyenne(notes):.2f}, de {min(notes)} à {max(notes)}")
