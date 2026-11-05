import random

score = 0
for i in range(1, 11):
    a = random.randint(2, 10)
    b = random.randint(2, 10)

    reponse = int(input(f"Question {i}: {a} * {b} = "))

    if reponse == a * b:
        print("Bravo")
        score += 1
    else:
        print(f"Retourne en CE1, la bonne réponse était {a * b}")

print(f"Score : {score}/10")

if score == 10:
    print("Parfait")
elif score >= 7:
    print("Très bien !")
elif score >= 5:
    print("Pas mal, fait un effort quand même")
else:
    print("C'était y'a longtemps la primaire non ?")