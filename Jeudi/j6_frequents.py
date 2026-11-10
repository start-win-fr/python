# ============================================================
# Exercice J6 : Les mots les plus fréquents
# ============================================================
# Objectifs :
# - lire tout un fichier d'un coup avec .read()
# - nettoyer un texte avec .replace()
# - trier les clés d'un dictionnaire selon leur valeur
# ============================================================
# Le fichier texte.txt doit être dans le même dossier.

with open("texte.txt", encoding="utf-8") as f:
    texte = f.read().lower()   # tout le fichier dans une seule chaîne

# On remplace chaque signe de ponctuation par un espace
for signe in ".,;:!?'":
    texte = texte.replace(signe, " ")

compte = {}
for mot in texte.split():
    compte[mot] = compte.get(mot, 0) + 1

# sorted(compte, ...) trie les CLÉS du dictionnaire.
# key=compte.get : on les compare selon leur valeur (le nombre d'apparitions).
# reverse=True : du plus grand au plus petit. [:5] : les cinq premiers.
for mot in sorted(compte, key=compte.get, reverse=True)[:5]:
    print(f"{mot} : {compte[mot]}")
