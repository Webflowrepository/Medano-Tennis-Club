import os, glob, re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"
html_files = glob.glob(os.path.join(directory, "*.html"))

# Regex para buscar el logo, sin importar el espaciado
logo_pattern = re.compile(r'<img\s+src="\./imagenes/Logo%20Medano\.png"\s+alt="Médano\s+Tennis\s+Club\s+Logo"[^>]*style="[^"]*"[^>]*>')
new_logo = '<img src="./imagenes/Logo%20Medano.png" alt="Médano Tennis Club Logo" class="nav-logo">'

for file_path in html_files:
    if os.path.basename(file_path) == "index.html":
        # index.html ya esta actualizado, solo le cambiamos el v=3 a v=4 del js
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        content = content.replace('app.js?v=3', 'app.js?v=4')
        content = content.replace('app.js?v=2', 'app.js?v=4')
        content = content.replace('app.js', 'app.js?v=4')
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        continue

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Reemplazar logo con Regex
    content = logo_pattern.sub(new_logo, content)

    # Actualizar links a css y js
    content = re.sub(r'<link\s+rel="stylesheet"\s+href="\./css/main\.css(\?v=\d+)?"\s*>', '<link rel="stylesheet" href="./css/main.css?v=4">', content)
    content = re.sub(r'<script\s+src="\./js/app\.js(\?v=\d+)?"\s*></script>', '<script src="./js/app.js?v=4"></script>', content)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("Update nav 2 script completed.")
