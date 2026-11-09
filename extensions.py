# ============================================================
# Exercice : Filtrer et compter les extensions
# ============================================================
# Objectifs :
# - filtrer des fichiers avec endswith()
# - extraire une extension avec os.path.splitext()
# - compter avec un dictionnaire (.get)
# ============================================================

import os

dossier = 'bac-a-sable'

# --- Partie 1 : afficher uniquement les fichiers .txt ---
print("Les fichiers texte : ")
for nom in sorted(os.listdir(dossier)):
    if nom.endswith('.txt'):
        print(" ", nom)


# --- Partie 2 : compter combien de fichiers par extension ---
# Exemple de résultat attendu :
# {
#     ".zip": 1,
#     '.csv': 1,
#     ".txt": 2,
#     ...
# }

compte = {}  # dictionnaire : clé = extension, valeur = nombre de fichiers

for nom in sorted(os.listdir(dossier)):
    chemin = os.path.join(dossier, nom)
    if os.path.isfile(chemin):
        # splitext("vide.txt") → ("vide", ".txt") → on prend l'index [1]
        extension = os.path.splitext(nom)[1]

        # .get(extension, 0) : si la clé n'existe pas encore, on part de 0
        # puis on ajoute 1
        compte[extension] = compte.get(extension, 0) + 1

print(compte)
