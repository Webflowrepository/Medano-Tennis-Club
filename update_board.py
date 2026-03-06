import os
import re

filepath = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis\club.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(
    r'<h2>Titulares</h2>.*?</div>\s*</div>\s*</div>', 
    re.DOTALL
)

new_html = """<h2>Titulares</h2>

                <table style="width: 100%; border-collapse: collapse; margin-bottom: var(--space-md);">
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted); width: 200px;">Presidente</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sra. Violeta Santamarina</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Vicepresidente 1°</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Juan Arocena</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Vicepresidente 2°</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Sebastián Gurmendi</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Secretaria</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sra. Pilar Cunha Ferré</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Tesorero</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Andrew Cooper</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Protesorero</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Enrique Smith Estrada</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Capitana de Tenis</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sra. Pilar Vigo Lamas</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Subcapitana de Tenis</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sra. Victoria Petroselli</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted); vertical-align: top;">Vocales</td>
                            <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text); line-height: 1.8;">
                                Sr. Fernando González Oliva · Sra. María Catalán · Sra. Cecilia Lamelas<br>
                                Sra. Virignia Brause · Sra. Pilar Rodríguez Folle · Sr. José Reyes Segade<br>
                                Sr. Fernando Jiménez de Arechaga
                            </td>
                        </tr>
                    </tbody>
                </table>

                <h2 style="margin-top: var(--space-md);">Suplentes</h2>
                <p style="font-size: 1rem; color: var(--color-muted); line-height: 2; columns: 2; column-gap: var(--space-md);">
                    Sr. Pedro Regules<br>
                    Sra. Ines San Martin<br>
                    Sr. Mauricio Delucchi<br>
                    Sr. Patricio Araujo Lynch<br>
                    Sr. Marcelo Pereira<br>
                    Sr. Antonio Arias<br>
                    Sr. Nicolas Etcheverry<br>
                    Sr. Pablo Quirno<br>
                    Sr. Alfredo Etchegaray<br>
                    Sra. Solana Iribarren
                </p>

                <h2 style="margin-top: var(--space-md);">Comisión Fiscal</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-sm);">
                    <div>
                        <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-accent); margin-bottom: 8px;">Titulares</div>
                        <p style="font-size: 1rem; color: var(--color-muted); line-height: 1.9;">
                            Sr. Ricardo Bibiloni<br>
                            Sr. Arturo Heber<br>
                            Sr. Marcos Vigo Lamas
                        </p>
                    </div>
                    <div>
                        <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-accent); margin-bottom: 8px;">Suplentes</div>
                        <p style="font-size: 1rem; color: var(--color-muted); line-height: 1.9;">
                            Sr. Pablo Thiele<br>
                            Sr. Carlos Bercianos<br>
                            Sr. Gerardo Segura
                        </p>
                    </div>
                </div>"""

new_content = pattern.sub(new_html, content, count=1)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated club.html")
