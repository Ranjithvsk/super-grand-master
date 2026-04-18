import re

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ── CHECK STATE ──────────────────────────────────────────
has_filter_bar  = 'id="filter-bar"' in src
has_filter_css  = '.profile-sync-note' in src  # profile CSS exists
has_filter_func = 'getFilteredPuzzles' in src
print(f"filter-bar HTML: {has_filter_bar}")
print(f"filter CSS:      {has_filter_css}")
print(f"filter func:     {has_filter_func}")

# ── CHANGE 1: CSS ────────────────────────────────────────
filter_css = """/* PUZZLE FILTER BAR */
#filter-bar{background:#1e1c1a;border-bottom:1px solid #2e2b28;padding:8px 12px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
#filter-bar label{font-size:11px;color:#666;text-transform:uppercase;letter-spacing:.5px;font-weight:600;white-space:nowrap}
#filter-bar select{padding:5px 8px;background:#302e2b;color:#bababa;border:1px solid #3a3632;border-radius:3px;font-size:13px;font-family:inherit;cursor:pointer}
#filter-bar select:focus{outline:none;border-color:#629924}
#filter-bar .fsep{width:1px;height:20px;background:#333;margin:0 2px}
#fc{font-size:12px;color:#555;margin-left:auto;white-space:nowrap}
#fc b{color:#629924;font-weight:700}
"""
# Insert before </style>
if '#filter-bar' not in src:
    src = src.replace('</style>', filter_css + '</style>', 1)
    print("CHANGE 1: CSS added")
else:
    print("CHANGE 1: CSS already present")

# ── CHANGE 2: HTML filter bar ────────────────────────────
filter_html = """<div id="filter-bar">
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
      <option value="hangingPiece">Hanging Piece (195)</option>
      <option value="trappedPiece">Trapped Piece (68)</option>
      <option value="defensiveMove">Defensive Move (219)</option>
      <option value="quietMove">Quiet Move (131)</option>
      <option value="intermezzo">Intermezzo (77)</option>
      <option value="clearance">Clearance (62)</option>
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
  <div class="fsep"></div>
  <label>Difficulty</label>
  <select id="f-diff">
    <option value="">All</option>
    <option value="beginner">Beginner (900-1199)</option>
    <option value="intermediate">Intermediate (1200-1499)</option>
    <option value="advanced">Advanced (1500-1799)</option>
    <option value="expert">Expert (1800-2000)</option>
  </select>
  <div class="fsep"></div>
  <label>Moves</label>
  <select id="f-moves">
    <option value="">Any</option>
    <option value="1">1 Move (523)</option>
    <option value="2">2 Moves (2851)</option>
    <option value="3">3 Moves (1381)</option>
    <option value="4">4 Moves (196)</option>
    <option value="5">5 Moves (41)</option>
  </select>
  <div id="fc"><b id="fc-num">5,000</b> puzzles</div>
</div>"""

if 'id="filter-bar"' not in src:
    # Insert before the puzzle view div
    src = src.replace('<div class="puzzle" id="v-puzzles">', filter_html + '\n<div class="puzzle" id="v-puzzles">', 1)
    print("CHANGE 2: Filter bar HTML added")
else:
    print("CHANGE 2: Filter bar HTML already present")

# ── CHANGE 3: JS filter functions ────────────────────────
filter_js = """
function getFilteredPuzzles(){
  const theme=document.getElementById('f-theme')?.value||'';
  const diff=document.getElementById('f-diff')?.value||'';
  const moves=document.getElementById('f-moves')?.value||'';
  const DR={beginner:[900,1199],intermediate:[1200,1499],advanced:[1500,1799],expert:[1800,2000]};
  let pool=PUZZLES;
  if(theme) pool=pool.filter(p=>(' '+p[4]+' ').includes(' '+theme+' '));
  if(diff){const [lo,hi]=DR[diff];pool=pool.filter(p=>p[3]>=lo&&p[3]<=hi);}
  if(moves){const n=parseInt(moves);pool=pool.filter(p=>Math.ceil((p[2].split(' ').length-1)/2)===n);}
  return pool.length?pool:PUZZLES;
}
function updFC(){
  const el=document.getElementById('fc-num');
  if(el) el.textContent=getFilteredPuzzles().length.toLocaleString();
}
"""

if 'getFilteredPuzzles' not in src:
    src = src.replace('function newPuzzle(){', filter_js + 'function newPuzzle(){', 1)
    print("CHANGE 3: Filter JS functions added")
else:
    print("CHANGE 3: Filter JS already present")

# ── CHANGE 4: newPuzzle uses filter pool ─────────────────
old_pick = 'const raw=PUZZLES[Math.floor(Math.random()*PUZZLES.length)];'
new_pick = 'const pool=getFilteredPuzzles();const raw=pool[Math.floor(Math.random()*pool.length)];'
if old_pick in src:
    src = src.replace(old_pick, new_pick, 1)
    print("CHANGE 4: newPuzzle uses filter pool")
elif new_pick in src:
    print("CHANGE 4: Already updated")
else:
    print("CHANGE 4 WARNING: pick line not found")

# ── CHANGE 5: Wire filter events ─────────────────────────
wire_js = """
// Wire filter dropdowns
['f-theme','f-diff','f-moves'].forEach(function(id){
  var el=document.getElementById(id);
  if(el) el.addEventListener('change',function(){updFC();newPuzzle();});
});
updFC();"""

if "Wire filter dropdowns" not in src:
    # Insert just before closing </script> of main script block
    # Find the newPuzzle(); standalone call before </script>
    target = "newPuzzle();\n</script>"
    if target in src:
        src = src.replace(target, "newPuzzle();" + wire_js + "\n</script>", 1)
        print("CHANGE 5: Filter events wired")
    else:
        print("CHANGE 5 WARNING: newPuzzle init not found - trying alternate")
        # try with different whitespace
        src = src.replace("newPuzzle(); </script>", "newPuzzle();" + wire_js + " </script>", 1)
else:
    print("CHANGE 5: Already wired")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print("\nDone! Run: git add . && git commit -m 'Fix filter bar' && git push origin HEAD:main")
