import json
import os

LEYENDA_HTML = """
<div class="leyenda">
  <small>
    📌 <strong>Información importante:</strong><br>
    Los datos nutricionales provienen de bases públicas oficiales
    (ArgenFood y fuentes reconocidas) y fueron procesados con fines informativos.<br><br>

    Los créditos alimentarios se calcularon según el
    <em>Sistema C del Dr. Alberto Cormillot</em>,
    utilizando porciones estándar y valores promedio.<br><br>

    <strong>Los valores son orientativos</strong> y no reemplazan
    el asesoramiento de un profesional de la salud.
    Ante cualquier duda, consulte con su médico o nutricionista.
  </small>
</div>
"""


# Crear carpeta creditos si no existe
os.makedirs("creditos", exist_ok=True)

with open("alimentos.json", encoding="utf-8") as f:
    alimentos = json.load(f)

template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Créditos de {nombre} | Dieta por créditos</title>
  <meta name="description" content="Cuántos créditos tiene {nombre}. Porción: {porcion}. Sistema de créditos tipo Cormillot.">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="../styles.css">
</head>

<body class="calidad-{calidad_clase}">
<header>
  <h1>{nombre}</h1>

  <!-- BLOQUE PUBLICITARIO ARTICULO -->
  <div class="ad ad-articulo">
    Espacio publicitario
  </div>
</header>

<main>
  <p><strong>Porción:</strong> {porcion}</p>
  <p><strong>Créditos por porción:</strong> {creditos_por_porcion}</p>
  <p><strong>Créditos cada 100 g:</strong> {creditos_100g}</p>
  <p><strong>Calidad del alimento:</strong> {calidad}</p>

{leyenda}

  <p>
    <a href="../index.html">⬅ Volver al buscador de alimentos</a>
  </p>
</main>

<footer>
  <p>© 2026 Créditos Alimentarios</p>
</footer>
</body>
</html>
"""

contador = 0

for item in alimentos:
    calidad_clase = (
        item["calidad"].strip().lower()
        if item.get("calidad")
        else "sin-dato"
    )

    html = template.format(
    **item,
    calidad_clase=calidad_clase,
    leyenda=LEYENDA_HTML
)


    filename = f"creditos/{item['id']}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    contador += 1

print(f"Generadas {contador} páginas HTML")
