import os
import re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = re.sub(r'Torneos de Tenis', 'Torneos', content)
        new_content = re.sub(r'Reglamento de torneos', 'Reglamento', new_content)
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
