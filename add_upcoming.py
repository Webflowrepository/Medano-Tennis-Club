filepath = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis\tenis.html"
with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

target = """                <h2>Resultados del Circuito Médano 2026</h2>
                <p>Repasá los campeones y finalistas de los torneos disputados en la temporada.</p>"""

replacement = """                <h2>Próximos torneos</h2>
                <p>Participá en nuestros torneos internos y externos. El Circuito Médano convoca a los mejores jugadores de la región en categorías para todos los niveles.</p>
                
                <div class="torneos-list" style="margin-top: var(--space-md); display: flex; flex-direction: column; gap: var(--space-sm); margin-bottom: 40px;">
                    <div class="torneo-item" style="display: flex; justify-content: space-between; align-items: center; padding: var(--space-sm) 0; border-bottom: 1px solid rgba(28, 28, 26, 0.07);">
                        <div class="torneo-item__name" style="font-size: 1.1rem; color: var(--color-text);">Torneo Semana Santa / Americano</div>
                        <div class="torneo-item__date" style="font-size: 0.85rem; color: var(--color-muted);">4 de Abril</div>
                    </div>
                </div>

                <h2>Resultados del Circuito Médano 2026</h2>
                <p>Repasá los campeones y finalistas de los torneos disputados en la temporada.</p>"""

if target in html:
    html = html.replace(target, replacement)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Success")
else:
    print("Target not found")
