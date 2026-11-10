# ============================================================
# Exercice M4 : Les statistiques d'une classe
# ============================================================
# Objectifs :
# - parcourir une liste avec for
# - gérer plusieurs accumulateurs dans la même boucle
# - retrouver soi-même ce que font sum(), min() et max()
# ============================================================

notes = [12, 8, 15, 10, 17, 6, 13, 9]

somme = 0
plus_basse = notes[0]   # on suppose que la première note est la plus basse...
plus_haute = notes[0]   # ... et la plus haute, puis on corrige si besoin

for note in notes:
    somme += note
    if note < plus_basse:
        plus_basse = note
    if note > plus_haute:
        plus_haute = note

moyenne = somme / len(notes)   # len() : nombre d'éléments de la liste

# Il faut une DEUXIÈME boucle : on ne peut compter les notes au-dessus
# de la moyenne qu'une fois la moyenne connue.
au_dessus = 0
for note in notes:
    if note > moyenne:
        au_dessus += 1

print(f"Moyenne : {moyenne:.2f}")   # :.2f = deux chiffres après la virgule
print(f"De {plus_basse} à {plus_haute}")
print(f"{au_dessus} note(s) au-dessus de la moyenne")

# Vérification avec les fonctions toutes faites de Python
print("Vérification :", sum(notes) / len(notes), min(notes), max(notes))
