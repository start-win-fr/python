# ============================================================
# Exercice L1 : Bonjour personnalisé
# ============================================================
# Objectifs :
# - lire deux saisies utilisateur avec input()
# - afficher un message formaté avec une f-string
# ============================================================

prenom = input("Votre prénom : ")
ville = input("Votre ville : ")

# Les variables sont injectées dans le texte grâce aux {}
print(f"Bonjour {prenom}, il fait beau à {ville} aujourd'hui")
