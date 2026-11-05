# ============================================================
# Exercice L4 : Conversion Celsius → Fahrenheit
# ============================================================
# Objectifs :
# - convertir une saisie en float
# - appliquer une formule mathématique
# - afficher le résultat formaté
# ============================================================

# Attention : orthographe correcte = "celsius" (ici on garde le nom du code)
celcius = float(input("Température en celcius : "))

# Formule : F = C × 9/5 + 32
fahrenheit = celcius * 9 / 5 + 32

print(f"{celcius} degrés celcius vaut {fahrenheit} degrés Fahrenheit")
