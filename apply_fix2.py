with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# FIX 1: Remove duplicate Firebase SDK block
sdk = (
    '<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>'
    '<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-auth-compat.js"></script>'
    '<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-database-compat.js"></script>'
)
first = src.find(sdk)
second = src.find(sdk, first + 1)
if second != -1:
    src = src[:second] + src[second + len(sdk):]
    print("FIX 1 done: removed duplicate Firebase SDK block")
else:
    print("FIX 1 skipped: no duplicate found")

# FIX 2: Add initializeApp() before firebase.auth() in the auth script
init_code = (
    'const FIREBASE_CONFIG={'
    'apiKey:"AIzaSyCA8oHffDPJP3fXGbQ5zJupPVJ0KsV7dhU",'
    'authDomain:"super-grand-master.firebaseapp.com",'
    'projectId:"super-grand-master",'
    'storageBucket:"super-grand-master.firebasestorage.app",'
    'messagingSenderId:"663805467661",'
    'appId:"1:663805467661:web:5d6e6584d3142b749d4944",'
    'databaseURL:"https://super-grand-master-default-rtdb.asia-southeast1.firebasedatabase.app"'
    '};\n'
    '  if(!firebase.apps.length) firebase.initializeApp(FIREBASE_CONFIG);\n'
    '  '
)
target = "const ADMINS=['ranjith.vsk@gmail.com'];"
if init_code not in src and target in src:
    pos = src.rfind(target)
    src = src[:pos] + init_code + src[pos:]
    print("FIX 2 done: added firebase.initializeApp()")
elif init_code in src:
    print("FIX 2 skipped: initializeApp already present")
else:
    print("FIX 2 WARNING: could not find insertion point")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print("Done! index.html saved.")
print("Now run: git add . && git commit -m Fix-auth && git push origin HEAD:main")
