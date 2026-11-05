# ============================================================
# Exercice L2 : Opérations arithmétiques
# ============================================================
# Objectifs :
# - convertir deux saisies en entiers
# - utiliser les opérateurs +, -, *, /, // et %
# ============================================================

a = int(input("Premier nombre : "))
b = int(input("Deuxième nombre : "))

print(f"{a} + {b} = {a + b}")   # addition
print(f"{a} - {b} = {a - b}")   # soustraction
print(f"{a} * {b} = {a * b}")   # multiplication
print(f"{a} / {b} = {a / b}")   # division (résultat flottant)
print(f"{a} // {b} = {a // b}") # division entière (quotient)
print(f"{a} % {b} = {a % b}")   # modulo (reste de la division)
