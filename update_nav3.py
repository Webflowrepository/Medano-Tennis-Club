import os, glob, re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    if os.path.basename(file_path) == "index.html":
        continue

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Buscamos el div con class logo-container y cualquier a > img adentro
    # Usamos re.sub con callback o simplemente capturamos el div entero
    
    # Pattern to match the whole logo-container div containing the image that might have inline styles
    pattern = re.compile(r'(<div\s+class="logo-container"\s*>.*?)<img\s+src="\./imagenes/Logo%20Medano\.png"[^>]*>(.*?</div>)', re.DOTALL | re.IGNORECASE)
    
    new_logo_tag = '<img src="./imagenes/Logo%20Medano.png" alt="Médano Tennis Club Logo" class="nav-logo">'
    
    content = pattern.sub(r'\1' + new_logo_tag + r'\2', content)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("Update nav 3 script completed.")
