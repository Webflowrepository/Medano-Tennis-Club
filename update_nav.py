import os, glob

# Definimos los strings a reemplazar
old_logo = """<img src="./imagenes/Logo%20Medano.png" alt="Médano Tennis Club Logo"
                style="height: 96px; width: auto; display: block; object-fit: contain;">"""
new_logo = '<img src="./imagenes/Logo%20Medano.png" alt="Médano Tennis Club Logo" class="nav-logo">'

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"

html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    if os.path.basename(file_path) == "index.html":
        continue

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Reemplazar logo inline style
    content = content.replace(old_logo, new_logo)

    # El logo podria estar en una linea
    old_logo_single = '<img src="./imagenes/Logo%20Medano.png" alt="Médano Tennis Club Logo" style="height: 96px; width: auto; display: block; object-fit: contain;">'
    content = content.replace(old_logo_single, new_logo)

    # Actualizar CSS
    content = content.replace('<link rel="stylesheet" href="./css/main.css">', '<link rel="stylesheet" href="./css/main.css?v=3">')
    
    # Actualizar JS
    content = content.replace('<script src="./js/app.js"></script>', '<script src="./js/app.js?v=3"></script>')

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("Update nav script completed.")
