a = int(input("Premier : "))
b = int(input("Deuxieme : "))
c = int(input("Troiseme : "))

plus_grand = a

if b > plus_grand:
    plus_grand = b
if c > plus_grand:
    plus_grand = c

print(f"Le plus grand nombre est {plus_grand}")