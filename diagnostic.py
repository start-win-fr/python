from pathlib import Path
from datetime import datetime
import csv

SIZE_LIMIT = 5 * 1024 * 1024 # 5Mo
total = 0
txt_count = 0
log_count = 0
other_count = 0
big_files = []

directory = Path(input("Chemin du dossier à diag : "))

if not directory.exists():
    print("Dossier introuvable")
    exit()

files = [f for f in directory.rglob('*') if f.is_file()]

for f in files:
    total += 1
    ext = f.suffix.lower()
    if ext == '.txt':
        txt_count += 1
    elif ext == ".log":
        log_count += 1
    else:
        other_count += 1

    size = f.stat().st_size
    if size > SIZE_LIMIT:
        big_files.append((f, size))

print(f"\n=== Diagnostic dossier ===")
print(f"Dossier diagnostiqué : {directory.resolve()}")
print(f"Nombre de fichiers total : {total}")
print(f"Nombre de fichiers .txt : {txt_count}")
print(f"Nombre de fichiers .log : {log_count}")
print(f"Nombre de fichiers autres : {other_count}")

print("\n=== Fichiers de plus de 5 Mo ===")
if len(big_files) == 0:
    print("Aucun fichier volumineux détecté")
else:
    for f, size in big_files:
        # size_mo = round(size / (1024 * 1024), 2)
        print(f"- {f.name} - {size / (1024 * 1024):.2f}")

print(f"Nombre de fichiers volumineux : {len(big_files)}")

print("\n=== Diagnostic final ===")
if len(big_files) == 0:
    print("Dossier propre")
else:
    print("Attention : Fichiers volumineux détectés !")

logs_dir = Path("AstraCorp/logs")
logs_dir.mkdir(parents=True, exist_ok=True)

csv_path = logs_dir / "diagnostic_global.csv"

file_exist = csv_path.exists()

with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

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