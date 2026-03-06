import os
import re

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"

# Match exactly what we previously inserted
pattern_old = re.compile(
    r'\s*<div style="font-size: 0\.65rem; color: var\(--color-muted\); opacity: 0\.7; margin-top: 12px; letter-spacing: 0\.05em; text-transform: uppercase;">'
    r'Designed by <a href="https://nexarhub\.com" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline; text-underline-offset: 3px; font-weight: var\(--font-weight-medium\);">Nexar Hub</a></div>',
    re.IGNORECASE | re.DOTALL
)

design_tag = '\n    <div style="position: absolute; bottom: 8px; right: var(--space-md); font-size: 0.6rem; color: var(--color-muted); opacity: 0.5; letter-spacing: 0.1em; text-transform: uppercase;">Designed by <a href="https://nexarhub.com" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none; font-weight: var(--font-weight-regular); transition: opacity 0.3s; opacity: 0.7;" onmouseover="this.style.opacity=1" onmouseout="this.style.opacity=0.7">Nexar Hub</a></div>'

def footer_replacer(m):
    attr = m.group(1)
    if 'position: relative;' not in attr:
        attr = attr.replace('style="', 'style="position: relative; ')
    return f'<footer{attr}>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content

        content = pattern_old.sub('', content)
        
        # Remove any stray new labels if script was re-run
        content = re.sub(r'\s*<div style="position: absolute; bottom: 8px;[^>]*>Designed by <a.*?</a></div>', '', content, flags=re.DOTALL)
        
        # Update footer tag
        content = re.sub(r'<footer([^>]*)>', footer_replacer, content)
        
        # Append before </footer>
        content = content.replace('</footer>', design_tag + '\n</footer>')
        
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
