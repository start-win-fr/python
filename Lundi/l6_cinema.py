# ============================================================
# Exercice L6 : Tarif cinéma
# ============================================================
# Objectifs :
# - imbriquer des conditions (if dans un elif)
# - utiliser .lower() pour ignorer la casse d'une réponse
# - attribuer un prix selon l'âge / le statut
# ============================================================
# Grille tarifaire :
# - moins de 14 ans          → 6 €
# - 65 ans et plus           → 8 €
# - moins de 26 ans étudiant → 8 €
# - sinon                    → 11 €
# ============================================================

age = int(input("Votre âge : "))

if age < 14:
    prix = 6
elif age >= 65:
    prix = 8
elif age < 26:
    # On demande si la personne est étudiante
    reponse = input("Etes vous étudiant (o/n) ? ")
    # .lower() transforme "O" ou "O" en "o" pour simplifier le test
    if reponse.lower() == 'o':
        prix = 8
    else:
        prix = 11
else:
    # 26 ≤ âge < 65 et non étudiant (cas adulte standard)
    prix = 11

print(f"Votre place coute {prix} €")
