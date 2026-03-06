import os
import re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"

pattern1 = re.compile(r'<a href="#">Torneos de Tenis</a>')
replacement1 = '<a href="#">Torneos</a>'

pattern2 = re.compile(r'<a href="#">Reglamento de torneos</a>')
replacement2 = '<a href="#">Reglamento</a>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content, num_subs1 = pattern1.subn(replacement1, content)
        new_content, num_subs2 = pattern2.subn(replacement2, new_content)
        
        if num_subs1 > 0 or num_subs2 > 0:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
