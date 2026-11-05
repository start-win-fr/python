import random

a = random.randint(2, 10)
b = random.randint(2, 10)

reponse = int(input(f"Combien fait {a} * {b} ? "))

if reponse == a * b:
    print("Bravo")
else:
    print("Retourne en CE1")