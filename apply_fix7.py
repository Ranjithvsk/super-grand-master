with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ============================================================
# FIX 1: Prevent login flash on refresh
# Hide the auth overlay by default, show it only if not logged in
# ============================================================

# Change the auth overlay to start hidden, then JS shows it only if needed
old_overlay_style = "#auth-overlay{position:fixed;inset:0;background:#161512;z-index:9999;display:flex;align-items:center;justify-content:center}"
new_overlay_style = "#auth-overlay{position:fixed;inset:0;background:#161512;z-index:9999;display:none;align-items:center;justify-content:center}"

if old_overlay_style in src:
    src = src.replace(old_overlay_style, new_overlay_style)
    print("FIX 1a done: auth overlay starts hidden")
else:
    print("FIX 1a WARNING: overlay style not found")

# Update onAuthStateChanged to show overlay only when definitely logged out
old_auth_state = """    } else {
      ov.style.display='flex';
      badge.style.display='none';
    }"""
new_auth_state = """    } else {
      ov.style.setProperty('display','flex','important');
      badge.style.display='none';
    }"""

if old_auth_state in src:
    src = src.replace(old_auth_state, new_auth_state)
    print("FIX 1b done: overlay shows with important on logout")
else:
    print("FIX 1b WARNING: auth state else block not found")

# ============================================================
# FIX 2: Replace plain text site title with styled chess logo
# ============================================================
old_title = """  <div class="site-title">
      <span style="font-size:26px;color:#b3b3b3">&#9822;</span>
      <span>Super Grand Master</span>
    </div>"""

new_title = """  <div class="site-title" onclick="switchView('puzzles')">
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="16" cy="16" r="15" fill="#262421" stroke="#629924" stroke-width="1.5"/>
        <text x="16" y="22" text-anchor="middle" font-size="20" fill="#d4af37">&#9822;</text>
      </svg>
      <span style="font-size:17px;font-weight:800;color:#fff;letter-spacing:-.3px;line-height:1.1">Super<br><span style="color:#629924">Grand Master</span></span>
    </div>"""

if old_title in src:
    src = src.replace(old_title, new_title)
    print("FIX 2 done: site title upgraded with chess logo")
else:
    print("FIX 2 WARNING: site title not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print("\nDone! Run: git add . && git commit -m 'Fix login flash + upgrade site logo' && git push origin HEAD:main")
