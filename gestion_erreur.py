# ============================================================
# Démo : gestion des erreurs avec try / except
# ============================================================
# Objectifs :
# - comprendre pourquoi int(input(...)) peut planter
# - attraper l'erreur pour afficher un message clair
# ============================================================
# Sans try/except, taper "dix" au lieu de 10 provoque ValueError
# et arrête le programme. Avec try/except, on contrôle le message.
# ============================================================

try:
    age = int(input('Votre age : '))
    print(f"Vous avez : {age} ans")
except:
    # Exécuté si int() échoue (saisie non numérique)
    print("Merci d'entrer un age correct (un nombre entier)")
