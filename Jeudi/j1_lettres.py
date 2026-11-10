# ============================================================
# Exercice J1 : Compter les lettres
# ============================================================
# Objectifs :
# - créer et remplir un dictionnaire
# - utiliser le patron du compteur avec .get()
# - parcourir un dictionnaire avec .items()
# ============================================================

mot = input("Un mot : ")

compte = {}   # dictionnaire vide : lettre -> nombre d'apparitions
for lettre in mot:
    # .get(lettre, 0) lit le compte actuel, ou 0 si la lettre n'a jamais été vue.
    # On ajoute 1 et on range le résultat sous la même clé.
    compte[lettre] = compte.get(lettre, 0) + 1

# .items() donne la clé ET la valeur à chaque tour
for lettre, nb in compte.items():
    print(f"{lettre} : {nb} fois")
# Les lettres sortent dans l'ordre de leur première apparition :
# un dictionnaire garde l'ordre dans lequel on a ajouté les clés.
