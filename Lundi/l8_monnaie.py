montant  = int(input("Montant à payer : "))

if montant > 50:
    print("C'est pas assez")
elif montant == 50:
    print("Le compte est bon")
else:
    reste = 50 - montant

    print(f"Rendu  : {reste}")

    if reste // 20 > 0:
        print(f"{reste // 20} billets de 20 rendu")
        reste = reste % 20
    if reste // 10 > 0:
        print(f"{reste // 10} billets de 10 rendu")
        reste = reste % 10
    if reste // 5 > 0:
        print(f"{reste // 5} billets de 5 rendu")
        reste = reste % 5
    if reste // 2 > 0:
        print(f"{reste // 2} pièce(s) de 2 rendu")
        reste = reste % 2

    if reste > 0:
        print(f"{reste} pièce(e) de 1 rendu")


    