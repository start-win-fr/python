# ============================================================
# TP AstraCorp : Diagnostic d'un dossier
# ============================================================
# Objectifs :
# - parcourir récursivement avec pathlib (Path.rglob)
# - compter les fichiers par extension (.txt, .log, autres)
# - détecter les fichiers volumineux (> 5 Mo)
# - écrire un rapport CSV (append + en-tête si besoin)
# ============================================================

from pathlib import Path
from datetime import datetime
import csv

SIZE_LIMIT = 5 * 1024 * 1024  # seuil : 5 Mo en octets
total = 0
txt_count = 0
log_count = 0
other_count = 0
big_files = []  # liste de tuples (chemin, taille) pour les gros fichiers

# Path() crée un objet chemin à partir de la saisie utilisateur
directory = Path(input("Chemin du dossier à diag : "))

if not directory.exists():
    print("Dossier introuvable")
    exit()

# rglob('*') parcourt tous les fichiers et dossiers récursivement
# On ne garde que les vrais fichiers (pas les dossiers)
files = [f for f in directory.rglob('*') if f.is_file()]

for f in files:
    total += 1

    # .suffix = extension (ex: ".txt"), .lower() ignore la casse
    ext = f.suffix.lower()
    if ext == '.txt':
        txt_count += 1
    elif ext == ".log":
        log_count += 1
    else:
        other_count += 1

    # .stat().st_size = taille du fichier en octets
    size = f.stat().st_size
    if size > SIZE_LIMIT:
        big_files.append((f, size))

# --- Affichage du résumé ---
print("\n=== Diagnostic dossier ===")
print(f"Dossier diagnostiqué : {directory.resolve()}")  # resolve() = chemin absolu
print(f"Nombre de fichiers total : {total}")
print(f"Nombre de fichiers .txt : {txt_count}")
print(f"Nombre de fichiers .log : {log_count}")
print(f"Nombre de fichiers autres : {other_count}")

print("\n=== Fichiers de plus de 5 Mo ===")
if len(big_files) == 0:
    print("Aucun fichier volumineux détecté")
else:
    for f, size in big_files:
        # Conversion octets → Mo pour l'affichage
        print(f"- {f.name} - {size / (1024 * 1024):.2f}")

print(f"Nombre de fichiers volumineux : {len(big_files)}")

print("\n=== Diagnostic final ===")
if len(big_files) == 0:
    print("Dossier propre")
else:
    print("Attention : Fichiers volumineux détectés !")

# --- Sauvegarde dans un CSV (historique des diagnostics) ---
logs_dir = Path("AstraCorp/logs")
logs_dir.mkdir(parents=True, exist_ok=True)  # crée le dossier s'il n'existe pas

csv_path = logs_dir / "diagnostic_global.csv"

file_exist = csv_path.exists()  # True si le CSV existe déjà

# "a" = append : on ajoute une ligne sans écraser l'historique
with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # En-tête écrit seulement à la première création du fichier
    if not file_exist:
        writer.writerow([
            "Date",
            "Dossier",
            "Total fichiers",
            "Nb .txt",
            "Nb .log",
            "Autres fichiers",
            "Fichiers volumineux"
        ])

    writer.writerow([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        directory.resolve(),
        total,
        txt_count,
        log_count,
        other_count,
        len(big_files)
    ])
