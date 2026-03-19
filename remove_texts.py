filepath = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis\tenis.html"
with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

target1_a = "<p>Participá en nuestros torneos internos y externos. El Circuito Médano convoca a los mejores jugadores de la región en categorías para todos los niveles.</p>"
target1_b = "<p>Participá en nuestros torneos internos y externos. El Circuito Médano convoca a los mejores jugadores\n                    de la región en categorías para todos los niveles.</p>"

target2_a = "<p>Repasá los campeones y finalistas de los torneos disputados en la temporada.</p>"
target2_b = "<p>Repasá los campeones y finalistas de los torneos disputados en la temporada.</p>"

if target1_a in html:
    html = html.replace(target1_a, "")
elif target1_b in html:
    html = html.replace(target1_b, "")

if target2_a in html:
    html = html.replace(target2_a, "")
elif target2_b in html:
    html = html.replace(target2_b, "")

# Remove any resulting double empty lines
import re
html = re.sub(r'\n\s*\n\s*\n', '\n\n', html)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
print("Removed texts.")
