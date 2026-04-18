with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# Find the exact closing of the style tag to insert profile CSS before it
# Look for the btn-out hover rule which is definitely last in the CSS
target = "#btn-out:hover{background:#302e2b;color:#fff} </style>"

profile_css = """#btn-out:hover{background:#302e2b;color:#fff}
/* PROFILE VIEW */
.profile-page{max-width:480px;margin:0 auto;padding:30px 12px}
.profile-section{text-align:center;margin-bottom:24px}
.profile-avatar{width:80px;height:80px;border-radius:50%;background:#629924;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:800;color:#fff;margin:0 auto 16px;overflow:hidden}
.profile-avatar img{width:100%;height:100%;object-fit:cover}
.profile-name{font-size:22px;font-weight:800;color:#fff;text-align:center;margin-bottom:4px}
.profile-email{font-size:13px;color:#666;text-align:center;margin-bottom:8px}
.profile-role{display:inline-block;padding:2px 10px;border-radius:10px;font-size:11px;font-weight:700;text-transform:uppercase;margin-bottom:24px}
.profile-role.admin{background:#629924;color:#fff}
.profile-role.user{background:#302e2b;color:#999;border:1px solid #3a3632}
.profile-stats{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:16px}
.profile-stat{background:#262421;border-radius:6px;padding:18px;text-align:center}
.profile-stat .num{font-size:30px;font-weight:800;color:#629924}
.profile-stat .lbl{font-size:11px;color:#999;text-transform:uppercase;letter-spacing:.5px;margin-top:3px}
.profile-sync-note{font-size:12px;color:#629924;text-align:center;margin-bottom:8px}
.profile-joined{font-size:12px;color:#555;text-align:center}
</style>"""

if target in src:
    src = src.replace(target, profile_css)
    print("CSS fix applied!")
else:
    # Try to find what's actually there
    idx = src.find("#btn-out:hover")
    print("btn-out:hover found at index:", idx)
    print("Context:", repr(src[idx:idx+80]))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)
print("Done. Run: git add . && git commit -m 'Fix profile page CSS' && git push origin HEAD:main")
