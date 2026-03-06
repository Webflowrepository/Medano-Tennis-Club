import re

with open("club.html", "r", encoding="utf-8") as f:
    content = f.read()

# The section starts with <!-- Bloque: Comisión Directiva -->
# and we need to replace it up to the next <!-- Bloque: Clubs Recíprocos -->

new_board_html = """        <!-- Bloque: Comisión Directiva Anterior -->
        <div class="content-block fade-up">
            <div class="content-block__label">Comisión Directiva Anterior<br><span
                    style="font-weight: 400; text-transform: none; letter-spacing: 0; font-size: 0.75rem;">2023 –
                    2025</span></div>
            <div class="content-block__body">
                <div style="margin-bottom: var(--space-xl);">
                    <h2>Titulares</h2>

                    <table style="width: 100%; border-collapse: collapse; margin-bottom: var(--space-md);">
                        <tbody>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted); width: 200px;">
                                    Presidente</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Juan Martín Arocena</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Vice – Presidente</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Sebastián Gurmendi</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">2º Vice – Presidente</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sra. Virginia Brause Jiménez de Aréchaga</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Secretario</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Fernando Jiménez de Aréchaga</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Tesorero</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Andrew Cooper</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Pro-Tesorero</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sr. Enrique Smith Estrada</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Capitán</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sra. Pilar Vigo</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted);">Sub-Capitán</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text);">Sra. Pilar Rodríguez</td>
                            </tr>
                            <tr>
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted); vertical-align: top;">
                                    Vocales</td>
                                <td style="padding: 10px 0; font-size: 1rem; color: var(--color-text); line-height: 1.8;">
                                    Sra. María Catalán · Sr. José Reyes Segade · Sr. Roberto Engels<br>
                                    Sra. María del Pilar Cunha Ferré · Sra. Violeta Santamarina<br>
                                    Sr. Pedro Regules · Sr. Fernando González Oliva
                                </td>
                            </tr>
                        </tbody>
                    </table>

                    <h2 style="margin-top: var(--space-md);">Suplentes</h2>
                    <p style="font-size: 1rem; color: var(--color-muted); line-height: 2; columns: 2; column-gap: var(--space-md);">
                        Sra. Cecilia Lamelas<br>
                        Sra. Marina Born<br>
                        Sra. Victoria Petroselli<br>
                        Sr. Patricio Araujo Lynch<br>
                        Sr. Antonio Arias<br>
                        Sra. Inés Arrosa<br>
                        Sr. Carlos Bercianos<br>
                        Sr. Mauricio Delucchi<br>
                        Sr. Marcelo Pereira<br>
                        Sr. Alfredo Etchegaray
                    </p>

                    <h2 style="margin-top: var(--space-md);">Comisión Fiscal</h2>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-sm);">
                        <div>
                            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-accent); margin-bottom: 8px;">
                                Titulares</div>
                            <p style="font-size: 1rem; color: var(--color-muted); line-height: 1.9;">
                                Sr. Mario Vigo Leguizamón<br>
                                Sr. Ricardo Bibiloni<br>
                                Sr. Arturo Heber
                            </p>
                        </div>
                        <div>
                            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-accent); margin-bottom: 8px;">
                                Suplentes</div>
                            <p style="font-size: 1rem; color: var(--color-muted); line-height: 1.9;">
                                Sr. Pablo Thiele<br>
                                Sr. Nicolás Etcheverry<br>
                                Sr. Rubén González Villaveiran
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Bloque: NUEVA Comisión Directiva -->
                <div style="margin-top: var(--space-xl); padding-top: var(--space-xl); border-top: 1px solid rgba(28,28,26,0.1);">
                    <div class="content-block__label" style="font-size: 1.5rem; color: var(--color-text); margin-bottom: var(--space-md);">Comisión Directiva<br><span
                        style="font-weight: 400; text-transform: none; letter-spacing: 0; font-size: 0.85rem; color: var(--color-muted);">2026 –
                        2028</span></div>

                    <h2>Titulares</h2>

                    <table style="width: 100%; border-collapse: collapse; margin-bottom: var(--space-md);">
                        <tbody>
                            <tr style="border-bottom: 1px solid rgba(28,28,26,0.07);">
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted); width: 200px;">
                                    Presidente</td>
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
                                <td style="padding: 10px 0; font-size: 0.9rem; color: var(--color-muted); vertical-align: top;">
                                    Vocales</td>
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
                            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-accent); margin-bottom: 8px;">
                                Titulares</div>
                            <p style="font-size: 1rem; color: var(--color-muted); line-height: 1.9;">
                                Sr. Ricardo Bibiloni<br>
                                Sr. Arturo Heber<br>
                                Sr. Marcos Vigo Lamas
                            </p>
                        </div>
                        <div>
                            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-accent); margin-bottom: 8px;">
                                Suplentes</div>
                            <p style="font-size: 1rem; color: var(--color-muted); line-height: 1.9;">
                                Sr. Pablo Thiele<br>
                                Sr. Carlos Bercianos<br>
                                Sr. Gerardo Segura
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

"""

pattern = r'<!-- Bloque: Comisión Directiva Anterior -->.*?<!-- Bloque: Clubs Recíprocos -->'
pattern2 = r'<!-- Bloque: Comisión Directiva -->.*?<!-- Bloque: Clubs Recíprocos -->'

if re.search(pattern, content, flags=re.DOTALL):
    new_content = re.sub(pattern, new_board_html + "        <!-- Bloque: Clubs Recíprocos -->", content, flags=re.DOTALL)
else:
    new_content = re.sub(pattern2, new_board_html + "        <!-- Bloque: Clubs Recíprocos -->", content, flags=re.DOTALL)

with open("club.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("HTML replaced successfully.")
