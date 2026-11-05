# ============================================================
# Découverte de Python : affichage, opérateurs et variables
# ============================================================
# Objectifs :
# - utiliser print() pour afficher du texte et des calculs
# - découvrir les opérateurs arithmétiques
# - créer des variables et connaître leur type
# - concaténer / formater des chaînes (f-strings)
# - lire une saisie utilisateur avec input()
# ============================================================

# Afficher un message à l'écran
print("Bonjour !")
print("Je m'appelle Robin et j'apprend python")

# Opérateurs arithmétiques de base
print(6 * 7)      # multiplication
print(7 / 2)      # division (résultat flottant : 3.5)
print(5 + 5)      # addition
print(10 - 2)     # soustraction
print(7 % 2)      # modulo : reste de la division (1)
print(7 // 2)     # division entière (quotient sans décimales : 3)
print(2 ** 3)     # puissance : 2³ = 8

# Variables : on stocke une valeur dans un nom
prenom = "Robin"   # str  (chaîne de caractères)
age = 29           # int  (nombre entier)
taille = 1.93      # float (nombre décimal)

print(prenom)
print(age)
print(taille)

# type() indique le type d'une variable
print(type(prenom), type(age), type(taille))

# Trois façons d'afficher du texte avec des variables :
# 1) Concaténation avec + (seulement des str)
print("Bonjour, je m'appelle " + prenom)

# 2) f-string (recommandé) : on place les variables entre {}
print(f"Bonjour je m'appelle {prenom}, j'ai {age} ans, et je mesure {taille} m")

# 3) print avec plusieurs arguments séparés par des virgules
print("Bonjour je m'appelle", prenom, ", j'ai", age, "ans, et je mesure", taille, "m")

# On peut faire un calcul directement dans une f-string
print(f"Dans 10 ans, j'aurai {age + 10}ans")

# input() affiche une question et récupère la réponse (toujours en str)
ville = input("Dans quelle ville habites-tu ? ")

print(f"Bienvenue à {ville}")
