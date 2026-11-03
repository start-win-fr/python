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

    