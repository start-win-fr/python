nombre = int(input("Entrez un nombre : "))

if nombre == 0:
    print("C'est zéro.")
elif nombre > 0 and nombre % 2 == 0:
    print("Positif et pair.")
elif nombre > 0:
    print("Positif et impair")
else:
    print("Négatif.")