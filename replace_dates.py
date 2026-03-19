import re
filepath = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis\tenis.html"
with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Replace Jan dates
html = re.sub(r'<h4>\d{2}/01/\d{2}</h4>', r'<h4>Enero</h4>', html)
# Replace Feb dates
html = re.sub(r'<h4>\d{2}/02/\d{2}</h4>', r'<h4>Febrero</h4>', html)
# We can also do a general replacement just in case any 2026 string is left, but the user requested replacing the exact date.
with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
print("Dates replaced successfully!")
