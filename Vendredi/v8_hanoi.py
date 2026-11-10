# ============================================================
# Exercice V8 : Les tours de Hanoï
# ============================================================
# Objectifs :
# - résoudre un problème récursif à trois étapes
# - compter les déplacements avec une variable globale
# ============================================================

deplacements = 0


def hanoi(n, depart, arrivee, intermediaire):
    """Déplace n disques de depart vers arrivee, en s'aidant d'intermediaire."""
    global deplacements   # pour MODIFIER la variable créée hors de la fonction
    if n == 0:
        return            # cas de base : aucun disque, rien à faire
    # 1. les n - 1 disques du dessus vont sur le piquet intermédiaire
    hanoi(n - 1, depart, intermediaire, arrivee)
    # 2. le plus grand disque va directement à l'arrivée
    print(f"Déplacer le disque {n} de {depart} vers {arrivee}")
    deplacements += 1
    # 3. les n - 1 disques reviennent par-dessus, sur l'arrivée
    hanoi(n - 1, intermediaire, arrivee, depart)


hanoi(3, "A", "C", "B")
print(deplacements, "déplacements")
# 7 pour 3 disques, 1023 pour 10 : la formule est 2 puissance n, moins 1.
