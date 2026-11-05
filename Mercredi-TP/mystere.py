import random

secret = random.randint(1, 100)
proposition = 0
coups = 0

while proposition != secret and coups < 7:
    try:
        proposition = int(input("Votre proposition : "))
        coups += 1

        if proposition < secret:
            print("C'est +")
        elif proposition > secret:
            print("C'est -")
    except:
        print("Merci d'entrer un nombre entier valide.")

if proposition == secret:
    print(f"Bravo, trouvé en {coups} coup(s) !")
else:
    print(f"Bouuuuuh, la bonne réponse était {secret}")