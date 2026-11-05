# ============================================================
# Exercice L8 : Rendu de monnaie
# ============================================================
# Objectifs :
# - utiliser // (division entière) et % (modulo)
# - décomposer un montant en billets / pièces
# - mettre à jour une variable "reste" à chaque étape
# ============================================================
# Principe : on paie avec 50 € max, et on rend la monnaie
# en priorisant les plus gros billets/pièces (20, 10, 5, 2, 1).
# ============================================================

montant = int(input("Montant à payer : "))

if montant > 50:
    # On ne peut pas rendre de la monnaie si le montant dépasse 50
    print("C'est pas assez")
elif montant == 50:
    print("Le compte est bon")
else:
    # Combien reste-t-il à rendre ?
    reste = 50 - montant

    print(f"Rendu  : {reste}")

    # Billets de 20
    if reste // 20 > 0:
        print(f"{reste // 20} billets de 20 rendu")
        reste = reste % 20  # on garde ce qui reste après les billets de 20

    # Billets de 10
    if reste // 10 > 0:
        print(f"{reste // 10} billets de 10 rendu")
        reste = reste % 10

    # Billets de 5
    if reste // 5 > 0:
        print(f"{reste // 5} billets de 5 rendu")
        reste = reste % 5

    # Pièces de 2
    if reste // 2 > 0:
        print(f"{reste // 2} pièce(s) de 2 rendu")
        reste = reste % 2

    # Pièces de 1 (ce qu'il reste éventuellement)
    if reste > 0:
        print(f"{reste} pièce(e) de 1 rendu")
