age = int(input("Votre âge : "))

if age < 14:
    prix = 6
elif age >= 65:
    prix = 8
elif age < 26:
    reponse = input("Etes vous étudiant (o/n) ? ")
    if reponse.lower() == 'o':
        prix = 8
    else:
        prix = 11
else:
    prix = 11

print(f"Votre place coute {prix} €")