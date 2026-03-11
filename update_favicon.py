import os, glob, re
from PIL import Image

directory = r"C:\Users\Equipo\.gemini\antigravity\scratch\medano-tennis"
html_files = glob.glob(os.path.join(directory, "*.html"))

# 1. Update Footer Text
footer_pattern = re.compile(
    r'(<div>\s*<div[^>]*>)\s*Medano Tennis\s*Club\s*(</div>)\s*<div[^>]*>\s*Desde 1943\s*</div>\s*(</div>)',
    re.IGNORECASE | re.DOTALL
)

# 2. Update Favicon Link
favicon_pattern = re.compile(
    r'<link[^>]*rel="icon"[^>]*href="\./imagenes/Logo%20Medano\.png"[^>]*>',
    re.IGNORECASE
)
new_favicon = '<link rel="icon" type="image/png" href="./imagenes/favicon.png">'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace Footer (Keep the first line styling, replace name, remove second line 'Desde 1943')
    content = footer_pattern.sub(r'\1Médano Tennis Club\2\3', content)
    
    # Replace Favicon
    content = favicon_pattern.sub(new_favicon, content)
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("HTML footer and favicon links updated.")

# Create the new favicon using Pillow
try:
    logo_path = os.path.join(directory, "imagenes", "Logo Medano.png")
    favicon_path = os.path.join(directory, "imagenes", "favicon.png")

    img = Image.open(logo_path).convert("RGBA")
    
    # 1. Extract alpha channel
    r, g, b, a = img.split()
    
    # 2. Create black RGB
    black_rgb = Image.new("RGB", img.size, (0, 0, 0))
    
    # 3. Create black logo with original alpha
    black_logo = Image.merge("RGBA", (*black_rgb.split(), a))
    
    # 4. Create white background
    width, height = img.size
    size = max(width, height)
    square_bg = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    
    # 5. Paste the black logo in the center of the white background 
    offset = ((size - width) // 2, (size - height) // 2)
    # The mask is the black_logo itself (it uses its alpha channel)
    square_bg.paste(black_logo, offset, black_logo)
    
    # 6. Resize to standard favicon scale and save
    # using Image.Resampling.LANCZOS for newer Pillow, or Image.LANCZOS for older
    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = Image.LANCZOS
        
    final_favicon = square_bg.resize((512, 512), resample)
    final_favicon.save(favicon_path, "PNG")
    
    print("Favicon created successfully.")
except Exception as e:
    print(f"Error creating favicon: {e}")
