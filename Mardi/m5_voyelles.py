# ============================================================
# Exercice M5 : Compter les voyelles
# ============================================================
# Objectifs :
# - écrire une fonction qui RENVOIE un résultat (return)
# - parcourir une chaîne caractère par caractère
# - tester l'appartenance avec in
# ============================================================


def compter_voyelles(texte):
    """Renvoie le nombre de voyelles du texte, majuscules comprises."""
    nb = 0
    # .lower() met tout en minuscules : "A" devient "a"
    for lettre in texte.lower():
        if lettre in "aeiouy":   # la lettre fait-elle partie de cette chaîne ?
            nb += 1
    return nb


def compter_voyelles_accents(texte):
    """Bonus : même chose, en comptant aussi les voyelles accentuées."""
    nb = 0
    for lettre in texte.lower():
        if lettre in "aeiouyàâäéèêëîïôöùûüÿ":
            nb += 1
    return nb


print(compter_voyelles("Anticonstitutionnellement"))   # 10
# Sans les accents, « Élève » ne compte qu'une voyelle : le dernier e.
print(compter_voyelles("Élève"), compter_voyelles_accents("Élève"))
