# ============================================================
# Exercice J2 : Le répertoire
# ============================================================
# Objectifs :
# - un menu qui tourne en boucle jusqu'à « Quitter »
# - ajouter, lire et parcourir un dictionnaire
# - lire une clé absente sans planter avec .get()
# ============================================================

repertoire = {}   # nom -> téléphone

choix = ""
while choix != "4":
    print("1. Ajouter  2. Chercher  3. Lister  4. Quitter")
    # Le choix reste un texte : pas de int(), donc pas de plantage
    # si l'utilisateur tape une lettre.
    choix = input("Choix : ")
    if choix == "1":
        nom = input("Nom : ")
        repertoire[nom] = input("Téléphone : ")   # ajoute (ou remplace) la paire
    elif choix == "2":
        nom = input("Nom : ")
        # repertoire[nom] planterait (KeyError) si le nom est absent.
        # .get() renvoie la valeur par défaut à la place.
        print(repertoire.get(nom, "Inconnu"))
    elif choix == "3":
        for nom, tel in repertoire.items():
            print(f"  {nom} : {tel}")
    elif choix != "4":
        print("Choix invalide.")
print("Au revoir.")
