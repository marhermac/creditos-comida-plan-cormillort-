import csv
import json
import unicodedata
import re

def generar_id(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    return texto.strip("-")

alimentos = []

with open("creditos_alimentos.csv", newline="", encoding="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        nombre = row["Alimento"].strip()

        alimento = {
    "id": generar_id(nombre),
    "nombre": nombre,
    "porcion": row["PORCION"].strip(),
    "creditos_por_porcion": row["creditospor porcion"].strip(),
    "creditos_100g": row["creditoscada100 grs."].strip(),
    "calidad": row["Color de los creditos(indica Calidad del alimento)"].strip()
        }

        alimentos.append(alimento)

with open("alimentos.json", "w", encoding="utf-8") as f:
    json.dump(alimentos, f, ensure_ascii=False, indent=2)

print(f"Generados {len(alimentos)} alimentos con ID")
