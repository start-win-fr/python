# ============================================================
# Exercice J3 : Le petit traducteur
# ============================================================
# Objectifs :
# - chercher des mots dans un dictionnaire
# - découper une phrase avec .split() et la recoller avec .join()
# ============================================================

dico = {"le": "the", "chat": "cat", "chien": "dog", "mange": "eats",
        "la": "the", "souris": "mouse", "petit": "small"}

phrase = input("Phrase : ")
traduction = []
for mot in phrase.lower().split():   # split() découpe aux espaces
    if mot in dico:                  # in teste les CLÉS du dictionnaire
        traduction.append(dico[mot])
    else:
        traduction.append(f"[{mot}]")   # mot inconnu : entre crochets
    # Version plus courte de ce if / else :
    # traduction.append(dico.get(mot, f"[{mot}]"))

print(" ".join(traduction))   # recolle les mots avec un espace entre eux
# « le petit chat » donne « the small cat » : en anglais l'adjectif est
# avant le nom, ici ça tombe juste. Ce n'est pas toujours le cas !
