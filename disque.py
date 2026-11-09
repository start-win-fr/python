# ============================================================
# Exercice : Espace disque disponible
# ============================================================
# Objectifs :
# - utiliser shutil.disk_usage() pour lire l'état du disque
# - dépaqueter un tuple en plusieurs variables
# - convertir des octets en Go (gigaoctets)
# ============================================================

import shutil

# disk_usage renvoie un tuple : (total, utilisé, libre) en octets
# "/" = racine du disque (sous Windows, on pourrait mettre "C:\\")
total, utilise, libre = shutil.disk_usage("/")

go = 1024 ** 3  # 1 Go = 1024³ octets

print(f"Disque : {total / go:.1f} Go")
print(f"Utilisé : {utilise / go:.1f} Go ({utilise / total * 100:.0f} %)")
print(f"Libre : {libre / go:.1f} Go")
