import os
import re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"

pattern = re.compile(
    r'<li class="has-subdropdown">\s*<a href="tenis\.html#torneos">Torneos de Tenis</a>\s*<ul class="subdropdown">.*?</ul>\s*</li>',
    re.DOTALL
)

replacement = '<li><a href="tenis.html#torneos">Torneos</a></li>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content, num_subs = pattern.subn(replacement, content)
        
        if num_subs > 0:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
