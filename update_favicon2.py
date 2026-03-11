import os, glob, re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"
html_files = glob.glob(os.path.join(directory, "*.html"))

# 2. Update Favicon Link
# Let's match both "Logo Medano.png" and "Logo%20Medano.png"
favicon_pattern = re.compile(
    r'<link[^>]*rel="icon"[^>]*href="\./imagenes/Logo(?: |%20)Medano\.png"[^>]*>',
    re.IGNORECASE
)
new_favicon = '<link rel="icon" type="image/png" href="./imagenes/favicon.png">'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace Favicon
    new_content = favicon_pattern.sub(new_favicon, content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)

print("HTML favicon links updated perfectly.")
