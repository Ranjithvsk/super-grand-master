
import re

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# FIX 1: Remove duplicate Firebase SDK block
sdk_block = (
    '<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>'
    '<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-auth-compat.js"></script>'
    '<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-database-compat.js"></script>'
)
first = src.find(sdk_block)
second = src.find(sdk_block, first + 1)
if second != -1:
    src = src[:second] + src[second + len(sdk_block):]
    print("FIX 1 applied: removed duplicate Firebase SDK block")
else:
    print("FIX 1: no duplicate found (already fixed)")

# FIX 2: Add firebase.initializeApp() at start of auth IIFE
firebase_config = (
    'const FIREBASE_CONFIG={'
    'apiKey:"AIzaSyCA8oHffDPJP3fXGbQ5zJupPVJ0KsV7dhU",'
    'authDomain:"super-grand-master.firebaseapp.com",'
    'projectId:"super-grand-master",'
    'storageBucket:"super-grand-master.firebasestorage.app",'
    'messagingSenderId:"663805467661",'
    'appId:"1:663805467661:web:5d6e6584d3142b749d4944",'
    'databaseURL:"https://super-grand-master-default-rtdb.asia-southeast1.firebasedatabase.app"'
    '};'
)
old = "(function(){
  const ADMINS=['ranjith.vsk@gmail.com'];
  const auth=firebase.auth();"
new = (
    "(function(){\n"
    "  " + firebase_config + "\n"
    "  if(!firebase.apps.length) firebase.initializeApp(FIREBASE_CONFIG);\n"
    "  const ADMINS=[\'ranjith.vsk@gmail.com\'];\n"
    "  const auth=firebase.auth();"
)

# Use a safer approach - find the IIFE and insert before firebase.auth()
iife_marker = "(function(){"
auth_call = "const auth=firebase.auth();"
admins_line = "const ADMINS=['ranjith.vsk@gmail.com'];"

if iife_marker in src and auth_call in src and firebase_config not in src:
    # Find the IIFE position
    iife_pos = src.rfind(iife_marker)  # use rfind to get the auth one (last occurrence)
    auth_pos = src.find(auth_call, iife_pos)
    # Insert before the ADMINS line
    admins_pos = src.rfind(admins_line)
    insert_text = (
        "  " + firebase_config + "\n"
        "  if(!firebase.apps.length) firebase.initializeApp(FIREBASE_CONFIG);\n"
        "  "
    )
    src = src[:admins_pos] + insert_text + src[admins_pos:]
    print("FIX 2 applied: added firebase.initializeApp()")
elif firebase_config in src:
    print("FIX 2: initializeApp already present")
else:
    print("FIX 2 WARNING: could not locate insertion point")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)
print("Done! index.html updated.")
