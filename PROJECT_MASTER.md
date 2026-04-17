# SUPER GRAND MASTER — PROJECT MASTER DOCUMENT
## Last Updated: April 17, 2026
## Save this file to: G:\My Drive\Super Grand Master\PROJECT_MASTER.md

---

## 1. PROJECT OVERVIEW

- **Name:** Super Grand Master
- **Type:** Chess Puzzle Trainer + Game Platform (like Lichess)
- **Data Source:** Lichess Open Database — 5,882,680 puzzles (CC0 license)
- **Live URL:** https://super-grand-master.web.app
- **Owner:** Ranjith VS (ranjith.vsk@gmail.com)

---

## 2. ACCOUNTS & SERVICES

### Firebase (Hosting + Database)
- **Project Name:** Super Grand Master
- **Project ID:** super-grand-master
- **Console:** https://console.firebase.google.com/u/0/project/super-grand-master/overview
- **Hosting URL:** https://super-grand-master.web.app
- **Realtime Database URL:** https://super-grand-master-default-rtdb.asia-southeast1.firebasedatabase.app
- **Database Location:** Singapore (asia-southeast1)
- **Plan:** Spark (free)
- **Account:** ranjith.vsk@gmail.com
- **App ID:** 1:663805467661:web:5d6e6584d3142b749d4944
- **Measurement ID:** G-CJCMN4CP5N

### Firebase Config (embed in index.html)
```javascript
const FIREBASE_CONFIG = {
  apiKey: "AIzaSyCA8oHffDPJP3fXGbQ5zJupPVJ0KsV7dhU",
  authDomain: "super-grand-master.firebaseapp.com",
  projectId: "super-grand-master",
  storageBucket: "super-grand-master.firebasestorage.app",
  messagingSenderId: "663805467661",
  appId: "1:663805467661:web:5d6e6584d3142b749d4944",
  measurementId: "G-CJCMN4CP5N",
  databaseURL: "https://super-grand-master-default-rtdb.asia-southeast1.firebasedatabase.app"
};
```

### GitHub (Version Control)
- **Repository:** https://github.com/Ranjithvsk/super-grand-master
- **Username:** Ranjithvsk
- **Account:** ranjith.vsk@gmail.com

### Google Drive (File Storage)
- **Path:** G:\My Drive\Super Grand Master\
- **Purpose:** Working directory, synced to cloud

### Google Cloud (Service Account)
- **Service Account:** firebase-adminsdk-fbsvc@super-grand-master.iam.gserviceaccount.com
- **Key File:** super-grand-master-58dcb7db3f91.json (store securely, do NOT commit to git)
- **Used for:** GitHub Actions auto-deploy authentication

---

## 3. FILE STRUCTURE

```
G:\My Drive\Super Grand Master\
├── index.html                    # Main app (single HTML file with everything)
├── firebase.json                 # Firebase hosting config (includes "site" field)
├── .firebaserc                   # Links to super-grand-master project
├── .github/
│   └── workflows/
│       └── deploy.yml            # GitHub Actions auto-deploy workflow
├── add_responsive.js             # One-time script used to add responsive CSS
├── PROJECT_MASTER.md             # This file
└── .git/                         # Git version control
```

---

## 4. TECH STACK

| Component | Technology | Details |
|-----------|-----------|---------|
| Frontend | Single HTML file | Vanilla JS, no framework needed yet |
| Chess Logic | chess.js v0.10.3 | Loaded from CDN |
| Piece Images | Lichess SVGs | Loaded from lichess1.org/assets/ |
| Board Colors | Lichess exact | Light #f0d9b5, Dark #b58863 |
| AI Engine | Custom minimax | Alpha-beta pruning + piece-square tables, 4 levels |
| Database | Firebase Realtime DB | Singapore region, test mode |
| Hosting | Firebase Hosting | Free tier, CDN-backed, SSL |
| Version Control | Git + GitHub | github.com/Ranjithvsk/super-grand-master |
| File Backup | Google Drive | G:\My Drive\Super Grand Master\ |
| CI/CD | GitHub Actions | Auto-deploy on every push to main |
| Auth (CI) | Google Service Account | firebase-adminsdk, stored as GitHub Secret |

---

## 5. GITHUB ACTIONS — AUTO DEPLOY

Every `git push` to `main` automatically deploys to Firebase Hosting.

### Workflow file: `.github/workflows/deploy.yml`
```yaml
name: Deploy to Firebase Hosting
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install -g firebase-tools
      - uses: google-github-actions/auth@v2
        with:
          credentials_json: ${{ secrets.FIREBASE_SERVICE_ACCOUNT }}
      - run: firebase deploy --only hosting --project super-grand-master
```

### GitHub Secrets configured:
- `FIREBASE_SERVICE_ACCOUNT` — full JSON content of service account key
- `FIREBASE_TOKEN` — (legacy, no longer used)

---

## 6. DAILY DEVELOPMENT WORKFLOW

```bash
# Navigate to project
cd /d "G:\My Drive\Super Grand Master"

# Make your changes to index.html...

# Push to GitHub (auto-deploys in ~30 seconds)
git add .
git commit -m "describe your change"
git push
```

> **Note:** Local branch is `master` but remote is `main`. Always use `git push origin HEAD:main` if plain `git push` fails. To fix permanently run:
> ```
> git branch -m master main
> git branch --set-upstream-to=origin/main main
> ```

---

## 7. FIREBASE.JSON

```json
{
  "hosting": {
    "site": "super-grand-master",
    "public": ".",
    "ignore": ["firebase.json","**/.*"],
    "headers": [{"source":"**","headers":[{"key":"Cache-Control","value":"public, max-age=3600"}]}]
  }
}
```

---

## 8. LICHESS PIECE SVG URLS

```javascript
const PIECE_SVG = {
  wK: 'https://lichess1.org/assets/hashed/wK.6a015951.svg',
  wQ: 'https://lichess1.org/assets/hashed/wQ.c3dc7fce.svg',
  wR: 'https://lichess1.org/assets/hashed/wR.53013fc8.svg',
  wB: 'https://lichess1.org/assets/hashed/wB.b7d1a118.svg',
  wN: 'https://lichess1.org/assets/hashed/wN.ef4cde0a.svg',
  wP: 'https://lichess1.org/assets/hashed/wP.0596b7ce.svg',
  bK: 'https://lichess1.org/assets/hashed/bK.b83f0a15.svg',
  bQ: 'https://lichess1.org/assets/hashed/bQ.b60573d7.svg',
  bR: 'https://lichess1.org/assets/hashed/bR.7b4fa825.svg',
  bB: 'https://lichess1.org/assets/hashed/bB.ede0f498.svg',
  bN: 'https://lichess1.org/assets/hashed/bN.28c70309.svg',
  bP: 'https://lichess1.org/assets/hashed/bP.09539f32.svg',
};
```

---

## 9. LICHESS EXACT CSS COLORS

```css
/* Body & Layout */
body background: #161512
sidebar background: #262421
header background: #2b2825

/* Board Squares */
light square: #f0d9b5
dark square: #b58863

/* Last Move Highlight */
light last-move: #cdd26a
dark last-move: #aaa23b

/* Selected Square */
light selected: #819669
dark selected: #646d40

/* Move Hint Dots */
dot color: rgba(20, 85, 30, 0.5)

/* Check Highlight */
radial-gradient(ellipse at center, rgba(255,0,0,0.9) 0%, rgba(231,0,0,0.65) 25%, rgba(169,0,0,0) 89%)

/* Lichess Blue (buttons, links) */
#3692e7

/* Lichess Green (success, play button) */
#629924
```

---

## 10. RESPONSIVE LAYOUT (Added April 17, 2026)

The app is fully responsive across all screen sizes:

| Screen | Breakpoint | Layout |
|--------|-----------|--------|
| Mobile | ≤ 480px | Full-width board (100vw), sidebar below |
| Tablet | ≤ 768px | 92vw board centered, sidebar below |
| Desktop | > 768px | Side-by-side Lichess style |

Key selectors for responsive CSS:
- Board: `.puzzle__board .cg-wrap` and `#gcol .cg-wrap`
- Sidebar: `.puzzle__side`
- Play layout: `#gcol`
- Stats: `.stats-grid`

---

## 11. LICHESS PUZZLE DATABASE STATS

From the uploaded file: lichess_db_puzzle_csv.zst (280MB compressed)

- **Total puzzles:** 5,882,680
- **74 unique themes**
- **Rating range:** 200 to 3,400
- **Top themes:** fork (760K), pin (355K), skewer (130K), backRankMate (199K)
- **Top openings:** Sicilian (184K), French (78K), Caro-Kann (67K), Italian (67K)
- **Peak rating bucket:** 1000-1200

### Currently Embedded Puzzles
- 60 curated puzzles across all themes and 3 difficulty levels (beginner/intermediate/advanced)

---

## 12. DEVELOPMENT ROADMAP

### Phase 1 — MVP ✅ COMPLETE
- [x] Firebase project created
- [x] Web app registered with hosting
- [x] Realtime Database created (Singapore)
- [x] Lichess puzzle DB extracted (5.8M puzzles)
- [x] Chess trainer with Lichess-style UI
- [x] Play vs engine (4 difficulty levels)
- [x] Stats tracking (localStorage)
- [x] Deployed to https://super-grand-master.web.app
- [x] GitHub repo created

### Phase 2 — Professional Setup ✅ COMPLETE
- [x] GitHub repository: Ranjithvsk/super-grand-master
- [x] Code pushed to GitHub from Google Drive
- [x] GitHub Actions auto-deploy to Firebase (on every push)
- [x] Firebase Service Account authentication
- [x] Responsive layout for mobile, tablet, desktop
- [x] GitHub connector linked to Claude

### Phase 3 — Firebase Auth (NEXT)
- [ ] Add Google sign-in (one-tap on mobile)
- [ ] User accounts with separate progress
- [ ] Sync progress across devices via Realtime DB
- [ ] User profile page

### Phase 4 — Full Database
- [ ] Move full 5.8M puzzles to Firebase Firestore
- [ ] Server-side puzzle filtering by theme/rating
- [ ] Spaced repetition (wrong puzzles come back)
- [ ] Daily puzzle challenge

### Phase 5 — Social Features
- [ ] Leaderboard
- [ ] Rating system (Elo-based)
- [ ] Daily/weekly challenges
- [ ] Share puzzles with friends

---

## 13. HOW TO CONTINUE IN A NEW CHAT

Copy-paste this to Claude in a new conversation:

```
I'm continuing development of my chess training app "Super Grand Master".

Live URL: https://super-grand-master.web.app
GitHub: https://github.com/Ranjithvsk/super-grand-master
Firebase project: super-grand-master (Spark plan)
Database: Realtime DB in Singapore
Working directory: G:\My Drive\Super Grand Master\
Account: ranjith.vsk@gmail.com / GitHub: Ranjithvsk

Current state:
- Phase 1 (MVP) and Phase 2 (CI/CD) are complete
- Single HTML file with Lichess-style UI
- 60 embedded puzzles, chess engine with 4 levels
- Uses actual Lichess SVG pieces and exact color scheme
- Firebase Hosting + Realtime DB configured
- GitHub Actions auto-deploy working (uses Service Account)
- Fully responsive: mobile, tablet, desktop

I have the full PROJECT_MASTER.md with all credentials,
SVG URLs, CSS colors, and architecture details.

I want to work on: [DESCRIBE WHAT YOU WANT TO DO NEXT]
```

---

## 14. IMPORTANT NOTES

1. **Firebase test mode expires** — Database rules allow read/write for 30 days from April 17, 2026. Update rules before **May 17, 2026**.

2. **Service account key** — `super-grand-master-58dcb7db3f91.json` is stored locally. Do NOT commit this to git. It's already in GitHub Secrets as `FIREBASE_SERVICE_ACCOUNT`.

3. **Lichess SVG URLs may change** — They use content hashes. If pieces stop loading, re-extract URLs from lichess.org.

4. **Free tier limits** — Firebase Spark plan: 10GB bandwidth/month, 1GB storage, 1GB Realtime DB.

5. **Puzzle data is CC0** — Lichess releases under Creative Commons Zero. Free for any use including commercial.

6. **chess.js version** — Using v0.10.3 from CDN. Methods: .move(), .undo(), .moves(), .board(), .fen(), .turn(), .in_check(), .in_checkmate(), .game_over()

7. **Git branch** — Local branch is `master`, remote is `main`. Use `git push origin HEAD:main` until you run the rename commands above.

---

## 15. KEY PYTHON SCRIPTS (for puzzle extraction)

### Extract puzzles from Lichess DB
```python
import zstandard as zstd
import io, json, random

dctx = zstd.ZstdDecompressor()

with open('lichess_db_puzzle_csv.zst', 'rb') as f:
    reader = dctx.stream_reader(f)
    text_stream = io.TextIOWrapper(reader, encoding='utf-8')
    next(text_stream)  # skip header

    for line in text_stream:
        parts = line.strip().split(',')
        if len(parts) < 9: continue
        # parts: [id, fen, moves, rating, ratingDev, popularity, nbPlays, themes, gameUrl, openingTags]
        puzzle_id = parts[0]
        fen = parts[1]
        moves = parts[2]
        rating = int(parts[3])
        themes = parts[7]
```

### Puzzle CSV format
```
PuzzleId,FEN,Moves,Rating,RatingDeviation,Popularity,NbPlays,Themes,GameUrl,OpeningTags
```

### Puzzle solving logic
- FEN = position BEFORE opponent's move
- Moves[0] = opponent's move (apply to get puzzle position)
- Moves[1:] = solution (player + opponent alternating)
- Player must find moves at index 1, 3, 5, ...
