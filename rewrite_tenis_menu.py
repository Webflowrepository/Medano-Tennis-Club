import os
import re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"

pattern = re.compile(r'<li class="has-dropdown">\s*<a href="tenis\.html">Tenis</a>\s*<ul class="dropdown">.*?</ul>\s*</li>', re.DOTALL)

replacement = """<li class="has-dropdown">
                <a href="tenis.html">Tenis</a>
                <ul class="dropdown">
                    <li><a href="tenis.html#torneos">Torneos</a></li>
                    <li><a href="profesores.html">Profesores</a></li>
                    <li><a href="reglamento.html">Reglamento</a></li>
                </ul>
            </li>"""

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
