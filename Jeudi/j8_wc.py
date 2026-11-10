# ============================================================
# Exercice J8 : wc en Python
# ============================================================
# Objectifs :
# - lire les arguments du programme avec sys.argv
# - rattraper un fichier introuvable avec FileNotFoundError
# - quitter avec un code d'erreur grâce à sys.exit(1)
# ============================================================
# Usage : python3 j8_wc.py texte.txt

import sys

# sys.argv[0] est le nom du programme, sys.argv[1] le premier argument
if len(sys.argv) != 2:
    print("Usage : python3 j8_wc.py fichier")
    sys.exit(1)

nom = sys.argv[1]
try:
    with open(nom, encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print(f"Fichier introuvable : {nom}")
    sys.exit(1)

lignes = contenu.count("\n")     # une ligne = un retour à la ligne
mots = len(contenu.split())      # split() découpe aux espaces et retours à la ligne
caracteres = len(contenu)
print(f"{lignes} {mots} {caracteres} {nom}")

# Comparez avec : wc texte.txt
# Lignes et mots identiques. Pour la 3e colonne, wc compte des OCTETS :
# un caractère accentué comme « é » en prend deux. wc -m compte les
# caractères, comme Python.
