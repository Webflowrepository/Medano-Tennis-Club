import os, glob, re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"
html_files = glob.glob(os.path.join(directory, "*.html"))

# This regex matches the entire <a ...>Restaurante</a> tag block, even with newlines
pattern = re.compile(r'<a[^>]*href="https://drive\.google\.com[^>]*>\s*Restaurante\s*</a>', re.IGNORECASE | re.DOTALL)

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace the Google Drive link with the internal link
    content = pattern.sub('<a href="restaurante.html">Restaurante</a>', content)
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("Restaurant link updated successfully.")
