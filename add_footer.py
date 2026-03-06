import os
import re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"

pattern = re.compile(
    r'(<div style="font-size:\s*0\.8rem;\s*color:\s*var\(--color-muted\);\s*letter-spacing:\s*0\.05em;">\s*Desde\s*1943\s*</div>)',
    re.IGNORECASE | re.DOTALL
)

replacement = r'\1\n            <div style="font-size: 0.65rem; color: var(--color-muted); opacity: 0.7; margin-top: 12px; letter-spacing: 0.05em; text-transform: uppercase;">Designed by <a href="https://nexarhub.com" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline; text-underline-offset: 3px; font-weight: var(--font-weight-medium);">Nexar Hub</a></div>'

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
