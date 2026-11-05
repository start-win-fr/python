secret = 42
proposition = -1

while proposition != secret:
    try:
        proposition = int(input("Votre proposition : "))

        if proposition < secret:
            print("C'est +")
        elif proposition > secret:
            print("C'est -")
        else:
            print("C'est gagné")
    except:
        print("Merci d'entrer un nombre entier valide.")