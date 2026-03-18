import os
import re

filepath = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis\tenis.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Replace CSS
old_css = """        .torneo-section {
            margin-top: var(--space-lg);
        }

        .torneo-section h3 {
            font-size: 1.5rem;
            font-weight: var(--font-weight-medium);
            margin-bottom: var(--space-sm);
            border-bottom: 1px solid rgba(28, 28, 26, 0.1);
            padding-bottom: 8px;
            color: var(--color-text);
        }"""

new_css = """        .torneo-section {
            margin-top: var(--space-lg);
            border-bottom: 1px solid rgba(28, 28, 26, 0.1);
        }

        .torneo-section summary {
            cursor: pointer;
            list-style: none;
            padding: 8px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .torneo-section summary::-webkit-details-marker {
            display: none;
        }

        .torneo-section summary::after {
            content: '+';
            font-size: 1.5rem;
            color: var(--color-accent);
            transition: transform 0.3s;
        }

        .torneo-section[open] summary::after {
            content: '\\2212';
            transform: rotate(180deg);
        }

        .torneo-section h3 {
            font-size: 1.5rem;
            font-weight: var(--font-weight-medium);
            margin: 0;
            color: var(--color-text);
            transition: color 0.2s;
        }
        
        .torneo-section summary:hover h3 {
            color: var(--color-accent);
        }

        .torneo-content {
            padding-top: var(--space-sm);
            padding-bottom: var(--space-md);
            animation: fadeIn 0.3s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }"""

html = html.replace(old_css, new_css)

html = html.replace('<div class="torneo-section">', '<details class="torneo-section">')
html = re.sub(r'<h3>(.*?)</h3>', r'<summary><h3>\1</h3></summary>\n                        <div class="torneo-content">', html)

# The replace logic needs to accurately close the `.torneo-content` and `<details>`
html = html.replace('                    </div>\n\n                    <details', '                        </div>\n                    </details>\n\n                    <details')
html = html.replace('                    </div>\n\n                </div>', '                        </div>\n                    </details>\n\n                </div>')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated tenis.html")
