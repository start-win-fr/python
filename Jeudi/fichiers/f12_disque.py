# ============================================================
# Exercice F12 : L'espace disque
# ============================================================
# Objectifs :
# - utiliser shutil.disk_usage()
# - déballer un tuple de trois valeurs en une ligne
# ============================================================

import shutil

# disk_usage renvoie trois nombres (en octets) : total, utilisé, libre
total, utilise, libre = shutil.disk_usage("/")
go = 1024 ** 3
print(f"Disque : {total / go:.1f} Go")
print(f"Utilisé : {utilise / go:.1f} Go ({utilise / total * 100:.0f} %)")
print(f"Libre : {libre / go:.1f} Go")
# À comparer avec : df -h /
# Utilisé + libre ne fait pas tout à fait le total : sous Linux,
# environ 5 % du disque est réservé au système.
