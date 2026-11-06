# Fabrique le dossier bac-a-sable, avec des fichiers de tailles et de dates connues.
# À lancer une seule fois : python3 creer_bac_a_sable.py
import os
import sys
from datetime import datetime

RACINE = "bac-a-sable"

# chemin du fichier : (taille en octets, date de dernière modification)
FICHIERS = {
    "rapport.txt": (1834, "2026-11-02 09:30"),
    "budget.csv": (612, "2026-10-15 18:05"),
    "vide.txt": (0, "2026-10-20 08:00"),
    "script.py": (245, "2026-11-04 16:42"),
    "archive.zip": (1048576, "2026-03-11 11:11"),
    "photos/plage.jpg": (2457600, "2026-07-14 19:20"),
    "photos/montagne.jpg": (1843200, "2026-08-03 07:45"),
    "photos/chat.png": (524288, "2026-10-28 13:02"),
    "photos/miniatures/plage_mini.jpg": (20480, "2026-07-14 19:21"),
    "documents/cv.pdf": (98304, "2026-09-30 22:10"),
    "documents/lettre.txt": (2150, "2026-10-31 10:00"),
    "documents/notes.md": (845, "2026-11-03 17:25"),
    "documents/2025/facture_janvier.pdf": (45056, "2025-01-31 12:00"),
    "documents/2025/facture_fevrier.pdf": (47104, "2025-02-28 12:00"),
}
DOSSIERS_VIDES = ["musique"]

if os.path.exists(RACINE):
    print(f"Le dossier {RACINE} existe déjà. Pour repartir de zéro : rm -r {RACINE}")
    sys.exit(1)

for chemin, (taille, date) in FICHIERS.items():
    complet = os.path.join(RACINE, chemin)
    os.makedirs(os.path.dirname(complet), exist_ok=True)
    with open(complet, "wb") as f:
        if chemin.endswith((".txt", ".csv", ".md", ".py")):
            ligne = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
            f.write((ligne * (taille // len(ligne) + 1))[:taille])
        else:
            f.write(bytes(taille))
    horodatage = datetime.strptime(date, "%Y-%m-%d %H:%M").timestamp()
    os.utime(complet, (horodatage, horodatage))

for dossier in DOSSIERS_VIDES:
    os.makedirs(os.path.join(RACINE, dossier), exist_ok=True)

print(f"Dossier {RACINE} créé : {len(FICHIERS)} fichiers, {len(DOSSIERS_VIDES)} dossier vide.")
