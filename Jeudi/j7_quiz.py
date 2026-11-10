# ============================================================
# Exercice J7 : Le quiz
# ============================================================
# Objectifs :
# - lire un fichier et ranger chaque ligne dans un tuple
# - mélanger une liste avec random.shuffle()
# - AJOUTER une ligne à un fichier avec le mode "a"
# ============================================================
# Le fichier questions.txt doit être dans le même dossier.

import random

questions = []
with open("questions.txt", encoding="utf-8") as f:
    for ligne in f:
        question, reponse = ligne.strip().split(";")
        questions.append((question, reponse))   # un tuple (question, réponse)

random.shuffle(questions)   # mélange la liste sur place
score = 0
# On « déballe » chaque tuple directement dans deux variables
for question, reponse in questions:
    proposition = input(question + " ")
    # strip() et lower() : « DEF » ou «  def  » sont acceptés
    if proposition.strip().lower() == reponse.lower():
        print("Bonne réponse !")
        score += 1
    else:
        print(f"Non, c'était : {reponse}")

print(f"Score : {score}/{len(questions)}")
prenom = input("Votre prénom : ")
# "a" (append) ajoute à la fin. Avec "w", seul le dernier score resterait.
with open("scores.txt", "a", encoding="utf-8") as f:
    f.write(f"{prenom};{score}\n")   # write n'ajoute pas le retour à la ligne
