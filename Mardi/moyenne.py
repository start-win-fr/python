# ============================================================
# Exercice : Calcul de moyenne avec une boucle
# ============================================================
# Objectifs :
# - parcourir une liste avec for
# - accumuler une somme dans une variable
# - utiliser len() pour connaître la taille de la liste
# ============================================================

notes = [12, 8, 15, 10, 17]

somme = 0  # accumulateur : on part de 0

# À chaque tour, on ajoute la note courante à la somme
for note in notes:
    somme = somme + note  # équivalent : somme += note

print(f"Somme total : {somme}")

# Moyenne = somme des notes / nombre de notes
print(f"Moyenne : {somme / len(notes)}")
