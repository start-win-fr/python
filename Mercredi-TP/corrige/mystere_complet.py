# ============================================================
# TP Jeu 1 : Le nombre mystère, version complète avec les bonus
# ============================================================
# Objectifs :
# - remplacer les nombres écrits en dur par des variables (niveau)
# - ignorer une saisie hors limites sans compter le coup
# - envelopper toute la partie dans une boucle pour rejouer
# ============================================================

import random

encore = "o"
while encore == "o":          # la grande boucle : une partie par tour
    niveau = int(input("Niveau (1, 2 ou 3) : "))
    if niveau == 1:
        maximum = 50
        coups_max = 10
    elif niveau == 2:
        maximum = 100
        coups_max = 7
    else:
        maximum = 1000
        coups_max = 10

    secret = random.randint(1, maximum)
    print(f"Un nombre entre 1 et {maximum}, en {coups_max} coups.")
    proposition = 0
    coups = 0

    while proposition != secret and coups < coups_max:
        proposition = int(input(f"Coup {coups + 1}/{coups_max} : "))
        if proposition < 1 or proposition > maximum:
            # Hors limites : on prévient, et le else ci-dessous n'est pas
            # exécuté, donc le coup n'est pas compté.
            print(f"Entre 1 et {maximum}, s'il vous plaît. Ce coup ne compte pas.")
        else:
            coups = coups + 1
            if proposition < secret:
                print("C'est plus")
            elif proposition > secret:
                print("C'est moins")

    if proposition == secret:
        print(f"Bravo, trouvé en {coups} coups !")
    else:
        print(f"Perdu ! Le nombre était {secret}.")
    encore = input("Rejouer (o/n) ? ")
