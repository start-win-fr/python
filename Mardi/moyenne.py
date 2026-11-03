notes = [12, 8, 15, 10, 17]

somme = 0

for note in notes:
    somme = somme + note

print(f"Somme total : {somme}")
print(f"Moyenne : {somme / len(notes)}")