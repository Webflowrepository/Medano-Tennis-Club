import glob
import os
import re

count = 0
for f_path in glob.glob('*.html'):
    if not os.path.isfile(f_path): continue
    
    with open(f_path, 'r', encoding='utf-8') as f:
        c = f.read()
        
    original_c = c
    c = c.replace('href="https://wa.me/"', 'href="https://wa.me/59898908062"')
    c = c.replace('href="https://api.whatsapp.com/send?phone=59894400338"', 'href="https://api.whatsapp.com/send?phone=59898908062"')
    c = c.replace('+598 94 400 338', '+598 98 908 062')
    c = c.replace('094 400 338', '098 908 062')
    
    if c != original_c:
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1
        
print(f"Updated {count} files.")
