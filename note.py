note = float(input("Votre note sur 20 : "))

if note >= 16:
    print("Mention très bien")
elif note >= 14:
    print("Mention bien")
elif note >= 12:
    print("Mention assez bien")
elif note >= 10:
    print("Admis")
else:
    print("Recalé")