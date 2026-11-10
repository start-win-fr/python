# ============================================================
# Exercice J5 : Le carnet de notes
# ============================================================
# Objectifs :
# - lire un fichier ligne par ligne avec with open(...)
# - découper une ligne avec .split(";")
# - convertir du texte en nombres
# ============================================================
# Le fichier eleves.txt doit être dans le même dossier.

meilleur_nom = ""
meilleure_moyenne = -1   # n'importe quelle vraie moyenne sera plus grande

with open("eleves.txt", encoding="utf-8") as fichier:
    for ligne in fichier:
        # .strip() retire le retour à la ligne, .split(";") découpe les champs
        champs = ligne.strip().split(";")
        prenom = champs[0]          # la première case : le prénom
        notes = []
        for n in champs[1:]:        # [1:] : toutes les cases sauf la première
            notes.append(int(n))    # tout ce qu'on lit est du TEXTE : int() !
        moyenne = sum(notes) / len(notes)
        print(f"{prenom} : {moyenne:.1f}")
        if moyenne > meilleure_moyenne:
            meilleure_moyenne = moyenne
            meilleur_nom = prenom

print(f"Meilleure moyenne : {meilleur_nom} ({meilleure_moyenne:.1f})")
# Une ligne vide en fin de fichier ferait planter (aucune note, division
# par zéro). Pour la sauter : if not ligne.strip(): continue
