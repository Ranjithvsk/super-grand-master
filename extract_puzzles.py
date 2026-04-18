"""
Lichess Puzzle Extractor
Rating range: 900-2000, all themes
Target: 5000 puzzles
Run from: G:\My Drive\Super Grand Master\
"""
import zstandard as zstd
import io, json, random, os, sys

ZST_PATH = os.path.join('Puzzle DB', 'lichess_db_puzzle.csv.zst')
TARGET   = 5000

# Balanced buckets within 900-2000
BUCKETS = [
    ("beginner",     900,  1199, 1250),
    ("intermediate", 1200, 1499, 1500),
    ("advanced",     1500, 1799, 1500),
    ("expert",       1800, 2000,  750),
]

print(f"Looking for: {os.path.abspath(ZST_PATH)}")
if not os.path.exists(ZST_PATH):
    print("ERROR: File not found!")
    print("Make sure you run this from: G:\\My Drive\\Super Grand Master\\")
    sys.exit(1)

def get_bucket(rating):
    for label, lo, hi, _ in BUCKETS:
        if lo <= rating <= hi:
            return label
    return None

reservoirs = {label: [] for label, *_ in BUCKETS}
counts     = {label: 0  for label, *_ in BUCKETS}
targets    = {label: tgt for label, lo, hi, tgt in BUCKETS}
total_read = 0

print("Reading puzzles (1-2 mins)...")
dctx = zstd.ZstdDecompressor()
with open(ZST_PATH, 'rb') as f:
    reader = dctx.stream_reader(f)
    stream = io.TextIOWrapper(reader, encoding='utf-8')
    next(stream)  # skip header

    for line in stream:
        total_read += 1
        if total_read % 500000 == 0:
            filled = sum(min(len(v), targets[k]) for k, v in reservoirs.items())
            print(f"  {total_read:,} read ... {filled}/{TARGET} collected")

        parts = line.strip().split(',')
        if len(parts) < 8:
            continue
        try:
            puzzle_id = parts[0]
            fen       = parts[1]
            moves     = parts[2]
            rating    = int(parts[3])
            themes    = parts[7]
        except (ValueError, IndexError):
            continue

        bucket = get_bucket(rating)
        if bucket is None:
            continue

        puzzle = [puzzle_id, fen, moves, rating, themes]
        counts[bucket] += 1
        res = reservoirs[bucket]
        tgt = targets[bucket]
        if len(res) < tgt:
            res.append(puzzle)
        else:
            j = random.randint(0, counts[bucket] - 1)
            if j < tgt:
                res[j] = puzzle

print(f"\nDone! Read {total_read:,} total puzzles.")
print()

all_puzzles = []
for label, lo, hi, tgt in BUCKETS:
    picked = reservoirs[label][:tgt]
    random.shuffle(picked)
    all_puzzles.extend(picked)
    print(f"  {label:15s}: {len(picked):4d} puzzles  (rating {lo}-{hi})")

random.shuffle(all_puzzles)
print(f"\n  TOTAL: {len(all_puzzles)} puzzles  (rating 900-2000, all themes)")

out = ["const PUZZLES = ["]
for p in all_puzzles:
    out.append(f"  {json.dumps(p)},")
out.append("];")

with open('puzzles_5000.js', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

size_kb = os.path.getsize('puzzles_5000.js') / 1024
print(f"\nWritten: puzzles_5000.js ({size_kb:.0f} KB)")
print("Next: run inject_puzzles.py")
