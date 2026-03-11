import os, glob, re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # We want to change:
    # style="position: absolute; bottom: 8px; right: var(--space-md); font-size: 0.6rem; color: var(--color-muted); opacity: 0.5; letter-spacing: 0.1em; text-transform: uppercase;"
    # To:
    # style="position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%); width: 100%; text-align: center; font-size: 0.6rem; color: var(--color-muted); opacity: 0.5; letter-spacing: 0.1em; text-transform: uppercase;"
    
    # The div might have slight spacing variations, so we use regex
    pattern = re.compile(
        r'<div\s+style="position:\s*absolute;\s*bottom:\s*8px;\s*right:\s*var\(--space-md\);\s*(.*?)">\s*(.*?)</div>',
        re.DOTALL | re.IGNORECASE
    )
    
    # Replacement string with centered styling
    replacement = r'<div style="position: absolute; bottom: 8px; left: 0; right: 0; text-align: center; \1">\2</div>'
    
    content = pattern.sub(replacement, content)
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("Footer centered successfully.")
