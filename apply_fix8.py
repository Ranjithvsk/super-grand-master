import re

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# Use regex to find and replace the site-title div regardless of whitespace
old_pattern = re.compile(
    r'<div class="site-title"[^>]*>.*?</div>',
    re.DOTALL
)

new_title = '''<div class="site-title" onclick="switchView('puzzles')" style="gap:10px">
      <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="18" cy="18" r="17" fill="#1a1917" stroke="#629924" stroke-width="1.5"/>
        <text x="18" y="25" text-anchor="middle" font-size="22" fill="#d4af37" font-family="serif">&#9822;</text>
      </svg>
      <div style="line-height:1.15">
        <div style="font-size:11px;font-weight:600;color:#888;letter-spacing:1px;text-transform:uppercase">Super</div>
        <div style="font-size:16px;font-weight:800;color:#fff;letter-spacing:-.3px">Grand Master</div>
      </div>
    </div>'''

match = old_pattern.search(src)
if match:
    print("Found site-title div:", repr(match.group()[:80]))
    src = old_pattern.sub(new_title, src, count=1)
    print("FIX 2 done: site logo upgraded!")
else:
    print("FIX 2 WARNING: site-title div not found by regex")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print("Done. Run: git add . && git commit -m 'Upgrade site logo' && git push origin HEAD:main")
