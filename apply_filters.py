import re

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ============================================================
# CHANGE 1: Add filter bar CSS
# ============================================================
filter_css = """
/* PUZZLE FILTER BAR */
#filter-bar{background:#1e1c1a;border-bottom:1px solid #2e2b28;padding:8px 12px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
#filter-bar label{font-size:11px;color:#666;text-transform:uppercase;letter-spacing:.5px;font-weight:600;white-space:nowrap}
#filter-bar select{padding:5px 8px;background:#302e2b;color:#bababa;border:1px solid #3a3632;border-radius:3px;font-size:13px;font-family:inherit;cursor:pointer}
#filter-bar select:focus{outline:none;border-color:#629924}
#filter-bar .filter-sep{width:1px;height:20px;background:#2e2b28;margin:0 2px}
#filter-count{font-size:12px;color:#555;margin-left:auto;white-space:nowrap}
#filter-count span{color:#629924;font-weight:700}
"""

old_css_end = "/* PROFILE VIEW */"
if old_css_end in src:
    src = src.replace(old_css_end, filter_css + "\n/* PROFILE VIEW */")
    print("CHANGE 1 done: Filter CSS added")
else:
    print("CHANGE 1 WARNING: CSS anchor not found")

# ============================================================
# CHANGE 2: Add filter bar HTML above puzzle view
# ============================================================
new_filter_html = """<!-- FILTER BAR -->
<div id="filter-bar">
  <label>Theme</label>
  <select id="f-theme">
    <option value="">All Themes</option>
    <optgroup label="Tactics">
      <option value="fork">Fork (714)</option>
      <option value="pin">Pin (333)</option>
      <option value="skewer">Skewer (122)</option>
      <option value="discoveredAttack">Discovered Attack (265)</option>
      <option value="deflection">Deflection (261)</option>
      <option value="attraction">Attraction (232)</option>
      <option value="sacrifice">Sacrifice (388)</option>
      <option value="clearance">Clearance (62)</option>
      <option value="intermezzo">Intermezzo (77)</option>
      <option value="hangingPiece">Hanging Piece (195)</option>
      <option value="trappedPiece">Trapped Piece (68)</option>
      <option value="defensiveMove">Defensive Move (219)</option>
      <option value="quietMove">Quiet Move (131)</option>
    </optgroup>
    <optgroup label="Mate Patterns">
      <option value="mateIn1">Mate in 1 (519)</option>
      <option value="mateIn2">Mate in 2 (654)</option>
      <option value="mateIn3">Mate in 3 (200)</option>
      <option value="backRankMate">Back Rank Mate (86)</option>
      <option value="exposedKing">Exposed King (136)</option>
      <option value="kingsideAttack">Kingside Attack (415)</option>
      <option value="queensideAttack">Queenside Attack (64)</option>
    </optgroup>
    <optgroup label="Endgame">
      <option value="rookEndgame">Rook Endgame (230)</option>
      <option value="pawnEndgame">Pawn Endgame (137)</option>
      <option value="queenEndgame">Queen Endgame (68)</option>
      <option value="bishopEndgame">Bishop Endgame (65)</option>
      <option value="advancedPawn">Advanced Pawn (292)</option>
      <option value="promotion">Promotion (123)</option>
    </optgroup>
    <optgroup label="Phase">
      <option value="opening">Opening (277)</option>
      <option value="middlegame">Middlegame (2329)</option>
      <option value="endgame">Endgame (2394)</option>
    </optgroup>
  </select>
  <div class="filter-sep"></div>
  <label>Difficulty</label>
  <select id="f-diff">
    <option value="">All</option>
    <option value="beginner">Beginner (900-1199)</option>
    <option value="intermediate">Intermediate (1200-1499)</option>
    <option value="advanced">Advanced (1500-1799)</option>
    <option value="expert">Expert (1800-2000)</option>
  </select>
  <div class="filter-sep"></div>
  <label>Moves</label>
  <select id="f-moves">
    <option value="">Any</option>
    <option value="1">1 Move (523)</option>
    <option value="2">2 Moves (2851)</option>
    <option value="3">3 Moves (1381)</option>
    <option value="4">4 Moves (196)</option>
    <option value="5">5 Moves (41)</option>
  </select>
  <div id="filter-count"><span id="fc-num">5,000</span> puzzles</div>
</div>

<!-- PUZZLE VIEW -->"""

if '<!-- PUZZLE VIEW -->' in src:
    src = src.replace('<!-- PUZZLE VIEW -->', new_filter_html)
    print("CHANGE 2 done: Filter bar HTML added")
else:
    # maybe already has filter bar, replace it
    old_filter = re.compile(r'<!-- FILTER BAR -->.*?<!-- PUZZLE VIEW -->', re.DOTALL)
    if old_filter.search(src):
        src = old_filter.sub(new_filter_html, src)
        print("CHANGE 2 done: Filter bar HTML replaced")
    else:
        print("CHANGE 2 WARNING: anchor not found")

# ============================================================
# CHANGE 3: Replace/add filter logic functions
# ============================================================
# Remove old filter functions if present
src = re.sub(r'function getFilteredPuzzles\(\)\{.*?\}\nfunction updateFilterCount\(\)\{.*?\}\n', '', src, flags=re.DOTALL)

new_filter_funcs = """function getFilteredPuzzles(){
  const theme=document.getElementById('f-theme')?.value||'';
  const diff=document.getElementById('f-diff')?.value||'';
  const moves=document.getElementById('f-moves')?.value||'';
  const DIFF_RANGES={beginner:[900,1199],intermediate:[1200,1499],advanced:[1500,1799],expert:[1800,2000]};
  let pool=PUZZLES;
  if(theme) pool=pool.filter(p=>p[4].split(' ').includes(theme));
  if(diff){const [lo,hi]=DIFF_RANGES[diff];pool=pool.filter(p=>p[3]>=lo&&p[3]<=hi);}
  if(moves){
    const n=parseInt(moves);
    pool=pool.filter(p=>{
      const allMoves=p[2].split(' ');
      const playerMoves=Math.ceil((allMoves.length-1)/2);
      return playerMoves===n;
    });
  }
  return pool.length>0?pool:PUZZLES;
}
function updateFilterCount(){
  const pool=getFilteredPuzzles();
  const el=document.getElementById('fc-num');
  if(el) el.textContent=pool.length.toLocaleString();
}
"""

# Insert before newPuzzle function
old_new_puzzle_fn = "function newPuzzle(){"
if old_new_puzzle_fn in src:
    src = src.replace(old_new_puzzle_fn, new_filter_funcs + old_new_puzzle_fn, 1)
    print("CHANGE 3 done: Filter functions added")
else:
    print("CHANGE 3 WARNING: newPuzzle anchor not found")

# ============================================================
# CHANGE 4: Update newPuzzle() to use filter pool
# ============================================================
old_np_body = """function newPuzzle(){
  const raw=PUZZLES[Math.floor(Math.random()*PUZZLES.length)];"""
new_np_body = """function newPuzzle(){
  const pool=getFilteredPuzzles();
  const raw=pool[Math.floor(Math.random()*pool.length)];"""

if old_np_body in src:
    src = src.replace(old_np_body, new_np_body)
    print("CHANGE 4 done: newPuzzle() uses filtered pool")
else:
    print("CHANGE 4 WARNING: newPuzzle body not found (may already be updated)")

# ============================================================
# CHANGE 5: Wire filter events + init count (replace old wiring if present)
# ============================================================
# Remove old filter wiring
src = re.sub(r"// Wire up filter controls\n\['f-theme','f-diff','f-len'\].*?updateFilterCount\(\);", '', src, flags=re.DOTALL)

old_init = "newPuzzle();\n</script>"
new_init = """newPuzzle();
// Wire filter controls
['f-theme','f-diff','f-moves'].forEach(id=>{
  const el=document.getElementById(id);
  if(el) el.addEventListener('change',()=>{updateFilterCount();newPuzzle();});
});
updateFilterCount();
</script>"""

if old_init in src:
    src = src.replace(old_init, new_init)
    print("CHANGE 5 done: Filter events wired up")
else:
    print("CHANGE 5 WARNING: script end anchor not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print("\nDone! Run: git add . && git commit -m 'Add theme/difficulty/moves filter controls' && git push origin HEAD:main")
