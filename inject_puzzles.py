"""
Injects puzzles_5000.js into index.html
Run from: G:\My Drive\Super Grand Master\
"""
import re, os, sys

for f in ['puzzles_5000.js', 'index.html']:
    if not os.path.exists(f):
        print(f"ERROR: {f} not found. Run from G:\\My Drive\\Super Grand Master\\")
        sys.exit(1)

with open('puzzles_5000.js', 'r', encoding='utf-8') as f:
    new_puzzles = f.read().strip()

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

pattern = re.compile(r'const PUZZLES\s*=\s*\[.*?\];', re.DOTALL)
match = pattern.search(src)
if not match:
    print("ERROR: Could not find PUZZLES array in index.html")
    sys.exit(1)

print(f"Found PUZZLES array ({len(match.group()):,} chars)")
src = pattern.sub(new_puzzles, src, count=1)
print(f"Replaced with new array ({len(new_puzzles):,} chars)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

size_kb = os.path.getsize('index.html') / 1024
print(f"index.html updated! ({size_kb:.0f} KB)")
print("\nNow run:")
print('  git add .')
print('  git commit -m "Load 5000 puzzles from Lichess DB"')
print('  git push origin HEAD:main')
