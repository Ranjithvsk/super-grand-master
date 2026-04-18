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

### Firebase (Hosting + Database + Auth)
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

### Firebase Auth Providers (Both Enabled)
- ✅ Google Sign-In
- ✅ Email/Password

### Firebase Config (embedded in index.html)
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

### Firebase SDK (in index.html head)
```html
<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-database-compat.js"></script>
```

### GitHub
- **Repository:** https://github.com/Ranjithvsk/super-grand-master
- **Username:** Ranjithvsk
- **Account:** ranjith.vsk@gmail.com

### Google Drive
- **Path:** G:\My Drive\Super Grand Master\
- **Purpose:** Working directory, synced to cloud

### Google Cloud Service Account
- **Email:** firebase-adminsdk-fbsvc@super-grand-master.iam.gserviceaccount.com
- **Key File:** super-grand-master-58dcb7db3f91.json (DO NOT commit to git)
- **Used for:** GitHub Actions CI/CD authentication

### Claude Connectors (linked)
- ✅ GitHub Integration
- ✅ Gmail
- ✅ Google Drive

---

## 3. FILE STRUCTURE

```
G:\My Drive\Super Grand Master\
├── index.html                              # Main app (everything in one file)
├── firebase.json                           # Firebase hosting config
├── .firebaserc                             # Firebase project link
├── .github/
│   └── workflows/
│       └── deploy.yml                      # GitHub Actions auto-deploy
├── add_responsive.js                       # One-time: added responsive CSS
├── add_auth.js                             # One-time: auth attempt v1
├── add_auth2.js                            # One-time: auth UI v2 (successful)
├── super-grand-master-58dcb7db3f91.json    # Service account key (KEEP SECRET)
├── PROJECT_MASTER.md                       # This file
└── .git/                                   # Git version control
```

---

## 4. TECH STACK

| Component | Technology | Details |
|-----------|-----------|---------|
| Frontend | Single HTML file | Vanilla JS, no framework |
| Chess Logic | chess.js v0.10.3 | CDN |
| Piece Images | Lichess SVGs | lichess1.org/assets/ |
| Board Colors | Lichess exact | Light #f0d9b5, Dark #b58863 |
| AI Engine | Custom minimax | Alpha-beta pruning, 4 levels |
| Auth | Firebase Auth | Google + Email/Password |
| Database | Firebase Realtime DB | Singapore |
| Hosting | Firebase Hosting | Free tier, SSL, CDN |
| Version Control | Git + GitHub | github.com/Ranjithvsk/super-grand-master |
| CI/CD | GitHub Actions | Auto-deploy on push to main |
| CI Auth | Google Service Account | Stored in GitHub Secrets |

---

## 5. GITHUB ACTIONS WORKFLOW

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

**GitHub Secrets:**
- `FIREBASE_SERVICE_ACCOUNT` — service account JSON ✅
- `FIREBASE_TOKEN` — legacy, not used

---

## 6. DAILY DEVELOPMENT WORKFLOW

```cmd
cd /d "G:\My Drive\Super Grand Master"
git add .
git commit -m "describe your change"
git push origin HEAD:main
```

Deploys automatically in ~35 seconds after push.

> **Tip:** To make `git push` work without `origin HEAD:main`, run once:
> ```cmd
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

## 8. USER ROLES & AUTH

### Admin (Super Admin)
- **Email:** ranjith.vsk@gmail.com
- **Sign-in:** Google Sign-In
- **Badge:** Green "Admin" badge in nav bar

### Normal Users
- **Sign-in:** Email/Password or Google
- **Example:** harinitharanjith — create via Sign Up on the app

### Admin detection in code
```javascript
const ADMINS = ['ranjith.vsk@gmail.com'];
const isAdmin = ADMINS.includes(user.email);
```

### User data saved to Firebase DB
```
users/{uid}/
  email: "user@example.com"
  name: "Display Name"
  role: "admin" | "user"
  lastLogin: "ISO timestamp"
```

---

## 9. LICHESS PIECE SVG URLS

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

## 10. LICHESS EXACT CSS COLORS

```css
body background:     #161512
sidebar:             #262421
header:              #2b2825
light square:        #f0d9b5
dark square:         #b58863
light last-move:     #cdd26a
dark last-move:      #aaa23b
light selected:      #819669
dark selected:       #646d40
hint dots:           rgba(20, 85, 30, 0.5)
check:               radial-gradient(ellipse, rgba(255,0,0,.9) 0%, rgba(169,0,0,0) 89%)
blue (buttons):      #3692e7
green (play/admin):  #629924
```

---

## 11. RESPONSIVE LAYOUT

| Screen | Breakpoint | Layout |
|--------|-----------|--------|
| Mobile | ≤ 480px | Full-width board (100vw), sidebar below |
| Tablet | ≤ 768px | 92vw board centered, sidebar below |
| Desktop | > 768px | Side-by-side Lichess style |

---

## 12. PUZZLE DATABASE STATS

- **Total:** 5,882,680 puzzles (CC0 license)
- **Themes:** 74 unique
- **Ratings:** 200–3,400
- **Top themes:** fork 760K, pin 355K, backRankMate 199K, skewer 130K
- **Top openings:** Sicilian 184K, French 78K, Caro-Kann 67K, Italian 67K
- **Currently embedded:** 60 curated puzzles (beginner/intermediate/advanced)

---

## 13. ROADMAP

### Phase 1 — MVP ✅ COMPLETE
- [x] Firebase project + hosting + Realtime DB
- [x] Lichess-style chess trainer UI
- [x] 60 embedded puzzles
- [x] Play vs engine (4 difficulty levels)
- [x] Stats tracking (localStorage)
- [x] Deployed live

### Phase 2 — Professional Setup ✅ COMPLETE
- [x] GitHub repo + code pushed
- [x] GitHub Actions auto-deploy (CI/CD)
- [x] Firebase Service Account auth
- [x] Fully responsive layout (mobile/tablet/desktop)
- [x] GitHub connector linked to Claude

### Phase 3 — Firebase Auth 🔄 IN PROGRESS
- [x] Google + Email/Password auth enabled in Firebase Console
- [x] Firebase SDK added to index.html
- [x] Login overlay UI (sign in/up + Google button)
- [x] Admin role detection + badge
- [x] User data saved to Realtime DB
- [ ] Fix browser cache (hard refresh Ctrl+Shift+R after deploy)
- [ ] Create Harinitharanjith's account via Sign Up
- [ ] Per-user puzzle progress synced to DB
- [ ] User profile page

### Phase 4 — Full Database
- [ ] 5.8M puzzles in Firebase Firestore
- [ ] Server-side filtering by theme/rating
- [ ] Spaced repetition system
- [ ] Daily puzzle challenge

### Phase 5 — Social Features
- [ ] Leaderboard
- [ ] Elo-based rating system
- [ ] Daily/weekly challenges
- [ ] Share puzzles

---

## 14. KNOWN ISSUES & FIXES

| Issue | Fix |
|-------|-----|
| Auth overlay not showing | Hard refresh: `Ctrl+Shift+R` on the site |
| Push rejected (non-fast-forward) | `git pull origin main --rebase` then `git push origin HEAD:main` |
| Vim opens during rebase | Press `Esc` then `:wq` then `Enter` |
| `git push` fails (branch mismatch) | `git push origin HEAD:main` |
| Firebase deploy: no site name error | Ensure `firebase.json` has `"site": "super-grand-master"` |
| Firebase 401 auth error in Actions | Use Service Account not login:ci token |

---

## 15. HOW TO START A NEW CHAT

```
I'm continuing development of "Super Grand Master" chess app.

Live: https://super-grand-master.web.app
GitHub: https://github.com/Ranjithvsk/super-grand-master
Firebase: super-grand-master (Spark plan, Singapore DB)
Working dir: G:\My Drive\Super Grand Master\
Account: ranjith.vsk@gmail.com | GitHub: Ranjithvsk

Status:
- Phase 1 ✅ MVP complete
- Phase 2 ✅ CI/CD complete (auto-deploy on git push)
- Phase 3 🔄 Firebase Auth in progress
  - Google + Email/Password enabled
  - Login overlay UI added
  - Admin: ranjith.vsk@gmail.com
  - Cache fix pending
- Single HTML file, Lichess-style UI
- 60 puzzles, 4-level chess engine
- Responsive: mobile/tablet/desktop

I want to work on: [DESCRIBE WHAT YOU WANT]
```

---

## 16. IMPORTANT NOTES

1. **DB rules expire May 17, 2026** — update Firebase rules before then
2. **Service account JSON** — never commit, stored in GitHub Secrets
3. **Lichess SVG URLs** — use content hashes, may change if Lichess updates
4. **Free tier** — 10GB bandwidth/month, 1GB storage, 1GB Realtime DB
5. **Puzzle data** — CC0 license, free for any use
6. **chess.js v0.10.3** — `.move()` `.undo()` `.moves()` `.fen()` `.turn()` `.in_check()` `.in_checkmate()` `.game_over()`
7. **Cache** — always `Ctrl+Shift+R` after deploying to see new version

---

## 17. PUZZLE EXTRACTION SCRIPT

```python
import zstandard as zstd, io

dctx = zstd.ZstdDecompressor()
with open('lichess_db_puzzle_csv.zst', 'rb') as f:
    reader = dctx.stream_reader(f)
    text_stream = io.TextIOWrapper(reader, encoding='utf-8')
    next(text_stream)  # skip header
    for line in text_stream:
        parts = line.strip().split(',')
        if len(parts) < 9: continue
        puzzle_id, fen, moves, rating, themes = parts[0], parts[1], parts[2], int(parts[3]), parts[7]
        # FEN = position BEFORE opponent's move
        # Moves[0] = opponent move, Moves[1:] = solution
        # Player moves at index 1, 3, 5...
```

**CSV format:**
```
PuzzleId,FEN,Moves,Rating,RatingDeviation,Popularity,NbPlays,Themes,GameUrl,OpeningTags
```
