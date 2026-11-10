# ============================================================
# Exercice M2 : Le compte à rebours, deux fois
# ============================================================
# Objectifs :
# - écrire la même boucle avec while puis avec for
# - utiliser range() avec un pas négatif
# - afficher sur une seule ligne avec end=" "
# ============================================================

# Version 1 : avec while. C'est à nous de faire évoluer le compteur.
n = 10
while n >= 1:
    print(n, end=" ")   # end=" " : un espace au lieu du retour à la ligne
    n -= 1              # sans cette ligne, la boucle ne s'arrête jamais
print("Décollage !")

# Version 2 : avec for. range(10, 0, -1) compte de 10 à 1 (le 0 est exclu).
for n in range(10, 0, -1):
    print(n, end=" ")
print("Décollage !")

# Laquelle choisir ?
# - for quand on sait d'avance combien de tours faire (ici : 10) ;
# - while quand on attend un événement (une bonne réponse, une saisie valide...).
# La version for est plus courte et ne peut pas tourner à l'infini.
