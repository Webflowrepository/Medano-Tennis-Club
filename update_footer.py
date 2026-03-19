import glob
import re
import os

os.chdir(r"c:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis")

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # We want to replace the container div's color and opacity
    # It currently is: color: var(--color-muted); opacity: 0.5;
    # We will change it to: color: var(--color-text); opacity: 0.8;
    # (only if it's the designed by text)
    
    # Let's target the exact blocks:
    def replacer(match):
        s = match.group(0)
        s = s.replace('color: var(--color-muted); opacity: 0.5;', 'color: var(--color-text); opacity: 0.9;')
        s = s.replace('opacity: 0.7;', 'opacity: 1;')
        s = s.replace('onmouseout="this.style.opacity=0.7"', 'onmouseout="this.style.opacity=1"')
        return s

    pattern = re.compile(r'<div[^>]*>.*?Designed by.*?Nexar Hub.*?</div>', re.DOTALL | re.IGNORECASE)
    
    new_content = pattern.sub(replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
